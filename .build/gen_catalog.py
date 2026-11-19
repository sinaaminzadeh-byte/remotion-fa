# -*- coding: utf-8 -*-
import json
imgs = json.load(open(".build/imgs.json"))
BIG = {int(k):v for k,v in imgs["big"].items()}
TINY = {int(k):v for k,v in imgs["tiny"].items()}

G = [
 ("A","تایپوگرافی و متن‌محور","وقتی خودِ کلمه تصویر است",[
  (1,"کینتیک تایپوگرافی","Bold Kinetic Type","حروف درشت تمام‌صفحه با ورود فنری، ماسک و خروج پله‌ای. ریتم و ضربه.",["قدرت","ریتم","مدرن"],"تیزر، اعلان، لوگو-ریویل، ریلز","جزئیات زیاد، متن طولانی","🟢","BoldKinetic.mp4"),
  (2,"تایپوگرافی سه‌بعدی","3D Typography","حروف حجم‌دار با ضخامت، چرخش در فضا، نور و سایه‌ی واقعی روی لبه‌ها.",["حجم","لوکس","سینمایی"],"تیزر برند، تیتر فیلم، معرفی محصول","متن ریز، محتوای آموزشی","🟡",None),
  (3,"ترمینال / CLI","Terminal / CLI","متن تک‌فاصله روی مشکی، تایپ کاراکتری، کورسور چشمک‌زن، پالت سبز فسفری.",["گیک","تکنیکال","مینیمال"],"محتوای توسعه‌دهنده، ابزار، امنیت","مخاطب عمومی، برند لوکس","🟢",None),
  (4,"انیمیشن کد","Code Animation","کد که تایپ می‌شود و بین دو نمونه مورف می‌شود، با هایلایت خط و حباب توضیح.",["آموزشی","دقیق","حرفه‌ای"],"آموزش برنامه‌نویسی، مستند فنی، معرفی API","مخاطب غیرفنی","🟢",None),
  (5,"زیرنویس تیک‌تاک","TikTok Captions","کلمه‌به‌کلمه ظاهر می‌شود، کلمه‌ی کلیدی بزرگ و رنگی، هم‌زمان با صدا.",["سریع","اعتیادآور","صامت‌پسند"],"ریلز، پادکست برشی، مصاحبه","ویدیوی رسمی، ارائه‌ی شرکتی","🟡",None)]),
 ("B","دیجیتال و رابط کاربری","زبان بصری محصولات نرم‌افزاری",[
  (6,"گرادیان + شیشه","Glassmorphism","پس‌زمینه‌ی گرادیانی متحرک، کارت نیمه‌شفاف با بلور، مرز نورانی نازک.",["مدرن","نرم","دیجیتال"],"اپ و SaaS، پست محصول، استارتاپ","برند چاپی، نیاز به کنتراست بالا","🟢","GradientGlass.mp4"),
  (7,"شیشه‌ی مایع","Liquid Glass","نسل بعدی شیشه: اعوجاج سیال، عمق بازتابی، لبه‌های نور که با حرکت خم می‌شوند.",["۲۰۲۶","سیال","پرمیوم"],"تکنولوژی، AI، معرفی محصول پرچمدار","متن زیاد روی سطح شیشه","🟡",None),
  (8,"نرم سینمایی","Soft Cinematic","کنتراست پایین، نور مه‌آلود، رنگ‌های خاکی-طلایی، حرکت بسیار آرام.",["آرام","گران","سینمایی"],"برند لوکس، مد، عطر، مستند","محتوای پرانرژی، فروش فوری","🟢",None),
  (9,"کلی / نرم سه‌بعدی","Claymorphism","حجم‌های پاستلی گرد با سایه‌ی دوگانه (نور و بازتاب)، حس لمس‌پذیر.",["دوستانه","نرم","کودکانه"],"اپ موبایل، کودک، سلامت، فین‌تک دوستانه","برند جدی، خبر، حقوقی","🟢","ClaySoft.mp4"),
  (10,"موشن رابط محصول","Product UI Motion","داشبورد یا موبایل واقعی که باز می‌شود، کلیک می‌خورد، داده‌اش لود می‌شود.",["دمو","قابل‌لمس","واقعی"],"SaaS، اپ، جذب سرمایه، آنبوردینگ","برند بدون محصول دیجیتال","🟡",None)]),
 ("C","جسور و خیابانی","برای دیده‌شدن، نه برای آرامش",[
  (11,"نئو-بروتالیست","Neo-Brutalism","رنگ فلورسنت، حاشیه‌ی ضخیم مشکی، سایه‌ی آفست سخت، نوار متحرک و برچسب کج.",["جسور","خیابانی","پرسروصدا"],"برند جوان، وایرال، رویداد، فشن خیابانی","لوکس، مالی، رسمی","🟢","NeoBrutalist.mp4"),
  (12,"ممفیس / دهه ۹۰","Memphis 90s","شکل‌های هندسی تصادفی، رنگ سیتی، پترن هاچ، زیگزاگ و نقطه‌چین.",["نوستالژیک","شاد","بازیگوش"],"سرگرمی، فشن، موسیقی، طنز","Corporate، پزشکی، حقوقی","🟢","Memphis90s.mp4"),
  (13,"وای۲کی / رترو-فیوچر","Y2K / Retro-Future","کروم براق، پیکسل، هولوگرافیک، آیکون‌های ویندوز ۹۸، گرادیان نقره‌ای.",["نوستالژیک","فوتوریست","پیکسلی"],"موسیقی، گیم، مد، محتوای گیک","برند رسمی، B2B","🟢",None),
  (14,"گلیچ / دیتاموش","Glitch / Datamosh","شکست کانال رنگ، پارگی تصویر، تایپ خراب، پرش فریم عمدی.",["آوانگارد","خشن","غیرمنتظره"],"موسیقی الکترونیک، امنیت، آرت‌هاوس","سلامت، آموزش، برند خانوادگی","🟡",None),
  (15,"نئون / سایبرپانک","Neon / Cyberpunk","مشکی-آبی، خطوط نئونی، درخشش، اسکن‌لاین، شبکه‌ی پرسپکتیو.",["آینده","شبانه","انرژی"],"موسیقی الکترونیک، گیم، AI، رویداد شبانه","آموزش آرام، برند سنتی","🟢","NeonFuturistic.mp4")]),
 ("D","بافت و دست‌ساز","واکنش به کمالِ مصنوعی",[
  (16,"بافت کاغذ / کلاژ","Paper Collage","کاغذ دانه‌دار، کارت چرخیده، چسب کاغذی، خط دستی قرمز.",["انسانی","گرم","مجله‌ای"],"برند شخصی، پادکست، رویداد هنری","محتوای تکنیکال و سریع","🟢","PaperCollage.mp4"),
  (17,"کرافت / کارگاه","Kraft Artisan","کاغذ کرافت قهوه‌ای، کارت زغالی، مهر گرد، حس دست‌ساز و گرم.",["دست‌ساز","اصل","گرم"],"کافه، قهوه، نان، محصول دست‌ساز","تکنولوژی، فین‌تک، فضای سرد","🟢","KraftStudio.mp4"),
  (18,"دست‌کشیده / اسکچ","Hand-drawn / Sketch","خط لرزان، فلش دستی، دایره‌ی نامنظم، بافت مداد و کاغذ.",["صمیمی","آموزشی","انسانی"],"توضیح مفهوم، آموزش، وایت‌بورد","برند لوکس، محصول پریمیوم","🟡",None),
  (19,"کاغذ بریده / استاپ‌موشن","Paper Cutout","عناصر بریده‌شده با لبه‌ی ناهموار که پله‌پله حرکت می‌کنند، نه نرم.",["دست‌ساز","کودکانه","قصه‌گو"],"روایت، آموزش کودک، برند فرهنگی","محتوای فوری، فروش","🟡",None),
  (20,"مدیای ترکیبی","Mixed Media","فوتیج واقعی که گرافیک رویش می‌نشیند: دایره‌ی رنگی، متن، خط، بریده‌ی روزنامه.",["مستند","معتبر","۲۰۲۶"],"برند کمپین، مستند کوتاه، مصاحبه","وقتی فوتیج در دسترس نیست","🟡",None)]),
 ("E","سینمایی و فضایی","عمق، دوربین، و حرکت در فضا",[
  (21,"عمق پارالاکس","Parallax Depth","چند لایه با سرعت‌های متفاوت؛ دوربین آرام حرکت می‌کند و عمق ساخته می‌شود.",["سینمایی","عمق","آرام"],"روایت، معرفی کسب‌وکار، ویدیوی شهری","متن زیاد، اطلاعات فنی","🟢",None),
  (22,"دانه‌ی فیلم / نشت نور","Film Grain / Light Leak","دانه‌ی آنالوگ روی همه‌چیز، نشت نور گرم، وینیت، حس ۱۶ میلی‌متری.",["آنالوگ","گرم","نوستالژیک"],"موسیقی، مد، عکاسی، تیزر احساسی","داشبورد داده، محتوای دقیق","🟢",None),
  (23,"ترکیب دوبعدی و سه‌بعدی","Hybrid 2D + 3D","شکل تخت دوبعدی روی صحنه‌ی سه‌بعدی، یا خط‌قلم روی حجم واقعی.",["۲۰۲۶","غنی","متمایز"],"برند تکنولوژی، تیزر رویداد، توضیح محصول","تولید سریع و کم‌بودجه","🔴",None),
  (24,"وکسل / ایزومتریک","Voxel / Isometric 3D","مکعب‌های سه‌بعدی پاستلی که آرام می‌چرخند و شناور می‌مانند.",["بازیگوش","حجم","گیک"],"آموزش، گیم، تکنولوژی دوستانه","متن طولانی، برند مینیمال","🟡","Voxel3D.mp4"),
  (25,"انیمیشن نقشه","Map Animation","دوربین روی نقشه پرواز می‌کند، مسیر کشیده می‌شود، پین‌ها می‌افتند.",["مکانی","سفر","داده"],"لجستیک، سفر، املاک، خبر منطقه‌ای","وقتی موقعیت مهم نیست","🔴",None)]),
 ("F","ادیتوریال، داده و صوت","وقتی پیام باید فهمیده شود، نه فقط حس شود",[
  (26,"مینیمال ادیتوریال","Minimal Editorial","کاغذ روشن، خط نازک، فضای خالی زیاد، ورود خط‌به‌خط از پشت ماسک.",["آرام","باکلاس","حرفه‌ای"],"برند شخصی، مستند، آموزشی، شرکتی","سرگرمی پرانرژی، تخفیف فوری","🟢","MinimalEditorial.mp4"),
  (27,"سوئیسی / گرید","Swiss / International","گرید دقیق، قرمز و مشکی روی سفید، چیدمان نامتقارن کنترل‌شده، تایپ بی‌تزئین.",["نظم","دقت","بی‌زمان"],"معماری، موزه، طراحی صنعتی، لوکس مینیمال","کودک، محتوای شاد و پرجزئیات","🟢","SwissGrid.mp4"),
  (28,"تخت مدرن","Corporate Flat","شکل‌های هندسی ساده، رنگ تخت، بدون گرادیان و سایه‌ی نرم.",["قابل‌اعتماد","ساده","روشن"],"شرکتی، آموزشی، ارائه، اینفوگرافیک","برند هنری و شخصیت‌محور","🟢","FlatCorporate.mp4"),
  (29,"اینفوگرافیک / داده","Data Infographic","میله و حلقه‌ی متحرک، عدد شمارشی، شبکه‌ی ظریف، کارت‌های آماری.",["اعتماد","شفافیت","عدد"],"گزارش سالانه، خبر، B2B، آموزش","تیزر زیر ۵ ثانیه","🟢","InfographicData.mp4"),
  (30,"ویژوالایزر صدا / پادکست","Audio Visualization","موج صوتی که با صدای واقعی می‌رقصد، کاور، زیرنویس و بک‌گراند تیره.",["صوتی","زنده","پادکستی"],"پادکست، موسیقی، کلیپ صوتی، رادیو","ویدیوی بی‌صدا","🟡",None)]),
]

def card(s):
    n,fa,en,d,tags,best,avoid,diff,bfile = s
    tagh="".join(f"<i>{t}</i>" for t in tags)
    badge='<span class="tag ok">نمونه‌ی ساخت ما</span>' if bfile else '<span class="tag ref">تصویر مرجع</span>'
    diffcls = {"🟢":"e","🟡":"m","🔴":"h"}[diff]
    diffname = {"🟢":"ساده","🟡":"متوسط","🔴":"سنگین"}[diff]
    return f'''
    <article class="card" data-g="{fa}" data-en="{en}" data-diff="{diffcls}" data-built="{'1' if bfile else '0'}"
             data-tags="{' '.join(tags)}" data-best="{best}">
      <div class="thumb">
        <img loading="lazy" src="data:image/jpeg;base64,{TINY[n]}" data-full="data:image/jpeg;base64,{BIG[n]}" alt="{fa}">
        <span class="n">{n:02d}</span>{badge}
        <span class="df {diffcls}"><i class="dotc"></i>{diffname}</span>
      </div>
      <div class="body">
        <h3>{fa}</h3><div class="en">{en}</div>
        <p>{d}</p>
        <div class="row"><b>مناسب</b><span>{best}</span></div>
        <div class="row"><b class="bad">پرهیز</b><span>{avoid}</span></div>
        <div class="foot"><div class="tags">{tagh}</div>
          <button class="pk" data-n="{n}" data-name="{fa}">انتخاب کن</button></div>
      </div>
    </article>'''

body=""
for code,title,sub,styles in G:
    body+=f'''
  <section class="grp" data-gcode="{code}">
    <div class="ghead"><span class="gcode">{code}</span>
      <div><h2>{title}</h2><div class="gsub">{sub}</div></div>
      <span class="gcount">{len(styles)} سبک</span></div>
    <div class="grid">{"".join(card(s) for s in styles)}</div>
  </section>'''

NAV='''
<nav class="topnav">
  <a class="brand" href="کاتالوگ-۳۰-سبک.html"><span class="dot"></span> استودیوی موشن آراِنا</a>
  <div class="tabs">
    <a href="آموزش-ساخت-موشن.html">راهنمای ساخت</a>
    <a class="active" href="کاتالوگ-۳۰-سبک.html">کاتالوگ ۳۰ سبک</a>
  </div>
</nav>'''

CSS='''
*{box-sizing:border-box}
body{margin:0;background:#0B0B0D;color:#EDEDEF;font-family:Tahoma,"Segoe UI",system-ui,sans-serif;line-height:1.7}
a{color:#7FD1FF;text-decoration:none}
code{background:#1B1B20;padding:2px 7px;border-radius:5px;font-size:12.5px;direction:ltr;display:inline-block}
.topnav{position:sticky;top:0;z-index:60;display:flex;align-items:center;justify-content:space-between;gap:16px;
  padding:12px 26px;background:rgba(11,11,13,.94);backdrop-filter:blur(12px);border-bottom:1px solid #222227}
.brand{display:flex;align-items:center;gap:9px;color:#EDEDEF;font-weight:800;font-size:15px}
.dot{width:10px;height:10px;border-radius:3px;background:#E4332B}
.tabs{display:flex;gap:6px}
.tabs a{padding:7px 16px;border-radius:9px;font-size:13.5px;color:#B4B4BE;border:1px solid transparent}
.tabs a:hover{background:#17171B;color:#fff}
.tabs a.active{background:#1E7A4C;color:#fff;border-color:#2A9E63}
.wrap{max-width:1440px;margin:0 auto;padding:34px 24px 90px}
header.pg{border-bottom:1px solid #222227;padding-bottom:26px}
header.pg h1{font-size:36px;margin:0 0 12px;font-weight:800;letter-spacing:-.5px}
.lede{color:#9C9CA6;font-size:15.5px;max-width:880px}
.stats{display:flex;gap:10px;margin-top:20px;flex-wrap:wrap}
.stat{background:#151518;border:1px solid #26262A;border-radius:11px;padding:10px 18px;font-size:13.5px;color:#B9B9C2}
.stat b{color:#fff;font-size:18px;margin-left:6px}

.toolbar{position:sticky;top:57px;z-index:55;background:rgba(11,11,13,.96);backdrop-filter:blur(10px);
  padding:14px 0;margin-top:22px;border-bottom:1px solid #222227;display:flex;gap:10px;flex-wrap:wrap;align-items:center}
.search{flex:1 1 240px;min-width:200px;background:#151518;border:1px solid #2C2C33;border-radius:10px;
  color:#EDEDEF;font-family:inherit;font-size:13.5px;padding:9px 14px;outline:none}
.search:focus{border-color:#E4332B}
.fbtn{background:#151518;border:1px solid #2C2C33;color:#B4B4BE;border-radius:9px;
  padding:8px 14px;font-size:12.5px;font-family:inherit;cursor:pointer}
.fbtn:hover{color:#fff;border-color:#3A3A42}
.fbtn.on{background:#E4332B;border-color:#E4332B;color:#fff;font-weight:700}
.count{font-size:12.5px;color:#7E7E8A;margin-right:auto}

.grp{margin-top:42px}
.grp.hide{display:none}
.ghead{display:flex;align-items:center;gap:15px;margin-bottom:18px}
.gcode{width:38px;height:38px;border-radius:10px;background:#E4332B;color:#fff;
  display:flex;align-items:center;justify-content:center;font-weight:800;font-size:17px;flex-shrink:0}
.ghead h2{margin:0;font-size:22px;font-weight:800}
.gsub{color:#7E7E8A;font-size:12.5px}
.gcount{margin-right:auto;font-size:12px;color:#6E6E78;border:1px solid #2A2A2E;padding:5px 12px;border-radius:999px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:20px}
.card{background:#131316;border:1px solid #26262A;border-radius:16px;overflow:hidden;display:flex;flex-direction:column;transition:border-color .15s,transform .15s}
.card:hover{border-color:#3E3E48;transform:translateY(-2px)}
.card.hide{display:none}
.card.picked{border-color:#2A9E63;box-shadow:0 0 0 1px #2A9E63}
.thumb{position:relative;aspect-ratio:16/9;background:#000;border-bottom:1px solid #26262A}
.thumb img{width:100%;height:100%;object-fit:cover;display:block}
.n{position:absolute;top:10px;right:10px;background:rgba(0,0,0,.74);color:#fff;font-size:12px;
  font-weight:800;padding:4px 10px;border-radius:7px;letter-spacing:1px;direction:ltr}
.tag{position:absolute;bottom:10px;left:10px;font-size:10.5px;font-weight:700;padding:4px 10px;border-radius:999px;backdrop-filter:blur(6px)}
.tag.ok{background:rgba(20,60,35,.88);color:#6EE7A0;border:1px solid rgba(80,200,130,.45)}
.tag.ref{background:rgba(0,0,0,.7);color:#B9B9C4;border:1px solid rgba(255,255,255,.22)}
.df{position:absolute;bottom:10px;right:10px;font-size:10.5px;padding:4px 9px;border-radius:999px;background:rgba(0,0,0,.72);border:1px solid rgba(255,255,255,.16)}
.df.e{color:#6EE7A0}.df.m{color:#FFD166}.df.h{color:#FF8A7A}
.df,.fbtn{display:inline-flex;align-items:center;gap:6px}
.dotc{width:8px;height:8px;border-radius:50%;display:inline-block;background:#6EE7A0;flex-shrink:0}
.dotc.e{background:#22C55E}.dotc.m{background:#F2B01E}.dotc.h{background:#EF5B4C}
.fbtn.on .dotc.e,.fbtn.on .dotc.m,.fbtn.on .dotc.h{background:#fff}
.body{padding:16px 20px 16px;display:flex;flex-direction:column;flex-grow:1}
h3{margin:0;font-size:19px;font-weight:800}
.en{color:#6E6E7A;font-size:11px;letter-spacing:1.6px;text-transform:uppercase;direction:ltr;text-align:right;margin-bottom:8px}
.body p{margin:0 0 11px;color:#B0B0BA;font-size:13.5px;flex-grow:1}
.row{display:flex;gap:8px;font-size:12.5px;margin-bottom:6px;color:#C2C2CB}
.row b{flex:0 0 38px;color:#2ECC9B;font-size:11px;font-weight:800;padding-top:3px}
.row b.bad{color:#FF6B5E}
.foot{display:flex;justify-content:space-between;align-items:center;gap:8px;margin-top:12px;
  padding-top:11px;border-top:1px dashed #2A2A2F}
.tags{display:flex;gap:5px;flex-wrap:wrap}
.tags i{font-style:normal;font-size:10.5px;color:#8E8E9A;background:#1B1B20;padding:3px 8px;border-radius:6px}
.pk{background:#1B1B20;border:1px solid #2C2C33;color:#B4B4BE;border-radius:8px;
  padding:5px 12px;font-size:11.5px;font-family:inherit;cursor:pointer;white-space:nowrap}
.pk:hover{background:#E4332B;border-color:#E4332B;color:#fff}

.note{margin-top:52px;background:#131316;border:1px solid #26262A;border-right:4px solid #E4332B;border-radius:14px;padding:24px 28px}
.note h2{margin:0 0 10px;font-size:20px}
.note p{margin:0 0 8px;color:#B0B0BA;font-size:14px}
footer{margin-top:36px;padding-top:20px;border-top:1px solid #222227;font-size:12.5px;color:#6E6E78}

.pickbar{position:fixed;left:0;right:0;bottom:0;z-index:70;background:#141418;border-top:1px solid #2C2C33;
  padding:12px 24px;display:none;align-items:center;gap:14px;flex-wrap:wrap}
.pickbar.show{display:flex}
.pickbar .lbl{font-size:13px;color:#8E8E9A}
.pickbar .chips{display:flex;gap:7px;flex-wrap:wrap}
.pickbar .chip{background:#1E2A22;border:1px solid #2A4A36;color:#6EE7A0;font-size:12px;padding:4px 11px;border-radius:999px}
.pickbar .go{margin-right:auto;background:#E4332B;color:#fff;border:none;border-radius:9px;
  padding:9px 18px;font-size:13px;font-family:inherit;font-weight:700;cursor:pointer}
.pickbar .go:hover{background:#FF5148}
.pickbar .clr{background:transparent;border:1px solid #3A3A42;color:#9C9CA6;border-radius:9px;
  padding:9px 14px;font-size:12.5px;font-family:inherit;cursor:pointer}
@media(max-width:640px){
  .wrap{padding:22px 14px 70px}.topnav{padding:10px 14px;flex-direction:column;align-items:stretch;gap:8px}
  .tabs{justify-content:center}header.pg h1{font-size:26px}.toolbar{top:auto;position:static}
}
'''

JS = '''
(function(){
  var picked = {};
  var cards = Array.prototype.slice.call(document.querySelectorAll(".card"));
  var groups = Array.prototype.slice.call(document.querySelectorAll(".grp"));
  var search = document.getElementById("q");
  var countEl = document.getElementById("cnt");
  var fBtns = Array.prototype.slice.call(document.querySelectorAll(".fbtn[data-f]"));

  function apply(){
    var q = (search.value || "").trim().toLowerCase();
    var active = fBtns.filter(function(b){ return b.classList.contains("on"); }).map(function(b){ return b.dataset.f; });
    var shown = 0;
    cards.forEach(function(c){
      var okText = !q || (c.dataset.g + " " + c.dataset.en + " " + c.dataset.tags + " " + c.dataset.best).toLowerCase().indexOf(q) > -1;
      var okDiff = active.filter(function(f){ return f[0] === "d"; }).length === 0 || active.indexOf("d" + c.dataset.diff) > -1;
      var okBuilt = active.indexOf("b1") === -1 || c.dataset.built === "1";
      var ok = okText && okDiff && okBuilt;
      c.classList.toggle("hide", !ok);
      if (ok) shown++;
    });
    groups.forEach(function(g){
      var any = g.querySelectorAll(".card:not(.hide)").length > 0;
      g.classList.toggle("hide", !any);
    });
    countEl.textContent = shown + " از ۳۰ سبک";
  }
  search.addEventListener("input", apply);
  fBtns.forEach(function(b){
    b.addEventListener("click", function(){
      var f = b.dataset.f;
      if (f === "all") { fBtns.forEach(function(x){ x.classList.remove("on"); }); b.classList.add("on"); }
      else { document.querySelector('.fbtn[data-f="all"]').classList.remove("on"); b.classList.toggle("on"); }
      apply();
    });
  });

  var bar = document.getElementById("pickbar");
  var chips = document.getElementById("chips");
  function renderPicks(){
    var keys = Object.keys(picked);
    chips.innerHTML = keys.map(function(k){ return '<span class="chip">' + picked[k] + "</span>"; }).join("");
    bar.classList.toggle("show", keys.length > 0);
  }
  document.querySelectorAll(".pk").forEach(function(btn){
    btn.addEventListener("click", function(){
      var n = btn.dataset.n, name = btn.dataset.name;
      if (picked[n]) { delete picked[n]; btn.textContent = "انتخاب کن"; }
      else { picked[n] = n.padStart(2,"0") + " · " + name; btn.textContent = "✓ انتخاب شد"; }
      btn.closest(".card").classList.toggle("picked", !!picked[n]);
      renderPicks();
    });
  });
  document.getElementById("clr").addEventListener("click", function(){
    picked = {}; renderPicks();
    document.querySelectorAll(".pk").forEach(function(b){ b.textContent = "انتخاب کن"; });
    document.querySelectorAll(".card").forEach(function(c){ c.classList.remove("picked"); });
  });
  document.getElementById("go").addEventListener("click", function(){
    var keys = Object.keys(picked).sort(function(a,b){ return a-b; });
    var txt = "سبک‌های انتخابی من از کاتالوگ: " + keys.map(function(k){ return k + " (" + picked[k].split(" · ")[1] + ")"; }).join(" ، ")
      + ". بر اساس این سبک‌ها برایم یک موشن‌گرافیک ۸ ثانیه‌ای بساز.";
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(txt).then(function(){ location.href = "آموزش-ساخت-موشن.html#s4"; });
    } else { location.href = "آموزش-ساخت-موشن.html#s4"; }
  });

  // بارگذاری تصویر کامل هنگام هاور (بهبود کیفیت)
  cards.forEach(function(c){
    var img = c.querySelector("img");
    c.addEventListener("mouseenter", function(){
      if (img.dataset.full && img.src !== img.dataset.full) img.src = img.dataset.full;
    });
  });

  apply();
})();
'''

html=f'''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>کاتالوگ ۳۰ سبک گرافیکی موشن</title>
<style>{CSS}</style>
</head>
<body>
{NAV}
<div class="wrap">
  <header class="pg">
    <h1>۳۰ سبک گرافیکی موشن</h1>
    <div class="lede">
      هر سبک با تصویر. ۱۳ موردِ برچسب «نمونه‌ی ساخت ما» رندر واقعی از پروژه است
      (ویدیو در <code>previews/</code>)؛ ۱۷ موردِ «تصویر مرجع» از نمونه‌های صنعت برداشته شده
      تا حس و زبان بصری را نشان دهد. سبک‌های مورد علاقه‌ات را انتخاب کن تا پرامپت آماده‌ی ساخت بگیری.
    </div>
    <div class="stats">
      <div class="stat"><b>۳۰</b>سبک</div><div class="stat"><b>۶</b>خانواده</div>
      <div class="stat"><b>۱۳</b>ساخته‌شده</div><div class="stat"><b>۱۷</b>آماده‌ی ساخت</div>
    </div>
  </header>

  <div class="toolbar">
    <input id="q" class="search" type="search" placeholder="جست‌وجو: کافه، لوکس، ریتم، آموزش…">
    <button class="fbtn on" data-f="all">همه</button>
    <button class="fbtn" data-f="de"><i class="dotc e"></i>ساده</button>
    <button class="fbtn" data-f="dm"><i class="dotc m"></i>متوسط</button>
    <button class="fbtn" data-f="dh"><i class="dotc h"></i>سنگین</button>
    <button class="fbtn" data-f="b1">فقط ساخته‌شده‌ها</button>
    <span class="count" id="cnt">۳۰ از ۳۰ سبک</span>
  </div>

  {body}

  <div class="note">
    <h2>بعد از انتخاب چه کنم؟</h2>
    <p><b>۱.</b> سبک‌های مورد نظرت را با دکمه‌ی «انتخاب کن» علامت بزن.</p>
    <p><b>۲.</b> دکمه‌ی «ساخت پرامپت» پایین صفحه، پرامپت آماده را کپی می‌کند و تو را به بخش پرامپت راهنما می‌برد.</p>
    <p><b>۳.</b> در <a href="آموزش-ساخت-موشن.html">راهنمای ساخت</a>، متن و فایل‌هایت را اضافه کن و به ایجنت بده.</p>
  </div>

  <footer>رنگ و فونت از هویت خودت بیاید، نه از سبک. سبک = ترکیب‌بندی، حرکت و بافت.</footer>
</div>

<div class="pickbar" id="pickbar">
  <span class="lbl">انتخاب‌های تو:</span>
  <div class="chips" id="chips"></div>
  <button class="clr" id="clr">پاک کردن</button>
  <button class="go" id="go">ساخت پرامپت →</button>
</div>

<script>{JS}</script>
</body>
</html>'''
open("کاتالوگ-۳۰-سبک.html","w").write(html)
print("catalog:", round(len(html)/1024/1024,2), "MB")
