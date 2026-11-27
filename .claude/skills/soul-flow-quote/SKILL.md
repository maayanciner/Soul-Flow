---
name: soul-flow-quote
description: Use whenever Maayan asks for a quote, proposal, price estimate or invoice-style PDF for a Soul Flow event (organizations, companies, community groups, private events), and whenever any Soul Flow document or graphic outside Canva needs her logo.
---

# Soul Flow quotes and the logo

## The logo (always this version)

Use `assets/soul-flow-logo-rectangle.png` (in this skill folder, also at `brand/soul-flow-logo-rectangle.png` in the repo).

- It is only the rectangle of her logo: the pastel sunset card with the thin gold frame, "Soul Flow by Maayan Ciner" and the tagline. The square pink background around it is cut away. Maayan asked for this version.
- Never use the full square logo with the background (Canva asset `MAHcIT5UeF0` and the website file `soul-flow-sunset-logo-square.png` both have it). If you have to start from the square one, crop it to the gold frame. On the 200 x 200 version the crop box is (9, 49, 191, 152).
- Show it with no extra border, shadow or rounded corners. It already has its own gold frame. Place it top left on a quote, about 2.3 inches wide.
- The file is small (182 x 103 px). It looks fine on screen and phone, but can look soft in print. If she wants a print-quality version, ask her to send the original logo file.

## Client logos

When Maayan sends the client's logo (often a phone screenshot of their website), cut out only the logo itself: the emblem plus any wording that is part of the logo (such as text curving around a circle). Leave out page titles, paragraphs and phone status bars. Remove the white background around it (flood-fill the white from the edges so white parts inside the logo stay), save it as a PNG with a transparent background in `brand/clients/`, and place it in the "Prepared for" card. Use the organization's name as the logo shows it (for example "BJI2OC", which stands for Bringing Jewish Inspiration to Orange County). Saved so far: `brand/clients/bji2oc-logo.png`.

## Pricing (from her website, soulflowbymaayan.com/teams)

- **Meditation & Painting Experience:** $45 per person. All art supplies included, and everyone takes a painting home.
- **Group Yoga & Meditation:** $30 per person.
- Keep $45 per person even when the painting is shorter than 2 hours, especially when she travels.
- Minimum of 20 guests. Bill on the final guest count.

## Out-of-town travel (her approved approach, Jan 2027 Irvine event)

- **Airfare:** the client pays. Best: they book it in her name. Otherwise they reimburse at cost with the receipt. For Orange County, fly Miami (MIA) to John Wayne (SNA).
- **Travel and supplies transport fee:** a flat $250 (fair range $200 to $350). It covers the travel days, extra checked bags or shipping for supplies, and local rides.
- **Lodging:** when she stays with family, write "No lodging charge". Never mention her family on the quote.
- **Supplies:** ship canvases and paint by Amazon to where she is staying. Pack only the brushes and palettes.
- **Deposit:** 50% holds the date. Book the flight only after the deposit arrives. If they cancel within 30 days, the deposit is non-refundable and the client covers the booked airfare.

## What every quote includes

1. The logo (above), top left. "QUOTE / EVENT PROPOSAL", the quote number (SF-YYYY-MMDD) and the issue date, top right. No "valid until" line (Maayan asked to leave it out).
2. A "Prepared for" card (the organization, the event, the city, with the client's logo on the right of the card, about 0.95 inch wide, when she sends one) and a "Prepared by" card (Soul Flow by Maayan Ciner, then three lines, each label in bold: "Contact: (646) 634-0765", "Email: soulflowbymaayan@gmail.com", "Web: soulflowbymaayan.com". The label is just "Contact", never "Contact number" (too long), "WhatsApp" or "call").
3. The event title: a script accent word, a Playfair Display title and the BREATHE · PAINT · CONNECT tagline. Then one or two warm lines. In quotes, state what is included in a professional, sharp, short way, never "I bring": use exactly "All materials are provided, and setup and cleanup are included." In the pricing row, write "All materials, setup and cleanup included." Match the time of day: for a daytime event write "gathering", never "evening" or "night".
4. A deep plum info box with a gold border: date with the weekday, location, time, program length, group size, price.
5. "What happens at the event" in three steps, plus an "Everything included" list.
6. A pricing table (rate and amount), then totals for the low, middle and high guest counts.
7. To reserve the date: deposit, final count due 10 days before, balance on the day. Payment: **Zelle or Venmo to Maayan · 646-634-0765**.
8. What the client provides (a room with tables and chairs, 45 minutes to set up, water, an outlet), and changes and cancellation terms.
9. The Meet Maayan bio, in a gold script heading, with exactly this text: "Maayan Ciner is an art, yoga and nutrition coach who helps people slow down through mindfulness and creativity. Guiding step-by-step painting workshops is one of her greatest passions."
10. Signature lines. A plum bottom band on each page: page 1 reads "Soul Flow by Maayan Ciner · WhatsApp (646) 634-0765 · @soul.flow_by_maayan · soulflowbymaayan.com" (the website is always included); page 2 starts with a short thank-you line.

Call it an event for women (for example "Women's Tu B'Shvat event"), not a "celebration", unless she says otherwise. Write "every participant" / "each participant", not "every guest". Leave out guests' ages and other demographics unless she asks for them. Her voice: warm, uses "you", no exclamation marks, no hype words.

## How to make it

- Start from `assets/quote-example.html`, the approved BJI to OC Tu B'Shvat quote. Copy it, with `fonts-local.css`, the `f*.woff2` fonts and the logo, into a scratch folder, then edit the text.
- Colors: plum #4F2958, gold #C9A24A / #F0C475, lavender #EFE8F3, cream #FBF7F2. Fonts: Playfair Display (headings), Nunito (body), Great Vibes (one script accent word).
- Render: `node assets/render.js /abs/quote.html /abs/output.pdf`. It writes the PDF and a preview PNG. Check the preview: two Letter pages, nothing cut off at the bottom of page 2.
- Check every date's weekday, every total and the phone number. Then save the PDF to `quotes/` in the repo and send it to her.
