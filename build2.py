import html,json,re
E=html.escape
src=open('build.py').read(); ns={}; exec(src[:src.index('def nav')],ns); old=ns['cars']
from notes import N
at=json.load(open('data-autotrader.json'))
ebay=[("840013706915","2002 1.8 Turbo",2002,"1.8","Turbo (modified)",3250,"OBO",111000,""),
("287597955967","Montana turbo, 270bhp",None,"1.8","Montana (turbo, modified)",9500,"",95620,""),
("189040969530","2003 1.8 S-VT Sport",2003,"1.8","Sport",5250,"auction, ends Wed 14 Oct 12:18",63336,"Full service history, MOT 08/27"),
("407284440544","2003 1.8 VVT LSD",2003,"1.8","Standard",2650,"OBO",82000,""),
("860036654760","2002 1.8 VVT",2002,"1.8","Standard",3495,"OBO",149600,""),
("407013077969","2003 1.8i",2003,"1.8","Standard",None,"price not shown",34000,"Full service history"),
("198710016355","2003 1.6 Nardi",2003,"1.6","Nardi",2300,"",None,""),
("327349134954","2004 1.6",2004,"1.6","Standard",8999,"",None,""),
("227514998935","2003 automatic",2003,"?","Automatic",2490,"",None,""),
("147623890978","1.8 Miyako",None,"1.8","Miyako",5800,"",54000,"")]
def edition(v):
    for e in ["Euphonic","Arctic","Montana","Icon","Sport","California","Nevada","Nardi","Miyako","Turbo"]:
        if e.lower() in v.lower(): return e
    return "Standard"
cars=[]
for c in at:
    p,ch,v,flag=N[c['id']]
    eng=c['variant'][:3]
    score=c['price']+0.025*c['miles']+8*c['dist']-(500 if c['history']=='Full' else 0)-(300 if edition(c['variant'])!='Standard' else 0)-(250 if eng=='1.8' else 0)
    if flag and 'Not an NB' in flag: score+=99999
    cars.append(dict(c,slug=f"at-{c['id']}",ed=edition(c['variant']),eng=eng,pros=p,checks=ch,verdict=v,flag=flag,score=score,title=f"{c['year']} MX-5 {c['variant'].replace(' Limited Edition','')}"))
for i,t,y,eng,ed,pr,pn,mi,ex in ebay:
    sc=(pr or 99999)+0.025*(mi or 120000)+8*120+(3000 if 'modified' in ed else 0)+(2000 if ed=='Automatic' else 0)
    cars.append(dict(id=i,src="eBay",verified=False,year=y,variant=t,colour=None,price=pr,pnote=pn,miles=mi,reg=None,owners=None,history=None,seller=None,loc=None,dist=None,desc=ex,url=f"https://www.ebay.co.uk/itm/{i}",imgs=[],slug=f"ebay-{i}",ed=ed.split(' (')[0],eng=eng,pros=[ex] if ex else [],checks=["Not fetched: eBay blocks automated checks. The details come from search results, so check year, location, MOT and condition on the ad"]+(["Modified/turbo: check insurance and look for any engineer's report"] if 'modified' in ed else []),verdict="Unverified: open the ad to judge it.",flag=None,score=sc,title=f"MX-5 {t}"))
from new17 import NEW
for (sid,src_,url,y,var,ed,eng,col,pr,mi,loc,dist,sel,imgs,vd,flags,special,pros,checks,verdict) in NEW:
    sc=pr+0.025*mi+8*(dist or 250)-(300 if ed not in('Standard',) else 0)-(250 if eng=='1.8' else 0)-(999999 if special=='nevada' else 0)+(800 if flags else 0)
    cars.append(dict(id=sid,src=src_,verified=bool(vd),vdate=vd,year=y,variant=var,colour=col,price=pr,miles=mi,reg=None,owners=None,history=None,seller=sel,loc=loc,dist=dist,desc='',url=url,imgs=imgs,slug=sid,ed=ed,eng=eng,pros=pros,checks=checks,verdict=verdict,flag=' · '.join(flags) or None,special=special,score=sc,title=f"{y} MX-5 {var}"))
cars.sort(key=lambda c:c['score'])
for n,c in enumerate(cars,1): c['rank']=n
money=lambda p:f"£{p:,}" if p else "Price not shown"
mil=lambda m:f"{m:,}" if m else "Not stated"

def nav(p):
    l="".join(f'<a href="{p}index.html#{a}">{t}</a>' for a,t in [("all","All NB-FL"),("nevada","The Nevada"),("earlier","Nevada finds"),("guide","Price guide"),("watch","Watch")])
    return f'<nav class="nav"><a class="brand" href="{p}index.html">MX-5 <i>HUNTER</i></a><button class="burger" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button><div class="links">{l}</div></nav>'
head=ns.get('head') or None
def head(t,p): return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{E(t)}</title><link rel="stylesheet" href="{p}assets/site.css"><meta name="theme-color" content="#070b1c"></head><body>'
def foot(p): return f'<footer class="foot"><div class="fm">MX-5 <b>NB-FL</b> · HUNTER</div><a class="bigcta" href="{p}index.html#all">Back to all cars →</a><p>Updated 12 Oct 2026 · AutoTrader ads checked live on 12 Oct · eBay details from search results only · Distances are rough road miles from Poole</p></footer><script src="{p}assets/site.js" defer></script></body></html>'
def ph(t,k="NO PHOTO"): return f'<div class="ph"><div class="ph-in"><span class="ph-k">{k}</span><span class="ph-m">{E(t)}</span><span class="ph-s">Mazda MX-5 NB</span></div></div>'
def badges(c):
    b=f'<span class="stb ok">✓ Checked {c.get("vdate") or "12 Oct"}</span>' if c['verified'] else ('<span class="stb unv">Not confirmed live</span>' if c.get('vdate',1) is None else '<span class="stb unv">From search results</span>')
    if c.get('special')=='nevada': b='<span class="stb nev">★ Genuine Nevada</span>'+b
    elif c.get('special')=='se': b+='<span class="stb se">Special edition, not a Nevada</span>'
    if c.get('flag'): b+=f'<span class="stb sold">{E(c["flag"])}</span>'
    return b

cards=""
for c in cars:
    im=f'<img src="{c["imgs"][0]}" alt="Seller photo: {E(c["title"])}" loading="lazy">' if c['imgs'] else ph(c['title'],"PHOTO ON "+c['src'].split(" (")[0].upper())
    cards+=f'''<article class="card rv fcar{' lead' if c.get('special')=='nevada' else ''}" data-ed="{c['ed']}" data-eng="{c['eng']}" data-price="{c['price'] or 0}" data-dist="{c['dist'] or 999}" data-src="{'AutoTrader' if c['verified'] else 'x'}"><a class="cimg" href="cars/{c['slug']}.html">{im}<span class="rank">#{c['rank']}</span><span class="cbadges">{badges(c)}</span><span class="sticker">{money(c['price'])}</span></a>
<div class="cbody"><div class="ky">{c['year'] or 'Year ?'} · {E(c['colour'] or c['src'])} · {c['ed']}</div><h3><a href="cars/{c['slug']}.html">{E(c['title'])}</a></h3><p class="hook">{E(c['verdict'])}</p>
<dl class="stats"><div><dt>Miles</dt><dd>{mil(c['miles'])}</dd></div><div><dt>From Poole</dt><dd>{('~%d mi'%c['dist']) if c['dist'] else '?'}</dd></div><div><dt>Engine</dt><dd>{c['eng']}</dd></div></dl>
<p class="loc">◉ {E(c['loc'] or 'Location on ad')} · {E(c['seller'] or c['src'])}</p><div class="ctas"><a class="cta" href="cars/{c['slug']}.html">Details <b>→</b></a><a class="orig" href="{c['url']}" target="_blank" rel="noopener">{c['src']} ↗</a></div></div></article>'''
eds=sorted({c['ed'] for c in cars})
filt=f'''<div class="filters rv"><label>Edition<select id="f-ed"><option value="">All</option>{"".join(f"<option>{e}</option>" for e in eds)}</select></label>
<label>Engine<select id="f-eng"><option value="">All</option><option>1.8</option><option>1.6</option></select></label>
<label>Max price<select id="f-price"><option value="0">Any</option><option>3000</option><option>4000</option><option>5000</option><option>6000</option></select></label>
<label>Max distance<select id="f-dist"><option value="0">Any</option><option value="50">50 mi</option><option value="75">75 mi</option><option value="100">100 mi</option></select></label>
<label class="chk"><input type="checkbox" id="f-ver"> Checked ads only</label><span id="f-count"></span></div>'''

oldcards=""
for c in old:
    im=f'<img src="{c["photo"]}" alt="Seller photo" loading="lazy">' if c['photo'] else ph("2003 "+c['trim'])
    oldcards+=f'''<article class="card rv gone"><a class="cimg" href="cars/{c['slug']}.html">{im}<span class="cbadges"><span class="stb {c['badge'][0]}">{E(c['badge'][1])}</span></span><span class="sticker">{c['price']}</span></a><div class="cbody"><div class="ky">2003 · {E(c['colour'])} · Nevada</div><h3><a href="cars/{c['slug']}.html">MX-5 Nevada <em>{E(c['trim'])}</em></a></h3><dl class="stats"><div><dt>Miles</dt><dd>{c['miles']}</dd></div><div><dt>From Poole</dt><dd>{c['dist']}</dd></div><div><dt>Where</dt><dd>{E(c['loc'])}</dd></div></dl><div class="ctas"><a class="cta" href="cars/{c['slug']}.html">Details <b>→</b></a><a class="orig" href="{c['url']}" target="_blank" rel="noopener">Ad ↗</a></div></div></article>'''

top=next(c for c in cars if c.get('special')=='nevada')
idx=src[src.index('idx=head('):src.index('open("index.html"')]  # reuse old sections text
nev=re.search(r'<section id="nevada".*?</section>\s*<section id="production".*?</section>\s*<section id="guide".*?</section>\s*<section id="watch".*?</section>',idx,re.S).group(0)
for a,b in [('class="snum">02','class="snum">03'),('class="snum">03<','class="snum">04<')]: pass
page=head("MX-5 NB-FL · The Hunt","")+nav("")+f'''<section class="cover typo" id="top"><div class="ghost">NEVADA</div><div class="cv-shade"></div>
<div class="mast"><div class="issue"><span>Issue 02</span><span>October 2026</span><span>Pete's shortlist</span></div><h1>MX-5<b>NB-FL</b></h1><div class="tag">THE HUNT</div></div>
<div class="lines"><a class="cl star" href="cars/{top['slug']}.html"><small>The only live Nevada</small>{E(top['title'])}<span>{mil(top['miles'])} miles · {money(top['price'])} · {E(top['loc'])}</span></a><a class="cl" href="#all"><small>Inside</small>1 live Nevada + {len(cars)-1} more</a><a class="cl" href="#nevada"><small>Cover story</small>The 2,050-car Nevada</a><a class="cl" href="#guide"><small>Price guide</small>What they really fetch</a></div>
<a class="pricebub" href="cars/{top['slug']}.html"><small>Top pick</small>{money(top['price'])}</a><div class="barcode">{len(cars)} cars · 1 Nevada</div></section><main>
<section id="all" class="sec"><div class="wrap"><header class="shead rv"><span class="snum">01</span><div><div class="kicker">Best value first</div><h2>All NB-FL for sale</h2></div></header>
<div class="intro rv"><p class="drop">Just one genuine Nevada is for sale: the Cerion Silver 1.8 in Berwick-upon-Tweed. Below it is every other facelift NB we found, {len(cars)} cars in all. Special editions that aren't Nevadas are labelled. Ads were checked live on 12–13 Oct 2026, and photos are the sellers' own where we could get them. The eBay ads come from search results only. Ranking: price, plus a penalty for miles and distance from Poole, with credit for full history, a limited edition and the 1.8. It's a rough guide, not gospel.</p><blockquote>“A clean, documented 1.8 within an hour of Poole beats a cheaper car three counties away.”</blockquote></div>
{filt}<div class="grid" id="cargrid">{cards}</div></div></section>
{nev.replace('class="snum">02','class="snum">02').replace('class="snum">03','class="snum">03')}
<section id="earlier" class="sec"><div class="wrap"><header class="shead rv"><span class="snum">06</span><div><div class="kicker">Earlier finds · probably gone</div><h2>The Nevadas we found first</h2></div></header><div class="intro rv"><p>These came from copy sites and a Gumtree ad that has since been removed. None could be confirmed live on 12 Oct. They're kept here for reference.</p></div><div class="grid">{oldcards}</div></div></section>
</main>'''+foot("")
open("index.html","w").write(page)

for c in cars:
    gal=(f'<div class="gmain"><img id="gm" src="../{c["imgs"][0]}" alt="Seller photo"></div><div class="gthumbs">'+"".join(f'<img class="gt" src="../{i}" alt="Photo {n+1}">' for n,i in enumerate(c['imgs']))+'</div><p class="muted">Seller photos from the AutoTrader ad.</p>') if c['imgs'] else f'<div class="gmain">{ph(c["title"],"PHOTO ON "+c["src"].split(" (")[0].upper())}</div>'
    f=[("Price",money(c['price'])+(f" ({c.get('pnote')})" if c.get('pnote') else "")),("Year",c['year'] or "Not stated"),("Miles",mil(c['miles'])),("Variant",c['variant']),("Edition",c['ed']),("Engine",c['eng']),("Colour",c['colour']),("Registration",c['reg']),("Owners",c['owners']),("Service history",c['history']),("Seller",c['seller']),("Location",c['loc']),("From Poole",f"~{c['dist']} mi (estimate)" if c['dist'] else None),("Source",(f"{c['src']}, checked {c.get('vdate') or '12 Oct'} 2026" if c['verified'] else f"{c['src']}: not confirmed live"))]
    ft="".join(f"<tr><th>{E(a)}</th><td>{E(str(b))}</td></tr>" for a,b in f if b)
    pr="".join(f"<li>{E(x)}</li>" for x in c['pros']) or "<li>See the ad</li>"
    ch="".join(f"<li><b>{E(x.split(' (')[0][:60])}</b><p>{E(x)}</p></li>" for x in c['checks'])
    desc=f'<div class="panel"><h2>Seller says (extract)</h2><p class="quote">“{E(c["desc"])}…”</p></div>' if c['verified'] and c['desc'] else ""
    pg=head(f"{c['title']} · {money(c['price'])} | MX-5 Hunter","../")+nav("../")+f'''<main class="bike"><div class="crumbs wrap"><a href="../index.html#all">← All NB-FL</a><span>Ranked #{c['rank']} of {len(cars)} for value</span></div>
<section class="bhero wrap"><div class="gallery">{gal}</div><div class="bintro">{badges(c)}<div class="kicker">{c['year'] or ''} · {E(c['ed'])}</div><h1>{E(c['title'])}</h1><p class="bhook">{E(c['verdict'])}</p>
<div class="bprice"><span class="sticker">{money(c['price'])}</span><span>{mil(c['miles'])} miles · {E(c['loc'] or 'see ad')}</span></div><a class="cta big" href="{c['url']}" target="_blank" rel="noopener">View on {c['src']} <b>↗</b></a></div></section>
<section class="wrap bgrid"><div class="panel facts"><h2>Key facts</h2><table class="spec light">{ft}</table></div><div class="panel why"><h2>Why buy it</h2><ul class="ticks">{pr}</ul><h2>Things to check</h2><ul class="checks">{ch}<li><b>Mk2.5 weak spots</b><p>Sills, rear arches and chassis rails for rust, the hood seams, and when the cambelt was last changed.</p></li></ul></div></section>
<section class="wrap">{desc}</section></main>'''+foot("../")
    open(f"cars/{c['slug']}.html","w").write(pg)
print(len(cars),[ (c['rank'],c['title'],c['price']) for c in cars[:6]])
