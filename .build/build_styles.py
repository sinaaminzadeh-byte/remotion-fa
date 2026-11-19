# -*- coding: utf-8 -*-
"""ساخت صفحهٔ «۳۹ سبک کدی» (animation-styles / Remotion)."""
import sys
sys.path.insert(0, ".build")
from design import head, topbar, toolbar, side_item, ICONS, CHEV
import asdata as A

STYLES = A.STYLES
FAM = A.FAM_FA
ORDER = A.FAM_ORDER
CODE = A.FAM_CODE

N = len(STYLES)


def card(s):
    nn = s["nn"]
    fa_name, fa_desc = A.fa(nn)
    fam_fa = FAM[s["family"]]
    eq = A.MATCH.get(nn, [])
    eq_html = ""
    if eq:
        eq_html = ('<a class="eq" href="کاتالوگ-۳۰-سبک.html" title="سبک معادل در کاتالوگ ما">'
                   + " · ".join(f"{n:02d}" for n in eq) + "</a>")
    return f'''
    <article class="scard" data-fam="{fam_fa}" data-q="{fa_name} {s['name']} {fa_desc} {s['id']}">
      <div class="sthumb">
        <video class="clip" muted loop playsinline preload="none" poster="{A.poster(nn)}"
               data-src="{A.clip(nn)}" aria-label="کلیپ سبک {fa_name}"></video>
        <button class="play" aria-label="پخش {fa_name}">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>
        </button>
        <span class="num">{nn}</span>
        <span class="code">{s["id"]}</span>
      </div>
      <div class="sbody">
        <h3>{fa_name} <span class="en">{s["name"]}</span></h3>
        <p>{fa_desc}</p>
        <div class="sfoot">
          <span class="famtag">{fam_fa}</span>
          <a class="src" href="{A.raw_video(s)}" target="_blank" rel="noopener">ویدیوی اصلی ↗</a>
          {eq_html}
        </div>
      </div>
    </article>'''


GROUPS = ""
for f in ORDER:
    items = [s for s in STYLES if s["family"] == f]
    if not items:
        continue
    GROUPS += f'''
  <section class="grp" id="f{CODE[f]}" data-fam="{FAM[f]}">
    <div class="ghead">
      <span class="gcode">{CODE[f]}</span>
      <div><h2>{FAM[f]}</h2><div class="gsub">{items[0]["family"]}</div></div>
      <span class="gcount">{len(items)} سبک</span>
    </div>
    <div class="sgrid">{"".join(card(s) for s in items)}</div>
  </section>'''

SIDEBAR = f'''
<aside class="sidebar">
  <div class="side-group">
    <div class="side-label">{ICONS['film']} ۳۹ سبک کدی</div>
    <div class="side" id="famnav">
      {"".join(side_item(FAM[f], f"#f{CODE[f]}", cnt=str(len([s for s in STYLES if s['family']==f]))) for f in ORDER if any(s['family']==f for s in STYLES))}
    </div>
  </div>
  <div class="side-group">
    <div class="side-label">{ICONS['book']} مرتبط</div>
    <div class="side">
      {side_item("کاتالوگ ۳۰ زبان بصری", "کاتالوگ-۳۰-سبک.html", cnt="۳۰")}
      {side_item("راهنمای نصب و استفاده", "آموزش-ساخت-موشن.html#as", pill="مهم")}
      {side_item("راهنمای ساخت موشن", "آموزش-ساخت-موشن.html")}
    </div>
  </div>
</aside>'''

RAIL = f'''
<aside class="rail">
  <div class="rail-card">
    <h4>این صفحه چیست؟</h4>
    <p>۳۹ سبک که با <b>کد</b> (SVG و Canvas) داخل Remotion کشیده شده‌اند — بدون هیچ مدل تصویر یا ویدیو.
       هر کارت، رندر واقعی همان سبک است.</p>
    <a class="btn accent" style="width:100%" href="آموزش-ساخت-موشن.html#as">چطور استفاده کنم</a>
  </div>
  <div class="rail-card dark">
    <h4 style="color:#fff">مجوز و منبع</h4>
    <p>ریپوی <span style="direction:ltr">deenukhan/animation-styles</span> با مجوز <b>MIT</b> —
       استفادهٔ آزاد، تغییر مجاز، با ذکر منبع.</p>
    <a class="btn" style="background:#fff;color:#0E1012;border-color:#fff;width:100%"
       href="https://github.com/deenukhan/animation-styles" target="_blank" rel="noopener">رفتن به ریپو ↗</a>
  </div>
  <div class="rail-card">
    <h4>ترتیب پیشنهادی</h4>
    <p>۱. زبان بصری را از <a href="کاتالوگ-۳۰-سبک.html">کاتالوگ ۳۰ سبک</a> انتخاب کن.<br>
       ۲. اگر معادل کدی داشت، از همین صفحه شماره‌اش را بردار.<br>
       ۳. شماره + قصه‌ات را به ایجنت بده.</p>
  </div>
</aside>'''

CONTENT = f'''
{toolbar()}
<div class="doc">
  <div class="crumbs">مرجع <span>/</span> <b>۳۹ سبک کدی</b></div>
  <h1>۳۹ سبک که با کد کشیده می‌شوند</h1>
  <p class="lead">
    این‌ها سبک‌های <b>آمادهٔ اجرا</b> هستند: هر کدام یک کامپوننت Remotion که یک ظاهر مشخص را
    با SVG و Canvas می‌کشد. برخلاف کاتالوگ ۳۰ سبک که «زبان بصری» را توصیف می‌کند، اینجا هر سبک
    <b>کد واقعی</b> دارد و می‌شود همان لحظه رندر گرفت. هر کارت، رندر واقعی همان سبک است.
  </p>

  <div class="note" style="margin:16px 0 6px">
    <span class="ic">i</span>
    <div>هر ۳۹ فیلم، <b>یک قصهٔ ثابت</b> را نشان می‌دهند (کتری چای می‌ریزد در کولاب و بخار بلند می‌شود).
      دلیلش این است که فقط <b>خود سبک</b> دیده شود. شما قصهٔ خودتان را می‌دهید و همان سبک آن را بازمی‌گوید.</div>
  </div>

  <div class="searchbar">
    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>
    <input id="q" type="search" placeholder="جست‌وجو: آبرنگ، اوکیویو، پیکسل، shader…">
    <span class="cnt" id="cnt">{N} سبک</span>
  </div>

  <div class="chips" id="chips">
    <button class="chip on" data-f="all">همه</button>
    {"".join(f'<button class="chip" data-f="{FAM[f]}">{FAM[f]} <i>{len([s for s in STYLES if s["family"]==f])}</i></button>' for f in ORDER if any(s["family"]==f for s in STYLES))}
  </div>

  <div class="empty" id="empty" hidden>سبکی با این عبارت پیدا نشد.</div>

  {GROUPS}

  <div class="cta-card" style="margin-top:46px">
    <div>
      <h3>می‌خواهی یکی از این‌ها را با قصهٔ خودت بسازی؟</h3>
      <p style="margin:4px 0 0;font-size:13px;color:var(--muted)">راهنمای نصب و پرامپت آماده در صفحهٔ آموزش، بخش «۳۹ سبک کدی».</p>
    </div>
    <a class="btn accent" href="آموزش-ساخت-موشن.html#as">رفتن به آموزش</a>
  </div>
</div>'''

EXTRA = """
.searchbar{display:flex;align-items:center;gap:10px;border:1px solid var(--line);background:#fff;
  border-radius:var(--r);padding:10px 14px;margin:22px 0 10px;box-shadow:var(--sh-sm);color:var(--faint)}
.searchbar input{flex:1;border:0;outline:0;font-family:inherit;font-size:14px;color:var(--fg);background:transparent}
.searchbar .cnt{font-size:12px;color:var(--faint);white-space:nowrap;font-variant-numeric:tabular-nums}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:8px}
.chip{font-family:inherit;font-size:12px;padding:5px 11px;border-radius:999px;border:1px solid var(--line);
  background:#fff;color:var(--muted);cursor:pointer;transition:.14s;display:inline-flex;align-items:center;gap:5px}
.chip:hover{color:var(--fg);border-color:rgba(14,16,18,.2)}
.chip.on{background:var(--fg);color:#fff;border-color:var(--fg)}
.chip i{font-style:normal;font-size:10.5px;opacity:.65;font-variant-numeric:tabular-nums}
.empty{border:1px dashed var(--line);border-radius:var(--r);padding:26px;text-align:center;
  color:var(--faint);font-size:13.5px;margin-top:20px}
.grp{margin-top:42px;scroll-margin-top:92px}
.ghead{display:flex;align-items:center;gap:12px;margin-bottom:14px}
.gcode{width:30px;height:30px;border-radius:9px;background:var(--soft);color:var(--fg);display:grid;
  place-items:center;font-weight:800;font-size:13px;flex-shrink:0;border:1px solid var(--line)}
.ghead h2{font-size:18px;margin:0}
.gsub{font-size:11.5px;color:var(--faint);direction:ltr;letter-spacing:.01em}
.gcount{margin-inline-start:auto;font-size:11.5px;color:var(--faint);border:1px solid var(--line);
  padding:3px 10px;border-radius:999px;background:#fff}
.sgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:14px}
.scard{border:1px solid var(--line);border-radius:var(--r-lg);background:#fff;overflow:hidden;
  box-shadow:var(--sh-sm);transition:.16s;display:flex;flex-direction:column}
.scard:hover{box-shadow:var(--sh);border-color:rgba(14,16,18,.18);transform:translateY(-2px)}
.sthumb{position:relative;aspect-ratio:4/5;background:#F0F1F2;overflow:hidden;border-bottom:1px solid var(--line2)}
.sthumb video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.sthumb .num{position:absolute;top:8px;right:8px;background:rgba(14,16,18,.82);color:#fff;
  font-size:10.5px;font-weight:700;padding:2px 7px;border-radius:6px;direction:ltr;backdrop-filter:blur(4px)}
.sthumb .code{position:absolute;top:8px;left:8px;font-size:9px;font-family:ui-monospace,monospace;
  background:rgba(255,255,255,.9);color:#3A4449;padding:2px 6px;border-radius:5px;direction:ltr;
  opacity:0;transition:.15s;max-width:70%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.scard:hover .sthumb .code{opacity:1}
.sthumb .play{position:absolute;bottom:8px;left:8px;width:26px;height:26px;border-radius:7px;
  background:rgba(14,16,18,.72);color:#fff;border:0;display:grid;place-items:center;cursor:pointer;
  backdrop-filter:blur(6px);transition:.15s;z-index:2}
.sthumb .play:hover{background:rgba(14,16,18,.92)}
.scard.playing .play{background:var(--accent)}
.scard.playing .play svg{display:none}
.scard.playing .play:after{content:"";width:7px;height:7px;border-radius:2px;background:#fff}
.sbody{padding:12px 13px 13px;display:flex;flex-direction:column;gap:5px;flex:1}
.sbody h3{font-size:13.5px;margin:0;display:flex;align-items:baseline;gap:6px;flex-wrap:wrap}
.sbody h3 .en{font-size:10.5px;color:var(--faint);font-weight:400;direction:ltr;letter-spacing:.01em}
.sbody p{font-size:11.5px;color:var(--muted);line-height:1.75;margin:0;flex:1}
.sfoot{display:flex;align-items:center;gap:7px;flex-wrap:wrap;margin-top:6px;font-size:10.5px}
.famtag{color:var(--faint);background:var(--soft);border-radius:5px;padding:1px 7px}
.sfoot a{color:var(--accent);font-weight:600;direction:ltr}
.sfoot a:hover{text-decoration:underline;text-underline-offset:2px}
.sfoot .eq{direction:ltr;color:var(--muted);border:1px solid var(--line);border-radius:5px;padding:0 6px}
.sfoot .eq:hover{color:var(--fg);border-color:rgba(14,16,18,.25);text-decoration:none}
@media(max-width:520px){.sgrid{grid-template-columns:repeat(2,1fr);gap:10px}
  .sbody p{display:none}.sbody h3{font-size:12px}}
"""

JS = """
document.querySelectorAll(".scard").forEach(function(c){
  var v=c.querySelector("video.clip"), b=c.querySelector(".play");
  function load(){ if(!v.src) v.src=v.dataset.src; }
  b.addEventListener("click",function(e){
    e.preventDefault(); e.stopPropagation(); load();
    if(v.paused){ v.play(); c.classList.add("playing"); } else { v.pause(); c.classList.remove("playing"); }
  });
  c.addEventListener("mouseenter",function(){ load(); var p=v.play();
    if(p) p.then(function(){c.classList.add("playing");}).catch(function(){}); });
  c.addEventListener("mouseleave",function(){ v.pause(); v.currentTime=0; c.classList.remove("playing"); });
});
var q=document.getElementById("q"), cnt=document.getElementById("cnt"),
    cards=[].slice.call(document.querySelectorAll(".scard")),
    grps=[].slice.call(document.querySelectorAll(".grp")),
    chips=[].slice.call(document.querySelectorAll(".chip")),
    empty=document.getElementById("empty"), fam="all";
function apply(){
  var t=(q.value||"").trim().toLowerCase(), n=0;
  cards.forEach(function(c){
    var ok=(fam==="all"||c.dataset.fam===fam) && (!t||c.dataset.q.toLowerCase().indexOf(t)>-1);
    c.hidden=!ok; if(ok)n++;
  });
  grps.forEach(function(g){
    g.hidden=![].some.call(g.querySelectorAll(".scard"),function(c){return !c.hidden;});
  });
  empty.hidden=n>0; cnt.textContent=n+" سبک";
}
q.addEventListener("input",apply);
chips.forEach(function(ch){ ch.addEventListener("click",function(){
  chips.forEach(function(x){x.classList.remove("on");}); ch.classList.add("on"); fam=ch.dataset.f; apply(); }); });
apply();
"""

html = (head("۳۹ سبک کدی — آمادهٔ رندر با Remotion", EXTRA) + topbar("styles") +
        f'<div class="shell">{SIDEBAR}<main class="content">{CONTENT}</main>{RAIL}</div>' +
        f'''<footer class="site">۳۹ سبک کدی · <span style="direction:ltr">animation-styles</span> (MIT) · رندر با Remotion</footer>
<script>{JS}</script>
</body></html>''')

open("۳۹-سبک-کدی.html", "w").write(html)
print("styles page:", round(len(html) / 1024), "KB")
