import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(args=["--no-sandbox","--disable-blink-features=AutomationControlled"])
        ctx = await b.new_context(
            viewport={"width":1440,"height":900},
            locale="en-US",
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        )
        pg = await ctx.new_page()
        for name,url in [("home","https://arena.ai/"),("agent","https://arena.ai/agent")]:
            try:
                r = await pg.goto(url, wait_until="domcontentloaded", timeout=45000)
                await pg.wait_for_timeout(6000)
                title = await pg.title()
                body = (await pg.inner_text("body"))[:300].replace("\n"," ")
                await pg.screenshot(path=f".build/real_{name}.png")
                print(f"{name}: status={r.status if r else None} title={title!r}")
                print("   body:", body[:200])
            except Exception as e:
                print(name, "ERROR", repr(e)[:200])
        await b.close()

asyncio.run(main())
