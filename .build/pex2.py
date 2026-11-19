import json,subprocess,urllib.parse
K="H2jk9uKnhRmL6WPwh89zBezWvr"
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
Q={5:["vertical video phone social media","caption text overlay"],
   6:["frosted glass abstract","blurred glass bokeh abstract"],
   9:["pastel 3d render shapes","soft 3d abstract pastel"],
   11:["colorful bold graphic shapes","abstract pop art colors"],
   13:["iridescent holographic","chrome liquid metal"],
   21:["layered paper landscape","3d layers landscape animation"],
   26:["beige minimalist aesthetic","white minimal texture"],
   29:["animated charts graphs","business graph animation"],
   10:["app interface screen","tablet dashboard interface"],
   2:["3d letters","neon text 3d"],
   8:["warm cinematic bokeh","soft golden light abstract"]}
out=json.load(open("pex.json"))
for n,qs in Q.items():
    seen={v["id"] for v in out[str(n)]}
    for q in qs:
        u=("https://www.pexels.com/en-us/api/v3/search/videos?query="+urllib.parse.quote(q)+"&per_page=6&page=1")
        r=subprocess.run(["curl","-s","-m","25","-H",f"User-Agent: {UA}","-H","Accept: application/json",
                          "-H",f"Secret-Key: {K}",u],capture_output=True,text=True)
        try: d=json.loads(r.stdout)
        except Exception: continue
        for v in d.get("data",[]):
            a=v["attributes"]
            if a["id"] in seen: continue
            files=[f for f in (a.get("video") or {}).get("video_files",[]) if f.get("width") and f["width"]<=1280]
            if not files: continue
            files.sort(key=lambda f:f["width"])
            seen.add(a["id"])
            out[str(n)].append({"id":a["id"],"slug":a.get("slug"),"desc":(a.get("description") or "")[:90],
              "dur":a.get("duration"),"q":q,"file":files[min(1,len(files)-1)]["link"],
              "w":files[min(1,len(files)-1)]["width"],"author":(a.get("user") or {}).get("username"),
              "author_url":"https://www.pexels.com/@"+((a.get("user") or {}).get("username") or "")})
    print(n,len(out[str(n)]),flush=True)
json.dump(out,open("pex.json","w"),ensure_ascii=False,indent=0)
