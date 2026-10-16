# Patel Oil Food website

Plain HTML, CSS and JavaScript. Open `index.html` in a browser; no build step needed.

- `images/logo.jpeg`, `images/factory.jpeg`: supplied by the client.
- Director page: replace `[Director Name]`, the message text and the SVG portrait (swap the `.portrait` SVG for `<img src="images/director.jpg" alt="...">`).
- Product photos: replace the striped `.ph` boxes in `index.html` with `<img>` tags.
- WhatsApp number / email: edit `WHATSAPP` and `EMAIL` in `js/script.js`, and the `wa.me` / `mailto:` links in the HTML.
- Colours: `:root` variables at the top of `css/style.css`.
- The contact form has no backend. It validates input, then opens WhatsApp or the visitor's email app with a pre-filled message.
- `build.py` is optional: it regenerates the four pages from one shared header/footer. Edit it and run `python3 build.py`, or edit the HTML files directly.

## v2 notes
- **Domain:** open `build.py`, set `SITE` to the real domain (used for canonical, Open Graph, sitemap, JSON-LD), then run `python3 build.py`. `sitemap.xml` and `robots.txt` are regenerated.
- **Google:** after going live, add the site in Google Search Console, submit `sitemap.xml`, and claim/verify the Google Business Profile with the same name, address and phone.
- **Map:** `contact.html` embeds Google Maps for the Sagar Nagar, Dhar Road address (no API key needed). If you have an exact map pin, replace the iframe `src` with the "Embed a map" link from Google Maps.
- **App feel:** phones get a bottom tab bar, safe-area padding and large tap targets. `manifest.json` lets visitors "Add to Home Screen".
- **Team and products:** photos are in `images/team/` and `images/products/`; names and titles are in `build.py`.
