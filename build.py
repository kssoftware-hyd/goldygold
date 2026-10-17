# Generates the 4 pages from one shared header/footer so they stay consistent.
import json
SITE="https://www.example.com"  # TODO: replace with the real domain, then run: python3 build.py
GST="27AARCP4844R1ZB"
ADDR="Plot No. 05, Sagar Nagar, Dhar Road, Parbhani 431401"
MAPQ="Plot+No+05+Sagar+Nagar+Dhar+Road+Parbhani+431401+Maharashtra"
# Structured data so Google can show the business, address and phone
LD=json.dumps({"@context":"https://schema.org","@type":"LocalBusiness","name":"Patel Oil And Food Process Company Pvt. Ltd.","alternateName":"Patel Oil Food","brand":{"@type":"Brand","name":"Goldy Gold"},"description":"Edible soybean oil, spices and food processing in Parbhani, Maharashtra.","url":SITE+"/","logo":SITE+"/images/logo.jpeg","image":SITE+"/images/factory.jpeg","taxID":GST,"email":"pateloilfood@gmail.com","telephone":["+919423471812","+917447663137","+918459608048"],"address":{"@type":"PostalAddress","streetAddress":"Plot No. 05, Sagar Nagar, Dhar Road","addressLocality":"Parbhani","addressRegion":"Maharashtra","postalCode":"431401","addressCountry":"IN"},"areaServed":["Parbhani","Maharashtra","India"],"founder":{"@type":"Person","name":"Atikh Patel"}})
WA="https://wa.me/919423471812"
def wa(msg): 
    from urllib.parse import quote
    return f"{WA}?text={quote(msg)}"
GEN=wa("Hello Patel Oil Food, I would like to know more about your products and business. Please share the details.")
NAV=[("index.html","Home"),("about.html","About Us"),("director.html","Our Team"),("contact.html","Contact Us")]
def page(fn,title,desc,body):
    TABS="".join(f'<a href="{h}"{" aria-current=\"page\"" if h==fn else ""}>{t.replace(" Us","")}</a>' for h,t in NAV)
    nav="".join(f'<li><a href="{h}"{" aria-current=\"page\"" if h==fn else ""}>{t}</a></li>' for h,t in NAV)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#1d1d1d">
<meta name="robots" content="index, follow">
<meta name="geo.region" content="IN-MH">
<meta name="geo.placename" content="Parbhani">
<link rel="canonical" href="{SITE}/{'' if fn=='index.html' else fn}">
<link rel="manifest" href="manifest.json">
<link rel="icon" href="images/icon-192.png">
<link rel="apple-touch-icon" href="images/icon-192.png">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Patel Oil Food">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Patel Oil Food">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/images/factory.jpeg">
<meta property="og:url" content="{SITE}/{'' if fn=='index.html' else fn}">
<meta property="og:locale" content="en_IN">
<script type="application/ld+json">{LD}</script>
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<!-- HEADER (same on every page) -->
<header class="site-header">
  <div class="wrap bar">
    <a class="brand" href="index.html" aria-label="Patel Oil And Food Process Company Pvt. Ltd. - home">
      <img src="images/logo-circle.png" alt="Goldy Gold - Patel Oil And Food Process Company logo" width="300" height="300">
      <span class="bname"><b>Patel Oil And Food Process</b><b>Company Pvt. Ltd.</b><small>Goldy Gold &middot; Foodie's Favorite</small></span>
    </a>
    <button class="menu-btn" aria-label="Open menu" aria-expanded="false" aria-controls="nav">
      <span></span><span></span><span></span>
    </button>
    <nav id="nav" aria-label="Main"><ul>{nav}</ul></nav>
  </div>
</header>
<main id="main">
{body}
</main>
<!-- FOOTER (same on every page) -->
<footer class="site-footer">
  <div class="wrap foot-grid">
    <div class="fcol brandcol">
      <a class="fbrand" href="index.html"><img src="images/logo-circle.png" alt="Goldy Gold logo" width="72" height="72"><span>Patel Oil And Food Process Company Pvt. Ltd.</span></a>
      <p>Edible soybean oil, spices and food processing in Parbhani, Maharashtra. Goldy Gold, Foodie's Favorite.</p>
      <a class="btn wa" href="{GEN}" target="_blank" rel="noopener">Chat on WhatsApp</a>
    </div>
    <div class="fcol">
      <h3>Quick links</h3>
      <ul>{"".join(f'<li><a href="{h}">{t}</a></li>' for h,t in NAV)}<li><a href="index.html#products">Our Products</a></li></ul>
    </div>
    <div class="fcol">
      <h3>Our spices</h3>
      <ul>{"".join(f'<li><a href="index.html#products">{n}</a></li>' for n in MQN[:7])}<li><a href="index.html#products">View all</a></li></ul>
    </div>
    <div class="fcol">
      <h3>Contact</h3>
      <address>
        Plot No. 05, Sagar Nagar, Dhar Road,<br>Parbhani - 431401, Maharashtra<br>
        <a href="https://www.google.com/maps/search/?api=1&query={MAPQ}" target="_blank" rel="noopener">Open in Google Maps</a><br>
        <a href="tel:+919423471812">9423471812</a>, <a href="tel:+917447663137">7447663137</a>, <a href="tel:+918459608048">8459608048</a><br>
        <a href="mailto:pateloilfood@gmail.com">pateloilfood@gmail.com</a><br>
        GST No.: {GST}<br>
        <a href="{GEN}" target="_blank" rel="noopener">WhatsApp: +91 942 347 1812</a>
      </address>
    </div>
  </div>
  <div class="wrap foot-bar">
    <p>&copy; <span id="year">2026</span> Patel Oil And Food Process Company Pvt. Ltd. All rights reserved.</p>
    <p class="dev">Designed &amp; Developed by <a href="https://kssoftware.co.in/" target="_blank" rel="noopener">KS Software</a></p>
  </div>
</footer>
<a class="wa-float" href="{GEN}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">WhatsApp</a>
<!-- Mobile app-style bottom tab bar (shown on phones only) -->
<nav class="tabbar" aria-label="Quick navigation">{TABS}<a class="tab-wa" href="{GEN}" target="_blank" rel="noopener">WhatsApp</a></nav>
<script src="js/script.js"></script>
</body>
</html>
'''
def btns(extra=""):
    return f'<a class="btn gold" href="contact.html">Contact Us</a> <a class="btn wa" href="{GEN}" target="_blank" rel="noopener">Chat on WhatsApp</a>{extra}'

boxes=[("Turmeric Powder","turmeric-powder"),("Kala Masala","kala-masala"),("Chicken Masala","chicken-masala"),("Mutton Masala","mutton-masala"),("Biryani Masala","biryani-masala"),("Pav Bhaji Masala","pav-bhaji-masala"),("Kashmiri Mirchi Masala","kashmiri-mirchi-masala"),("Kitchen King Masala","kitchen-king-masala"),("Yeser Banga Gravy Masala","yeser-banga-gravy-masala")]
prods=[("Kala Masala","kala-masala"),("Pav Bhaji Masala","pav-bhaji-masala"),("Red Chilli Powder","red-chilli-powder"),("Chicken Masala","chicken-masala"),("Biryani Masala","biryani-masala"),("Turmeric Powder","turmeric-powder"),("Garam Masala","garam-masala"),("Coriander Powder","coriander-powder"),("Veg Masala","veg-masala")]
MQN=list(dict.fromkeys([n for n,f in boxes]+[n for n,f in prods]))
def _card(n,f,d,cls,w,h): return f'<article class="pcard {cls}"><img src="images/{d}/{f}.jpg" alt="Goldy Gold {n} 100 g {cls}" width="{w}" height="{h}" loading="lazy"><h3>{n}</h3><a class="enq" href="{wa("Hello Patel Oil Food, I would like to enquire about "+n+".")}" target="_blank" rel="noopener">Enquire</a></article>'
pc='<h3 class="sub">Spice boxes</h3><div class="pgrid">'+"".join(_card(n,f,"boxes","box",480,480) for n,f in boxes)+'</div><h3 class="sub">Spice pouches</h3><div class="pgrid">'+"".join(_card(n,f,"products","pouch",300,460) for n,f in prods)+'</div>'

_w="Quality You Can Trust, Taste You Can Love.".split()
H1=" ".join(f'<span class="w{' gold' if k>=4 else ''}" style="--i:{k}">{w}</span>' for k,w in enumerate(_w))
MQ="".join(f"<span>{n}</span>" for n in MQN)
STEPS=[('Source','Soybeans and spices from local farmers and traders.'),('Extract','Crude oil extracted from soybean seed.'),('Refine','Oil refined and purified.'),('Process','Spices cleaned, dried, ground and blended.'),('Pack','Sachets, bottles, tins and spice packs.'),('Deliver','Branding and distribution to markets.')]
PROC="".join(f'<li><i>{k+1}</i><h3>{a}</h3><p>{b}</p></li>' for k,(a,b) in enumerate(STEPS))
index=f'''<section class="hero" id="top">
  <div class="hero-bg" style="background-image:url('images/factory.jpeg')"></div>
  <div class="wrap hero-in">
    <div class="hero-copy">
      <p class="eyebrow">Edible oil &middot; Spices &middot; Food processing</p>
      <h1>{H1}</h1>
      <p class="hero-p">Patel Oil And Food Process Company Pvt. Ltd. plans to produce refined soybean oil and a full range of Goldy Gold spices in Parbhani, Maharashtra, and supply them to the local market, Maharashtra and other states.</p>
      <div class="cta">{btns()}</div>
    </div>
    <div class="packs" aria-hidden="true">
      <img class="pk p1" data-depth="18" src="images/products/turmeric-powder.jpg" alt="" width="300" height="460">
      <img class="pk p2" data-depth="30" src="images/products/garam-masala.jpg" alt="" width="300" height="460">
      <img class="pk p3" data-depth="14" src="images/products/red-chilli-powder.jpg" alt="" width="300" height="460">
      <img class="badge-logo" src="images/logo.jpeg" alt="" width="110" height="96">
    </div>
  </div>
  <a class="scroll-cue" href="#products" aria-label="Scroll to products"><span></span></a>
</section>
<div class="marquee" aria-hidden="true"><div class="track">{MQ}{MQ}</div></div>
<section class="stats"><div class="wrap sgrid">
  <div><b data-count="13">13</b><span>Spice products</span></div>
  <div><b data-count="3">3</b><span>Oil pack formats</span></div>
  <div><b data-count="6">6</b><span>Process stages</span></div>
  <div><b data-count="5">5</b><span>Leadership team</span></div>
</div></section>
<section class="sec">
  <div class="wrap">
    <h2 id="products">Our products</h2>
    <p class="lead">Goldy Gold spices in 9 g, 50 g, 100 g and 200 g packs. Tap Enquire to message us on WhatsApp.</p>
    {pc}
  </div>
</section>
<section class="sec dark"><div class="wrap"><h2>From farm to pack</h2><p class="lead">Our planned production flow.</p><ol class="steps">{PROC}</ol></div></section>
<section class="sec tint">
  <div class="wrap two">
    <div>
      <h2>Business highlights</h2>
      <ul class="ticks">
        <li>Soybean oil extraction, refining and packaging</li>
        <li>Spice cleaning, drying, grinding, blending and packing</li>
        <li>Branding, packaging and distribution of food products</li>
        <li>Soybean meal supplied to the animal feed industry</li>
      </ul>
    </div>
    <img class="rounded" src="images/factory.jpeg" alt="Patel Oil And Food Process Company factory and office building" loading="lazy">
  </div>
</section>
<section class="sec">
  <div class="wrap">
    <h2>Why choose us</h2>
    <div class="grid g3">
      <article class="card"><h3>Safe, quality food</h3><p>Our first objective is quality and safe edible oils and spices.</p></article>
      <article class="card"><h3>Local sourcing</h3><p>We aim to work with local farmers, soybean producers and spice traders.</p></article>
      <article class="card"><h3>Local jobs</h3><p>We plan employment for local youth and women in production, packing and distribution.</p></article>
    </div>
  </div>
</section>
<section class="sec cta-band"><div class="wrap"><h2>Need prices or bulk supply details?</h2><p>Message us and we will reply with details.</p><div class="cta">{btns()}</div></div></section>'''

about=f'''<section class="page-head"><div class="wrap"><h1>About Us</h1><p>Patel Oil And Food Process Company Pvt. Ltd.</p></div></section>
<section class="sec">
  <div class="wrap two">
    <div>
      <h2>Company overview</h2>
      <p>Our primary objective is to produce refined edible oil from soybeans, manufacture a variety of edible spices, and provide local employment. We plan to make high-quality edible products and supply them to the local market, Maharashtra and other states.</p>
      <p>Our fields of work are edible oil production, edible spice manufacturing and food processing.</p>
      <a class="btn wa" href="{wa("Hello Patel Oil Food, I read your About Us page and would like to enquire about your business.")}" target="_blank" rel="noopener">WhatsApp enquiry</a>
    </div>
    <img class="rounded" src="images/factory.jpeg" alt="Factory building with storage tanks and delivery trucks" loading="lazy">
  </div>
</section>
<section class="sec tint">
  <div class="wrap">
    <h2>What we plan to make</h2>
    <div class="grid g3">
      <article class="card"><h3>Edible oil</h3><p>Crude oil extraction from soybean seeds, refining and purification, and packing in sachets, bottles and tins. Other edible oils may follow.</p></article>
      <article class="card"><h3>Edible spices</h3><p>Turmeric, red chili, coriander, garam masala, chicken masala, biryani masala, veg masala, pav bhaji masala, kala masala and other blends.</p></article>
      <article class="card"><h3>By-products</h3><p>Soybean meal for the animal feed industry, plus branding, packaging and distribution.</p></article>
    </div>
  </div>
</section>
<section class="sec">
  <div class="wrap two">
    <div>
      <h2>Mission</h2>
      <p>To add value to local agricultural produce by making quality, safe edible oils and spices, and to create jobs for local youth and women.</p>
      <h2>Vision</h2>
      <p>To contribute to the industrial and economic development of our region and expand into new markets as production capacity grows.</p>
    </div>
    <div>
      <h2>Our commitments</h2>
      <ul class="ticks">
        <li>Quality and safe products</li>
        <li>Collaboration with farmers, traders and small businesses</li>
        <li>Employment in production, packing, quality control, warehousing, transport, sales and office roles</li>
        <li>Customer satisfaction and reliable supply</li>
      </ul>
    </div>
  </div>
</section>'''

team=[("Atikh Patel","CEO and Founder","atikh-patel"),("Abdul Haque","Chief Financial Officer","abdul-haque"),("Shaikh Juned","Director and Business Strategy","shaikh-juned"),("Maheen Khan","Director","maheen-khan"),("Afreen Shaikh","Director","afreen-shaikh")]
# Order matters: Abdul | Juned on row 1, Maheen (below Abdul) | Afreen (below Juned) on row 2
tc="".join(f'<article class="member"><img src="images/team/{f}.jpg" alt="Portrait of {n}, {r}" width="480" height="600" loading="lazy"><div><h3>{n}</h3><p>{r}</p></div></article>' for n,r,f in team[1:])
director=f'''<section class="page-head"><div class="wrap"><h1>Our Team</h1><p>The people leading Patel Oil And Food Process Company Pvt. Ltd.</p></div></section>
<section class="sec tint ceo-sec">
  <div class="wrap ceo">
    <div class="ceo-text">
      <p class="eyebrow dk">CEO and Founder</p>
      <h2>Atikh Patel</h2>
      <p>Leading Patel Oil And Food Process Company Pvt. Ltd. in Parbhani, Maharashtra, with Goldy Gold edible oil and spices.</p>
      <a class="btn wa" href="{wa("Hello Atikh Patel, I would like to connect with Patel Oil Food.")}" target="_blank" rel="noopener">Message on WhatsApp</a>
    </div>
    <div class="ceo-photo"><img src="images/team/atikh-patel.jpg" alt="Portrait of Atikh Patel, CEO and Founder" width="480" height="648"></div>
    <div class="ceo-points">
      <h3>What we stand for</h3>
      <ul class="ticks">
        <li>Quality and safe edible oils and spices</li>
        <li>Value addition to local agricultural produce</li>
        <li>Jobs for local youth and women</li>
        <li>Collaboration with farmers, traders and small businesses</li>
      </ul>
    </div>
  </div>
</section>
<section class="sec">
  <div class="wrap">
    <h2>Leadership team</h2>
    <div class="team team2">{tc}</div>
  </div>
</section>'''

contact=f'''<section class="page-head"><div class="wrap"><h1>Contact Us</h1><p>Send an enquiry on WhatsApp or email.</p></div></section>
<section class="sec">
  <div class="wrap two">
    <div>
      <h2>Patel Oil Food</h2>
      <p><strong>Patel Oil And Food Process Company Pvt. Ltd.</strong></p>
      <p>Plot No. 05, Sagar Nagar, Dhar Road,<br>Parbhani - 431401</p>
      <p>Phone: <a href="tel:+919423471812">9423471812</a>, <a href="tel:+917447663137">7447663137</a>, <a href="tel:+918459608048">8459608048</a></p>
      <p>WhatsApp: <a href="{GEN}" target="_blank" rel="noopener">+91 942 347 1812</a></p>
      <p>Email: <a href="mailto:pateloilfood@gmail.com">pateloilfood@gmail.com</a></p>
      <p>GST No.: <strong>{GST}</strong></p>
      <div class="cta"><a class="btn wa" href="{GEN}" target="_blank" rel="noopener">Chat on WhatsApp</a> <a class="btn gold" href="mailto:pateloilfood@gmail.com?subject=Business%20enquiry">Email Us</a></div>
    </div>
    <form id="enquiry" novalidate>
      <h2>Business enquiry</h2>
      <p class="note">This form does not send data to a server. It prepares your message, then opens WhatsApp or your email app for you to send.</p>
      <label for="name">Name</label><input id="name" name="name" type="text" autocomplete="name" required>
      <span class="err" data-for="name"></span>
      <label for="phone">Phone number</label><input id="phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required>
      <span class="err" data-for="phone"></span>
      <label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" required>
      <span class="err" data-for="email"></span>
      <label for="message">Message</label><textarea id="message" name="message" rows="5" required></textarea>
      <span class="err" data-for="message"></span>
      <div class="cta"><button class="btn wa" type="submit" data-via="whatsapp">Send on WhatsApp</button> <button class="btn gold" type="submit" data-via="email">Send by email</button></div>
    </form>
  </div>
</section>
<section class="sec tint">
  <div class="wrap">
    <h2>Find us</h2>
    <p>{ADDR}</p>
    <div class="map"><iframe title="Map of Patel Oil And Food Process Company, Sagar Nagar, Dhar Road, Parbhani" src="https://www.google.com/maps?q={MAPQ}&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
    <div class="cta"><a class="btn gold" href="https://www.google.com/maps/dir/?api=1&destination={MAPQ}" target="_blank" rel="noopener">Get directions</a> <a class="btn wa" href="https://www.google.com/maps/search/?api=1&query={MAPQ}" target="_blank" rel="noopener">Open in Google Maps</a></div>
  </div>
</section>'''

pages=[("index.html","Patel Oil Food | Goldy Gold Spices and Edible Oil, Parbhani","Goldy Gold spices and soybean edible oil by Patel Oil Food, Parbhani, Maharashtra. Kala, Pav Bhaji, Garam, Biryani, Chicken masala, turmeric, chilli and more.",index),
("about.html","About Us | Patel Oil Food","About Patel Oil And Food Process Company: mission, vision and planned products.",about),
("director.html","Our Team | Patel Oil Food","Meet the CEO, CFO and directors of Patel Oil And Food Process Company, Parbhani.",director),
("contact.html","Contact Us | Patel Oil Food","Patel Oil Food, Sagar Nagar, Dhar Road, Parbhani 431401. Call, WhatsApp, email or get directions on Google Maps.",contact)]
for fn,t,d,b in pages: open(fn,"w").write(page(fn,t,d,b))

open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"<url><loc>{SITE}/{'' if f=='index.html' else f}</loc></url>\n" for f,*_ in pages)+"</urlset>\n")
open("robots.txt","w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
