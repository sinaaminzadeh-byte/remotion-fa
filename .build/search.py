import json,subprocess,sys
Q={
1:"kinetic typography animation",2:"3d typography animation",3:"terminal typing animation screen",
4:"code animation motion graphics",5:"tiktok captions dynamic subtitles",6:"glassmorphism motion graphics",
7:"liquid glass animation",8:"soft cinematic motion graphics",9:"claymorphism 3d animation",
10:"app ui motion design",11:"neo brutalism motion graphics",12:"memphis design animation",
13:"y2k aesthetic animation",14:"glitch effect motion graphics",15:"cyberpunk neon motion graphics",
16:"paper collage animation",17:"kraft paper animation",18:"hand drawn sketch animation",
19:"paper cutout stop motion",20:"mixed media motion graphics",21:"parallax 2.5d animation",
22:"film grain light leak",23:"2d 3d hybrid motion graphics",24:"voxel animation showcase",
25:"map animation fly through",26:"minimal editorial motion graphics",27:"swiss style typography animation",
28:"flat design motion graphics",29:"infographic data animation",30:"audio visualizer waveform animation"}
out={}
for n,q in Q.items():
    try:
        r=subprocess.run(["yt-dlp",f"ytsearch6:{q}","--flat-playlist","-J","--no-warnings"],
                         capture_output=True,text=True,timeout=120)
        d=json.loads(r.stdout)
        out[n]=[{"id":e.get("id"),"t":e.get("title"),"ch":e.get("channel") or e.get("uploader"),
                 "dur":e.get("duration"),"v":e.get("view_count")} for e in d.get("entries",[])]
    except Exception as ex:
        out[n]=[{"err":str(ex)[:80]}]
    print(n,"ok",len(out[n]),flush=True)
json.dump(out,open("cands.json","w"),ensure_ascii=False,indent=0)
