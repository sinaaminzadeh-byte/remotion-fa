import asyncio, json
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=["--no-sandbox"])
        pg=await b.new_page(viewport={"width":1440,"height":900})
        await pg.goto("https://remocn.dev/docs/", wait_until="networkidle", timeout=90000)
        await pg.wait_for_timeout(2000)
        d=await pg.evaluate("""()=>{
          const out={};
          // muted paragraph text
          const p=[...document.querySelectorAll('p')].find(e=>e.textContent.includes('shadcn/ui for video'));
          if(p){const s=getComputedStyle(p); out.lead={color:s.color,fs:s.fontSize,lh:s.lineHeight};}
          // sidebar link colors
          const a=[...document.querySelectorAll('aside a')];
          out.sideLinks=a.slice(0,8).map(e=>{const s=getComputedStyle(e);return {t:e.textContent.trim().slice(0,18),c:s.color,fs:s.fontSize,fw:s.fontWeight};});
          // badge colors
          const badge=[...document.querySelectorAll('*')].find(e=>/^\\s*(new|New)\\s*$/.test(e.textContent) && e.children.length===0);
          if(badge){const s=getComputedStyle(badge); out.badge={bg:s.backgroundColor,c:s.color,fs:s.fontSize,br:s.borderRadius,pad:s.padding};}
          // card
          const card=[...document.querySelectorAll('div')].find(e=>e.textContent.startsWith('Copy-paste components')&&e.className.includes('rounded'));
          if(card){const s=getComputedStyle(card); out.card={bg:s.backgroundColor,bd:s.border,br:s.borderRadius,pad:s.padding,shadow:s.boxShadow};}
          // nav pill container
          const nav=document.querySelector('header')||document.querySelector('nav');
          const pill=nav?nav.closest('div'):null;
          if(pill){const s=getComputedStyle(pill); out.pill={bg:s.backgroundColor,br:s.borderRadius,h:pill.getBoundingClientRect().height,shadow:s.boxShadow};}
          // accent line
          const act=[...document.querySelectorAll('aside a')].find(e=>getComputedStyle(e).fontWeight>=500);
          if(act){const s=getComputedStyle(act); out.active={c:s.color,fw:s.fontWeight,bg:s.backgroundColor};}
          return out;
        }""")
        print(json.dumps(d,ensure_ascii=False,indent=1))
        await b.close()
asyncio.run(main())
