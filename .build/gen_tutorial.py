# -*- coding: utf-8 -*-
import json

shots = json.load(open(".build/shots.json"))
real = json.load(open(".build/real.json"))

NAV = '''
<nav class="topnav">
  <a class="brand" href="کاتالوگ-۳۰-سبک.html">
    <span class="dot"></span> استودیوی موشن آراِنا
  </a>
  <div class="tabs">
    <a class="active" href="آموزش-ساخت-موشن.html">راهنمای ساخت</a>
    <a href="کاتالوگ-۳۰-سبک.html">کاتالوگ ۳۰ سبک</a>
  </div>
</nav>'''

def realshot(key, cap):
    return f'''
        <figure class="shot real">
          <img src="data:image/jpeg;base64,{real[key]}" alt="{cap}">
          <figcaption>{cap}</figcaption>
        </figure>'''

def step(num, title, sub, body, img=None, extra=""):
    figure = ""
    if img:
        figure = f'''
        <figure class="shot">
          <img src="data:image/jpeg;base64,{shots[img]}" alt="{title}">
          <figcaption>{extra}</figcaption>
        </figure>'''
    return f'''
    <section class="step" id="s{num}">
      <div class="stephead">
        <span class="badge">{num}</span>
        <div>
          <h2>{title}</h2>
          <p class="sub">{sub}</p>
        </div>
      </div>
      <div class="stepbody">
        {body}
        {figure}
      </div>
    </section>'''

PROMPT_MAIN = """ساخت موشن‌گرافیک با Remotion

━━━━ ۱) موضوع و پیام
موضوع: معرفی کافه‌ی «دانه»
پیام اصلی در یک جمله: قهوه‌ی تازه، هر روز صبح
مخاطب: مشتری‌های محلی، ۲۵ تا ۴۵ سال

━━━━ ۲) سبک گرافیکی
سبک انتخابی از کاتالوگ: شماره ۱۷ — کرافت / کارگاه (Kraft Artisan)
رنگ‌های برند: #C6A57A ، #2A2521 ، #F2E7D3
فونت: وزیرمتن (فارسی) — داخل پروژه لود شود

━━━━ ۳) متن و محتوا
متن روی ویدیو: «قهوه‌ی تازه، هر روز صبح»
زیرمتن: «دانه — از ۱۳۹۸»
نریشن: لینک فایل صوتی در بخش ۴
موسیقی: لینک فایل موسیقی در بخش ۴
لوگو: لینک تصویر PNG در بخش ۴

━━━━ ۴) فایل‌ها (لینک مستقیم)
نریشن: https://‌لینک-فایل-صوتی.mp3
موسیقی: https://‌لینک-موسیقی.mp3
لوگو: https://‌لینک-لوگو.png

━━━━ ۵) مشخصات فنی
ابعاد: ۱۰۸۰×۱۹۲۰ (ریلز) — نسخه‌ی ۱۹۲۰×۱۰۸۰ هم بساز
مدت: ۸ ثانیه | fps: ۳۰

━━━━ ۶) کارهایی که باید انجام بدهی
۱. ابزار Remotion را نصب کن (npx create-video@latest --blank --skills) و پروژه را بساز
۲. فونت فارسی وزیرمتن را در public/fonts بگذار و با delayRender لود کن
۳. کامپوننت را در src/styles/Daneh.tsx بساز و در Root.tsx با شناسه‌ی Daneh ثبت کن
۴. پیش‌نمایش بده و بعد با npx remotion render خروجی MP4 بگیر
۵. فایل MP4 و ZIP کل پروژه را در ورک‌اسپیس بگذار تا دانلود کنم

اگر لینکی کار نکرد یا فایلی نبود، قبل از شروع از من بپرس. همه‌ی متن‌ها فارسی و راست‌به‌چپ باشند."""

PROMPT_QUICK = """یک موشن‌گرافیک ۸ ثانیه‌ای عمودی (۱۰۸۰×۱۹۲۰) با Remotion بساز.
سبک: مینیمال ادیتوریال (شماره ۲۶ کاتالوگ). رنگ برند #E4332B روی کاغذ #F4F1EA.
متن: «ایده، حرکت، ویدیو»
فونت فارسی وزیرمتن با پشتیبانی RTL.
Remotion را نصب کن، کامپوننت را بساز، پیش‌نمایش بده و در پایان MP4 را رندر کن و در ورک‌اسپیس بگذار."""

PROMPT_FIX = """در ویدیوی ساخته‌شده این سه چیز را اصلاح کن:
۱. انیمیشن ورودی متن ۲۰٪ کندتر و با spring نرم‌تر (damping: 18) باشد.
۲. نریشن و زیرنویس با هم سینک نیستند — زمان‌بندی را از فایل صدا دوباره محاسبه کن.
۳. رنگ پس‌زمینه را به #F4F1EA تغییر بده و دوباره MP4 را رندر کن."""

FREE_HOSTING = """
<table class="tbl">
  <thead><tr><th>نوع فایل</th><th>سرویس رایگان</th><th>نکته‌ی مهم</th></tr></thead>
  <tbody>
    <tr><td><b>صدا / نریشن / موسیقی</b></td><td>tmpfiles.org · file.io · catbox.moe · Google Drive · Dropbox</td><td>لینک <b>مستقیم</b> بده که با .mp3 تمام شود، نه صفحه‌ی پیش‌نمایش</td></tr>
    <tr><td><b>لوگو / تصویر</b></td><td>imgur.com · postimages.org · Google Drive</td><td>PNG با پس‌زمینه‌ی شفاف، حداقل ۱۰۰۰ پیکسل</td></tr>
    <tr><td><b>ویدیو</b></td><td>catbox.moe · streamable · Google Drive</td><td>MP4 با کدک H.264</td></tr>
    <tr><td><b>فونت</b></td><td>Google Drive · GitHub (raw)</td><td>فایل ttf/otf + نام دقیق خانواده که در CSS بنویسیم</td></tr>
    <tr><td><b>فایل پروژه / دیتا</b></td><td>GitHub · Google Drive</td><td>CSV یا JSON برای نمودار و لیست</td></tr>
  </tbody>
</table>
<div class="tip">
  <b>ساده‌ترین راه:</b> لازم نیست جایی آپلود کنی — فایل را مستقیم در چت ایجنت آپلود کن
  (دکمه‌ی گیره‌ی کاغذ در کادر پیام). ایجنت فایل را در ورک‌اسپیس می‌بیند و استفاده می‌کند.
  آپلود در سرویس بیرونی فقط وقتی لازم است که لینک را جایی نگه می‌داری یا فایل بزرگ است.
</div>
"""

CONTENT = f'''
{NAV}
<div class="wrap">
  <header class="hero">
    <span class="kicker">راهنمای کامل · بدون نیاز به دانش برنامه‌نویسی</span>
    <h1>با ایجنت آراِنا یک ویدیوی موشن فارسی بساز</h1>
    <p class="lede">
      در هفت قدم، از ثبت‌نام تا فایل MP4 — با اسکرین‌شات واقعی از خود سایت. ابزار <b>Remotion</b> را ایجنت برایت نصب می‌کند،
      سبک را از کاتالوگ ۳۰ سبکی انتخاب می‌کنی، متن و نریشن و لوگو را می‌دهی،
      و در پایان یک فایل ویدیو و کل پروژه را دانلود می‌کنی.
    </p>
    <div class="meta">
      <span>زمان: حدود ۱۰ دقیقه برای اولین ویدیو</span>
      <span>هزینه: رایگان</span>
      <span>زبان: فارسی و راست‌به‌چپ</span>
    </div>
    <div class="toc">
      <a href="#s1">۱ · ثبت‌نام</a>
      <a href="#s2">۲ · حالت ایجنت</a>
      <a href="#s3">۳ · فایل‌ها</a>
      <a href="#s4">۴ · پرامپت</a>
      <a href="#s5">۵ · ساخت</a>
      <a href="#s6">۶ · اصلاح</a>
      <a href="#s7">۷ · خروجی</a>
      <a href="#fix">عیب‌یابی</a>
    </div>
  </header>

  <div class="prereq">
    <h3>قبل از شروع، این چهار چیز را آماده کن</h3>
    <ol>
      <li><b>یک جمله‌ی پیام.</b> «قهوه‌ی تازه، هر روز صبح» — نه «ما یک کافه هستیم».</li>
      <li><b>متن‌هایی که روی ویدیو می‌آید.</b> حداکثر ۷ تا ۱۰ کلمه. کمتر، بهتر.</li>
      <li><b>فایل‌ها.</b> لوگو، نریشن، موسیقی — اگر داری. اگر نداری، ویدیو بدون صدا هم ساخته می‌شود.</li>
      <li><b>یک سبک از کاتالوگ.</b> <a href="کاتالوگ-۳۰-سبک.html">۳۰ سبک با تصویر</a> — شماره‌اش را یادداشت کن.</li>
    </ol>
  </div>

  {step(1, "در آراِنا ثبت‌نام کن", "یک حساب رایگان، کمتر از یک دقیقه", """
    <ol class="list">
      <li>به <code>arena.ai</code> برو.</li>
      <li>بالای صفحه روی <b>Sign up for free</b> بزن (یا <b>Log in</b> اگر حساب داری).</li>
      <li>با ایمیل یا حساب گوگل ثبت‌نام کن و ایمیل تأیید را کلیک کن.</li>
    </ol>
    <p class="note-sm">ثبت‌نام رایگان است و برای ساخت ویدیو نیازی به کارت بانکی یا اشتراک نیست.</p>
  """)}

  <div class="realblock">
    <div class="rbhead"><span class="rbdot"></span> اسکرین‌شات واقعی از arena.ai — شماره ۱ همان دکمه‌ی ثبت‌نام است</div>
    {realshot("r1", "صفحه‌ی اصلی · دکمه‌ی Sign up for free گوشه‌ی بالا-راست")}
  </div>

  {step(2, "حالت ایجنت را انتخاب کن", "این مهم‌ترین انتخاب صفحه است", """
    <p>آراِنا چند حالت دارد (Battle، Side by Side، Agent). تو باید <b>Agent Mode</b> را انتخاب کنی،
    چون فقط این حالت است که فایل می‌سازد، ابزار نصب می‌کند و برایت رندر می‌گیرد.</p>
    <ol class="list">
      <li>مستقیم به <code>arena.ai/agent</code> برو — <b>یا</b> از صفحه‌ی اصلی، منوی بالا-چپ را باز کن و
      حالت را از <b>Battle Mode</b> به <b>Agent Mode</b> تغییر بده.</li>
      <li>در کادر پیام، پرامپتت را بنویس (قدم ۴).</li>
      <li>سمت راست صفحه پنل <b>Workspace</b> است — همه‌ی فایل‌های ساخته‌شده آنجا ظاهر می‌شوند.</li>
      <li>دکمه‌ی فلش را بزن تا کار شروع شود.</li>
    </ol>
  """)}

  <div class="realblock">
    <div class="rbhead"><span class="rbdot"></span> اسکرین‌شات واقعی — روی دکمه‌ی حالت (کنار کادر پیام) بزن تا این منو باز شود</div>
    {realshot("r2", "منوی انتخاب حالت · گزینه‌ی Agent Mode را انتخاب کن")}
  </div>

  <div class="realblock">
    <div class="rbhead"><span class="rbdot"></span> اسکرین‌شات واقعی — بعد از انتخاب Agent، صفحه این‌طور می‌شود</div>
    {realshot("r3", "صفحه‌ی Agent Mode · کادر پرامپت و دکمه‌ی ارسال")}
  </div>

  {step(3, "فایل‌هایت را آماده کن", "یا در چت آپلود کن، یا لینک بده", FREE_HOSTING)}

  {step(4, "پرامپت را بفرست", "شش بخش، و ایجنت بی‌نقص می‌سازد", f"""
    <p>پرامپت خوب برای موشن، شش بخش دارد. هرچه دقیق‌تر بنویسی، کمتر باید اصلاح کنی:</p>
    <div class="fields">
      <div><b>۱ · موضوع و پیام</b><span>چه چیزی، برای چه کسی</span></div>
      <div><b>۲ · سبک</b><span>شماره از کاتالوگ + کدهای رنگ + فونت</span></div>
      <div><b>۳ · متن و صدا</b><span>متن روی ویدیو، نریشن، موسیقی</span></div>
      <div><b>۴ · فایل‌ها</b><span>لینک مستقیم صدا، لوگو، تصویر</span></div>
      <div><b>۵ · مشخصات فنی</b><span>ابعاد، مدت، fps</span></div>
      <div><b>۶ · وظایف ایجنت</b><span>نصب ابزار، ساخت، پیش‌نمایش، رندر، تحویل فایل</span></div>
    </div>

    <div class="promptbox">
      <div class="pbhead">
        <span>پرامپت کامل و آماده — فقط جاهای [کروشه] را عوض کن</span>
        <button class="copy" data-target="p-main">کپی</button>
      </div>
      <pre id="p-main">{PROMPT_MAIN}</pre>
    </div>

    <div class="warn">
      <b>سه نکته که بیشترین تفاوت را می‌سازند:</b>
      <ul>
        <li>بخش <b>۶</b> را حذف نکن — همان است که به ایجنت می‌گوید Remotion را نصب کند و در پایان MP4 بدهد.</li>
        <li>اگر لینک فایل نداری، جمله‌ی «بدون صدا بساز» را اضافه کن تا ایجنت معطل نماند.</li>
        <li>ننویس «قشنگ بساز». بنویس «سبک شماره ۹، رنگ #C7B8FF، ورودی فنری با damping 12».</li>
      </ul>
    </div>

    <div class="promptbox small">
      <div class="pbhead">
        <span>نسخه‌ی کوتاه — وقتی عجله داری</span>
        <button class="copy" data-target="p-quick">کپی</button>
      </div>
      <pre id="p-quick">{PROMPT_QUICK}</pre>
    </div>
  """, "p2_prompt", "پرامپت با شش بخش در کادر پیام")}

  {step(5, "ایجنت پروژه را می‌سازد", "چند دقیقه صبر، بدون کار اضافه", """
    <p>بعد از ارسال، ایجنت این کارها را به ترتیب انجام می‌دهد. لازم نیست چیزی نصب کنی یا ترمینال باز کنی:</p>
    <ol class="list">
      <li><b>نصب ابزار:</b> Remotion و اسکیل‌های رسمی‌اش را نصب می‌کند.</li>
      <li><b>فونت فارسی:</b> فونت وزیرمتن را اضافه و قبل از رندر لود می‌کند تا متن خراب نشود.</li>
      <li><b>ساخت سبک:</b> کامپوننت ویدیو را با رنگ، تایپوگرافی و انیمیشن‌های سبک انتخابی تو می‌سازد.</li>
      <li><b>پیش‌نمایش:</b> یک محیط پیش‌نمایش زنده بالا می‌آورد تا فریم‌به‌فریم ببینی.</li>
      <li><b>رندر خروجی:</b> فایل MP4 را می‌سازد و کنارش کل پروژه را می‌گذارد.</li>
    </ol>
    <p class="note-sm">اگر پرامپتت کامل باشد، معمولاً بین ۵ تا ۱۵ دقیقه طول می‌کشد. کارهای سنگین‌تر مثل
    سه‌بعدی یا نقشه بیشتر طول می‌کشند.</p>
  """, "p3_files", "فایل‌های نتیجه در پنل Workspace")}

  {step(6, "ببین و اصلاح کن", "بهترین بخش: تغییر با حرف زدن", f"""
    <p>ویدیو را ببین. بعد لازم نیست کد را دست بزنی — فقط به فارسی بگو چه چیزی را عوض کند:</p>
    <div class="promptbox small">
      <div class="pbhead">
        <span>پرامپت اصلاح — نمونه</span>
        <button class="copy" data-target="p-fix">کپی</button>
      </div>
      <pre id="p-fix">{PROMPT_FIX}</pre>
    </div>
    <div class="examples">
      <div>«سرعت انیمیشن را ۲۰٪ کم کن»</div>
      <div>«این کلمه را پررنگ‌تر و بزرگ‌تر کن»</div>
      <div>«پس‌زمینه را روشن‌تر کن»</div>
      <div>«نسخه‌ی عمودی هم بساز»</div>
      <div>«زیرنویس را بزرگ‌تر کن»</div>
      <div>«صحنه‌ی دوم را حذف کن»</div>
    </div>
  """, "p4_preview", "پیش‌نمایش زنده در محیط ایجنت")}

  {step(7, "خروجی را دانلود کن", "MP4 آماده‌ی انتشار", """
    <div class="twocol">
      <div>
        <h4>دانلود ویدیو</h4>
        <p>فایل <code>out/*.mp4</code> در ورک‌اسپیس است. روی آن کلیک کن و دانلود کن.
        همین فایل مستقیم در اینستاگرام، یوتیوب یا لینکدین قابل انتشار است.</p>
      </div>
      <div>
        <h4>دانلود کل پروژه</h4>
        <p>در پنل <b>Workspace</b> دکمه‌ی <b>Download</b> را بزن تا همه‌ی فایل‌ها به‌صورت ZIP بگیری.
        با این ZIP بعداً می‌توانی همان ویدیو را برای محصول دیگر یا رنگ دیگر دوباره بسازی.</p>
      </div>
    </div>
    <div class="tip">
      <b>نکته‌ی نگهداری:</b> ZIP را نگه دار. دفعه‌ی بعد لازم نیست از صفر شروع کنی —
      کافی است بگویی «همان پروژه، این بار با متن جدید» و فقط چند دقیقه وقت می‌برد.
    </div>
  """, "p5_timeline", "تایم‌لاین صحنه‌ها و مرحله‌ی رندر")}

  <section class="step" id="fix">
    <div class="stephead">
      <span class="badge">!</span>
      <div><h2>عیب‌یابی — اگر چیزی درست نشد</h2>
      <p class="sub">شش مشکل رایج و جمله‌ای که باید به ایجنت بگویی</p></div>
    </div>
    <div class="stepbody">
      <table class="tbl">
        <thead><tr><th>چه می‌بینی</th><th>چه بگو</th></tr></thead>
        <tbody>
          <tr><td>حروف فارسی مربع یا نامنظم است</td><td>«فونت وزیرمتن لود نشده؛ با delayRender اضافه کن و دوباره رندر بگیر»</td></tr>
          <tr><td>متن برعکس یا جدا-جدا نشان داده می‌شود</td><td>«direction: rtl را روی کانتینر اصلی بگذار و letterSpacing منفی را بردار»</td></tr>
          <tr><td>ویدیو خیلی کند رندر می‌شود</td><td>«بلور و فیلترهای سنگین را کم کن و سایز را ۱۰۸۰p نگه دار»</td></tr>
          <tr><td>نریشن با متن هم‌زمان نیست</td><td>«زمان‌بندی را از مدت فایل صوتی دوباره حساب کن»</td></tr>
          <tr><td>خروجی سیاه است</td><td>«کامپوننت را در Root.tsx ثبت کن و شناسه‌ی درست را در رندر بده»</td></tr>
          <tr><td>حجم فایل زیاد است</td><td>«bitrate را کم کن یا به WebM تبدیل کن»</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <div class="cta">
    <div>
      <h2>آماده‌ای؟</h2>
      <p>اول سبکت را از کاتالوگ انتخاب کن، بعد برگرد و پرامپت را پر کن.</p>
    </div>
    <a class="btn" href="کاتالوگ-۳۰-سبک.html">دیدن ۳۰ سبک گرافیکی →</a>
  </div>

  <footer>
    ساخته‌شده برای کاربران ایجنت آراِنا · موتور ویدیو: Remotion ·
    تصاویر این صفحه بازسازی محیط ایجنت است و برای آموزش مسیر کار آمده.
  </footer>
</div>
'''

CSS = '''
*{box-sizing:border-box}
body{margin:0;background:#0B0B0D;color:#EDEDEF;font-family:Tahoma,"Segoe UI",system-ui,sans-serif;line-height:1.85;font-size:15px}
a{color:#7FD1FF;text-decoration:none}
code{background:#1B1B20;border:1px solid #2C2C33;padding:1px 7px;border-radius:5px;font-size:13px;direction:ltr;display:inline-block}
.topnav{position:sticky;top:0;z-index:50;display:flex;align-items:center;justify-content:space-between;
  gap:16px;padding:12px 26px;background:rgba(11,11,13,.92);backdrop-filter:blur(12px);border-bottom:1px solid #222227}
.brand{display:flex;align-items:center;gap:9px;color:#EDEDEF;font-weight:800;font-size:15px}
.dot{width:10px;height:10px;border-radius:3px;background:#E4332B;display:inline-block}
.tabs{display:flex;gap:6px}
.tabs a{padding:7px 16px;border-radius:9px;font-size:13.5px;color:#B4B4BE;border:1px solid transparent}
.tabs a:hover{background:#17171B;color:#fff}
.tabs a.active{background:#1E7A4C;color:#fff;border-color:#2A9E63}
.wrap{max-width:960px;margin:0 auto;padding:36px 22px 80px}

.hero{border-bottom:1px solid #222227;padding-bottom:28px;margin-bottom:26px}
.kicker{display:inline-block;font-size:12px;color:#6EE7A0;background:#132A1E;border:1px solid #1F4630;
  padding:5px 13px;border-radius:999px;margin-bottom:16px}
.hero h1{margin:0 0 14px;font-size:36px;line-height:1.35;font-weight:800;letter-spacing:-.5px}
.lede{color:#A8A8B2;font-size:16px;margin:0 0 18px}
.meta{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:20px}
.meta span{font-size:12.5px;color:#9C9CA6;background:#151518;border:1px solid #26262A;padding:6px 13px;border-radius:8px}
.toc{display:flex;gap:7px;flex-wrap:wrap}
.toc a{font-size:12.5px;color:#C4C4CC;background:#151518;border:1px solid #26262A;padding:7px 13px;border-radius:8px}
.toc a:hover{border-color:#E4332B;color:#fff}

.prereq{background:#131316;border:1px solid #26262A;border-right:4px solid #E4332B;border-radius:14px;padding:22px 26px;margin-bottom:34px}
.prereq h3{margin:0 0 12px;font-size:17px}
.prereq ol{margin:0;padding-right:20px;color:#B7B7C0;font-size:14px}
.prereq li{margin-bottom:7px}

.step{margin-bottom:46px;scroll-margin-top:80px}
.stephead{display:flex;gap:15px;align-items:flex-start;margin-bottom:16px}
.badge{flex-shrink:0;width:40px;height:40px;border-radius:11px;background:#E4332B;color:#fff;
  display:flex;align-items:center;justify-content:center;font-weight:800;font-size:17px}
.stephead h2{margin:0;font-size:24px;font-weight:800}
.sub{margin:2px 0 0;color:#7E7E8A;font-size:13.5px}
.stepbody{padding-right:0}
.list{margin:0 0 14px;padding-right:22px;color:#B7B7C0}
.list li{margin-bottom:9px}
.list b{color:#EDEDEF}
.note-sm{font-size:13.5px;color:#8E8E9A;background:#131316;border-radius:10px;padding:11px 16px;border:1px solid #222227}

.shot{margin:20px 0 0;background:#131316;border:1px solid #26262A;border-radius:14px;overflow:hidden}
.shot img{width:100%;display:block}
.realblock{margin:22px 0 0;border:1px solid #2A4A36;border-radius:14px;padding:12px;background:#0E1512}
.rbhead{display:flex;align-items:center;gap:9px;font-size:12.5px;color:#6EE7A0;padding:2px 4px 10px}
.rbdot{width:8px;height:8px;border-radius:50%;background:#22C55E;box-shadow:0 0 0 3px rgba(34,197,94,.18)}
.shot.real{margin:0;border-color:#26382E;background:#000}
.shot.real{position:relative}
.shot.real .realtag{position:absolute;top:10px;left:10px;background:rgba(20,60,35,.9);
  color:#6EE7A0;font-size:10.5px;font-weight:700;padding:4px 10px;border-radius:999px;border:1px solid rgba(80,200,130,.45);z-index:2}
.shot figcaption{padding:10px 16px;font-size:12.5px;color:#8E8E9A;border-top:1px solid #26262A}

.tbl{width:100%;border-collapse:collapse;margin:6px 0 18px;font-size:13.5px}
.tbl th{text-align:right;padding:11px 14px;background:#17171B;color:#C9C9D2;font-weight:700;border-bottom:1px solid #2A2A2F}
.tbl td{padding:11px 14px;border-bottom:1px solid #222227;color:#B0B0BA;vertical-align:top}
.tbl tr:last-child td{border-bottom:none}
.tbl b{color:#EDEDEF}

.tip{background:#12211A;border:1px solid #1F4630;border-radius:11px;padding:13px 18px;font-size:13.5px;color:#B6E7C8}
.warn{background:#231516;border:1px solid #4A2326;border-radius:11px;padding:14px 18px;font-size:13.5px;color:#F0C9C6;margin:16px 0}
.warn ul{margin:9px 0 0;padding-right:20px}
.warn li{margin-bottom:5px}
.warn b{color:#fff}

.fields{display:grid;grid-template-columns:repeat(auto-fill,minmax(215px,1fr));gap:10px;margin:14px 0 20px}
.fields div{background:#131316;border:1px solid #26262A;border-radius:11px;padding:12px 15px}
.fields b{display:block;font-size:13.5px;color:#EDEDEF;margin-bottom:2px}
.fields span{font-size:12px;color:#8E8E9A}

.promptbox{background:#0E0E11;border:1px solid #2C2C33;border-radius:13px;overflow:hidden;margin:14px 0 20px}
.pbhead{display:flex;justify-content:space-between;align-items:center;gap:12px;
  padding:10px 16px;background:#17171B;border-bottom:1px solid #2C2C33;font-size:12.5px;color:#9C9CA6}
.copy{background:#E4332B;color:#fff;border:none;border-radius:7px;padding:5px 14px;font-size:12px;
  font-family:inherit;cursor:pointer;font-weight:700}
.copy:hover{background:#FF5148}
.promptbox pre{margin:0;padding:18px 20px;font-size:12.5px;line-height:1.95;white-space:pre-wrap;
  color:#D6D6DE;font-family:"Courier New",monospace;direction:rtl;text-align:right;max-height:460px;overflow:auto}
.promptbox.small pre{max-height:none;font-size:12px}

.examples{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:9px;margin-top:14px}
.examples div{background:#131316;border:1px solid #26262A;border-radius:9px;padding:10px 14px;font-size:13px;color:#B7B7C0}

.twocol{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:14px}
.twocol h4{margin:0 0 6px;font-size:15px;color:#EDEDEF}
.twocol p{margin:0;font-size:13.5px;color:#A8A8B2}

.cta{margin-top:52px;display:flex;align-items:center;justify-content:space-between;gap:20px;
  background:linear-gradient(120deg,#161619,#1B1220);border:1px solid #2C2C33;border-radius:16px;padding:26px 30px;flex-wrap:wrap}
.cta h2{margin:0 0 4px;font-size:21px}
.cta p{margin:0;color:#9C9CA6;font-size:14px}
.btn{background:#E4332B;color:#fff;padding:12px 24px;border-radius:11px;font-weight:700;font-size:14px;white-space:nowrap}
.btn:hover{background:#FF5148}
footer{margin-top:40px;padding-top:22px;border-top:1px solid #222227;font-size:12.5px;color:#6E6E78}

@media(max-width:640px){
  .hero h1{font-size:26px}
  .wrap{padding:24px 14px 60px}
  .topnav{padding:10px 14px;flex-direction:column;align-items:stretch;gap:8px}
  .tabs{justify-content:center}
  .twocol{grid-template-columns:1fr}
}
'''

html = f'''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>راهنمای ساخت موشن با ایجنت آراِنا</title>
<style>{CSS}</style>
</head>
<body>
{CONTENT}
<script>
document.querySelectorAll(".copy").forEach(function(btn){{
  btn.addEventListener("click", function(){{
    var el = document.getElementById(btn.dataset.target);
    var txt = el.innerText;
    var done = function(){{ btn.textContent = "کپی شد ✓"; setTimeout(function(){{ btn.textContent="کپی"; }}, 1600); }};
    if (navigator.clipboard && navigator.clipboard.writeText) {{
      navigator.clipboard.writeText(txt).then(done).catch(function(){{ fallback(); }});
    }} else {{ fallback(); }}
    function fallback(){{
      var ta = document.createElement("textarea");
      ta.value = txt; document.body.appendChild(ta); ta.select();
      try {{ document.execCommand("copy"); done(); }} catch(e) {{}}
      document.body.removeChild(ta);
    }}
  }});
}});
</script>
</body>
</html>'''

open("آموزش-ساخت-موشن.html","w").write(html)
print("tutorial written:", round(len(html)/1024), "KB")
