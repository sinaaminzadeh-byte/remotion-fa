import asyncio
from playwright.async_api import async_playwright

async def pass_gate(pg,label):
    for i in range(30):
        await pg.wait_for_timeout(2000)
        try: txt = await pg.inner_text("body")
        except: continue
        if not ("Verify you are human" in txt or "Verifying" in txt):
            print(" ",label,"PASSED"); return True
        if i==1:
            try: await pg.mouse.click(594,516)
            except: pass
    print(" ",label,"blocked"); return False

async def main():
    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            user_data_dir="/home/user/.build/profile2", headless=False,
            viewport={"width":1440,"height":900}, locale="en-US",
            args=["--no-sandbox","--disable-blink-features=AutomationControlled"])
        pg = ctx.pages[0] if ctx.pages else await ctx.new_page()

        # 1) agent page
        await pg.goto("https://arena.ai/agent", wait_until="domcontentloaded", timeout=60000)
        await pass_gate(pg,"agent"); await pg.wait_for_timeout(2500)

        # 2) mode selector dropdown
        try:
            await pg.click("text=Agent", timeout=8000)
            await pg.wait_for_timeout(1200)
            await pg.screenshot(path=".build/real_modes.png")
            print("  modes dropdown ok")
            await pg.keyboard.press("Escape")
        except Exception as e:
            print("  modes err", repr(e)[:120])
        await pg.wait_for_timeout(800)

        # 3) signup
        try:
            await pg.click("text=Sign up for free", timeout=8000)
            await pg.wait_for_timeout(3500)
            await pg.screenshot(path=".build/real_signup.png")
            print("  signup url:", pg.url)
        except Exception as e:
            print("  signup err", repr(e)[:120])

        # 4) cleaned agent shot
        await pg.goto("https://arena.ai/agent", wait_until="domcontentloaded", timeout=60000)
        await pass_gate(pg,"agent2"); await pg.wait_for_timeout(2500)
        await pg.screenshot(path=".build/real_agent_clean.png")
        await ctx.close()

asyncio.run(main())
