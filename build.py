import html
E=html.escape
cars=[
dict(slug="2003-18-strato-blue-ashford",rank=1,trim="1.8",colour="Strato Blue",price="£2,500",miles="39,400",loc="Ashford, Surrey",dist="~85 mi",seller="Private",badge=("sold","Likely sold · ad removed"),
 hook="Strato Blue 1.8 with a factory LSD, big brakes and a clean MOT. If it's still around, it's the pick.",
 facts=[("Engine","1,839 cc, manual"),("Hood","Grey"),("MOT (ad)","Fresh, 13 months, no advisories"),("Extras (ad)","Factory big brakes, working Fuji LSD"),("Ad status","Gumtree page returned 404 on 12 Oct 2026")],
 pros=["Lowest mileage in the hunt","1.8 with a working Fuji LSD and factory big brakes","Fresh MOT with no advisories (ad)","ULEZ compliant (ad)"],
 checks=[("Right-rear wing repair","Repaired about 10 years ago. The filler has cracked and shows, so get it looked at before rust spreads."),("Is it still for sale?","The ad is gone, so it has probably sold.")],
 verdict="The best car on paper for the money. The ad has disappeared, though, so treat it as gone.",
 url="https://www.gumtree.com/p/mazda/mazda-mx-5-nevada-2003-manual-1839-cc-2-doors/1801938798",site="Gumtree",photo=None),
dict(slug="2003-18-blue-sv03lje",rank=2,trim="1.8i",colour="Blue (ad: 'purple / blue')",price="£2,995 ono",miles="46,314",loc="Not stated",dist="Unknown",seller="Not stated (ad says it was also on eBay)",badge=("unv","Unverified · copy site"),
 hook="Low miles and well equipped: leather, heated seats, air con and a 12-month MOT.",
 facts=[("Engine","1,839 cc, manual"),("Registration","SV03 LJE (visible in the ad photo)"),("Equipment (ad)","Alloys, leather, heated seats, air con, electric windows, central locking"),("MOT (ad)","12 months (date not given)"),("Source","Copy of an eBay ad on car-us.com")],
 pros=["Second-lowest mileage","The only listing with a real photo","1.8 with leather"],
 checks=[("Air con and heated seats","Air con isn't part of the Nevada spec and heated seats aren't a standard Nevada feature, so they may be dealer extras or the ad may be wrong. Check the VIN and spec."),("Is it live?","This is a copy site. Search eBay for SV03 LJE and find the seller and location."),("Sills and rear arches","The usual Mk2.5 rust areas. Not covered in the ad.")],
 verdict="The most promising live-looking car, if the original eBay ad still exists.",
 url="https://car-us.com/car/mazda-mx5/39749",site="car-us.com",photo="img/car2-1.jpg"),
dict(slug="2003-16-silver-andover",rank=3,trim="1.6",colour="Silver",price="£1,950",miles="120,000",loc="Andover",dist="~50 mi",seller="Private",badge=("unv","Unverified · copy site"),
 hook="The closest to Poole and the cheapest, with the big jobs done in the last year.",
 facts=[("Plate","53 (2003)"),("Engine","1.6, manual"),("MOT (ad)","Until 13 Aug 2026, now probably expired"),("Work done (ad)","New roof, clutch, cambelt, fan belt, water pump, all pads")],
 pros=["About 50 miles from Poole","The expensive jobs are done","Offers welcome (ad)"],
 checks=[("Rust","Bubbling and rust on the arches (ad). Check the sills and chassis rails too."),("Damage","Dent on the front left and a missing bumper vent (ad)."),("MOT","The stated MOT ran out on 13 Aug 2026."),("1.6 engine","Rarer (only 300 Nevadas had it), but slower and with no LSD.")],
 verdict="A cheap, honest-sounding runner to fix up. Budget for bodywork.",
 url="https://carfinduk.com/detail-page_127788416.html",site="carfinduk.com",photo=None),
dict(slug="2003-18-vvt-strato-blue-solihull",rank=4,trim="1.8 VVT",colour="Strato Blue",price="£4,195",miles="~89,000",loc="Solihull",dist="~150 mi",seller="Private",badge=("unv","Unverified · copy site"),
 hook="Built to drive hard: remapped ECU, coilovers and a colour-matched hardtop.",
 facts=[("Engine","1.8 VVT, 5-speed manual"),("Interior","Light grey leather"),("Hood","Light grey, heated glass rear window"),("Mods (ad)","ME221 ECU (Digitune map), MeisterR ZetaCRD coilovers, 15\" BBS-style wheels, intake, high-flow cat, custom exhaust, wideband gauge"),("Diff (ad)","'Believed to have' a Fuji LSD")],
 pros=["Genuine colour-matched Mazda hardtop","Well-known parts and tuner","Leather 1.8 in Strato Blue (one of 410 built)"],
 checks=[("Originality","Heavily modified, which lowers its appeal as a special edition."),("Price","£4,195 is far above the £2,010 auction guide."),("Emissions and insurance","A high-flow cat and standalone ECU need declaring to insurers and may affect the MOT.")],
 verdict="Only for someone who wants a modified car. Poor value as a Nevada.",
 url="https://carfinduk.com/detail-page_131930757.html",site="carfinduk.com",photo=None),
dict(slug="2003-18-leeds-project",rank=5,trim="1.8",colour="Not stated",price="£2,280",miles="45,000",loc="Leeds",dist="~250 mi",seller="Dealer: RH Car Sales (sold as seen)",badge=("unv","Unverified · copy site"),
 hook="Low miles and one owner for 23 years, but it needs welding.",
 facts=[("MOT (ad)","Until 01/2027"),("Owners (ad)","Same owner for 23 years"),("Recent work (ad)","New clutch"),("Keys","2"),("Warranty","None, sold as seen")],
 pros=["Low miles","Long single ownership","MOT into 2027"],
 checks=[("Corrosion","Both front wings and underside parts corroded. Two holes need welding (ad)."),("Roof","Stitching coming apart (ad)."),("Window","Front passenger window doesn't work (ad)."),("Distance","About 250 miles from Poole.")],
 verdict="A welding project. Not worth the trip from Dorset.",
 url="https://carfinduk.com/detail-page_131900395.html",site="carfinduk.com",photo=None)]

def nav(p):
    l="".join(f'<a href="{p}index.html#{a}">{t}</a>' for a,t in [("cars","The Cars"),("nevada","The Nevada"),("production","Production"),("guide","Price Guide"),("watch","Watch")])
    return f'<nav class="nav"><a class="brand" href="{p}index.html">MX-5 <i>HUNTER</i></a><button class="burger" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button><div class="links">{l}</div></nav>'
def head(t,p): return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{E(t)}</title><link rel="stylesheet" href="{p}assets/site.css"><meta name="theme-color" content="#070b1c"></head><body>'
def ph(c): return f'<div class="ph"><div class="ph-in"><span class="ph-k">NO PHOTO AVAILABLE</span><span class="ph-m">2003 {E(c["trim"])}</span><span class="ph-s">Mazda MX-5 Nevada</span></div></div>'
def img(c,p): return f'<picture class="small-photo"><img src="{p}{c["photo"]}" alt="Seller photo of this car (SV03 LJE)" loading="lazy"></picture>' if c["photo"] else ph(c)
def badge(c): return f'<span class="stb {c["badge"][0]}">{E(c["badge"][1])}</span>'
def foot(p): return f'<footer class="foot"><div class="fm">MX-5 <b>NEVADA</b> · HUNTER</div><a class="bigcta" href="{p}index.html#cars">Back to the cars →</a><p>Updated 12 Oct 2026 · Facts are as stated in the ads and haven\'t been checked · Distances are rough road miles from Poole</p></footer><script src="{p}assets/site.js" defer></script></body></html>'

cards=""
for c in cars:
    cls="card"+(" lead" if c["rank"]==1 else "")+(" gone" if c["badge"][0]=="sold" else "")
    cards+=f'''<article class="{cls} rv"><a class="cimg" href="cars/{c["slug"]}.html">{img(c,"")}<span class="rank">#{c["rank"]}</span>{badge(c)}<span class="sticker">{c["price"]}</span></a>
<div class="cbody"><div class="ky">2003 · {E(c["colour"])}</div><h3><a href="cars/{c["slug"]}.html">MX-5 Nevada <em>{E(c["trim"])}</em></a></h3><p class="hook">{E(c["hook"])}</p>
<dl class="stats"><div><dt>Miles</dt><dd>{c["miles"]}</dd></div><div><dt>From Poole</dt><dd>{c["dist"]}</dd></div><div><dt>Price</dt><dd>{c["price"]}</dd></div></dl>
<p class="loc">◉ {E(c["loc"])} · {E(c["seller"])}</p><div class="ctas"><a class="cta" href="cars/{c["slug"]}.html">See this car <b>→</b></a><a class="orig" href="{c["url"]}" target="_blank" rel="noopener">Original ad ↗</a></div></div></article>'''

idx=head("MX-5 Nevada · The Hunt","")+nav("")+f'''<section class="cover typo" id="top"><div class="ghost">NB</div><div class="cv-shade"></div>
<div class="mast"><div class="issue"><span>Issue 01</span><span>October 2026</span><span>Pete's shortlist</span></div><h1>MX-5<b>NEVADA</b></h1><div class="tag">THE HUNT</div></div>
<div class="lines"><a class="cl star" href="cars/{cars[1]["slug"]}.html"><small>Best bet still listed</small>1.8i, 46k miles<span>£2,995 ono · unverified</span></a><a class="cl" href="#nevada"><small>Cover story</small>The 2,050-car Mk2.5</a><a class="cl" href="#guide"><small>Price guide</small>What they really fetch</a><a class="cl" href="#cars"><small>Inside</small>5 cars ranked on value</a></div>
<a class="pricebub" href="#guide"><small>Auction guide</small>£2,010</a><div class="barcode">5 cars · 2,050 built</div></section><main>
<section id="cars" class="sec"><div class="wrap"><header class="shead rv"><span class="snum">01</span><div><div class="kicker">Best value first</div><h2>Five Nevadas, ranked</h2></div></header>
<div class="intro rv"><p class="drop">All five are 2003 cars. One is the private Strato Blue 1.8 that topped the list, but its Gumtree ad has gone. The other four come from copy sites that repost eBay and Gumtree ads, so check that each is still for sale before you call. Every fact below comes from the ad text.</p><blockquote>“Clean Nevadas fetch good money. Rusty ones are projects, whatever the mileage.”</blockquote></div>
<div class="grid">{cards}</div></div></section>
<section id="nevada" class="sec"><div class="wrap"><header class="shead rv"><span class="snum">02</span><div><div class="kicker">Cover story</div><h2>The Nevada, explained</h2></div></header>
<div class="intro rv"><p class="drop">The Nevada was a UK-only special edition of the facelifted NB (the Mk2.5), built in February and March 2003. Mazda made 2,050, in Cerion Silver with a blue hood and interior or Strato Blue with grey. New prices were £15,995 for the 1.6, £16,495 for the 1.8 and £16,995 for the 1.8 with leather.</p>
<p>The spec adds a two-tone leather steering wheel and gear knob, an aluminium-look centre console and vent surrounds, chrome door handles, stainless scuff plates, a wind blocker, a colour-matched hood cover, remote central locking, an alarm and a CD player. Sources disagree on the wheels: mx5-mazda.co.uk says 15-inch alloys, while the March 2003 launch report says 16-inch.</p>
<p class="muted">Sources: <a href="http://mx5-mazda.co.uk/nevada.htm" target="_blank" rel="noopener">mx5-mazda.co.uk</a> · <a href="https://mx5info.com/2003-silver-blues-twins-nevada-classic-edition/" target="_blank" rel="noopener">MX5info</a> · <a href="https://www.kentonline.co.uk/kent/news/nevada-is-mazdas-latest-special-a7791/" target="_blank" rel="noopener">KentOnline, 14 Mar 2003</a></p></div></div></section>
<section id="production" class="sec"><div class="wrap"><header class="shead rv"><span class="snum">03</span><div><div class="kicker">How many were built</div><h2>Production numbers</h2></div></header>
<table class="prodt rv"><thead><tr><th>Colour</th><th>1.6</th><th>1.8 cloth</th><th>1.8 leather</th><th>Total</th></tr></thead><tbody><tr><td>Cerion Silver</td><td>200</td><td>370</td><td>780</td><td>1,350</td></tr><tr><td>Strato Blue</td><td>100</td><td>190</td><td>410</td><td>700</td></tr><tr><th>All</th><th>300</th><th>560</th><th>1,190</th><th>2,050</th></tr></tbody></table></div></section>
<section id="guide" class="sec"><div class="wrap"><header class="shead rv"><span class="snum">04</span><div><div class="kicker">Price guide</div><h2>What they really fetch</h2></div></header>
<div class="guide rv"><b>£2,010</b><p>Anglia Car Auctions, June 2024, Lot 285: a 2003 Nevada 1.8 with 87,561 miles, five keepers, a stamped service book and MOT certificates back to 2006. Sold with no reserve, price including buyer's premium. <a href="https://angliacarauctions.co.uk/auctions/2649-22-Jun-2024/6653~1-2003-mazda-mx-5-nevada" target="_blank" rel="noopener" style="color:var(--y)">See the result ↗</a></p></div></div></section>
<section id="watch" class="sec"><div class="wrap"><header class="shead rv"><span class="snum">05</span><div><div class="kicker">Keep hunting</div><h2>Where to watch</h2></div></header><div class="intro rv"><ul class="ticks">
<li><a href="https://www.autotrader.co.uk/car-search?make=Mazda&model=MX-5&postcode=BH15%201AA&keywords=nevada" target="_blank" rel="noopener">AutoTrader: MX-5 'nevada', sorted by distance from Poole ↗</a></li>
<li><a href="https://www.ebay.co.uk/sch/i.html?_nkw=mx5+nevada&_sacat=9801" target="_blank" rel="noopener">eBay Motors: 'mx5 nevada' ↗</a></li>
<li><a href="https://www.pistonheads.com/buy/search?keyword=mx5%20nevada" target="_blank" rel="noopener">PistonHeads: 'mx5 nevada' ↗</a></li>
<li><a href="https://www.gumtree.com/search?search_category=cars&q=mx5+nevada" target="_blank" rel="noopener">Gumtree: 'mx5 nevada' ↗</a></li></ul></div></div></section>
</main>'''+foot("")
open("index.html","w").write(idx)

for c in cars:
    f="".join(f"<tr><th>{E(a)}</th><td>{E(b)}</td></tr>" for a,b in [("Price",c["price"]),("Year","2003"),("Miles",c["miles"]),("Trim",c["trim"]),("Colour",c["colour"]),("Location",c["loc"]),("From Poole",c["dist"]),("Seller",c["seller"])]+c["facts"])
    pr="".join(f"<li>{E(x)}</li>" for x in c["pros"])
    ch="".join(f"<li><b>{E(a)}</b><p>{E(b)}</p></li>" for a,b in c["checks"])
    pg=head(f'2003 MX-5 Nevada {c["trim"]} · {c["loc"]} · {c["price"]} | MX-5 Hunter',"../")+nav("../")+f'''<main class="bike"><div class="crumbs wrap"><a href="../index.html#cars">← Back to the cars</a><span>Ranked #{c["rank"]} for value</span></div>
<section class="bhero wrap"><div class="gallery"><div class="gmain">{img(c,"../")}</div>{'<p class="muted">The seller\'s only photo, saved from the copy site at low resolution.</p>' if c["photo"] else ''}</div>
<div class="bintro">{badge(c)}<div class="kicker">2003 · {E(c["colour"])}</div><h1>MX-5 Nevada <em>{E(c["trim"])}</em></h1><p class="bhook">{E(c["hook"])}</p>
<div class="bprice"><span class="sticker">{c["price"]}</span><span>{c["miles"]} miles · {E(c["loc"])}</span></div>
<a class="cta big" href="{c["url"]}" target="_blank" rel="noopener">View ad on {c["site"]} <b>↗</b></a><p class="dealer">Seller: <b>{E(c["seller"])}</b>. Contact details are on the original ad.</p></div></section>
<section class="wrap bgrid"><div class="panel facts"><h2>Key facts</h2><table class="spec light">{f}</table><p class="muted">Facts marked (ad) come from the listing and haven't been checked. Distances are rough.</p></div>
<div class="panel why"><h2>Why buy it</h2><ul class="ticks">{pr}</ul><h2>Things to check</h2><ul class="checks">{ch}</ul></div></section>
<section class="wrap"><div class="guide"><b>£2,010</b><p><b style="font:inherit;color:#fff">Our verdict:</b> {E(c["verdict"])}<br><span class="muted">Guide: a 2003 Nevada 1.8 with 87.5k miles sold for £2,010 at Anglia Car Auctions in June 2024.</span></p></div></section>
</main>'''+foot("../")
    open(f"cars/{c['slug']}.html","w").write(pg)
