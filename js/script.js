// ---- Business settings (edit here) ----
const WHATSAPP = "917447663137";
const EMAIL = "pateloilfood@gmail.com";

// ---- Mobile menu toggle ----
const btn = document.querySelector(".menu-btn");
const nav = document.getElementById("nav");
btn.addEventListener("click", () => {
  const open = nav.classList.toggle("open");
  btn.setAttribute("aria-expanded", open);
  btn.setAttribute("aria-label", open ? "Close menu" : "Open menu");
});
document.addEventListener("keydown", e => {
  if (e.key === "Escape" && nav.classList.contains("open")) { btn.click(); btn.focus(); }
});

// ---- Footer year ----
document.getElementById("year").textContent = new Date().getFullYear();

// ---- Contact form: validate, then open WhatsApp or email (no server involved) ----
const form = document.getElementById("enquiry");
if (form) {
  let via = "whatsapp";
  form.querySelectorAll("button[type=submit]").forEach(b =>
    b.addEventListener("click", () => (via = b.dataset.via)));

  const rules = {
    name: v => v.trim().length >= 2 || "Enter your name.",
    phone: v => /^[+]?[0-9\s-]{10,15}$/.test(v.trim()) || "Enter a valid phone number (10 to 15 digits).",
    email: v => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v.trim()) || "Enter a valid email address.",
    message: v => v.trim().length >= 10 || "Write at least 10 characters."
  };

  form.addEventListener("submit", e => {
    e.preventDefault();
    let ok = true, first = null;
    for (const [id, check] of Object.entries(rules)) {
      const field = form.elements[id];
      const res = check(field.value);
      const err = form.querySelector(`.err[data-for=${id}]`);
      err.textContent = res === true ? "" : res;
      field.setAttribute("aria-invalid", res !== true);
      if (res !== true) { ok = false; first = first || field; }
    }
    if (!ok) { first.focus(); return; }

    const d = Object.fromEntries(new FormData(form));
    const text = `Hello Patel Oil Food,\nName: ${d.name}\nPhone: ${d.phone}\nEmail: ${d.email}\nMessage: ${d.message}`;
    if (via === "whatsapp") {
      window.open(`https://wa.me/${WHATSAPP}?text=${encodeURIComponent(text)}`, "_blank", "noopener");
    } else {
      location.href = `mailto:${EMAIL}?subject=${encodeURIComponent("Business enquiry from " + d.name)}&body=${encodeURIComponent(text)}`;
    }
  });
}

// ===== v3 animations =====
const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
// Scroll progress bar + header shadow
const bar = Object.assign(document.createElement("div"), {className: "progress"});
document.body.prepend(bar);
const header = document.querySelector(".site-header");
addEventListener("scroll", () => {
  const h = document.documentElement;
  bar.style.width = (h.scrollTop / (h.scrollHeight - h.clientHeight || 1)) * 100 + "%";
  header.classList.toggle("shrunk", h.scrollTop > 20);
}, {passive: true});

// Reveal-on-scroll with stagger
document.querySelectorAll("main h2, main .lead, .card, .pcard, .member, .steps li, .sgrid > div, .two > *, form, .map, .cta-band .cta")
  .forEach((el, i) => { el.classList.add("reveal"); el.style.setProperty("--d", (i % 4) * 0.09 + "s"); });
const io = new IntersectionObserver(es => es.forEach(e => {
  if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
}), {threshold: 0.15});
document.querySelectorAll(".reveal").forEach(el => reduce ? el.classList.add("in") : io.observe(el));

// Count-up numbers
const co = new IntersectionObserver(es => es.forEach(e => {
  if (!e.isIntersecting) return;
  const el = e.target, n = +el.dataset.count; let v = 0;
  const t = setInterval(() => { v++; el.textContent = v; if (v >= n) clearInterval(t); }, 900 / n);
  co.unobserve(el);
}), {threshold: .6});
document.querySelectorAll("[data-count]").forEach(el => { if (!reduce) { el.textContent = "0"; co.observe(el); } });

// Hero mouse parallax on the floating packs (desktop only)
const hero = document.querySelector(".hero");
if (hero && !reduce && matchMedia("(hover:hover)").matches) {
  hero.addEventListener("mousemove", e => {
    const x = e.clientX / innerWidth - .5, y = e.clientY / innerHeight - .5;
    hero.querySelectorAll(".pk").forEach(p => {
      const d = +p.dataset.depth;
      p.style.setProperty("--mx", x * d + "px"); p.style.setProperty("--my", y * d + "px");
    });
  });
}

// 3D tilt on product cards (desktop only)
if (!reduce && matchMedia("(hover:hover)").matches) {
  document.querySelectorAll(".pcard").forEach(c => {
    c.addEventListener("mousemove", e => {
      const r = c.getBoundingClientRect();
      c.style.transform = `perspective(700px) rotateY(${((e.clientX - r.left) / r.width - .5) * 10}deg) rotateX(${-((e.clientY - r.top) / r.height - .5) * 10}deg) translateY(-6px)`;
    });
    c.addEventListener("mouseleave", () => c.style.transform = "");
  });
}
