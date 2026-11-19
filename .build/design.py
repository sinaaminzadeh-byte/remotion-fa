# -*- coding: utf-8 -*-
"""توکن‌های طراحی مشترک - بازطراحی به سبک remocn.dev (نسخه ۲)"""
FONT_CSS = open(".build/fonts/embed.css").read()

BASE_CSS = """
:root{
  --bg:#FAFAFA; --fg:#0E1012; --muted:#57646A; --faint:#8A969B;
  --line:rgba(14,16,18,.10); --line2:rgba(14,16,18,.06);
  --card:#FFFFFF; --soft:#F4F5F6; --soft2:#EEEFF1;
  --accent:#E4332B; --accent-ink:#B0231C; --accent-soft:#FDECEB;
  --purple:#86198F; --purple-soft:#F5D0FE;
  --green:#0F7A4A; --green-soft:#E6F5EC;
  --r-sm:8px; --r:10px; --r-lg:14px; --r-xl:18px;
  --sh-xs:0 1px 1px rgba(14,16,18,.04);
  --sh-sm:0 1px 2px rgba(14,16,18,.05);
  --sh:0 1px 2px rgba(14,16,18,.05),0 8px 20px -14px rgba(14,16,18,.18);
  --sh-lg:0 1px 3px rgba(14,16,18,.06),0 18px 40px -22px rgba(14,16,18,.28);
  --ring:0 0 0 3px rgba(228,51,43,.16);
  --maxw:1280px;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{
  margin:0;background:var(--bg);color:var(--fg);
  font-family:'Vazirmatn','Segoe UI',system-ui,sans-serif;
  font-size:15.5px;line-height:1.75;font-weight:400;
  -webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;
  font-feature-settings:"ss01";
}
::selection{background:#FFE0B2;color:#0E1012}
a{color:inherit;text-decoration:none}
:focus-visible{outline:none;box-shadow:var(--ring);border-radius:8px}
code{
  font-family:'JetBrains Mono',ui-monospace,SFMono-Regular,Menlo,monospace;
  font-size:.85em;background:var(--soft);border:1px solid var(--line2);
  padding:.1em .42em;border-radius:6px;direction:ltr;display:inline-block;
  color:#243038;
}
h1,h2,h3,h4{font-weight:700;letter-spacing:-.025em;line-height:1.28;margin:0}
p{margin:0}
svg{flex-shrink:0}

/* ================= top bar (floating) ================= */
.topbar{position:sticky;top:0;z-index:80;padding:10px 24px 0;
  background:linear-gradient(180deg,rgba(250,250,250,.96) 55%,rgba(250,250,250,0))}
.bar{max-width:var(--maxw);margin:0 auto;display:flex;align-items:center;gap:10px;
  height:54px;padding:0 8px 0 10px;border-radius:16px;
  background:rgba(255,255,255,.82);border:1px solid var(--line);
  box-shadow:var(--sh-sm);backdrop-filter:saturate(180%) blur(16px)}
.brand{display:flex;align-items:center;gap:9px;font-weight:800;font-size:15px;
  letter-spacing:-.015em;padding:0 6px 0 2px;white-space:nowrap}
.brand .mark{width:26px;height:26px;border-radius:8px;background:var(--fg);
  display:grid;place-items:center;flex-shrink:0;box-shadow:var(--sh-xs)}
.nav{display:flex;align-items:center;gap:2px;background:var(--soft);
  border-radius:12px;padding:3px;position:relative}
.nav a,.nav summary{padding:6px 13px;border-radius:9px;font-size:13.5px;color:var(--muted);
  font-weight:500;transition:color .14s,background .14s,box-shadow .14s;
  white-space:nowrap;cursor:pointer;display:flex;align-items:center;gap:6px;list-style:none}
.nav summary::-webkit-details-marker{display:none}
.nav a:hover,.nav summary:hover{color:var(--fg)}
.nav a.active,.nav details[open] summary{color:var(--fg);background:#fff;font-weight:600;
  box-shadow:var(--sh-sm),0 0 0 .5px rgba(14,16,18,.06)}
.nav .new{font-size:10px;font-weight:700;padding:1px 6px;border-radius:6px;
  background:var(--purple-soft);color:var(--purple);line-height:1.5}
.navdrop{position:relative}
.navdrop .menu{position:absolute;top:calc(100% + 10px);inset-inline-start:0;min-width:214px;
  background:#fff;border:1px solid var(--line);border-radius:12px;padding:6px;
  box-shadow:var(--sh-lg);display:flex;flex-direction:column;gap:1px;z-index:90}
.navdrop .menu a{padding:8px 10px;border-radius:8px;font-size:13px;color:var(--muted)}
.navdrop .menu a:hover{background:var(--soft);color:var(--fg)}
.navdrop .menu .k{font-size:11px;color:var(--faint);margin-inline-start:auto}
.spacer{flex:1}
.ghost{display:inline-flex;align-items:center;gap:7px;height:34px;padding:0 12px;
  border-radius:10px;border:1px solid var(--line);background:#fff;font-size:13px;
  color:var(--muted);font-weight:500;box-shadow:var(--sh-xs);transition:.14s}
.ghost:hover{color:var(--fg);border-color:rgba(14,16,18,.2);background:#fff}
.ghost .num{font-size:12px;color:var(--faint);font-variant-numeric:tabular-nums}
.vline{width:1px;height:20px;background:var(--line);margin:0 2px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:7px;height:34px;
  padding:0 16px;border-radius:10px;background:var(--fg);color:#fff;font-size:13.5px;
  font-weight:600;border:1px solid var(--fg);transition:.14s;white-space:nowrap;
  font-family:inherit;cursor:pointer;box-shadow:var(--sh-xs)}
.btn:hover{background:#000;transform:translateY(-.5px)}
.btn:active{transform:none}
.btn.accent{background:var(--accent);border-color:var(--accent)}
.btn.accent:hover{background:var(--accent-ink);border-color:var(--accent-ink)}

/* ================= content toolbar ================= */
.toolbar{display:flex;align-items:center;gap:9px;margin-bottom:26px}
.toolset{display:flex;gap:3px;background:#fff;border:1px solid var(--line);
  border-radius:12px;padding:4px;box-shadow:var(--sh-sm)}
.tbtn{width:32px;height:28px;border-radius:8px;display:grid;place-items:center;
  color:var(--faint);border:0;background:transparent;cursor:pointer;transition:.13s}
.tbtn:hover{background:var(--soft);color:var(--fg)}
.tbtn.cur{background:var(--soft2);color:var(--fg)}
.tarrows{display:flex;gap:3px}
.copypage{margin-inline-start:auto;display:inline-flex;align-items:center;gap:9px;
  height:32px;padding:0 8px 0 13px;border-radius:10px;border:1px solid var(--line);
  background:#fff;font-size:12.5px;color:var(--muted);cursor:pointer;
  font-family:inherit;box-shadow:var(--sh-sm);transition:.14s}
.copypage:hover{color:var(--fg);border-color:rgba(14,16,18,.2)}
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
.side a.on{color:var(--fg);font-weight:600;background:var(--soft);
  border-inline-start-color:var(--accent)}
.side .cnt{margin-inline-start:auto;font-size:11px;color:var(--faint);
  font-variant-numeric:tabular-nums;letter-spacing:0}
.side .pill{font-size:10px;font-weight:700;padding:1px 7px;border-radius:6px;
  background:var(--purple-soft);color:var(--purple);line-height:1.6}
.side .chev{color:var(--faint);opacity:.55;margin-inline-start:auto;display:inline-flex}
.side a:has(.cnt) .chev{margin-inline-start:4px}
.side a.on .chev{opacity:1;color:var(--fg)}

.content{min-width:0}
.crumbs{display:flex;align-items:center;gap:8px;font-size:12.5px;color:var(--faint);
  margin-bottom:12px}
.crumbs b{color:var(--muted);font-weight:500}
.doc h1{font-size:clamp(29px,3.35vw,45px);letter-spacing:-.038em;line-height:1.2;
  margin:0 0 16px;font-weight:700}
.doc .lead{font-size:17px;line-height:1.85;color:var(--muted);max-width:68ch;
  margin-bottom:10px;letter-spacing:-.005em}
.doc h2{font-size:22px;margin:46px 0 12px;letter-spacing:-.028em;scroll-margin-top:90px}
.doc h3{font-size:16px;margin:26px 0 8px;letter-spacing:-.02em}
.doc p{margin:0 0 13px;color:#374247;max-width:72ch}
.doc ul,.doc ol{margin:0 0 14px;padding-inline-start:19px;color:#374247}
.doc li{margin-bottom:7px}
.doc li::marker{color:var(--faint)}
.doc strong,.doc b{font-weight:700;color:var(--fg)}
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
.rail-card.dark{background:#0E0F10;border-color:#0E0F10;color:#E9EDEF}
.rail-card.dark p{color:#A7B1B6}
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
.card:hover{border-color:rgba(14,16,18,.17);box-shadow:var(--sh);transform:translateY(-1px)}
.card .ico{width:32px;height:32px;border-radius:9px;background:var(--soft);
  display:grid;place-items:center;margin-bottom:11px;font-size:14px;color:var(--muted);
  border:1px solid var(--line2)}
.card h3{font-size:14.5px;margin:0 0 5px}
.card p{font-size:13px;color:var(--muted);margin:0;line-height:1.7}
/* یک کارت با ستون‌های جدا شده (سبک remocn) */
.cardrow{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));
  border:1px solid var(--line);border-radius:var(--r-xl);background:#fff;
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
  padding:12px 15px;font-size:13.3px;color:#374247;display:flex;gap:10px;
  align-items:flex-start;line-height:1.7}
.note.a{border-color:#F3D6D3;background:var(--accent-soft)}
.note.g{border-color:#CFE8DA;background:var(--green-soft)}
.note .ic{flex-shrink:0;font-weight:800;color:var(--accent);line-height:1.5}
.note.g .ic{color:var(--green)}

table.tbl{width:100%;border-collapse:separate;border-spacing:0;font-size:13.3px;
  border:1px solid var(--line);border-radius:var(--r);overflow:hidden;margin:6px 0 16px;
  background:#fff}
table.tbl th{text-align:right;padding:10px 14px;background:var(--soft);color:var(--fg);
  font-weight:700;font-size:12.5px;border-bottom:1px solid var(--line)}
table.tbl td{padding:10px 14px;border-bottom:1px solid var(--line2);color:#374247;
  vertical-align:top}
table.tbl tr:last-child td{border-bottom:0}
table.tbl tr:hover td{background:#FBFBFC}

footer.site{border-top:1px solid var(--line2);margin-top:56px;padding:26px 24px;
  text-align:center;font-size:12.5px;color:var(--faint)}

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
        ("catalog", "۳۰ سبک گرافیکی",  "کاتالوگ-۳۰-سبک.html",      "جدید"),
        ("report",  "گزارش تحقیق",     "گزارش-سبک‌ها-و-ابزارهای-موشن.md", None),
    ]
    nav = f'''
      <details class="navdrop">
        <summary class="{first_active}">{first_label} {CHEV_D}</summary>
        <div class="menu">
          <a href="index.html">صفحه‌ی خانه <span class="k">H</span></a>
          <a href="آموزش-ساخت-موشن.html">راهنمای ساخت <span class="k">G</span></a>
          <a href="کاتالوگ-۳۰-سبک.html">کاتالوگ ۳۰ سبک <span class="k">C</span></a>
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
    var map={h:"index.html",g:"آموزش-ساخت-موشن.html",c:"کاتالوگ-۳۰-سبک.html"};
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
<meta name="color-scheme" content="light">
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
