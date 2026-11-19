# -*- coding: utf-8 -*-
"""توکن‌های طراحی مشترک - بازطراحی به سبک remocn.dev"""
FONT_CSS = open(".build/fonts/embed.css").read()

BASE_CSS = """
:root{
  --bg:#FAFAFA; --fg:#0E1012; --muted:#57646A; --faint:#8A969B;
  --line:rgba(14,16,18,.10); --line2:rgba(14,16,18,.06);
  --card:#FFFFFF; --soft:#F4F5F6; --soft2:#EDEFF1;
  --accent:#E4332B; --accent-ink:#B0231C; --accent-soft:#FDECEB;
  --purple:#86198F; --purple-soft:#F5D0FE;
  --green:#0F7A4A; --green-soft:#E6F5EC;
  --r-sm:8px; --r:12px; --r-lg:16px; --r-xl:20px;
  --sh-sm:0 1px 2px rgba(14,16,18,.04);
  --sh:0 1px 3px rgba(14,16,18,.06),0 8px 24px -12px rgba(14,16,18,.12);
  --maxw:1120px;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{
  margin:0;background:var(--bg);color:var(--fg);
  font-family:'Vazirmatn','Segoe UI',system-ui,sans-serif;
  font-size:16px;line-height:1.75;font-weight:400;
  -webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;
  font-feature-settings:"ss01";
}
::selection{background:#FFE0B2;color:#0E1012}
a{color:inherit;text-decoration:none}
code{
  font-family:'JetBrains Mono',ui-monospace,SFMono-Regular,Menlo,monospace;
  font-size:.86em;background:var(--soft);border:1px solid var(--line2);
  padding:.12em .45em;border-radius:6px;direction:ltr;display:inline-block;
  color:#243038;
}
h1,h2,h3,h4{font-weight:700;letter-spacing:-.02em;line-height:1.3;margin:0}
p{margin:0}

/* ---------- top bar ---------- */
.topbar{position:sticky;top:0;z-index:60;background:rgba(250,250,250,.86);
  backdrop-filter:saturate(180%) blur(14px);border-bottom:1px solid var(--line2)}
.topbar-in{max-width:1280px;margin:0 auto;padding:12px 24px;display:flex;align-items:center;gap:14px}
.brand{display:flex;align-items:center;gap:9px;font-weight:800;font-size:15.5px;letter-spacing:-.01em}
.brand .mark{width:22px;height:22px;border-radius:6px;background:var(--fg);color:#fff;
  display:grid;place-items:center;font-size:12px;font-weight:800;flex-shrink:0}
.nav{display:flex;align-items:center;gap:2px;background:#fff;border:1px solid var(--line);
  border-radius:999px;padding:4px;box-shadow:var(--sh-sm)}
.nav a{padding:7px 15px;border-radius:999px;font-size:13.5px;color:var(--muted);font-weight:500;
  transition:color .15s,background .15s;white-space:nowrap}
.nav a:hover{color:var(--fg);background:var(--soft)}
.nav a.active{color:var(--fg);background:var(--soft);font-weight:600}
.spacer{flex:1}
.ghost{display:inline-flex;align-items:center;gap:7px;height:34px;padding:0 14px;border-radius:999px;
  border:1px solid var(--line);background:#fff;font-size:13px;color:var(--muted);font-weight:500;
  box-shadow:var(--sh-sm);transition:.15s}
.ghost:hover{color:var(--fg);border-color:rgba(14,16,18,.2)}
.btn{display:inline-flex;align-items:center;gap:8px;height:34px;padding:0 18px;border-radius:999px;
  background:var(--fg);color:#fff;font-size:13.5px;font-weight:600;border:1px solid var(--fg);
  transition:.15s;white-space:nowrap}
.btn:hover{background:#000}
.btn.accent{background:var(--accent);border-color:var(--accent)}
.btn.accent:hover{background:var(--accent-ink)}

/* ---------- docs shell ---------- */
.shell{max-width:1280px;margin:0 auto;padding:24px;display:grid;
  grid-template-columns:236px minmax(0,1fr) 244px;gap:36px;align-items:start}
.sidebar{position:sticky;top:74px;font-size:13.5px}
.side-group{margin-bottom:22px}
.side-label{display:flex;align-items:center;gap:7px;font-weight:700;font-size:12.5px;
  color:var(--fg);margin:0 0 8px;padding:0 8px;letter-spacing:.01em}
.side-label svg{opacity:.75}
.side a{display:flex;align-items:center;gap:8px;padding:6px 10px;border-radius:8px;
  color:var(--muted);font-weight:400;line-height:1.55;border-inline-start:2px solid transparent;
  transition:.13s;font-size:13.5px}
.side a:hover{color:var(--fg);background:var(--soft)}
.side a.on{color:var(--fg);font-weight:600;background:var(--soft);border-inline-start-color:var(--accent)}
.side .cnt{margin-inline-start:auto;font-size:11px;color:var(--faint);font-variant-numeric:tabular-nums}
.side .pill{font-size:10px;font-weight:700;padding:1px 7px;border-radius:999px;
  background:var(--purple-soft);color:var(--purple)}

.content{min-width:0}
.crumbs{display:flex;align-items:center;gap:8px;font-size:12.5px;color:var(--faint);margin-bottom:14px}
.crumbs b{color:var(--muted);font-weight:500}
.doc h1{font-size:clamp(28px,3.1vw,40px);letter-spacing:-.03em;line-height:1.24;margin:0 0 14px}
.doc .lead{font-size:17px;line-height:1.85;color:var(--muted);max-width:70ch;margin-bottom:8px}
.doc h2{font-size:23px;margin:44px 0 12px;letter-spacing:-.02em;scroll-margin-top:80px}
.doc h3{font-size:16.5px;margin:26px 0 8px}
.doc p{margin:0 0 13px;color:#374247;max-width:72ch}
.doc ul,.doc ol{margin:0 0 14px;padding-inline-start:20px;color:#374247}
.doc li{margin-bottom:7px}
.doc li::marker{color:var(--faint)}
.doc strong,.doc b{font-weight:700;color:var(--fg)}
.hr{height:1px;background:var(--line2);border:0;margin:34px 0}

/* ---------- right rail ---------- */
.rail{position:sticky;top:74px;display:flex;flex-direction:column;gap:14px}
.rail-card{border:1px solid var(--line);border-radius:var(--r-lg);background:var(--card);
  padding:16px;box-shadow:var(--sh-sm)}
.rail-card h4{font-size:13px;margin:0 0 8px}
.rail-card p{font-size:12.5px;color:var(--muted);line-height:1.7;margin:0 0 10px}
.rail-card.dark{background:#0E0F10;border-color:#0E0F10;color:#E9EDEF}
.rail-card.dark p{color:#A7B1B6}

/* ---------- cards / grids ---------- */
.grid{display:grid;gap:14px}
.g2{grid-template-columns:repeat(2,minmax(0,1fr))}
.g3{grid-template-columns:repeat(3,minmax(0,1fr))}
.card{background:var(--card);border:1px solid var(--line);border-radius:var(--r-lg);
  padding:18px;box-shadow:var(--sh-sm);transition:.16s}
.card:hover{border-color:rgba(14,16,18,.18);box-shadow:var(--sh)}
.card .ico{width:34px;height:34px;border-radius:9px;background:var(--soft);display:grid;
  place-items:center;margin-bottom:12px;font-size:15px}
.card h3{font-size:15px;margin:0 0 6px}
.card p{font-size:13px;color:var(--muted);margin:0;line-height:1.7}

.note{border:1px solid var(--line);border-radius:var(--r);background:var(--soft);
  padding:13px 16px;font-size:13.5px;color:#374247;display:flex;gap:10px;align-items:flex-start}
.note.a{border-color:#F3D6D3;background:var(--accent-soft)}
.note.g{border-color:#CFE8DA;background:var(--green-soft)}
.note .ic{flex-shrink:0;font-weight:800;color:var(--accent)}
.note.g .ic{color:var(--green)}

table.tbl{width:100%;border-collapse:separate;border-spacing:0;font-size:13.5px;
  border:1px solid var(--line);border-radius:var(--r);overflow:hidden;margin:6px 0 16px;background:#fff}
table.tbl th{text-align:right;padding:10px 14px;background:var(--soft);color:var(--fg);
  font-weight:700;font-size:12.5px;border-bottom:1px solid var(--line)}
table.tbl td{padding:10px 14px;border-bottom:1px solid var(--line2);color:#374247;vertical-align:top}
table.tbl tr:last-child td{border-bottom:0}

footer.site{border-top:1px solid var(--line2);margin-top:60px;padding:26px 24px;
  text-align:center;font-size:12.5px;color:var(--faint)}

@media(max-width:1180px){.shell{grid-template-columns:220px minmax(0,1fr)}.rail{display:none}}
@media(max-width:860px){
  .shell{grid-template-columns:1fr;padding:18px 16px;gap:20px}
  .sidebar{position:static;order:2;border-top:1px solid var(--line2);padding-top:18px}
  .content{order:1}
  .topbar-in{padding:10px 16px;gap:8px;flex-wrap:wrap}
  .nav{order:3;width:100%;overflow-x:auto;justify-content:flex-start}
  .g2,.g3{grid-template-columns:1fr}
}
"""

def topbar(active):
    a1 = "active" if active=="guide" else ""
    a2 = "active" if active=="catalog" else ""
    return f'''
<header class="topbar">
  <div class="topbar-in">
    <a class="brand" href="index.html">
      <span class="mark">م</span> استودیوی موشن
    </a>
    <nav class="nav">
      <a class="{a1}" href="آموزش-ساخت-موشن.html">راهنمای ساخت</a>
      <a class="{a2}" href="کاتالوگ-۳۰-سبک.html">۳۰ سبک گرافیکی</a>
      <a href="index.html">خانه</a>
    </nav>
    <span class="spacer"></span>
    <a class="ghost" href="https://github.com/sinaaminzadeh-byte/remotion-fa" target="_blank" rel="noopener">GitHub</a>
    <a class="btn accent" href="آموزش-ساخت-موشن.html#s4">شروع ساخت</a>
  </div>
</header>'''

def head(title, css_extra=""):
    return f'''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
{FONT_CSS}
{BASE_CSS}
{css_extra}
</style>
</head>
<body>'''

ICONS = {
 "spark":'<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3v3M12 18v3M3 12h3M18 12h3M5.6 5.6l2.1 2.1M16.3 16.3l2.1 2.1M18.4 5.6l-2.1 2.1M7.7 16.3l-2.1 2.1"/></svg>',
 "book":'<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>',
 "grid":'<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/></svg>',
 "type":'<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 7V5h16v2M9 19h6M12 5v14"/></svg>',
 "palette":'<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><circle cx="9" cy="9" r="1"/><circle cx="15" cy="9" r="1"/><circle cx="9" cy="15" r="1"/></svg>',
 "film":'<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M7 4v16M17 4v16M2 9h5M2 15h5M17 9h5M17 15h5"/></svg>',
}
