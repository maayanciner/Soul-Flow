// Usage: node render.js /abs/path/quote.html /abs/path/output.pdf
const {chromium}=require('playwright');
(async()=>{const [html,pdf]=process.argv.slice(2);const b=await chromium.launch();
const p=await b.newPage({viewport:{width:816,height:1056}});
await p.goto('file://'+html);await p.evaluate(()=>document.fonts.ready);
await p.pdf({path:pdf,format:'Letter',printBackground:true,margin:{top:0,bottom:0,left:0,right:0}});
await p.screenshot({path:pdf.replace(/\.pdf$/,'-preview.png'),fullPage:true});await b.close();})();
