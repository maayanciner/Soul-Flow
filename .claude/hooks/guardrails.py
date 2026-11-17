#!/usr/bin/env python3
"""Soul Flow guardrails for Claude.

Three rules Claude must never break on its own:
  1. Never send email.
  2. Never publish anything.
  3. Never touch money.

This runs as a Claude Code PreToolUse hook (see .claude/settings.json).
For a risky tool call it answers "ask", so the action pauses until Maayan
approves it. Read-only calls, Gmail drafts and WordPress drafts go through.
Anything this script does not recognise as safe also asks, so new tools
start out locked rather than open.
"""
import json
import re
import sys

# ---------- Gmail, Calendar, Drive: anything that sends email ----------

GMAIL_SEND = {"send_message", "reply", "forward"}

# ---------- WordPress: anything that publishes or changes the live site ----------

# Building blocks for drafts: images and private preview links.
WP_DRAFT_SAFE = {
    "media-create",
    "media-upload",
    "media-generate",
    "site-preview-links-create",
}
# New posts and pages are fine only as drafts.
WP_DRAFT_CREATE = {"posts-create", "pages-create", "content-items-create"}
DRAFT_STATUSES = {"draft", "pending"}

READ_LAST = {"get", "list", "search", "lookup", "status"}
WP_WRITE = {
    "create", "update", "delete", "insert", "replace", "remove", "move",
    "switch", "activate", "deactivate", "install", "uninstall", "upload",
    "purchase", "checkout", "reset", "transfer", "attach", "detach", "enable",
    "save", "send", "invite", "import", "run", "provision", "mark", "like",
    "reblog", "cancel", "resend", "change", "set", "start", "configure",
    "generate", "request", "manage", "backup", "scan", "monitor",
    "protection", "newsletter",
}
WP_READ = {
    "docs", "details", "records", "check", "stats", "active", "presets",
    "variations", "styles", "settings", "screenshot", "profile", "sites",
    "domains", "connections", "subscriptions", "achievements", "security",
    "notifications", "inbox", "invites", "metrics", "log", "allowed",
    "themes", "nameservers",
}

# ---------- QuickBooks: anything that changes the books or moves money ----------

QB_SAFE = {"company_select", "company_wait", "onboarding_wait"}
QB_WRITE = {
    "create", "update", "delete", "void", "send", "save", "categorize",
    "review", "undo", "finish", "begin", "cancel", "set", "close",
    "reclassify", "start", "deactivate", "upload", "assign", "sync",
    "connect",
}
QB_READ = {
    "get", "search", "list", "balances", "reports", "read", "check", "wait",
    "ping", "help", "preview", "benchmarking", "benchmark", "estimate",
    "directory", "recommendation", "widget", "metadata", "history", "status",
    "connections", "context",
}


def tokens(name):
    return [t for t in re.split(r"[-_]", name) if t]


def decide(tool_name, tool_input):
    """Return a reason string when the call needs Maayan's OK, else None."""
    parts = tool_name.split("__")
    if len(parts) < 3 or parts[0] != "mcp":
        return None
    server = parts[1].lower()
    tool = "__".join(parts[2:]).lower()
    args = tool_input if isinstance(tool_input, dict) else {}
    toks = tokens(tool)

    if "gmail" in server:
        if tool in GMAIL_SEND or "send" in toks:
            return "this sends an email."
        return None

    if "calendar" in server:
        quiet = args.get("notificationLevel") == "NONE"
        if tool == "respond_to_event":
            return "answering an invitation emails the organizer."
        if tool == "create_event":
            if (args.get("attendees") or args.get("attendeeEmails")) and not quiet:
                return "inviting people to an event emails them."
            return None
        if tool in {"update_event", "delete_event"} and not quiet:
            return "changing or deleting an event can email its guests."
        return None

    if "drive" in server:
        if tool == "share_file":
            return "sharing a file emails the person and gives them access."
        return None

    if "wordpress" in server:
        short = re.sub(r"^wpcom-(mcp-)?", "", tool)
        if short in WP_DRAFT_SAFE:
            return None
        if short in WP_DRAFT_CREATE:
            status = str(args.get("status", "")).lower()
            if status in DRAFT_STATUSES:
                return None
            return "a post or page that isn't a draft goes live on the website."
        stoks = tokens(short)
        if stoks and stoks[-1] in READ_LAST:
            return None
        if any(t in WP_WRITE for t in stoks):
            return "this changes the live website, sends something, or costs money."
        if any(t in WP_READ for t in stoks):
            return None
        return "this WordPress action isn't on the known-safe list."

    if "quickbooks" in server:
        if tool in QB_SAFE:
            return None
        if any(t in QB_WRITE for t in toks):
            return "this changes the books or moves money."
        if any(t in QB_READ for t in toks):
            return None
        return "this QuickBooks action isn't on the known-safe list."

    return None


def main():
    data = json.load(sys.stdin)
    reason = decide(data.get("tool_name", ""), data.get("tool_input") or {})
    if reason:
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "ask",
                "permissionDecisionReason": (
                    "Soul Flow rule: " + reason + " This needs Maayan's OK first."
                ),
            }
        }))


if __name__ == "__main__":
    main()
