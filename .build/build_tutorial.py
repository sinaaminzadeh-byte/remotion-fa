# -*- coding: utf-8 -*-
import json, sys
sys.path.insert(0,".build")
from design import head, topbar, toolbar, side_item, ICONS, footer

real   = json.load(open(".build/real.json"))
shots  = json.load(open(".build/shots.json"))

def realshot(key, cap):
    return f'''<figure class="fig real"><img src="data:image/jpeg;base64,{real[key]}" alt="{cap}">
      <figcaption><span class="dotg"></span> اسکرین‌شات واقعی از arena.ai — {cap}</figcaption></figure>'''

def mock(key, cap):
    return f'''<figure class="fig"><img src="data:image/jpeg;base64,{shots[key]}" alt="{cap}">
      <figcaption><span class="dotm"></span> بازسازی محیط ایجنت — {cap}</figcaption></figure>'''

PROMPT_MAIN = """ساخت موشن‌گرافیک با Remotion

━━ ۱) موضوع و پیام
موضوع: معرفی کافه‌ی «دانه»
پیام اصلی در یک جمله: قهوه‌ی تازه، هر روز صبح
مخاطب: مشتری‌های محلی، ۲۵ تا ۴۵ سال

━━ ۲) سبک گرافیکی
سبک انتخابی از کاتالوگ: شماره ۱۷ — کرافت / کارگاه (Kraft Artisan)
رنگ‌های برند: #C6A57A ، #2A2521 ، #F2E7D3
فونت: وزیرمتن (فارسی) — داخل پروژه لود شود

━━ ۳) متن و محتوا
متن روی ویدیو: «قهوه‌ی تازه، هر روز صبح»
زیرمتن: «دانه — از ۱۳۹۸»
نریشن: لینک فایل صوتی در بخش ۴
موسیقی: لینک فایل موسیقی در بخش ۴
لوگو: لینک تصویر PNG در بخش ۴

━━ ۴) فایل‌ها (لینک مستقیم)
نریشن: https://لینک-فایل-صوتی.mp3
موسیقی: https://لینک-موسیقی.mp3
لوگو: https://لینک-لوگو.png

━━ ۵) مشخصات فنی
ابعاد: ۱۰۸۰×۱۹۲۰ (ریلز) — نسخه‌ی ۱۹۲۰×۱۰۸۰ هم بساز
مدت: ۸ ثانیه | fps: ۳۰

━━ ۶) کارهایی که باید انجام بدهی
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

SIDEBAR = f'''
<aside class="sidebar">
  <div class="side-group">
    <div class="side-label">{ICONS['spark']} شروع سریع</div>
    <div class="side">
      {side_item("۱. ثبت‌نام", "#s1", cnt="۱ دقیقه", on=True)}
      {side_item("۲. انتخاب حالت ایجنت", "#s2", cnt="۱ دقیقه")}
      {side_item("۳. آماده‌سازی فایل‌ها", "#s3", cnt="۵ دقیقه")}
    </div>
  </div>
  <div class="side-group">
    <div class="side-label">{ICONS['book']} ساخت ویدیو</div>
    <div class="side">
      {side_item("۴. پرامپت شش‌بخشی", "#s4", pill="مهم")}
      {side_item("۵. ساخت توسط ایجنت", "#s5", cnt="۱۰ دقیقه")}
      <a href="#s6">۶. اصلاح و بازبینی</a>
      <a href="#s7">۷. دانلود خروجی</a>
    </div>
  </div>
  <div class="side-group">
    <div class="side-label">{ICONS['grid']} مرجع</div>
    <div class="side">
      {side_item("کاتالوگ ۳۰ سبک", "کاتالوگ-۳۰-سبک.html", cnt="۳۰")}
      {side_item("۳۹ سبک کدی", "۳۹-سبک-کدی.html", cnt="۳۹", pill="مهم")}
      <a href="#fix">عیب‌یابی رایج</a>
      <a href="#faq">پرسش‌های متداول</a>
    </div>
  </div>
</aside>'''

def step(id_, n, title, sub, body):
    return f'''
<section class="doc step" id="{id_}" style="margin-top:46px">
  <div style="display:flex;gap:14px;align-items:flex-start;margin-bottom:10px">
    <span style="flex-shrink:0;width:30px;height:30px;border-radius:9px;background:var(--fg);color:#fff;
      display:grid;place-items:center;font-size:13.5px;font-weight:700">{n}</span>
    <div>
      <h2 style="margin:2px 0 0">{title}</h2>
      <div style="font-size:13px;color:var(--faint);margin-top:2px">{sub}</div>
    </div>
  </div>
  {body}
</section>'''

CONTENT = f'''
{toolbar()}
<div class="doc">
  <div class="crumbs">راهنما <span>/</span> <b>ساخت موشن با ایجنت</b></div>
  <h1>با ایجنت آراِنا یک ویدیوی موشن فارسی بساز</h1>
  <p class="lead">
    در هفت قدم، از ثبت‌نام تا فایل MP4. ابزار <b>Remotion</b> را ایجنت برایت نصب می‌کند،
    سبک را از کاتالوگ ۳۰ سبکی انتخاب می‌کنی، متن و نریشن و لوگو را می‌دهی،
    و در پایان یک فایل ویدیو و کل پروژه را دانلود می‌کنی.
  </p>

  <div class="cardrow">
    <div>
      <div class="ico">{ICONS['film']}</div>
      <h3>حدود ۱۰ دقیقه</h3>
      <p>برای اولین ویدیو، از صفر تا خروجی MP4 — بدون نصب چیزی روی سیستم خودت.</p>
      <div class="tags"><span>8s · 30fps</span></div>
    </div>
    <div>
      <div class="ico">{ICONS['spark']}</div>
      <h3>بدون کدنویسی</h3>
      <p>فقط پرامپت می‌نویسی؛ نصب ابزار، ساخت کامپوننت و رندر را ایجنت انجام می‌دهد.</p>
      <div class="tags"><span>agent mode</span></div>
    </div>
    <div>
      <div class="ico">{ICONS['type']}</div>
      <h3>فارسی و راست‌به‌چپ</h3>
      <p>فونت وزیرمتن با ۹ وزن و چیدمان RTL از پیش تنظیم شده — بدون به‌هم‌ریختگی حروف.</p>
      <div class="tags"><span dir="ltr">Vazirmatn</span></div>
    </div>
  </div>

  <div class="note" style="margin-top:14px">
    <span class="ic">!</span>
    <div><b>قبل از شروع، چهار چیز آماده کن:</b>
      یک جمله پیام · متن‌های روی ویدیو (۷ تا ۱۰ کلمه) · فایل لوگو و نریشن (اگر داری) ·
      یک سبک از <a href="کاتالوگ-۳۰-سبک.html" style="color:var(--accent);font-weight:600">کاتالوگ ۳۰ سبک</a>.
    </div>
  </div>

  {step("s1","۱","در آراِنا ثبت‌نام کن","یک حساب رایگان، کمتر از یک دقیقه", f"""
    <ol>
      <li>به <code>arena.ai</code> برو.</li>
      <li>بالای صفحه روی <b>Sign up for free</b> بزن (یا <b>Log in</b> اگر حساب داری).</li>
      <li>با ایمیل یا حساب گوگل ثبت‌نام کن و ایمیل تأیید را کلیک کن.</li>
    </ol>
    <div class="note g"><span class="ic">✓</span><div>ثبت‌نام رایگان است و برای ساخت ویدیو نیازی به کارت بانکی یا اشتراک نیست.</div></div>
    {realshot("r1","دکمه‌ی ثبت‌نام گوشه‌ی بالا-راست")}
  """)}

  {step("s2","۲","حالت ایجنت را انتخاب کن","این مهم‌ترین انتخاب صفحه است", f"""
    <p>آراِنا چند حالت دارد (Battle، Side by Side، Agent). تو باید <b>Agent Mode</b> را انتخاب کنی،
    چون فقط این حالت است که فایل می‌سازد، ابزار نصب می‌کند و برایت رندر می‌گیرد.</p>
    <ol>
      <li>مستقیم به <code>arena.ai/agent</code> برو — <b>یا</b> از صفحه‌ی اصلی، دکمه‌ی حالت کنار کادر پیام را باز کن.</li>
      <li>گزینه‌ی <b>Agent Mode</b> را انتخاب کن.</li>
      <li>سمت راست صفحه پنل <b>Workspace</b> است — همه‌ی فایل‌های ساخته‌شده آنجا ظاهر می‌شوند.</li>
    </ol>
    {realshot("r2","منوی انتخاب حالت · Agent Mode را بزن")}
    {realshot("r3","صفحه‌ی Agent Mode · کادر پرامپت و دکمه‌ی ارسال")}
  """)}

  {step("s3","۳","فایل‌هایت را آماده کن","یا در چت آپلود کن، یا لینک بده", """
    <table class="tbl">
      <thead><tr><th>نوع فایل</th><th>سرویس رایگان</th><th>نکته‌ی مهم</th></tr></thead>
      <tbody>
        <tr><td><b>صدا / نریشن / موسیقی</b></td><td>tmpfiles.org · file.io · catbox.moe · Google Drive</td><td>لینک <b>مستقیم</b> بده که با .mp3 تمام شود، نه صفحه‌ی پیش‌نمایش</td></tr>
        <tr><td><b>لوگو / تصویر</b></td><td>imgur.com · postimages.org · Google Drive</td><td>PNG با پس‌زمینه‌ی شفاف، حداقل ۱۰۰۰ پیکسل</td></tr>
        <tr><td><b>ویدیو</b></td><td>catbox.moe · streamable · Google Drive</td><td>MP4 با کدک H.264</td></tr>
        <tr><td><b>فونت</b></td><td>Google Drive · GitHub (raw)</td><td>فایل ttf/otf + نام دقیق خانواده</td></tr>
        <tr><td><b>دیتا / نمودار</b></td><td>GitHub · Google Drive</td><td>CSV یا JSON</td></tr>
      </tbody>
    </table>
    <div class="note g"><span class="ic">✓</span><div><b>ساده‌ترین راه:</b> لازم نیست جایی آپلود کنی —
    فایل را مستقیم در چت ایجنت آپلود کن (دکمه‌ی گیره‌ی کاغذ در کادر پیام).
    آپلود در سرویس بیرونی فقط وقتی لازم است که لینک را نگه می‌داری یا فایل بزرگ است.</div></div>
  """)}

  {step("s4","۴","پرامپت را بفرست","شش بخش، و ایجنت بی‌نقص می‌سازد", f"""
    <p>پرامپت خوب برای موشن، شش بخش دارد. هرچه دقیق‌تر بنویسی، کمتر باید اصلاح کنی.</p>
    <div class="grid g3" style="margin:14px 0 20px">
      <div class="card"><h3>۱ · موضوع و پیام</h3><p>چه چیزی، برای چه کسی</p></div>
      <div class="card"><h3>۲ · سبک</h3><p>شماره از کاتالوگ + کد رنگ + فونت</p></div>
      <div class="card"><h3>۳ · متن و صدا</h3><p>متن روی ویدیو، نریشن، موسیقی</p></div>
      <div class="card"><h3>۴ · فایل‌ها</h3><p>لینک مستقیم صدا، لوگو، تصویر</p></div>
      <div class="card"><h3>۵ · مشخصات فنی</h3><p>ابعاد، مدت، fps</p></div>
      <div class="card"><h3>۶ · وظایف ایجنت</h3><p>نصب ابزار، ساخت، پیش‌نمایش، رندر، تحویل</p></div>
    </div>

    <div class="pbox">
      <div class="phead">
        <span>پرامپت کامل و آماده — فقط جاهای [کروشه] را عوض کن</span>
        <button class="copy" data-target="p-main">کپی</button>
      </div>
      <pre id="p-main">{PROMPT_MAIN}</pre>
    </div>

    <div class="note a"><span class="ic">!</span><div>
      <b>سه نکته که بیشترین تفاوت را می‌سازند:</b><br>
      بخش <b>۶</b> را حذف نکن — همان است که به ایجنت می‌گوید Remotion را نصب کند و در پایان MP4 بدهد.<br>
      اگر لینک فایل نداری، بنویس «بدون صدا بساز» تا ایجنت معطل نماند.<br>
      ننویس «قشنگ بساز». بنویس «سبک شماره ۹، رنگ #C7B8FF، ورودی فنری با damping 12».
    </div></div>

    <h3>نسخه‌ی کوتاه — وقتی عجله داری</h3>
    <div class="pbox">
      <div class="phead"><span>پرامپت کوتاه</span><button class="copy" data-target="p-quick">کپی</button></div>
      <pre id="p-quick">{PROMPT_QUICK}</pre>
    </div>
    {mock("p2_prompt","پرامپت شش‌بخشی در کادر پیام")}
  """)}

  {step("s5","۵","ایجنت پروژه را می‌سازد","چند دقیقه صبر، بدون کار اضافه", f"""
    <p>بعد از ارسال، ایجنت این کارها را به ترتیب انجام می‌دهد. لازم نیست چیزی نصب کنی:</p>
    <ol>
      <li><b>نصب ابزار:</b> Remotion و اسکیل‌های رسمی‌اش را نصب می‌کند.</li>
      <li><b>فونت فارسی:</b> فونت وزیرمتن را اضافه و قبل از رندر لود می‌کند تا متن خراب نشود.</li>
      <li><b>ساخت سبک:</b> کامپوننت ویدیو را با رنگ، تایپوگرافی و انیمیشن‌های سبک انتخابی می‌سازد.</li>
      <li><b>پیش‌نمایش:</b> یک محیط پیش‌نمایش زنده بالا می‌آورد تا فریم‌به‌فریم ببینی.</li>
      <li><b>رندر خروجی:</b> فایل MP4 را می‌سازد و کنارش کل پروژه را می‌گذارد.</li>
    </ol>
    {mock("p3_files","فایل‌های نتیجه در پنل Workspace")}
  """)}

  {step("s6","۶","ببین و اصلاح کن","بهترین بخش: تغییر با حرف زدن", f"""
    <p>ویدیو را ببین. بعد لازم نیست کد را دست بزنی — فقط به فارسی بگو چه چیزی را عوض کند.</p>
    <div class="pbox">
      <div class="phead"><span>پرامپت اصلاح — نمونه</span><button class="copy" data-target="p-fix">کپی</button></div>
      <pre id="p-fix">{PROMPT_FIX}</pre>
    </div>
    <div class="grid g3" style="margin-top:14px">
      <div class="card"><p>«سرعت انیمیشن را ۲۰٪ کم کن»</p></div>
      <div class="card"><p>«این کلمه را پررنگ‌تر و بزرگ‌تر کن»</p></div>
      <div class="card"><p>«پس‌زمینه را روشن‌تر کن»</p></div>
      <div class="card"><p>«نسخه‌ی عمودی هم بساز»</p></div>
      <div class="card"><p>«زیرنویس را بزرگ‌تر کن»</p></div>
      <div class="card"><p>«صحنه‌ی دوم را حذف کن»</p></div>
    </div>
    {mock("p4_preview","پیش‌نمایش زنده در محیط ایجنت")}
  """)}

  {step("s7","۷","خروجی را دانلود کن","MP4 آماده‌ی انتشار", f"""
    <div class="grid g2">
      <div class="card"><h3>دانلود ویدیو</h3><p>فایل <code>out/*.mp4</code> در ورک‌اسپیس است.
        روی آن کلیک کن و دانلود کن. مستقیم در اینستاگرام، یوتیوب یا لینکدین قابل انتشار است.</p></div>
      <div class="card"><h3>دانلود کل پروژه</h3><p>در پنل <b>Workspace</b> دکمه‌ی <b>Download</b> را بزن تا ZIP بگیری.
        با این ZIP بعداً همان ویدیو را برای محصول یا رنگ دیگر دوباره بسازی.</p></div>
    </div>
    <div class="note g" style="margin-top:14px"><span class="ic">✓</span><div>
      <b>نکته‌ی نگهداری:</b> ZIP را نگه دار. دفعه‌ی بعد لازم نیست از صفر شروع کنی —
      بگو «همان پروژه، این بار با متن جدید» و چند دقیقه وقت می‌برد.</div></div>
    {mock("p5_timeline","تایم‌لاین صحنه‌ها و مرحله‌ی رندر")}
  """)}


  <hr class="hr">

  <h2 id="as">۳۹ سبک کدی — وقتی می‌خواهی سبک «آمادهٔ اجرا» باشد</h2>
  <p>
    تا اینجا با <a href="کاتالوگ-۳۰-سبک.html">۳۰ زبان بصری</a> کار کردیم: هر سبک یک <b>توصیف</b> است و
    ایجنت باید از صفر آن را با کد بسازد. کنار آن، یک مجموعهٔ آماده هم هست:
    ریپوی <b><span style="direction:ltr">deenukhan/animation-styles</span></b> با <b>۳۹ سبک که کدشان نوشته شده</b> —
    وای‌بورد، تخته‌سیاه، آبرنگ، وودکات، اوکیویو، شیشهٔ رنگی، لیدار، برد مدار و…
  </p>

  <div class="cardrow" style="margin:18px 0">
    <div>
      <div class="ico">{ICONS['palette']}</div>
      <h3>کاتالوگ ۳۰ سبک = نقشه</h3>
      <p>زبان بصری را انتخاب می‌کنی و پرامپت می‌نویسی. آزادی کامل، ولی نتیجه بستگی به برداشت ایجنت دارد.</p>
      <div class="tags"><span>prompt-first</span></div>
    </div>
    <div>
      <div class="ico">{ICONS['film']}</div>
      <h3>۳۹ سبک کدی = قالب</h3>
      <p>کد سبک از قبل نوشته شده؛ ایجنت فقط قصهٔ تو را جایش می‌گذارد. نتیجه دقیق و تکرارپذیر.</p>
      <div class="tags"><span>code-first</span></div>
    </div>
    <div>
      <div class="ico">{ICONS['spark']}</div>
      <h3>هر دو با هم</h3>
      <p>از کاتالوگ انتخاب کن، اگر معادل کدی داشت شماره‌اش را بردار. ۱۴ سبک، معادل کدی دارند.</p>
      <div class="tags"><span>14 matches</span></div>
    </div>
  </div>

  <h3>قدم ۱ — نصب (یک‌بار، حدود ۵ دقیقه)</h3>
  <p>پیش‌نیاز: <b>Node.js 18+</b> و <b>Git</b>. اگر با ایجنت کار می‌کنی، همین جمله را به او بده:</p>
  <div class="pbox">
    <div class="phead"><span>پرامپت نصب</span><span class="phint">copy-paste</span>
      <button class="copy" data-target="p-install">کپی</button></div>
    <pre id="p-install">این اسکیل را برایم نصب کن:
https://github.com/deenukhan/animation-styles

بعد از نصب چک کن که «npm run list» هر ۳۹ سبک را نشان بدهد،
و به من بگو آماده است.</pre>
  </div>
  <p style="font-size:13px;color:var(--muted)">
    نصب دستی هم ساده است (بعد از آن یک مرورگر بی‌سر ~۱۰۰MB فقط بار اول دانلود می‌شود):
  </p>
  <div class="pbox">
    <div class="phead"><span>نصب دستی</span><span class="phint">terminal</span></div>
    <pre dir="ltr" style="max-height:none;line-height:1.9">git clone --depth 1 https://github.com/deenukhan/animation-styles.git ~/.claude/skills/animation-styles
cd ~/.claude/skills/animation-styles
npm install
npm run list    # باید ۳۹ سبک را نشان بدهد</pre>
  </div>

  <h3>قدم ۲ — سبک را انتخاب کن</h3>
  <p>شمارهٔ سبک را از <a href="۳۹-سبک-کدی.html">صفحهٔ ۳۹ سبک کدی</a> بردار (هر کارت، رندر واقعی همان سبک است).
     اگر مطمئن نیستی، در پرامپت بنویس «سه سبک پیشنهاد بده» و ایجنت از همان لیست انتخاب می‌کند.</p>

  <h3>قدم ۳ — پرامپت اصلی (قصهٔ خودت، سبک آماده)</h3>
  <div class="pbox">
    <div class="phead"><span>پرامپت ساخت با اسکیل</span><span class="phint">copy-paste</span>
      <button class="copy" data-target="p-skill">کپی</button></div>
    <pre id="p-skill">با اسکیل animation-styles یک ویدیو ۵ ثانیه‌ای بساز.

سبک: ۳۳ اوکیویو (ukiyo-e) — انتخاب دوم: ۱۱ آبرنگ
قصه (شش بیت):
۱. یک فنجان خالی روی میز چوبی
۲. قوری از راست وارد می‌شود
۳. چای می‌ریزد، فنجان پر می‌شود
۴. بخار بلند می‌شود
۵. متن «هر صبح، تازه» ظاهر می‌شود
۶. قوری از کادر خارج می‌شود

رنگ‌ها: #2A2521 ، #C6A57A ، #F2E7D3
ابعاد: ۱۰۸۰×۱۳۵۰ (۴:۵) | ۳۰fps | بی‌صدا

مسیر کار: اول جدول شش بیت را نشانم بده، بعد فایل شکل‌ها (shapes) را بساز،
بعد کامپوننت سبک را، بعد چند فریم را چک کن و در آخر MP4 نهایی را بده.
اگر سبک انتخاب‌شده برای این قصه مناسب نبود، قبل از شروع بگو.</pre>
  </div>

  <h3>قدم ۴ — تعویض سبک با یک جمله</h3>
  <p>همان قصه، سبک دیگر. ایجنت شکل‌ها را نگه می‌دارد و فقط لایهٔ سبک را عوض می‌کند:</p>
  <div class="pbox">
    <div class="phead"><span>پرامپت تغییر سبک</span><span class="phint">copy-paste</span>
      <button class="copy" data-target="p-restyle">کپی</button></div>
    <pre id="p-restyle">همان قصه را نگه دار، حالا به سبک ۶۴ پیکسل‌آرت RPG بساز.
فایل شکل‌ها را عوض نکن؛ فقط کامپوننت سبک را عوض کن و نسخهٔ قبلی را پاک نکن.
اسم‌گذاری: chai-pixel</pre>
  </div>

  <h3>قدم ۵ — بیرون بردن پروژه از پوشهٔ اسکیل</h3>
  <p>برای پروژهٔ واقعی، داخل اسکیل کار نکن. یک پوشهٔ مستقل بساز تا کد مال خودت باشد:</p>
  <div class="pbox">
    <div class="phead"><span>ساخت پروژهٔ مستقل</span><span class="phint">terminal</span></div>
    <pre dir="ltr">node ~/.claude/skills/animation-styles/scripts/new-project.mjs animation-films
cd animation-films &amp;&amp; npm install</pre>
  </div>

  <div class="note a" style="margin-top:14px"><span class="ic">!</span><div>
    <b>سه محدودیت را بدان:</b>
    ۱) قصهٔ پیش‌فرض همهٔ ۳۹ فیلم یکی است (کتری و کولاب) — باید قصهٔ خودت را بدهی.
    ۲) سبک‌های سه‌بعدی (۵۷، ۵۸، ۵۹، ۶۲، ۸۰) با مش سه‌بعدی ساخته می‌شوند و تغییرشان سخت‌تر است؛
    برای شروع از سبک‌های دو‌بعدی استفاده کن.
    ۳) خروجی این اسکیل عمودی ۴:۵ است؛ برای ریلز ۹:۱۶ باید ابعاد را در پرامپت بدهی.
  </div></div>

  <div class="note g" style="margin-top:12px"><span class="ic">✓</span><div>
    نمونه‌های آمادهٔ همهٔ این سبک‌ها را در <a href="۳۹-سبک-کدی.html">صفحهٔ ۳۹ سبک کدی</a> ببین.
  </div></div>

  <hr class="hr">
  <h2 id="fix">عیب‌یابی — اگر چیزی درست نشد</h2>
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

  <h2 id="faq">پرسش‌های متداول</h2>
  <h3>بدون نریشن هم می‌شود ویدیو ساخت؟</h3>
  <p>بله. در پرامپت بنویس «بدون صدا بساز». خیلی از موشن‌های شبکه‌های اجتماعی صامت‌اند و با زیرنویس کار می‌کنند.</p>
  <h3>چند ویدیو می‌شود ساخت؟</h3>
  <p>محدودیتی از طرف این ابزار نیست. محدودیت فقط زمان خودت است — هر ویدیو چند دقیقه ایجنت می‌برد.</p>
  <h3>اگر از سبک انتخابی خوشم نیامد؟</h3>
  <p>به ایجنت بگو «سبک را به شماره ۲۶ تغییر بده». تعویض سبک فقط عوض کردن یک کامپوننت است.</p>
  <h3>خروجی چه کیفیتی دارد؟</h3>
  <p>تا ۴K. با <code>--scale 2</code> در دستور رندر می‌شود دو برابر رزولوشن گرفت.</p>

  <div class="cta-card" style="margin-top:46px">
    <div>
      <h3 style="margin:0 0 4px">آماده‌ای؟</h3>
      <p style="margin:0;font-size:13.5px;color:var(--muted)">اول سبکت را از کاتالوگ انتخاب کن، بعد برگرد و پرامپت را پر کن.</p>
    </div>
    <a class="btn accent" href="۳۹-سبک-کدی.html">دیدن ۳۹ سبک کدی</a>
  </div>
</div>'''

RAIL = '''
<aside class="rail">
  <div class="rail-card">
    <h4>در این صفحه</h4>
    <div class="side" style="margin-top:4px">
      <a href="#s1">ثبت‌نام</a>
      <a href="#s2">انتخاب حالت ایجنت</a>
      <a href="#s3">آماده‌سازی فایل‌ها</a>
      <a href="#s4">پرامپت شش‌بخشی</a>
      <a href="#s5">ساخت توسط ایجنت</a>
      <a href="#s6">اصلاح و بازبینی</a>
      <a href="#s7">دانلود خروجی</a>
      <a href="#fix">عیب‌یابی</a>
      <a href="#faq">پرسش‌های متداول</a>
    </div>
  </div>
  <div class="rail-card dark">
    <h4>شروع سریع</h4>
    <p>پرامپت کامل را کپی کن، جاهای خالی را پر کن و در ایجنت بچسبان.</p>
    <a class="btn accent" style="width:100%;justify-content:center" href="#s4">رفتن به پرامپت</a>
  </div>
  <div class="rail-card">
    <h4>منابع</h4>
    <p><a href="کاتالوگ-۳۰-سبک.html" style="color:var(--accent);font-weight:600">کاتالوگ ۳۰ سبک</a><br>
       <a href="۳۹-سبک-کدی.html" style="color:var(--accent);font-weight:600">۳۹ سبک کدی (animation-styles)</a><br>
       <a href="https://www.remotion.dev/docs" target="_blank" rel="noopener" style="color:var(--muted)">مستندات Remotion</a><br>
       <a href="https://arena.ai/agent" target="_blank" rel="noopener" style="color:var(--muted)">صفحه‌ی ایجنت آراِنا</a></p>
  </div>
</aside>'''

EXTRA_CSS = """
.doc h2{scroll-margin-top:96px}
/* --- پرامپت‌باکس به سبک کارت کد remocn --- */
.pbox .phead{background:var(--card);border-bottom:1px solid var(--line2);padding:9px 12px 9px 15px}
.pbox .phead>span{display:inline-flex;align-items:center;gap:7px;font-weight:600;
  color:var(--fg);font-size:12.5px}
.pbox .phead>span:before{content:"";width:7px;height:7px;border-radius:2px;
  background:var(--accent);display:inline-block}
.pbox .phint{font-size:11px;color:var(--faint);font-family:ui-monospace,monospace;
  direction:ltr;margin-inline-start:auto;margin-inline-end:10px}
.pbox pre{background:#0A0D11;font-size:12.4px;line-height:2.05;padding:16px 18px}
.pbox pre::-webkit-scrollbar{width:8px}
.pbox pre::-webkit-scrollbar-thumb{background:#D8DCDF;border-radius:8px}
/* --- حالت فهرستی --- */
html.view-list .cardrow{grid-template-columns:1fr}
html.view-list .cardrow>*{border-inline-start:0;border-top:1px solid var(--line2)}
html.view-list .cardrow>*:first-child{border-top:0}
html.view-list .grid.g3{grid-template-columns:1fr}
html.view-list .fig,html.view-list .pbox{margin-top:12px}
/* --- شکل‌ها --- */
.fig img{aspect-ratio:16/9;object-fit:cover;object-position:top center}
.fig{border-radius:var(--r-lg)}

.fig{margin:18px 0 0;border:1px solid var(--line);border-radius:var(--r-lg);overflow:hidden;background:var(--card);box-shadow:var(--sh-sm)}
.fig img{width:100%;display:block}
.fig figcaption{display:flex;align-items:center;gap:8px;padding:9px 15px;font-size:12px;
  color:var(--muted);border-top:1px solid var(--line2);background:rgba(255,255,255,.03)}
.fig.real figcaption{background:rgba(52,211,153,.1);color:#7FE8C0}
.dotg,.dotm{width:7px;height:7px;border-radius:50%;flex-shrink:0}
.dotg{background:#15A05E;box-shadow:0 0 0 3px rgba(21,160,94,.15)}
.dotm{background:#B7BEC2}
.pbox{border:1px solid var(--line);border-radius:var(--r-lg);overflow:hidden;margin:12px 0 18px;background:var(--card);box-shadow:var(--sh-sm)}
.phead{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:10px 15px;
  border-bottom:1px solid var(--line2);background:var(--soft);font-size:12.5px;color:var(--muted)}
.copy{background:linear-gradient(180deg,#3D8BFF,#2069E8);color:#fff;border:0;border-radius:8px;padding:6px 14px;font-size:12px;
  font-family:inherit;font-weight:600;cursor:pointer;transition:.15s}
.copy:hover{filter:brightness(1.08)}
.pbox pre{margin:0;padding:16px 18px;font-size:12.5px;line-height:2;white-space:pre-wrap;
  color:#C9D6E4;font-family:'JetBrains Mono',ui-monospace,monospace;direction:rtl;text-align:right;
  max-height:430px;overflow:auto}
.cta-card{display:flex;align-items:center;justify-content:space-between;gap:18px;flex-wrap:wrap;
  border:1px solid var(--line);border-radius:var(--r-lg);background:linear-gradient(180deg,#11161D,#0C1015);
  padding:20px 22px;box-shadow:var(--sh-sm)}
"""

html = head("راهنمای ساخت موشن با ایجنت آراِنا", EXTRA_CSS) + \
 topbar("guide") + \
 f'<div class="shell">{SIDEBAR}<main class="content">{CONTENT}</main>{RAIL}</div>' + \
 footer() + '''<script>
document.querySelectorAll(".copy").forEach(function(b){
  b.addEventListener("click",function(){
    var t=document.getElementById(b.dataset.target).innerText;
    var done=function(){b.textContent="کپی شد";setTimeout(function(){b.textContent="کپی";},1600);};
    if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(t).then(done).catch(fb);}
    else fb();
    function fb(){var a=document.createElement("textarea");a.value=t;document.body.appendChild(a);a.select();
      try{document.execCommand("copy");done();}catch(e){}document.body.removeChild(a);}
  });
});
// active sidebar on scroll
var secs=[...document.querySelectorAll("section[id],h2[id]")];
var links=[...document.querySelectorAll(".sidebar .side a")];
function sync(){
  var y=window.scrollY+120,cur=null;
  secs.forEach(function(s){if(s.offsetTop<=y)cur=s.id;});
  links.forEach(function(a){a.classList.toggle("on",a.getAttribute("href")==="#"+cur);});
}
window.addEventListener("scroll",sync,{passive:true});sync();
</script>
</body></html>'''

open("آموزش-ساخت-موشن.html","w").write(html)
print("tutorial:", round(len(html)/1024), "KB")
