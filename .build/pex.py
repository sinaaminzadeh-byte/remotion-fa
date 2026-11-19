import json,subprocess,urllib.parse
K="H2jk9uKnhRmL6WPwh89zBezWvr"
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
Q={
1:["typography kinetic","text animation"],2:["3d text","typography 3d"],
3:["code screen","hacker code"],4:["programming code screen","coding"],
5:["subtitle","social media video phone"],6:["glass abstract","gradient transparent"],
7:["liquid glass","fluid abstract"],8:["cinematic soft light","slow motion aesthetic"],
9:["clay 3d","pastel 3d render"],10:["mobile app interface","smartphone app"],
11:["brutalist design","colorful bold shapes"],12:["memphis pattern","90s pattern"],
13:["y2k chrome","metallic abstract"],14:["glitch","datamosh error"],
15:["neon city","cyberpunk"],16:["paper collage","old paper texture"],
17:["kraft paper","craft handmade"],18:["sketch drawing hand","hand drawn"],
19:["stop motion paper","paper cutout"],20:["collage mixed media","newspaper"],
21:["parallax","layers depth"],22:["film grain","light leak"],
23:["3d abstract shapes","2d 3d animation"],24:["voxel cubes","isometric cubes"],
25:["map animation","world map"],26:["minimal editorial","minimalist paper"],
27:["swiss typography","grid design"],28:["flat design shapes","geometric flat"],
29:["data chart","infographic numbers"],30:["audio visualizer","sound wave"]}
out={}
for n,qs in Q.items():
    res=[]
    for q in qs:
        u=("https://www.pexels.com/en-us/api/v3/search/videos?query="+urllib.parse.quote(q)+
           "&per_page=6&page=1")
        r=subprocess.run(["curl","-s","-m","25","-H",f"User-Agent: {UA}","-H","Accept: application/json",
                          "-H",f"Secret-Key: {K}",u],capture_output=True,text=True)
        try:
            d=json.loads(r.stdout)
        except Exception: continue
        for v in d.get("data",[]):
            a=v["attributes"]
            files=[f for f in (a.get("video") or {}).get("video_files",[]) if f.get("width") and f["width"]<=1280]
            if not files: continue
            files.sort(key=lambda f:f["width"])
            res.append({"id":a["id"],"slug":a.get("slug"),"desc":(a.get("description") or "")[:90],
                        "dur":a.get("duration"),"q":q,
                        "file":files[min(1,len(files)-1)]["link"],"w":files[min(1,len(files)-1)]["width"]})
    out[n]=res[:10]
    print(n,qs[0],"->",len(res),flush=True)
json.dump(out,open("pex.json","w"),ensure_ascii=False,indent=0)
