# -*- coding: utf-8 -*-
import sys, json
sys.path.insert(0,".build")
from design import head, topbar, ICONS, CHEV

imgs = json.load(open(".build/imgs.json"))["tiny"]
thumbs = "".join(f'<div class="mini"><img src="data:image/jpeg;base64,{imgs[str(i)]}" alt=""></div>' for i in [1,7,11,16,24,27,15,9])

EXTRA = """
.hero{max-width:1280px;margin:0 auto;padding:56px 24px 8px;text-align:center}
.hero h1{font-size:clamp(32px,4.4vw,56px);line-height:1.18;letter-spacing:-.035em;margin:0 auto 16px;max-width:19ch}
.hero h1 em{font-style:normal;background:linear-gradient(180deg,transparent 62%,#FFE28A 62%);padding:0 4px}
.hero .lead{font-size:17.5px;color:var(--muted);max-width:60ch;margin:0 auto 26px;line-height:1.9}
.hero .cta{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-bottom:14px}
.btn-lg{height:42px;padding:0 24px;font-size:14.5px}
.hero .hint{font-size:12.5px;color:var(--faint)}
.hero .eyebrow{display:inline-flex;align-items:center;gap:7px;font-size:12px;font-weight:600;
  color:var(--muted);background:#fff;border:1px solid var(--line);border-radius:999px;
  padding:5px 12px;margin-bottom:20px;box-shadow:var(--sh-xs)}
.hero .eyebrow em{font-style:normal;width:6px;height:6px;border-radius:50%;background:#15A05E;
  box-shadow:0 0 0 3px rgba(21,160,94,.14);display:inline-block}
.wrap{max-width:1280px;margin:0 auto;padding:0 24px 70px}
.strip{display:grid;grid-template-columns:repeat(8,1fr);gap:10px;margin:38px 0 0}
.mini{aspect-ratio:16/9;border-radius:10px;overflow:hidden;border:1px solid var(--line);background:#eee;box-shadow:var(--sh-sm)}
.mini img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .4s}
.mini:hover img{transform:scale(1.06)}
.sec-title{display:flex;align-items:baseline;gap:12px;margin:56px 0 18px}
.sec-title h2{font-size:22px;margin:0}
.sec-title span{font-size:13px;color:var(--faint)}
.big{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px}
.bcard{border:1px solid var(--line);border-radius:var(--r-xl);background:#fff;padding:24px;
  box-shadow:var(--sh-sm);transition:.18s;display:flex;flex-direction:column;gap:8px}
.cmdbar{border:1px solid var(--line);border-radius:var(--r-xl);background:#fff;
  box-shadow:var(--sh-sm);margin:26px 0 0;overflow:hidden}
.cmdtabs{display:flex;gap:4px;direction:ltr;padding:8px 10px;border-bottom:1px solid var(--line2);
  background:var(--soft)}
.cmdtabs span{font-size:11.5px;padding:4px 10px;border-radius:7px;color:var(--muted);
  direction:ltr;font-family:ui-monospace,monospace;cursor:default}
.cmdtabs span.cur{background:#fff;color:var(--fg);box-shadow:var(--sh-sm);font-weight:600}
.cmdline{display:flex;align-items:center;gap:12px;padding:12px 14px;direction:ltr}
.cmdline code{background:transparent;border:0;font-size:13px;padding:0;flex:1;
  color:#243038;white-space:nowrap;overflow:auto}
.copycmd{background:var(--fg);color:#fff;border:0;border-radius:8px;padding:6px 14px;
  font-family:inherit;font-size:12px;font-weight:600;cursor:pointer;transition:.15s;flex-shrink:0}
.copycmd:hover{background:#000}
.cmdfoot{display:flex;align-items:center;gap:8px;direction:rtl;font-size:12.5px;color:var(--muted);
  padding:9px 14px;border-top:1px solid var(--line2);background:#FCFCFD}
.cmdfoot svg{color:var(--accent)}
.bcard{border:1px solid var(--line);border-radius:var(--r-xl);background:#fff;padding:24px;
  box-shadow:var(--sh-sm);transition:.18s;display:flex;flex-direction:column;gap:8px}

.cardrow a{display:block;transition:background .15s}
.cardrow a:hover{background:#FCFCFD}
.cardrow a .ico{width:38px;height:38px;border-radius:10px;background:var(--soft);display:grid;place-items:center;font-size:16px;margin-bottom:6px}
.bcard h3{font-size:16px}
.bcard p{font-size:13.5px;color:var(--muted);margin:0;flex-grow:1}
.bcard .go{font-size:13px;font-weight:600;color:var(--accent);margin-top:6px}
.steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;counter-reset:s}
.stepc{border:1px solid var(--line);border-radius:var(--r-lg);background:#fff;padding:18px}
.stepc:before{counter-increment:s;content:counter(s);display:grid;place-items:center;width:26px;height:26px;
  border-radius:8px;background:var(--fg);color:#fff;font-size:12px;font-weight:700;margin-bottom:10px}
.stepc h4{font-size:14px;margin:0 0 4px}
.stepc p{font-size:12.5px;color:var(--muted);margin:0}
.dark-cta{background:#0E0F10;color:#fff;border-radius:var(--r-xl);padding:38px 34px;margin-top:56px;
  display:flex;align-items:center;justify-content:space-between;gap:24px;flex-wrap:wrap}
.dark-cta h2{font-size:24px;margin:0 0 6px;color:#fff}
.dark-cta p{margin:0;color:#A7B1B6;font-size:14px}
@media(max-width:900px){.strip{grid-template-columns:repeat(4,1fr)}}
@media(max-width:560px){.strip{grid-template-columns:repeat(2,1fr)}.hero{padding:34px 16px 6px}}
"""

CONTENT = f'''
<section class="hero">
  <div class="eyebrow"><em></em> ۱۳ نمونه‌ی ساخته‌شده · ۳۰ سبک · فارسی و RTL</div>
  <h1>موشن‌گرافیک فارسی، با <em>حرف زدن</em> ساخته می‌شود</h1>
  <p class="lead">
    یک راهنمای کامل برای ساخت ویدیوی موشن با ایجنت آراِنا و Remotion — بدون خط کد.
    سبک را از ۳۰ زبان بصری انتخاب کن، متن و نریشن را بده، فایل MP4 را تحویل بگیر.
  </p>
  <div class="cta">
    <a class="btn accent btn-lg" href="آموزش-ساخت-موشن.html">شروع راهنمای ساخت</a>
    <a class="btn btn-lg" style="background:#fff;color:var(--fg);border-color:var(--line)" href="کاتالوگ-۳۰-سبک.html">دیدن ۳۰ سبک</a>
  </div>
  <div class="hint">رایگان · بدون نصب · خروجی فارسی و راست‌به‌چپ</div>
  <div class="strip">{thumbs}</div>
</section>

<div class="wrap">
  <div class="sec-title"><h2>از کجا شروع کنم؟</h2><span>دو مسیر، بسته به اینکه چه می‌دانی</span></div>
  <div class="cardrow">
    <a href="آموزش-ساخت-موشن.html">
      <div class="ico">{ICONS['book']}</div>
      <h3>راهنمای گام‌به‌گام</h3>
      <p>از ثبت‌نام در آراِنا تا فایل MP4، در هفت قدم با اسکرین‌شات واقعی از خود سایت.
         شامل پرامپت آماده، جدول آپلود فایل و عیب‌یابی.</p>
      <div class="tags"><span>7 steps</span></div>
    </a>
    <a href="کاتالوگ-۳۰-سبک.html">
      <div class="ico">{ICONS['palette']}</div>
      <h3>کاتالوگ ۳۰ سبک</h3>
      <p>سی زبان بصری با تصویر: از کینتیک تایپوگرافی و نئون تا کرافت، وکسل و اینفوگرافیک.
         سبک‌هایت را انتخاب کن و پرامپت آماده بگیر.</p>
      <div class="tags"><span>30 styles</span></div>
    </a>
    <a href="گزارش-سبک‌ها-و-ابزارهای-موشن.md">
      <div class="ico">{ICONS['spark']}</div>
      <h3>گزارش تحقیق</h3>
      <p>۲۲ سبک دیگر که می‌شود اضافه کرد، به‌همراه ابزارهای مکمل: پکیج‌های رسمی،
         کتابخانه‌های کامپوننت و موتورهای جایگزین.</p>
      <div class="tags"><span>MIT · 2026</span></div>
    </a>
  </div>

  <div class="cmdbar">
    <div class="cmdtabs">
      <span class="cur">npx create-video</span><span>npm run dev</span><span>npx remotion</span>
    </div>
    <div class="cmdline">
      <code dir="ltr">$ npx remotion render Daneh out/daneh.mp4</code>
      <button class="copycmd">کپی</button>
    </div>
    <div class="cmdfoot">
      {ICONS['spark']} توی ایجنت هم فقط کافی است بنویسی: «ویدیو را رندر کن و MP4 را بده».
    </div>
  </div>

  <div class="sec-title"><h2>مسیر در چهار قدم</h2><span>همان چیزی که در راهنما قدم‌به‌قدم می‌بینی</span></div>
  <div class="steps">
    <div class="stepc"><h4>سبک را انتخاب کن</h4><p>از کاتالوگ، شماره‌ی سبک و رنگ برندت را بردار.</p></div>
    <div class="stepc"><h4>پرامپت را پر کن</h4><p>شش بخش: موضوع، سبک، متن، فایل‌ها، مشخصات، وظایف ایجنت.</p></div>
    <div class="stepc"><h4>به ایجنت بده</h4><p>ایجنت Remotion را نصب می‌کند و ویدیو را می‌سازد.</p></div>
    <div class="stepc"><h4>MP4 را بردار</h4><p>نسخه‌ی افقی و عمودی، به‌همراه ZIP کل پروژه.</p></div>
  </div>

  <div class="dark-cta">
    <div>
      <h2>آماده‌ای اولین موشن را بسازی؟</h2>
      <p>حدود ۱۰ دقیقه وقت می‌برد. فقط یک جمله پیام و یک سبک لازم داری.</p>
    </div>
    <a class="btn accent btn-lg" href="آموزش-ساخت-موشن.html#s4">رفتن به پرامپت آماده</a>
  </div>
</div>'''

html = head("استودیوی موشن — ساخت موشن‌گرافیک فارسی با Remotion", EXTRA) + topbar("home") + CONTENT + \
 '''<footer class="site">استودیوی موشن · ساخته‌شده برای کاربران ایجنت آراِنا · موتور ویدیو: Remotion</footer>
<script>
document.querySelectorAll(".copycmd").forEach(function(b){
  b.addEventListener("click",function(){
    var t=document.querySelector(".cmdline code").innerText.replace(/^\$\s*/,"");
    var d=function(){b.textContent="کپی شد";setTimeout(function(){b.textContent="کپی";},1500);};
    if(navigator.clipboard){navigator.clipboard.writeText(t).then(d).catch(d);}else{d();}
  });
});
</script>
</body></html>'''
open("index.html","w").write(html)
print("home:", round(len(html)/1024), "KB")
