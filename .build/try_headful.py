import asyncio, os
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            user_data_dir="/home/user/.build/profile",
            headless=False,
            viewport={"width":1440,"height":900},
            locale="en-US",
            args=["--no-sandbox","--disable-blink-features=AutomationControlled","--start-maximized"],
        )
        pg = ctx.pages[0] if ctx.pages else await ctx.new_page()
        await pg.goto("https://arena.ai/", wait_until="domcontentloaded", timeout=60000)
        for i in range(12):
            await pg.wait_for_timeout(2500)
            txt = await pg.inner_text("body")
            has_turn = "Verify you are human" in txt
            print(f"t={i*2.5:4.0f}s turnstile={has_turn}")
            if not has_turn:
                break
        await pg.wait_for_timeout(1500)
        await pg.screenshot(path=".build/hf_home.png")
        print("title:", await pg.title())
        # try agent
        await pg.goto("https://arena.ai/agent", wait_until="domcontentloaded", timeout=60000)
        await pg.wait_for_timeout(7000)
        t2 = await pg.inner_text("body")
        print("agent turnstile:", "Verify you are human" in t2)
        await pg.screenshot(path=".build/hf_agent.png")
        await ctx.close()

asyncio.run(main())
