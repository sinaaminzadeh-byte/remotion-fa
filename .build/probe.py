import asyncio, json
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=["--no-sandbox"])
        pg=await b.new_page(viewport={"width":1440,"height":900})
        await pg.goto("https://remocn.dev/docs/", wait_until="networkidle", timeout=90000)
        await pg.wait_for_timeout(2500)
        data=await pg.evaluate("""()=>{
          const cs=e=>e?getComputedStyle(e):null;
          const body=cs(document.body), html=cs(document.documentElement);
          const grab=(sel)=>{const e=document.querySelector(sel); if(!e) return null;
            const s=getComputedStyle(e);
            return {sel, color:s.color, bg:s.backgroundColor, fs:s.fontSize, fw:s.fontWeight,
                    ff:s.fontFamily.slice(0,40), lh:s.lineHeight, ls:s.letterSpacing,
                    br:s.borderRadius, bd:s.border, pad:s.padding, w:e.getBoundingClientRect().width};};
          const nav=document.querySelector('nav');
          return {
            bodyBg: body.backgroundColor, bodyColor: body.color, bodyFont: body.fontFamily.slice(0,60),
            htmlBg: html.backgroundColor,
            nav: nav?{bg:cs(nav).backgroundColor, h:nav.getBoundingClientRect().height, bd:cs(nav).borderBottom}:null,
            samples:[".docs-sidebar","aside","main h1","article h1","h1","h2","h3","p","a","code","pre","table","button"]
              .map(grab).filter(Boolean).slice(0,14),
            fonts:[...new Set([...document.querySelectorAll('*')].slice(0,400).map(e=>getComputedStyle(e).fontFamily))].slice(0,6)
          };
        }""")
        print(json.dumps(data, ensure_ascii=False, indent=1)[:3000])
        await pg.screenshot(path=".build/remocn_top.png")
        await b.close()
asyncio.run(main())
