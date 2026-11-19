import asyncio,sys
from playwright.async_api import async_playwright
files=[("tutorial","آموزش-ساخت-موشن.html"),("catalog","کاتالوگ-۳۰-سبک.html"),("home","index.html")]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=["--no-sandbox"])
        for name,f in files:
            pg=await b.new_page(viewport={"width":1440,"height":950},device_scale_factor=1)
            await pg.goto(f"file:///home/user/{f}"); await pg.wait_for_timeout(1400)
            await pg.screenshot(path=f".build/v2_{name}_top.png")
            await pg.evaluate("window.scrollTo(0,1500)"); await pg.wait_for_timeout(700)
            await pg.screenshot(path=f".build/v2_{name}_mid.png")
            if name=="home":
                await pg.evaluate("window.scrollTo(0,2300)"); await pg.wait_for_timeout(500)
                await pg.screenshot(path=f".build/v2_home_bot.png")
            # mobile check
            m=await b.new_page(viewport={"width":390,"height":844})
            await m.goto(f"file:///home/user/{f}"); await m.wait_for_timeout(900)
            print(name,"overflow:",await m.evaluate("document.documentElement.scrollWidth-390"),
                  "font:",await pg.evaluate("document.fonts.check('16px Vazirmatn')"))
            if name=="home": await m.screenshot(path=".build/v2_mobile.png")
            await m.close(); await pg.close()
        await b.close()
asyncio.run(main())
