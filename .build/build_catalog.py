# -*- coding: utf-8 -*-
import json, sys
sys.path.insert(0,".build")
from design import head, topbar, ICONS

imgs = json.load(open(".build/imgs.json"))
BIG  = {int(k):v for k,v in imgs["big"].items()}
TINY = {int(k):v for k,v in imgs["tiny"].items()}

G = [
 ("A","تایپوگرافی","وقتی خودِ کلمه تصویر است",[
  (1,"کینتیک تایپوگرافی","Bold Kinetic Type","حروف درشت تمام‌صفحه با ورود فنری، ماسک و خروج پله‌ای. ریتم و ضربه.",["قدرت","ریتم","مدرن"],"تیزر، اعلان، لوگو-ریویل، ریلز","جزئیات زیاد، متن طولانی","e","ساده","BoldKinetic.mp4"),
  (2,"تایپوگرافی سه‌بعدی","3D Typography","حروف حجم‌دار با ضخامت، چرخش در فضا، نور و سایه‌ی واقعی روی لبه‌ها.",["حجم","لوکس","سینمایی"],"تیزر برند، تیتر فیلم، معرفی محصول","متن ریز، محتوای آموزشی","m","متوسط",None),
  (3,"ترمینال / CLI","Terminal / CLI","متن تک‌فاصله روی مشکی، تایپ کاراکتری، کورسور چشمک‌زن، پالت سبز فسفری.",["گیک","تکنیکال","مینیمال"],"محتوای توسعه‌دهنده، ابزار، امنیت","مخاطب عمومی، برند لوکس","e","ساده",None),
  (4,"انیمیشن کد","Code Animation","کد که تایپ می‌شود و بین دو نمونه مورف می‌شود، با هایلایت خط و حباب توضیح.",["آموزشی","دقیق","حرفه‌ای"],"آموزش برنامه‌نویسی، مستند فنی، معرفی API","مخاطب غیرفنی","e","ساده",None),
  (5,"زیرنویس تیک‌تاک","TikTok Captions","کلمه‌به‌کلمه ظاهر می‌شود، کلمه‌ی کلیدی بزرگ و رنگی، هم‌زمان با صدا.",["سریع","اعتیادآور","صامت‌پسند"],"ریلز، پادکست برشی، مصاحبه","ویدیوی رسمی، ارائه‌ی شرکتی","m","متوسط",None)]),
 ("B","دیجیتال","زبان بصری محصولات نرم‌افزاری",[
  (6,"گرادیان + شیشه","Glassmorphism","پس‌زمینه‌ی گرادیانی متحرک، کارت نیمه‌شفاف با بلور، مرز نورانی نازک.",["مدرن","نرم","دیجیتال"],"اپ و SaaS، پست محصول، استارتاپ","برند چاپی، نیاز به کنتراست بالا","e","ساده","GradientGlass.mp4"),
  (7,"شیشه‌ی مایع","Liquid Glass","نسل بعدی شیشه: اعوجاج سیال، عمق بازتابی، لبه‌های نور که با حرکت خم می‌شوند.",["۲۰۲۶","سیال","پرمیوم"],"تکنولوژی، AI، معرفی محصول پرچمدار","متن زیاد روی سطح شیشه","m","متوسط",None),
  (8,"نرم سینمایی","Soft Cinematic","کنتراست پایین، نور مه‌آلود، رنگ‌های خاکی-طلایی، حرکت بسیار آرام.",["آرام","گران","سینمایی"],"برند لوکس، مد، عطر، مستند","محتوای پرانرژی، فروش فوری","e","ساده",None),
  (9,"کلی / نرم سه‌بعدی","Claymorphism","حجم‌های پاستلی گرد با سایه‌ی دوگانه (نور و بازتاب)، حس لمس‌پذیر.",["دوستانه","نرم","کودکانه"],"اپ موبایل، کودک، سلامت، فین‌تک دوستانه","برند جدی، خبر، حقوقی","e","ساده","ClaySoft.mp4"),
  (10,"موشن رابط محصول","Product UI Motion","داشبورد یا موبایل واقعی که باز می‌شود، کلیک می‌خورد، داده‌اش لود می‌شود.",["دمو","قابل‌لمس","واقعی"],"SaaS، اپ، جذب سرمایه، آنبوردینگ","برند بدون محصول دیجیتال","m","متوسط",None)]),
 ("C","جسور","برای دیده‌شدن، نه برای آرامش",[
  (11,"نئو-بروتالیست","Neo-Brutalism","رنگ فلورسنت، حاشیه‌ی ضخیم مشکی، سایه‌ی آفست سخت، نوار متحرک و برچسب کج.",["جسور","خیابانی","پرسروصدا"],"برند جوان، وایرال، رویداد، فشن خیابانی","لوکس، مالی، رسمی","e","ساده","NeoBrutalist.mp4"),
  (12,"ممفیس / دهه ۹۰","Memphis 90s","شکل‌های هندسی تصادفی، رنگ سیتی، پترن هاچ، زیگزاگ و نقطه‌چین.",["نوستالژیک","شاد","بازیگوش"],"سرگرمی، فشن، موسیقی، طنز","Corporate، پزشکی، حقوقی","e","ساده","Memphis90s.mp4"),
  (13,"وای۲کی / رترو-فیوچر","Y2K / Retro-Future","کروم براق، پیکسل، هولوگرافیک، آیکون‌های ویندوز ۹۸، گرادیان نقره‌ای.",["نوستالژیک","فوتوریست","پیکسلی"],"موسیقی، گیم، مد، محتوای گیک","برند رسمی، B2B","e","ساده",None),
  (14,"گلیچ / دیتاموش","Glitch / Datamosh","شکست کانال رنگ، پارگی تصویر، تایپ خراب، پرش فریم عمدی.",["آوانگارد","خشن","غیرمنتظره"],"موسیقی الکترونیک، امنیت، آرت‌هاوس","سلامت، آموزش، برند خانوادگی","m","متوسط",None),
  (15,"نئون / سایبرپانک","Neon / Cyberpunk","مشکی-آبی، خطوط نئونی، درخشش، اسکن‌لاین، شبکه‌ی پرسپکتیو.",["آینده","شبانه","انرژی"],"موسیقی الکترونیک، گیم، AI، رویداد شبانه","آموزش آرام، برند سنتی","e","ساده","NeonFuturistic.mp4")]),
 ("D","بافت","واکنش به کمالِ مصنوعی",[
  (16,"بافت کاغذ / کلاژ","Paper Collage","کاغذ دانه‌دار، کارت چرخیده، چسب کاغذی، خط دستی قرمز.",["انسانی","گرم","مجله‌ای"],"برند شخصی، پادکست، رویداد هنری","محتوای تکنیکال و سریع","e","ساده","PaperCollage.mp4"),
  (17,"کرافت / کارگاه","Kraft Artisan","کاغذ کرافت قهوه‌ای، کارت زغالی، مهر گرد، حس دست‌ساز و گرم.",["دست‌ساز","اصل","گرم"],"کافه، قهوه، نان، محصول دست‌ساز","تکنولوژی، فین‌تک، فضای سرد","e","ساده","KraftStudio.mp4"),
  (18,"دست‌کشیده / اسکچ","Hand-drawn / Sketch","خط لرزان، فلش دستی، دایره‌ی نامنظم، بافت مداد و کاغذ.",["صمیمی","آموزشی","انسانی"],"توضیح مفهوم، آموزش، وایت‌بورد","برند لوکس، محصول پریمیوم","m","متوسط",None),
  (19,"کاغذ بریده / استاپ‌موشن","Paper Cutout","عناصر بریده‌شده با لبه‌ی ناهموار که پله‌پله حرکت می‌کنند، نه نرم.",["دست‌ساز","کودکانه","قصه‌گو"],"روایت، آموزش کودک، برند فرهنگی","محتوای فوری، فروش","m","متوسط",None),
  (20,"مدیای ترکیبی","Mixed Media","فوتیج واقعی که گرافیک رویش می‌نشیند: دایره‌ی رنگی، متن، خط، بریده‌ی روزنامه.",["مستند","معتبر","۲۰۲۶"],"برند کمپین، مستند کوتاه، مصاحبه","وقتی فوتیج در دسترس نیست","m","متوسط",None)]),
 ("E","سینمایی","عمق، دوربین، و حرکت در فضا",[
  (21,"عمق پارالاکس","Parallax Depth","چند لایه با سرعت‌های متفاوت؛ دوربین آرام حرکت می‌کند و عمق ساخته می‌شود.",["سینمایی","عمق","آرام"],"روایت، معرفی کسب‌وکار، ویدیوی شهری","متن زیاد، اطلاعات فنی","e","ساده",None),
  (22,"دانه‌ی فیلم / نشت نور","Film Grain","دانه‌ی آنالوگ روی همه‌چیز، نشت نور گرم، وینیت، حس ۱۶ میلی‌متری.",["آنالوگ","گرم","نوستالژیک"],"موسیقی، مد، عکاسی، تیزر احساسی","داشبورد داده، محتوای دقیق","e","ساده",None),
  (23,"ترکیب دوبعدی و سه‌بعدی","Hybrid 2D + 3D","شکل تخت دوبعدی روی صحنه‌ی سه‌بعدی، یا خط‌قلم روی حجم واقعی.",["۲۰۲۶","غنی","متمایز"],"برند تکنولوژی، تیزر رویداد، توضیح محصول","تولید سریع و کم‌بودجه","h","سنگین",None),
  (24,"وکسل / ایزومتریک","Voxel 3D","مکعب‌های سه‌بعدی پاستلی که آرام می‌چرخند و شناور می‌مانند.",["بازیگوش","حجم","گیک"],"آموزش، گیم، تکنولوژی دوستانه","متن طولانی، برند مینیمال","m","متوسط","Voxel3D.mp4"),
  (25,"انیمیشن نقشه","Map Animation","دوربین روی نقشه پرواز می‌کند، مسیر کشیده می‌شود، پین‌ها می‌افتند.",["مکانی","سفر","داده"],"لجستیک، سفر، املاک، خبر منطقه‌ای","وقتی موقعیت مهم نیست","h","سنگین",None)]),
 ("F","داده و ادیتوریال","وقتی پیام باید فهمیده شود، نه فقط حس شود",[
  (26,"مینیمال ادیتوریال","Minimal Editorial","کاغذ روشن، خط نازک، فضای خالی زیاد، ورود خط‌به‌خط از پشت ماسک.",["آرام","باکلاس","حرفه‌ای"],"برند شخصی، مستند، آموزشی، شرکتی","سرگرمی پرانرژی، تخفیف فوری","e","ساده","MinimalEditorial.mp4"),
  (27,"سوئیسی / گرید","Swiss Grid","گرید دقیق، قرمز و مشکی روی سفید، چیدمان نامتقارن کنترل‌شده، تایپ بی‌تزئین.",["نظم","دقت","بی‌زمان"],"معماری، موزه، طراحی صنعتی، لوکس مینیمال","کودک، محتوای شاد و پرجزئیات","e","ساده","SwissGrid.mp4"),
  (28,"تخت مدرن","Corporate Flat","شکل‌های هندسی ساده، رنگ تخت، بدون گرادیان و سایه‌ی نرم.",["قابل‌اعتماد","ساده","روشن"],"شرکتی، آموزشی، ارائه، اینفوگرافیک","برند هنری و شخصیت‌محور","e","ساده","FlatCorporate.mp4"),
  (29,"اینفوگرافیک / داده","Data Infographic","میله و حلقه‌ی متحرک، عدد شمارشی، شبکه‌ی ظریف، کارت‌های آماری.",["اعتماد","شفافیت","عدد"],"گزارش سالانه، خبر، B2B، آموزش","تیزر زیر ۵ ثانیه","e","ساده","InfographicData.mp4"),
  (30,"ویژوالایزر صدا","Audio Visualization","موج صوتی که با صدای واقعی می‌رقصد، کاور، زیرنویس و بک‌گراند تیره.",["صوتی","زنده","پادکستی"],"پادکست، موسیقی، کلیپ صوتی، رادیو","ویدیوی بی‌صدا","m","متوسط",None)]),
]

def card(s):
    n,fa,en,d,tags,best,avoid,dc,dn,bfile = s
    tagh="".join(f"<i>{t}</i>" for t in tags)
    badge = '<span class="chip ok">نمونه‌ی ساخته‌شده</span>' if bfile else '<span class="chip ref">تصویر مرجع</span>'
    return f'''
    <article class="tcard" data-g="{fa}" data-en="{en}" data-diff="{dc}" data-built="{'1' if bfile else '0'}"
             data-tags="{' '.join(tags)}" data-best="{best}" data-n="{n}">
      <div class="thumb">
        <img loading="lazy" src="data:image/jpeg;base64,{TINY[n]}" data-full="data:image/jpeg;base64,{BIG[n]}" alt="{fa}">
        <span class="idx">{n:02d}</span>
        <span class="lvl {dc}"><i></i>{dn}</span>
      </div>
      <div class="tbody">
        <div class="thead">
          <h3>{fa}</h3>
          <span class="en">{en}</span>
        </div>
        <p>{d}</p>
        <dl class="meta">
          <div><dt>مناسب</dt><dd>{best}</dd></div>
          <div><dt class="no">پرهیز</dt><dd>{avoid}</dd></div>
        </dl>
        <div class="tfoot">
          {badge}
          <div class="tags">{tagh}</div>
          <button class="pick" data-n="{n}" data-name="{fa}">انتخاب</button>
        </div>
      </div>
    </article>'''

SECTIONS = ""
for code,title,sub,styles in G:
    SECTIONS += f'''
  <section class="grp" data-code="{code}">
    <div class="ghead">
      <span class="gcode">{code}</span>
      <div><h2>{title}</h2><div class="gsub">{sub}</div></div>
      <span class="gcount">{len(styles)} سبک</span>
    </div>
    <div class="tgrid">{"".join(card(s) for s in styles)}</div>
  </section>'''

SIDEBAR = f'''
<aside class="sidebar">
  <div class="side-group">
    <div class="side-label">{ICONS['palette']} خانواده‌های بصری</div>
    <div class="side" id="famnav">
      <a href="#gA">تایپوگرافی <span class="cnt">۵</span></a>
      <a href="#gB">دیجیتال و رابط کاربری <span class="cnt">۵</span></a>
      <a href="#gC">جسور و خیابانی <span class="cnt">۵</span></a>
      <a href="#gD">بافت و دست‌ساز <span class="cnt">۵</span></a>
      <a href="#gE">سینمایی و فضایی <span class="cnt">۵</span></a>
      <a href="#gF">داده و ادیتوریال <span class="cnt">۵</span></a>
    </div>
  </div>
  <div class="side-group">
    <div class="side-label">{ICONS['grid']} فیلتر سریع</div>
    <div class="side">
      <a href="#" data-f="all" class="on">همه‌ی سبک‌ها <span class="cnt">۳۰</span></a>
      <a href="#" data-f="de">ساده <span class="cnt">۱۸</span></a>
      <a href="#" data-f="dm">متوسط <span class="cnt">۹</span></a>
      <a href="#" data-f="dh">سنگین <span class="cnt">۳</span></a>
      <a href="#" data-f="b1">فقط ساخته‌شده‌ها <span class="cnt">۱۳</span></a>
    </div>
  </div>
  <div class="side-group">
    <div class="side-label">{ICONS['book']} مرتبط</div>
    <div class="side">
      <a href="آموزش-ساخت-موشن.html">راهنمای ساخت</a>
      <a href="آموزش-ساخت-موشن.html#s4">پرامپت آماده <span class="pill">مهم</span></a>
    </div>
  </div>
</aside>'''

CONTENT = f'''
<div class="doc">
  <div class="crumbs">کاتالوگ <span>/</span> <b>۳۰ سبک گرافیکی</b></div>
  <h1>۳۰ سبک گرافیکی موشن</h1>
  <p class="lead">
    هر سبک با تصویر. ۱۳ موردِ «نمونه‌ی ساخته‌شده» رندر واقعی از پروژه است؛
    ۱۷ موردِ «تصویر مرجع» از نمونه‌های صنعت برداشته شده تا حس و زبان بصری را نشان دهد.
    سبک‌های مورد علاقه‌ات را انتخاب کن تا پرامپت آماده‌ی ساخت بگیری.
  </p>

  <div class="searchbar">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>
    <input id="q" type="search" placeholder="جست‌وجو: کافه، لوکس، ریتم، آموزش…">
    <span class="cnt" id="cnt">۳۰ سبک</span>
  </div>

  {SECTIONS}

  <div class="cta-card" style="margin-top:44px">
    <div>
      <h3 style="margin:0 0 4px">بعد از انتخاب چه کنم؟</h3>
      <p style="margin:0;font-size:13.5px;color:var(--muted)">
        سبک‌ها را با دکمه‌ی «انتخاب» علامت بزن، بعد پرامپت آماده را بگیر و در ایجنت بچسبان.</p>
    </div>
    <a class="btn accent" href="آموزش-ساخت-موشن.html#s4">رفتن به پرامپت</a>
  </div>
</div>'''

RAIL = '''
<aside class="rail">
  <div class="rail-card">
    <h4>راهنمای انتخاب</h4>
    <p>سه کلمه‌ای که برندت باید منتقل کند را بنویس؛ بعد ببین کدام کلیدواژه به آن نزدیک‌تر است.</p>
    <p style="color:var(--fg)"><b>گرم، اصل، دست‌ساز</b> → کرافت<br>
    <b>سریع، جسور، خیابانی</b> → بروتالیست<br>
    <b>دقیق، بی‌زمان، آرام</b> → سوئیسی</p>
  </div>
  <div class="rail-card dark">
    <h4 style="color:#fff">انتخاب‌های تو</h4>
    <p id="railpicks">هنوز چیزی انتخاب نکردی.</p>
    <button class="btn" id="raingo" style="background:#fff;color:#0E1012;border-color:#fff;width:100%;justify-content:center">ساخت پرامپت</button>
  </div>
  <div class="rail-card">
    <h4>یادت باشد</h4>
    <p>سبک = ترکیب‌بندی، حرکت و بافت.<br>رنگ و فونت = برند تو.</p>
  </div>
</aside>'''

EXTRA = """
.side a[data-f]{cursor:pointer}
.searchbar{display:flex;align-items:center;gap:10px;border:1px solid var(--line);background:#fff;
  border-radius:var(--r);padding:10px 14px;margin:20px 0 6px;box-shadow:var(--sh-sm);color:var(--faint)}
.searchbar input{flex:1;border:0;outline:0;font-family:inherit;font-size:14px;color:var(--fg);background:transparent}
.searchbar input::placeholder{color:var(--faint)}
.searchbar .cnt{font-size:12px;color:var(--faint);white-space:nowrap;font-variant-numeric:tabular-nums}
.grp{margin-top:44px;scroll-margin-top:86px}
.grp.hide{display:none}
.ghead{display:flex;align-items:center;gap:12px;margin-bottom:16px}
.gcode{width:30px;height:30px;border-radius:9px;background:var(--soft);color:var(--fg);
  display:grid;place-items:center;font-weight:800;font-size:13px;flex-shrink:0;border:1px solid var(--line)}
.ghead h2{font-size:19px;margin:0}
.gsub{font-size:12.5px;color:var(--faint)}
.gcount{margin-inline-start:auto;font-size:11.5px;color:var(--faint);border:1px solid var(--line);
  padding:3px 10px;border-radius:999px;background:#fff}
.tgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:16px}
.tcard{border:1px solid var(--line);border-radius:var(--r-lg);background:#fff;overflow:hidden;
  display:flex;flex-direction:column;transition:.16s;box-shadow:var(--sh-sm)}
.tcard:hover{box-shadow:var(--sh);border-color:rgba(14,16,18,.18);transform:translateY(-2px)}
.tcard.hide{display:none}
.tcard.picked{border-color:#15A05E;box-shadow:0 0 0 1px #15A05E,var(--sh)}
.thumb{position:relative;aspect-ratio:16/9;background:#F0F1F2;border-bottom:1px solid var(--line2)}
.thumb img{width:100%;height:100%;object-fit:cover;display:block}
.idx{position:absolute;top:9px;right:9px;background:rgba(14,16,18,.82);color:#fff;font-size:11px;
  font-weight:700;padding:2px 8px;border-radius:6px;direction:ltr;backdrop-filter:blur(4px)}
.lvl{position:absolute;bottom:9px;left:9px;display:inline-flex;align-items:center;gap:5px;
  background:rgba(255,255,255,.94);color:#243038;font-size:10.5px;font-weight:600;
  padding:2px 9px;border-radius:999px;box-shadow:0 1px 3px rgba(0,0,0,.15)}
.lvl i{width:6px;height:6px;border-radius:50%;display:block}
.lvl.e i{background:#15A05E}.lvl.m i{background:#D99B12}.lvl.h i{background:#DC4C3E}
.tbody{padding:14px 16px 14px;display:flex;flex-direction:column;flex-grow:1}
.thead h3{font-size:15px;margin:0}
.thead .en{font-size:10.5px;letter-spacing:.09em;text-transform:uppercase;color:var(--faint);
  direction:ltr;text-align:right;display:block;margin-bottom:6px}
.tbody p{font-size:12.8px;color:var(--muted);line-height:1.75;margin:0 0 10px;flex-grow:1}
.meta{margin:0 0 10px;display:flex;flex-direction:column;gap:4px}
.meta div{display:flex;gap:7px;font-size:12px;line-height:1.6}
.meta dt{flex:0 0 34px;font-size:10.5px;font-weight:700;color:#15A05E;padding-top:2px}
.meta dt.no{color:#DC4C3E}
.meta dd{margin:0;color:#374247}
.tfoot{display:flex;align-items:center;gap:6px;flex-wrap:wrap;padding-top:10px;border-top:1px solid var(--line2)}
.chip{font-size:9.5px;font-weight:700;padding:2px 8px;border-radius:999px}
.chip.ok{background:var(--green-soft);color:var(--green);border:1px solid #CFE8DA}
.chip.ref{background:var(--soft);color:var(--muted);border:1px solid var(--line2)}
.tags{display:flex;gap:4px;flex-wrap:wrap}
.tags i{font-style:normal;font-size:9.5px;color:var(--faint);background:var(--soft);padding:2px 7px;border-radius:5px}
.pick{margin-inline-start:auto;border:1px solid var(--line);background:#fff;color:var(--muted);
  border-radius:7px;padding:4px 11px;font-size:11px;font-family:inherit;cursor:pointer;transition:.14s;font-weight:600}
.pick:hover{background:var(--fg);color:#fff;border-color:var(--fg)}
.tcard.picked .pick{background:#15A05E;border-color:#15A05E;color:#fff}
@media(max-width:520px){.tgrid{grid-template-columns:1fr}}
"""

JS = """
(function(){
  var picked={}, cards=[].slice.call(document.querySelectorAll(".tcard")),
      groups=[].slice.call(document.querySelectorAll(".grp")),
      q=document.getElementById("q"), cnt=document.getElementById("cnt"),
      famLinks=[].slice.call(document.querySelectorAll("#famnav a")),
      fLinks=[].slice.call(document.querySelectorAll('.side a[data-f]'));
  function apply(){
    var t=(q.value||"").trim().toLowerCase(), act=fLinks.filter(function(a){return a.classList.contains("on");})
        .map(function(a){return a.dataset.f;}), shown=0;
    cards.forEach(function(c){
      var okT=!t||(c.dataset.g+" "+c.dataset.en+" "+c.dataset.tags+" "+c.dataset.best).toLowerCase().indexOf(t)>-1;
      var diffs=act.filter(function(f){return f[0]==="d";});
      var okD=diffs.length===0||diffs.indexOf("d"+c.dataset.diff)>-1;
      var okB=act.indexOf("b1")===-1||c.dataset.built==="1";
      var ok=okT&&okD&&okB; c.classList.toggle("hide",!ok); if(ok) shown++;
    });
    groups.forEach(function(g){g.classList.toggle("hide",g.querySelectorAll(".tcard:not(.hide)").length===0);});
    cnt.textContent=shown+" سبک";
  }
  q.addEventListener("input",apply);
  fLinks.forEach(function(a){
    a.addEventListener("click",function(e){
      e.preventDefault(); var f=a.dataset.f;
      if(f==="all"){fLinks.forEach(function(x){x.classList.remove("on");});a.classList.add("on");}
      else{document.querySelector('.side a[data-f="all"]').classList.remove("on");a.classList.toggle("on");}
      apply();
    });
  });
  function renderPicks(){
    var ks=Object.keys(picked);
    document.getElementById("railpicks").innerHTML = ks.length
      ? ks.sort(function(a,b){return a-b;}).map(function(k){return picked[k];}).join("<br>")
      : "هنوز چیزی انتخاب نکردی.";
  }
  document.querySelectorAll(".pick").forEach(function(b){
    b.addEventListener("click",function(){
      var n=b.dataset.n;
      if(picked[n]){delete picked[n];b.textContent="انتخاب";}
      else{picked[n]=n.padStart(2,"0")+" · "+b.dataset.name;b.textContent="✓ انتخاب شد";}
      b.closest(".tcard").classList.toggle("picked",!!picked[n]); renderPicks();
    });
  });
  document.getElementById("raingo").addEventListener("click",function(){
    var ks=Object.keys(picked).sort(function(a,b){return a-b;});
    var txt=ks.length
      ? "سبک‌های انتخابی من از کاتالوگ: "+ks.map(function(k){return k+" ("+picked[k].split(" · ")[1]+")";}).join(" ، ")+". بر اساس این سبک‌ها برایم یک موشن‌گرافیک ۸ ثانیه‌ای بساز."
      : "یک موشن‌گرافیک ۸ ثانیه‌ای با Remotion بساز؛ سبک را از کاتالوگ ۳۰ سبکی پیشنهاد بده.";
    if(navigator.clipboard&&navigator.clipboard.writeText){
      navigator.clipboard.writeText(txt).then(function(){location.href="آموزش-ساخت-موشن.html#s4";});
    } else location.href="آموزش-ساخت-موشن.html#s4";
  });
  cards.forEach(function(c){
    var i=c.querySelector("img");
    c.addEventListener("mouseenter",function(){if(i.dataset.full&&i.src!==i.dataset.full)i.src=i.dataset.full;});
  });
  // map group code -> anchor id
  groups.forEach(function(g,i){g.id="g"+g.dataset.code;});
  apply();
})();
"""

html = head("کاتالوگ ۳۰ سبک گرافیکی موشن", EXTRA) + topbar("catalog") + \
  f'<div class="shell">{SIDEBAR}<main class="content">{CONTENT}</main>{RAIL}</div>' + \
  f'''<footer class="site">۳۰ سبک گرافیکی · ۱۳ نمونه‌ی ساخته‌شده · ۱۷ تصویر مرجع</footer>
<script>{JS}</script>
</body></html>'''
open("کاتالوگ-۳۰-سبک.html","w").write(html)
print("catalog:", round(len(html)/1024/1024,2), "MB")
