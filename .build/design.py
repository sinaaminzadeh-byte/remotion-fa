# -*- coding: utf-8 -*-
"""توکن‌های طراحی مشترک - بازطراحی به سبک remocn.dev (نسخه ۲)"""
FONT_CSS = open(".build/fonts/embed.css").read()

BASE_CSS = """
:root{
  --bg:#080A0D; --bg2:#0C0F14; --fg:#EEF2F6; --muted:#9AA8B6; --faint:#6B7B8A;
  --line:rgba(255,255,255,.10); --line2:rgba(255,255,255,.06);
  --card:#10141A; --card2:#0D1117; --soft:#151A21; --soft2:#1B222B;
  --accent:#2F80FF; --accent-ink:#1E6BFA; --accent-soft:rgba(47,128,255,.14);
  --accent-glow:rgba(47,128,255,.35);
  --purple:#A78BFA; --purple-soft:rgba(167,139,250,.16);
  --green:#34D399; --green-soft:rgba(52,211,153,.14);
  --r-sm:8px; --r:10px; --r-lg:14px; --r-xl:18px;
  --sh-xs:0 1px 1px rgba(0,0,0,.3);
  --sh-sm:0 1px 2px rgba(0,0,0,.35);
  --sh:0 1px 2px rgba(0,0,0,.4),0 10px 24px -16px rgba(0,0,0,.8);
  --sh-lg:0 1px 3px rgba(0,0,0,.5),0 22px 44px -24px rgba(0,0,0,.9);
  --ring:0 0 0 3px rgba(47,128,255,.35);
  --maxw:1280px;
  --grad:linear-gradient(180deg,#0B0E13,#080A0D);
}
*{box-sizing:border-box}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{
  margin:0;color:var(--fg);
  background:
    radial-gradient(1100px 520px at 50% -180px, rgba(47,128,255,.10), transparent 70%),
    radial-gradient(700px 400px at 90% 10%, rgba(47,128,255,.05), transparent 70%),
    var(--bg);
  background-attachment:fixed;
  font-family:'Vazirmatn','Segoe UI',system-ui,sans-serif;
  font-size:15.5px;line-height:1.75;font-weight:400;
  -webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;
  font-feature-settings:"ss01";
}
::selection{background:rgba(47,128,255,.35);color:#fff}
a{color:inherit;text-decoration:none}
:focus-visible{outline:none;box-shadow:var(--ring);border-radius:8px}
code{
  font-family:'JetBrains Mono',ui-monospace,SFMono-Regular,Menlo,monospace;
  font-size:.85em;background:var(--soft);border:1px solid var(--line);
  padding:.1em .42em;border-radius:6px;direction:ltr;display:inline-block;
  color:#C9D6E4;
}
h1,h2,h3,h4{font-weight:700;letter-spacing:-.025em;line-height:1.28;margin:0}
p{margin:0}
svg{flex-shrink:0}

/* ================= top bar (floating) ================= */
.topbar{position:sticky;top:0;z-index:80;padding:10px 24px 0;
  background:linear-gradient(180deg,rgba(8,10,13,.94) 60%,rgba(8,10,13,0))}
.bar{max-width:var(--maxw);margin:0 auto;display:flex;align-items:center;gap:10px;
  height:54px;padding:0 8px 0 10px;border-radius:16px;
  background:rgba(16,20,26,.78);border:1px solid var(--line);
  box-shadow:0 1px 0 rgba(255,255,255,.04) inset,var(--sh-sm);backdrop-filter:saturate(160%) blur(18px)}
.brand{display:flex;align-items:center;gap:9px;font-weight:800;font-size:15px;
  letter-spacing:-.015em;padding:0 6px 0 2px;white-space:nowrap}
.brand .mark{width:26px;height:26px;border-radius:8px;background:linear-gradient(160deg,#3D8BFF,#1E5FE0);
  display:grid;place-items:center;flex-shrink:0;box-shadow:var(--sh-xs)}
.nav{display:flex;align-items:center;gap:2px;background:rgba(255,255,255,.04);
  border-radius:12px;padding:3px;position:relative}
.nav a,.nav summary{padding:6px 13px;border-radius:9px;font-size:13.5px;color:var(--muted);
  font-weight:500;transition:color .14s,background .14s,box-shadow .14s;
  white-space:nowrap;cursor:pointer;display:flex;align-items:center;gap:6px;list-style:none}
.nav summary::-webkit-details-marker{display:none}
.nav a:hover,.nav summary:hover{color:var(--fg)}
.nav a.active,.nav details[open] summary{color:#fff;background:rgba(47,128,255,.16);font-weight:600;
  box-shadow:0 0 0 1px rgba(47,128,255,.35) inset}
.nav .new{font-size:10px;font-weight:700;padding:1px 6px;border-radius:6px;
  background:var(--purple-soft);color:var(--purple);line-height:1.5}
.navdrop{position:relative}
.navdrop .menu{position:absolute;top:calc(100% + 10px);inset-inline-start:0;min-width:214px;
  background:var(--card);border:1px solid var(--line);border-radius:12px;padding:6px;
  box-shadow:var(--sh-lg);display:flex;flex-direction:column;gap:1px;z-index:90}
.navdrop .menu a{padding:8px 10px;border-radius:8px;font-size:13px;color:var(--muted)}
.navdrop .menu a:hover{background:var(--soft);color:var(--fg)}
.navdrop .menu .k{font-size:11px;color:var(--faint);margin-inline-start:auto}
.spacer{flex:1}
.ghost{display:inline-flex;align-items:center;gap:7px;height:34px;padding:0 12px;
  border-radius:10px;border:1px solid var(--line);background:rgba(255,255,255,.04);font-size:13px;
  color:var(--muted);font-weight:500;box-shadow:var(--sh-xs);transition:.14s}
.ghost:hover{color:#fff;border-color:rgba(47,128,255,.5);background:rgba(47,128,255,.10)}
.ghost .num{font-size:12px;color:var(--faint);font-variant-numeric:tabular-nums}
.vline{width:1px;height:20px;background:var(--line);margin:0 2px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:7px;height:34px;
  padding:0 16px;border-radius:10px;background:var(--soft2);color:var(--fg);font-size:13.5px;
  font-weight:600;border:1px solid var(--line);transition:.14s;white-space:nowrap;
  font-family:inherit;cursor:pointer;box-shadow:var(--sh-xs)}
.btn:hover{background:#232C37;transform:translateY(-.5px)}
.btn:active{transform:none}
.btn.accent{background:linear-gradient(180deg,#3D8BFF,#1E63E0);border-color:#2F80FF;color:#fff;
  box-shadow:0 1px 0 rgba(255,255,255,.18) inset,0 6px 18px -8px var(--accent-glow)}
.btn.accent:hover{background:linear-gradient(180deg,#57A0FF,#2A72F2);border-color:#4A94FF}

/* ================= content toolbar ================= */
.toolbar{display:flex;align-items:center;gap:9px;margin-bottom:26px}
.toolset{display:flex;gap:3px;background:var(--card);border:1px solid var(--line);
  border-radius:12px;padding:4px;box-shadow:var(--sh-sm)}
.tbtn{width:32px;height:28px;border-radius:8px;display:grid;place-items:center;
  color:var(--muted);border:0;background:transparent;cursor:pointer;transition:.13s}
.tbtn:hover{background:var(--soft);color:var(--fg)}
.tbtn.cur{background:rgba(47,128,255,.16);color:#8FB9FF;box-shadow:0 0 0 1px rgba(47,128,255,.3) inset}
.tarrows{display:flex;gap:3px}
.copypage{margin-inline-start:auto;display:inline-flex;align-items:center;gap:9px;
  height:32px;padding:0 8px 0 13px;border-radius:10px;border:1px solid var(--line);
  background:var(--card);font-size:12.5px;color:var(--muted);cursor:pointer;
  font-family:inherit;box-shadow:var(--sh-sm);transition:.14s}
.copypage:hover{color:#fff;border-color:rgba(47,128,255,.45)}
.copypage .k{display:grid;place-items:center;min-width:26px;height:20px;padding:0 5px;
  border-radius:6px;background:var(--soft);font-size:10.5px;color:var(--faint);
  font-family:ui-monospace,monospace}

/* ================= docs shell ================= */
.shell{max-width:var(--maxw);margin:0 auto;padding:22px 24px 40px;display:grid;
  grid-template-columns:236px minmax(0,1fr) 244px;gap:38px;align-items:start}
.sidebar{position:sticky;top:82px;font-size:13.5px}
.side-group{margin-bottom:20px;padding-bottom:16px;border-bottom:1px solid var(--line2)}
.side-group:last-child{border-bottom:0;padding-bottom:0;margin-bottom:0}
.side-label{display:flex;align-items:center;gap:7px;font-weight:700;font-size:12.5px;
  color:var(--fg);margin:0 0 7px;padding:0 9px;letter-spacing:.005em}
.side-label svg{opacity:.55}
.side a{display:flex;align-items:center;gap:8px;padding:6px 9px;border-radius:8px;
  color:var(--muted);font-weight:400;line-height:1.5;border-inline-start:2px solid transparent;
  transition:.13s;font-size:13.5px;position:relative}
.side a:hover{color:var(--fg);background:var(--soft)}
.side a.on{color:#fff;font-weight:600;background:rgba(47,128,255,.12);
  border-inline-start-color:var(--accent)}
.side .cnt{margin-inline-start:auto;font-size:11px;color:var(--faint);
  font-variant-numeric:tabular-nums;letter-spacing:0}
.side .pill{font-size:10px;font-weight:700;padding:1px 7px;border-radius:6px;
  background:var(--purple-soft);color:#C4B5FD;line-height:1.6}
.side .chev{color:var(--faint);opacity:.55;margin-inline-start:auto;display:inline-flex}
.side a:has(.cnt) .chev{margin-inline-start:4px}
.side a.on .chev{opacity:1;color:var(--fg)}

.content{min-width:0}
.crumbs{display:flex;align-items:center;gap:8px;font-size:12.5px;color:var(--faint);
  margin-bottom:12px}
.crumbs b{color:var(--muted);font-weight:500}
.doc h1{font-size:clamp(29px,3.35vw,45px);letter-spacing:-.038em;line-height:1.2;color:#F5F8FB;
  margin:0 0 16px;font-weight:700}
.doc .lead{font-size:17px;line-height:1.85;color:var(--muted);max-width:68ch;
  margin-bottom:10px;letter-spacing:-.005em}
.doc h2{font-size:22px;margin:46px 0 12px;letter-spacing:-.028em;scroll-margin-top:90px}
.doc h3{font-size:16px;margin:26px 0 8px;letter-spacing:-.02em}
.doc p{margin:0 0 13px;color:#B9C6D3;max-width:72ch}
.doc ul,.doc ol{margin:0 0 14px;padding-inline-start:19px;color:#B9C6D3}
.doc li{margin-bottom:7px}
.doc li::marker{color:var(--faint)}
.doc strong,.doc b{font-weight:700;color:#F0F4F8}
.doc a[href]:not(.btn):not(.card):not(.bcard){color:var(--accent);font-weight:500}
.doc a[href]:not(.btn):not(.card):not(.bcard):hover{text-decoration:underline;
  text-underline-offset:3px}
.hr{height:1px;background:var(--line2);border:0;margin:34px 0}

/* ================= right rail ================= */
.rail{position:sticky;top:82px;display:flex;flex-direction:column;gap:12px}
.rail-card{border:1px solid var(--line);border-radius:var(--r-lg);background:var(--card);
  padding:14px;box-shadow:var(--sh-sm)}
.rail-card h4{font-size:12.5px;margin:0 0 8px;letter-spacing:-.01em}
.rail-card p{font-size:12.5px;color:var(--muted);line-height:1.7;margin:0 0 10px}
.rail-card.dark{background:linear-gradient(165deg,#132033,#0E1622);border-color:rgba(47,128,255,.35);color:#E9EDEF}
.rail-card.dark p{color:#9FB2C6}
.rail-card.dark a{color:#fff}
.rail-thumb{border-radius:10px;background:var(--soft);border:1px solid var(--line2);
  height:66px;margin-bottom:10px;display:flex;align-items:center;justify-content:center;
  gap:6px;overflow:hidden}
.rail-thumb i{display:block;border-radius:4px;background:#fff;box-shadow:var(--sh-sm)}

/* ================= cards ================= */
.grid{display:grid;gap:14px}
.g2{grid-template-columns:repeat(2,minmax(0,1fr))}
.g3{grid-template-columns:repeat(3,minmax(0,1fr))}
.card{background:var(--card);border:1px solid var(--line);border-radius:var(--r-lg);
  padding:17px;box-shadow:var(--sh-sm);transition:.16s}
.card:hover{border-color:rgba(47,128,255,.35);box-shadow:var(--sh);transform:translateY(-1px)}
.card .ico{width:32px;height:32px;border-radius:9px;background:var(--soft);
  display:grid;place-items:center;margin-bottom:11px;font-size:14px;color:var(--muted);
  border:1px solid var(--line2)}
.card h3{font-size:14.5px;margin:0 0 5px}
.card p{font-size:13px;color:var(--muted);margin:0;line-height:1.7}
/* یک کارت با ستون‌های جدا شده (سبک remocn) */
.cardrow{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));
  border:1px solid var(--line);border-radius:var(--r-xl);background:var(--card);
  box-shadow:var(--sh-sm);overflow:hidden;margin:22px 0 8px}
.cardrow>*{padding:20px;border-inline-start:1px solid var(--line2)}
.cardrow>*:first-child{border-inline-start:0}
.cardrow h3{font-size:14.5px;margin:0 0 6px}
.cardrow p{font-size:12.8px;color:var(--muted);line-height:1.75;margin:0}
.cardrow .ico{width:32px;height:32px;border-radius:9px;background:var(--bg);
  border:1px solid var(--line2);display:grid;place-items:center;margin-bottom:12px;
  color:var(--muted)}
.cardrow .tags{margin-top:10px;display:flex;gap:6px;flex-wrap:wrap}
.cardrow .tags span{font-size:11px;padding:2px 8px;border-radius:6px;
  background:var(--soft);color:var(--muted);direction:ltr}

.note{border:1px solid var(--line);border-radius:var(--r);background:var(--soft);
  padding:12px 15px;font-size:13.3px;color:#C3CFDB;display:flex;gap:10px;
  align-items:flex-start;line-height:1.7}
.note.a{border-color:rgba(47,128,255,.4);background:var(--accent-soft)}
.note.g{border-color:rgba(52,211,153,.35);background:var(--green-soft)}
.note .ic{flex-shrink:0;font-weight:800;color:#6EA8FF;line-height:1.5}
.note.g .ic{color:#34D399}

table.tbl{width:100%;border-collapse:separate;border-spacing:0;font-size:13.3px;
  border:1px solid var(--line);border-radius:var(--r);overflow:hidden;margin:6px 0 16px;
  background:var(--card)}
table.tbl th{text-align:right;padding:10px 14px;background:var(--soft);color:#DDE6EF;
  font-weight:700;font-size:12.5px;border-bottom:1px solid var(--line)}
table.tbl td{padding:10px 14px;border-bottom:1px solid var(--line2);color:#B9C6D3;
  vertical-align:top}
table.tbl tr:last-child td{border-bottom:0}
table.tbl tr:hover td{background:rgba(255,255,255,.025)}

footer.site{border-top:1px solid var(--line2);margin-top:56px;padding:30px 24px 34px;
  text-align:center;font-size:12.5px;color:var(--faint);background:linear-gradient(180deg,transparent,rgba(47,128,255,.04))}
.foot-in{max-width:640px;margin:0 auto;display:flex;flex-direction:column;align-items:center;gap:12px}
.foot-name{font-size:14px;color:#E7EEF6;font-weight:700;letter-spacing:-.01em}
.foot-name span{display:block;font-size:11.5px;color:var(--faint);font-weight:400;margin-top:3px}
.foot-social{display:flex;align-items:center;gap:8px;flex-wrap:wrap;justify-content:center}
.foot-social a{display:inline-flex;align-items:center;gap:6px;height:30px;padding:0 12px;border-radius:8px;
  border:1px solid var(--line);background:rgba(255,255,255,.03);color:var(--muted);font-size:12px;
  transition:.15s;direction:ltr}
.foot-social a:hover{color:#fff;border-color:rgba(47,128,255,.5);background:rgba(47,128,255,.1)}
.foot-social svg{opacity:.85}

@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
@media(max-width:1180px){.shell{grid-template-columns:220px minmax(0,1fr)}.rail{display:none}}
@media(max-width:860px){
  .shell{grid-template-columns:1fr;padding:16px;gap:22px}
  .sidebar{position:static;order:2;border-top:1px solid var(--line2);padding-top:18px}
  .content{order:1}
  .topbar{padding:8px 10px 0}
  .bar{height:auto;padding:8px;gap:8px;border-radius:14px;display:grid;
    grid-template-columns:auto 1fr auto auto;
    grid-template-areas:"brand . gh cta" "nav nav nav nav";row-gap:9px}
  .brand{grid-area:brand}
  .spacer{display:none}
  .vline{display:none}
  .ghost{grid-area:gh;width:34px;padding:0;justify-content:center}
  .ghost .num,.ghost .ghtext{display:none}
  .btn{grid-area:cta}
  .nav{grid-area:nav;width:100%;overflow-x:auto;justify-content:flex-start;
    -webkit-overflow-scrolling:touch;padding:3px}
  .nav::-webkit-scrollbar{display:none}
  .brand{font-size:14px}
  .ghost .num{display:none}
  .g2,.g3,.cardrow{grid-template-columns:1fr}
  .cardrow>*{border-inline-start:0;border-top:1px solid var(--line2)}
  .cardrow>*:first-child{border-top:0}
  .toolbar{margin-bottom:18px}
  .copypage{display:none}
}
@media print{
  .topbar,.toolbar,.rail,.sidebar,footer.site{display:none!important}
  .shell{grid-template-columns:1fr;padding:0}
  body{background:#fff}
}
"""

BRAND_MARK = ('<svg width="15" height="15" viewBox="0 0 24 24" fill="none" '
  'stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">'
  '<path d="M3 17l5-9 4 6 3-5 6 8"/></svg>')

GH_ICON = ('<svg width="14" height="14" viewBox="0 0 16 16" fill="currentColor">'
  '<path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38'
  ' 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15'
  '-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07'
  '-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12'
  ' 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82'
  ' 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95'
  ' .29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0016 8'
  'c0-4.42-3.58-8-8-8z"/></svg>')

CHEV = ('<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
  'stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">'
  '<path d="M14 6l-6 6 6 6"/></svg>')

CHEV_D = ('<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
  'stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">'
  '<path d="M6 9l6 6 6-6"/></svg>')

NAV_ITEMS = [
    ("home",    "خانه",              "index.html",              None,        "خانه"),
    ("guide",   "راهنمای ساخت",      "آموزش-ساخت-موشن.html",    None,        "راهنمای ساخت"),
    ("catalog", "۳۰ سبک گرافیکی",    "کاتالوگ-۳۰-سبک.html",     "جدید",      "کاتالوگ ۳۰ سبک"),
    ("report",  "گزارش تحقیق",       "گزارش-سبک‌ها-و-ابزارهای-موشن.md", None, "گزارش تحقیق"),
]


def topbar(active):
    """نوار بالا: برند + پیل ناوبری + GitHub + دکمه‌ی اصلی."""
    first_label = "خانه"
    first_active = "active" if active == "home" else ""
    links = [
        ("guide",   "راهنمای ساخت",    "آموزش-ساخت-موشن.html",     None),
        ("catalog", "۳۰ سبک گرافیکی",  "کاتالوگ-۳۰-سبک.html",      None),
        ("styles",  "۳۹ سبک کدی",      "۳۹-سبک-کدی.html",          "جدید"),
        ("report",  "گزارش تحقیق",     "گزارش-سبک‌ها-و-ابزارهای-موشن.md", None),
    ]
    nav = f'''
      <details class="navdrop">
        <summary class="{first_active}">{first_label} {CHEV_D}</summary>
        <div class="menu">
          <a href="index.html">صفحه‌ی خانه <span class="k">H</span></a>
          <a href="آموزش-ساخت-موشن.html">راهنمای ساخت <span class="k">G</span></a>
          <a href="کاتالوگ-۳۰-سبک.html">کاتالوگ ۳۰ سبک <span class="k">C</span></a>
          <a href="۳۹-سبک-کدی.html">۳۹ سبک کدی <span class="k">S</span></a>
          <a href="گزارش-سبک‌ها-و-ابزارهای-موشن.md">گزارش و منابع <span class="k">R</span></a>
        </div>
      </details>'''
    for key, label, href, badge in links:
        cls = "active" if active == key else ""
        b = f' <span class="new">{badge}</span>' if badge else ""
        nav += f'\n      <a class="{cls}" href="{href}">{label}{b}</a>'
    return f'''
<header class="topbar">
  <div class="bar">
    <a class="brand" href="index.html">
      <span class="mark">{BRAND_MARK}</span> استودیوی موشن
    </a>
    <nav class="nav">{nav}</nav>
    <span class="spacer"></span>
    <a class="ghost" href="https://github.com/sinaaminzadeh-byte/remotion-fa"
       target="_blank" rel="noopener">{GH_ICON} <span class="ghtext">GitHub</span> <span class="num">۱۳۸۵+</span></a>
    <span class="vline"></span>
    <a class="btn accent" href="آموزش-ساخت-موشن.html#s4">شروع ساخت</a>
  </div>
</header>'''


TOOLBAR_ICONS = {
    "grid": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"><rect x="3" y="3" width="7" height="7" rx="2"/><rect x="14" y="3" width="7" height="7" rx="2"/><rect x="3" y="14" width="7" height="7" rx="2"/><rect x="14" y="14" width="7" height="7" rx="2"/></svg>',
    "list": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"><path d="M8 6h13M8 12h13M8 18h13M3.5 6h.01M3.5 12h.01M3.5 18h.01"/></svg>',
    "print": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"><path d="M6 9V3h12v6M6 18H4a2 2 0 0 1-2-2v-4a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="7" rx="1"/></svg>',
    "up": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"><path d="M12 19V5M5 12l7-7 7 7"/></svg>',
    "top": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M9 18l6-6-6-6"/></svg>',
    "prev": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M15 18l-6-6 6-6"/></svg>',
    "link": '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M10 13a5 5 0 0 0 7 0l2-2a5 5 0 0 0-7-7l-1 1"/><path d="M14 11a5 5 0 0 0-7 0l-2 2a5 5 0 0 0 7 7l1-1"/></svg>',
}


IG_ICON = ('<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
  'stroke-width="2" stroke-linecap="round"><rect x="3" y="3" width="18" height="18" rx="5"/>'
  '<circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r=".9" fill="currentColor" stroke="none"/></svg>')
TG_ICON = ('<svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor">'
  '<path d="M21.9 4.3L18.6 20c-.2 1-.9 1.3-1.8.8l-4.9-3.6-2.4 2.3c-.3.3-.5.5-1 .5l.4-4.9 9-8.1c.4-.4-.1-.6-.6-.2L6.2 13.1 1.6 11.6c-1-.3-1-1 .2-1.5l18.7-7.2c.8-.3 1.6.2 1.4 1.4z"/></svg>')
SOC_IG = "https://instagram.com/ai_sinaaminzadeh"
SOC_TG = "https://t.me/ai_sinaaminzadeh"

def footer(extra=""):
    return f'''<footer class="site">
  <div class="foot-in">
    <div class="foot-name">تهیه شده توسط سینا امین‌زاده<span>استودیوی موشن — راهنمای ساخت موشن‌گرافیک فارسی با Remotion</span></div>
    <div class="foot-social">
      <a href="{SOC_IG}" target="_blank" rel="noopener">{IG_ICON} {SOC_IG.replace("https://instagram.com/","@")}</a>
      <a href="{SOC_TG}" target="_blank" rel="noopener">{TG_ICON} {SOC_TG.replace("https://t.me/","@")}</a>
    </div>
    {extra}
  </div>
</footer>'''

def side_item(label, href="#", cnt=None, pill=None, on=False, chev=True):
    """آیتم سایدبار: [برچسب] [شمارنده] [‹]  (فلش قبل از شمارنده، مثل remocn)"""
    cls = ' class="on"' if on else ""
    tail = ""
    if cnt:
        tail += f'<span class="cnt">{cnt}</span>'
    if pill:
        tail += f'<span class="pill">{pill}</span>'
    if chev:
        tail += f'<span class="chev">{CHEV}</span>'
    return f'<a href="{href}"{cls}>{label}{tail}</a>'


def toolbar(mode="doc"):
    """نوار ابزار محتوا (شبیه toolbar صفحه‌ی remocn)."""
    I = TOOLBAR_ICONS
    return f'''
<div class="toolbar">
  <div class="toolset">
    <button class="tbtn cur" data-tb="grid" title="نمایش کارتی">{I['grid']}</button>
    <button class="tbtn" data-tb="list" title="نمایش فهرستی">{I['list']}</button>
    <button class="tbtn" data-tb="print" title="چاپ / PDF">{I['print']}</button>
    <button class="tbtn" data-tb="up" title="بالای صفحه">{I['up']}</button>
  </div>
  <div class="tarrows">
    <button class="tbtn" data-tb="back" title="بازگشت">{I['top']}</button>
    <button class="tbtn" data-tb="fwd" title="جلو">{I['prev']}</button>
  </div>
  <button class="copypage" data-tb="link">{I['link']} کپی لینک صفحه <span class="k">⌘C</span></button>
</div>'''


HEAD_JS = r"""
<script>
document.addEventListener("DOMContentLoaded",function(){
  /* دکمه‌های نوار ابزار */
  document.querySelectorAll("[data-tb]").forEach(function(b){
    b.addEventListener("click",function(e){
      var k=b.dataset.tb;
      if(k==="print"){window.print();return;}
      if(k==="up"){window.scrollTo({top:0,behavior:"smooth"});return;}
      if(k==="back"){history.back();return;}
      if(k==="fwd"){history.forward();return;}
      if(k==="link"){
        var url=location.href;
        var done=function(){var o=b.innerHTML;b.innerHTML='<span style="color:#0F7A4A;font-weight:600">لینک کپی شد</span>';setTimeout(function(){b.innerHTML=o;},1500);};
        if(navigator.clipboard){navigator.clipboard.writeText(url).then(done).catch(function(){prompt("لینک صفحه:",url);});}
        else{prompt("لینک صفحه:",url);}
        return;
      }
      if(k==="grid"||k==="list"){
        document.querySelectorAll("[data-tb=grid],[data-tb=list]").forEach(function(x){x.classList.remove("cur");});
        b.classList.add("cur");
        document.documentElement.classList.toggle("view-list",k==="list");
      }
    });
  });
  /* بستن منوی ناوبری با کلیک بیرون */
  document.querySelectorAll(".navdrop").forEach(function(d){
    document.addEventListener("click",function(e){if(!d.contains(e.target))d.removeAttribute("open");});
  });
  /* میان‌برهای صفحه‌کلید */
  document.addEventListener("keydown",function(e){
    if(e.target.matches("input,textarea"))return;
    var map={h:"index.html",g:"آموزش-ساخت-موشن.html",c:"کاتالوگ-۳۰-سبک.html",s:"۳۹-سبک-کدی.html"};
    var k=e.key.toLowerCase();
    if(map[k]&&!e.metaKey&&!e.ctrlKey){location.href=map[k];}
  });
});
</script>
"""


def head(title, css_extra=""):
    return f'''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="dark">
<title>{title}</title>
<style>
{FONT_CSS}
{BASE_CSS}
{css_extra}
</style>
{HEAD_JS}
</head>
<body>'''


ICONS = {
 "spark": '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"><path d="M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9z"/><path d="M18 15.5l.9 2.1 2.1.9-2.1.9-.9 2.1-.9-2.1-2.1-.9 2.1-.9z"/></svg>',
 "book": '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>',
 "grid": '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"><rect x="3" y="3" width="7" height="7" rx="2"/><rect x="14" y="3" width="7" height="7" rx="2"/><rect x="3" y="14" width="7" height="7" rx="2"/><rect x="14" y="14" width="7" height="7" rx="2"/></svg>',
 "type": '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"><path d="M4 7V5h16v2M9 19h6M12 5v14"/></svg>',
 "palette": '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"><path d="M12 21a9 9 0 1 1 9-9c0 2.2-1.8 3.5-3.6 3.5H16a2 2 0 0 0-1.4 3.4c.5.6.2 2.1-2.6 2.1z"/><circle cx="8.5" cy="10.5" r="1"/><circle cx="12" cy="7.5" r="1"/><circle cx="15.5" cy="10" r="1"/></svg>',
 "film": '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M7 4v16M17 4v16M2 9h5M2 15h5M17 9h5M17 15h5"/></svg>',
 "check": '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg>',
}
