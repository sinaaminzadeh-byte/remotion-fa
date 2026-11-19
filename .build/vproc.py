import json,subprocess,os
sel=json.load(open("vsel.json")); os.makedirs("vid/clips",exist_ok=True)
FF="ffmpeg"
res={}
for n in sorted(sel,key=int):
    v=sel[n]; src=f"vid/clips/src_{n}.mp4"; out=f"vid/clips/c{n}.mp4"
    subprocess.run(["curl","-sL","-m","180","-o",src,v["file"]],check=False)
    if not os.path.exists(src) or os.path.getsize(src)<20000:
        print(n,"download fail",os.path.getsize(src) if os.path.exists(src) else 0); continue
    dur=float(v["dur"] or 6); start=max(0.0,min(dur*0.35, dur-5.2))
    cmd=[FF,"-y","-loglevel","error","-ss",f"{start:.2f}","-i",src,"-t","4.5","-an",
         "-vf","scale=480:-2:flags=lanczos,fps=18","-c:v","libx264","-crf","32",
         "-preset","slow","-pix_fmt","yuv420p","-movflags","+faststart","-g","36",out]
    r=subprocess.run(cmd,capture_output=True,text=True)
    kb=os.path.getsize(out)/1024 if os.path.exists(out) else 0
    res[n]={"kb":round(kb),"desc":v["desc"],"author":v.get("author"),"url":v["url"],"dur":v["dur"]}
    print(n,f"{kb:.0f}KB",r.stderr[:80],flush=True)
    os.remove(src)
json.dump(res,open("vres.json","w"),ensure_ascii=False,indent=0)
print("TOTAL KB",round(sum(x['kb'] for x in res.values())))
