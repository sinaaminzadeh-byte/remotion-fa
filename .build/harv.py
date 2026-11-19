import asyncio,sys,re,json
from playwright.async_api import async_playwright
async def grab(pg,url,pat=r'https://cdn\.pixabay\.com/(?:video|vimeo)/[^"\'\s]+?\.mp4'):
    await pg.goto(url,wait_until="domcontentloaded",timeout=45000)
    await pg.wait_for_timeout(2500)
    for _ in range(3):
        await pg.mouse.wheel(0,3000); await pg.wait_for_timeout(900)
    h=await pg.content()
    urls=sorted(set(re.findall(pat,h)))
    return urls,h
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=["--no-sandbox"])
        pg=await b.new_page(viewport={"width":1400,"height":900},locale="en-US")
        for u in ["https://pixabay.com/videos/search/glitch/","https://mixkit.co/free-stock-video/glitch/"]:
            urls,h=await grab(pg,u)
            print(u,"->",len(urls),"| title:",(h[h.find("<title>"):h.find("<title>")+80] if "<title>" in h else "?"))
            for x in urls[:4]: print("   ",x)
        await b.close()
asyncio.run(main())
