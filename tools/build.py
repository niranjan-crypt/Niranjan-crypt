"""Profile README generator. Edit ROWS / DOMAINS below, then run:  python3 tools/build.py ."""
import os, sys, math, random
from xml.sax.saxutils import escape as E

random.seed(11)
ROOT = sys.argv[1] if len(sys.argv) > 1 else "/mnt/user-data/outputs/profile2"
A = f"{ROOT}/assets"
os.makedirs(A, exist_ok=True)
MONO = "font-family:'JetBrains Mono','SF Mono',Menlo,Consolas,monospace"
SANS = "font-family:'Helvetica Neue',Helvetica,Arial,sans-serif"
U = "niranjan-crypt"

# ------------------------------------------------------------------ EDIT ME
ROWS = [  # (index, title, description, right-hand label, link or None)
    ("01", "Physics-Informed MPPT", "Diode-physics features · 300-state Markov validation · R² 0.9994", "IEEE SPICES 2026", None),
    ("02", "Congestion Management", "Tri-hybrid OOA · KHA · SHO optimizer on a DC-OPF framework", "IEEE EPREC 2026", "https://doi.org/10.1109/EPREC66546.2026.11412040"),
    ("03", "Hyperspectral Face ID", "1,200+ bands · PUMA selection · 3D-CNN · ArcFace · explainable AI", "COMPUTER VISION", f"https://github.com/{U}/Hyperspectral-Face-Identification-XAI"),
    ("04", "Federated Text AI", "Flower · FedAvg · resource-aware clients · encrypted LSTM", "PRIVATE LEARNING", f"https://github.com/{U}/Privacy-Preserving-Federated-Learning-FL-System-for-Text-Prediction"),
    ("05", "CommerceIQ", "1.5M-record ETL · star schema · 5.35× query speedup", "DATA ENGINEERING", f"https://github.com/{U}/CommerceIQ"),
    ("··", "All repositories", "Power quality, smart glove, MRI segmentation, formal verification and more", "GITHUB", f"https://github.com/{U}?tab=repositories"),
]
DOMAINS = [
    ("Physics-informed AI", "governing equations as features", "MPPT · DC-OPF · Markov validation"),
    ("Vision & explainability", "hyperspectral · 3D-CNN · ArcFace", "SHAP · LIME · Grad-CAM++"),
    ("Private learning", "federated LSTM · Flower · FedAvg", "encrypted, resource-aware clients"),
    ("Power & embedded", "power quality · EV · BMS · SCADA", "ESP32 · STM32 · edge AI"),
]
TAGLINES = ["physics-informed intelligence", "vision that explains itself", "learning that stays private", "algorithms that meet hardware"]
# ---------------------------------------------------------------------------


def svg(w, h, body, defs="", css="", fade_x=.06, fade_y=0.0):
    fx = f'<linearGradient id="fx"><stop offset="0" stop-color="#000"/><stop offset="{fade_x}" stop-color="#fff"/><stop offset="{1-fade_x}" stop-color="#fff"/><stop offset="1" stop-color="#000"/></linearGradient><mask id="mx" maskUnits="userSpaceOnUse" x="0" y="0" width="{w}" height="{h}"><rect width="{w}" height="{h}" fill="url(#fx)"/></mask>'
    fy = ""
    open_, close = '<g mask="url(#mx)">', "</g>"
    if fade_y:
        fy = f'<linearGradient id="fy" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#000"/><stop offset="{fade_y}" stop-color="#fff"/><stop offset="{1-fade_y}" stop-color="#fff"/><stop offset="1" stop-color="#000"/></linearGradient><mask id="my" maskUnits="userSpaceOnUse" x="0" y="0" width="{w}" height="{h}"><rect width="{w}" height="{h}" fill="url(#fy)"/></mask>'
        open_ += '<g mask="url(#my)">'; close += "</g>"
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'
            f'<defs>{fx}{fy}{defs}</defs><style>{css}</style>{open_}{body}{close}</svg>')


LG = ('<linearGradient id="lg" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="1200" y2="0">'
      '<stop offset="0" stop-color="#67E8F9" stop-opacity="0"/><stop offset=".25" stop-color="#67E8F9" stop-opacity=".9"/>'
      '<stop offset=".6" stop-color="#818CF8"/><stop offset=".85" stop-color="#C084FC" stop-opacity=".9"/>'
      '<stop offset="1" stop-color="#C084FC" stop-opacity="0"/></linearGradient>')
SPLINE = 'calcMode="spline" keyTimes="0;.33;.66;1" keySplines=".45 0 .55 1;.45 0 .55 1;.45 0 .55 1"'


def wave_d(base, amp, lam, ph, W=1200):
    pts = []
    for x in range(-20, W + 21, 20):
        t = .35 + .65 * math.sin(math.pi * min(max(x, 0), W) / W)
        y = base + amp * t * math.sin(2 * math.pi * x / lam + ph) + amp * .35 * t * math.sin(2 * math.pi * x / (lam * .53) + ph * 1.7)
        pts.append(f"{x} {y:.1f}")
    return "M" + " L".join(pts)


def waves(n, y0, spread, amp, op=(.10, .55)):
    out = ""
    for i in range(n):
        k = i / (n - 1)
        base, a = y0 + i * spread, amp * (.6 + .8 * k)
        lam, ph, dur = random.uniform(650, 950), random.uniform(0, 6.28), random.uniform(16, 28)
        ds = [wave_d(base, a, lam, ph + j * 2.1) for j in range(3)]
        o = op[0] + (op[1] - op[0]) * k
        out += (f'<path d="{ds[0]}" fill="none" stroke="url(#lg)" stroke-width="1" opacity="{o:.2f}">'
                f'<animate attributeName="d" values="{";".join([ds[0], ds[1], ds[2], ds[0]])}" dur="{dur:.1f}s" repeatCount="indefinite" {SPLINE}/></path>')
    return out


def hero():
    W, H = 1200, 520
    blobs = ""
    for cx, cy, rx, ry, col, op, tx, ty, dur in [(280, 120, 330, 85, "#22D3EE", .20, 160, 30, 19), (760, 150, 360, 95, "#6366F1", .26, -170, 20, 23),
                                                 (1000, 100, 260, 70, "#A855F7", .20, -120, 40, 17), (560, 190, 300, 60, "#10B981", .10, 100, -20, 21)]:
        blobs += (f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{col}" opacity="{op}"><animateTransform attributeName="transform" type="translate" '
                  f'values="0 0;{tx} {ty};0 0" dur="{dur}s" repeatCount="indefinite" calcMode="spline" keyTimes="0;.5;1" keySplines=".45 0 .55 1;.45 0 .55 1"/></ellipse>')
    dust = ""
    for _ in range(34):
        x, y, r = random.randint(30, 1170), random.randint(30, 400), round(random.uniform(.6, 1.5), 1)
        d, b = random.uniform(4, 9), random.uniform(0, 8)
        dust += (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" opacity=".1"><animate attributeName="opacity" values=".08;.7;.08" dur="{d:.1f}s" begin="-{b:.1f}s" repeatCount="indefinite"/>'
                 f'<animateTransform attributeName="transform" type="translate" values="0 0;{random.randint(-18,18)} {random.randint(-24,-6)};0 0" dur="{d*2:.1f}s" repeatCount="indefinite"/></circle>')
    tl = "".join(f'<text class="tg" style="animation-delay:{i*4}s;{MONO}" x="600" y="300" text-anchor="middle" font-size="15" letter-spacing="4" fill="#67E8F9">{E(t)}</text>' for i, t in enumerate(TAGLINES))
    defs = (LG + '<filter id="bl" x="-30%" y="-100%" width="160%" height="300%"><feGaussianBlur stdDeviation="55"/></filter>'
            '<linearGradient id="sh" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="1200" y2="0"><stop offset="0" stop-color="#C4C4CC"/><stop offset=".36" stop-color="#C4C4CC"/><stop offset=".5" stop-color="#FFFFFF"/><stop offset=".64" stop-color="#C4C4CC"/><stop offset="1" stop-color="#C4C4CC"/><animateTransform attributeName="gradientTransform" type="translate" values="-1200 0;1200 0" dur="9s" repeatCount="indefinite"/></linearGradient>')
    css = (".nm{animation:up 2.4s .2s cubic-bezier(.2,.7,.2,1) backwards}.sm{animation:up 2.4s .8s cubic-bezier(.2,.7,.2,1) backwards}"
           "@keyframes up{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:none}}"
           ".tg{opacity:0;animation:cy 16s infinite}@keyframes cy{0%{opacity:0}6%,22%{opacity:.9}28%,100%{opacity:0}}")
    body = (f'<rect width="{W}" height="{H}" fill="#000"/><g filter="url(#bl)">{blobs}</g>{dust}{waves(16, 350, 9, 26)}'
            f'<text class="sm" x="600" y="150" text-anchor="middle" style="{MONO}" font-size="12" letter-spacing="7" fill="#71717A">ELECTRICAL &amp; COMPUTER ENGINEERING · B.TECH 2027</text>'
            f'<text class="nm" x="600" y="236" text-anchor="middle" style="{SANS}" font-size="54" font-weight="300" letter-spacing="11" fill="url(#sh)">NIRANJAN KRISHNAKUMAR</text>{tl}')
    return svg(W, H, body, defs, css, fade_x=.08, fade_y=.12)


def divider(label=""):
    W, H = 1200, 70
    ds = [wave_d(35, 7, 700, j * 2.1) for j in range(3)]
    gap = f'<rect x="{600 - len(label)*7 - 24}" y="14" width="{len(label)*14 + 48}" height="42" fill="#000"/>' if label else ""
    txt = f'<text x="600" y="40" text-anchor="middle" style="{MONO}" font-size="11" letter-spacing="5" fill="#71717A">{E(label.upper())}</text>' if label else ""
    body = (f'<path d="{ds[0]}" fill="none" stroke="url(#lg)" stroke-width="1" opacity=".7"><animate attributeName="d" values="{";".join([ds[0], ds[1], ds[2], ds[0]])}" dur="14s" repeatCount="indefinite" {SPLINE}/></path>{gap}{txt}')
    return svg(W, H, body, LG, fade_x=.1)


def row(idx, title, desc, tag, last=False, delay=0):
    W, H = 1200, 118
    defs = ('<linearGradient id="sw" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="320" y2="0"><stop offset="0" stop-color="#67E8F9" stop-opacity="0"/><stop offset=".5" stop-color="#67E8F9"/><stop offset="1" stop-color="#A78BFA" stop-opacity="0"/>'
            f'<animateTransform attributeName="gradientTransform" type="translate" values="-320 0;1200 0" dur="7s" begin="{delay}s" repeatCount="indefinite"/></linearGradient>')
    line = lambda y: f'<path d="M0 {y}H1200" stroke="#27272A"/><path d="M0 {y}H1200" stroke="url(#sw)" stroke-width="1.5"/>'
    body = (f'<rect width="{W}" height="{H}" fill="#000" opacity=".0"/>{line(1)}{line(H-1) if last else ""}'
            f'<text x="28" y="64" style="{MONO}" font-size="13" fill="#52525B">{E(idx)}</text>'
            f'<text x="92" y="60" style="{SANS}" font-size="33" font-weight="300" letter-spacing="1" fill="#F4F4F5">{E(title)}</text>'
            f'<text x="92" y="90" style="{MONO}" font-size="13" fill="#71717A">{E(desc)}</text>'
            f'<text x="1120" y="56" text-anchor="end" style="{MONO}" font-size="12" letter-spacing="3" fill="#67E8F9" opacity=".85">{E(tag)}</text>'
            f'<text x="1172" y="70" text-anchor="end" style="{SANS}" font-size="26" fill="#A1A1AA">→<animateTransform attributeName="transform" type="translate" values="0 0;7 0;0 0" dur="3.2s" repeatCount="indefinite" calcMode="spline" keyTimes="0;.5;1" keySplines=".45 0 .55 1;.45 0 .55 1"/></text>')
    return svg(W, H, body, defs, fade_x=.04)


def domains():
    W, H = 1200, 250
    xs = [150, 450, 750, 1050]
    c1 = "M0 70 C150 40 300 100 450 70 S750 40 900 70 S1100 90 1200 60"
    c2 = "M0 60 C150 95 300 45 450 70 S750 100 900 65 S1100 40 1200 75"
    body = f'<path d="{c1}" fill="none" stroke="url(#lg)" stroke-width="1.2"><animate attributeName="d" values="{c1};{c2};{c1}" dur="12s" repeatCount="indefinite" calcMode="spline" keyTimes="0;.5;1" keySplines=".45 0 .55 1;.45 0 .55 1"/></path>'
    for i, ((t, l1, l2), x) in enumerate(zip(DOMAINS, xs)):
        d = i * 1.1
        body += (f'<circle cx="{x}" cy="70" r="14" fill="none" stroke="#67E8F9"><animate attributeName="r" values="6;30;6" dur="5s" begin="{d}s" repeatCount="indefinite"/><animate attributeName="opacity" values=".7;0;.7" dur="5s" begin="{d}s" repeatCount="indefinite"/></circle>'
                 f'<circle cx="{x}" cy="70" r="4.5" fill="#67E8F9"/>'
                 f'<text x="{x}" y="140" text-anchor="middle" style="{SANS}" font-size="21" font-weight="300" letter-spacing=".5" fill="#F4F4F5">{E(t)}</text>'
                 f'<text x="{x}" y="172" text-anchor="middle" style="{MONO}" font-size="12" fill="#71717A">{E(l1)}</text>'
                 f'<text x="{x}" y="194" text-anchor="middle" style="{MONO}" font-size="12" fill="#52525B">{E(l2)}</text>')
    return svg(W, H, body, LG, fade_x=.04)


def footer():
    W, H = 1200, 300
    body = (f'{waves(14, 150, 9, 24, op=(.08, .5))}'
            f'<text x="600" y="104" text-anchor="middle" style="{SANS}" font-size="24" font-weight="300" font-style="italic" letter-spacing="2" fill="#E4E4E7">understand the system. engineer the intelligence.</text>'
            f'<text x="600" y="136" text-anchor="middle" style="{MONO}" font-size="11" letter-spacing="6" fill="#52525B">NIRANJAN KRISHNAKUMAR · COIMBATORE</text>')
    return svg(W, H, body, LG, fade_x=.08, fade_y=.2)


def w(name, s):
    open(f"{A}/{name}.svg", "w", encoding="utf-8").write(s)


w("hero", hero()); w("domains", domains()); w("footer", footer())
for n, lab in [("d-build", "what i build"), ("d-work", "selected work"), ("d-path", "path"), ("d-kit", "toolkit"), ("d-motion", "in motion")]:
    w(n, divider(lab))
for i, (idx, t, d, tag, _) in enumerate(ROWS):
    w(f"row{i+1}", row(idx, t, d, tag, last=i == len(ROWS) - 1, delay=i * .9))

im = lambda n, href=None: (f'<a href="{href}"><img src="assets/{n}.svg" width="100%"></a>' if href else f'<img src="assets/{n}.svg" width="100%">')
rows = "\n".join(im(f"row{i+1}", r[4]) for i, r in enumerate(ROWS))
readme = f'''<div align="center">

{im("hero")}

<sub><a href="https://github.com/{U}/{U}.github.io">portfolio</a> &nbsp;·&nbsp; <a href="https://github.com/{U}?tab=repositories">repositories</a> &nbsp;·&nbsp; <a href="https://doi.org/10.1109/EPREC66546.2026.11412040">ieee paper</a> &nbsp;·&nbsp; <a href="https://www.linkedin.com/in/YOUR-LINKEDIN-ID">linkedin</a></sub>

<br><br>

<p align="center">I study Electrical &amp; Computer Engineering at Amrita Vishwa Vidyapeetham, Coimbatore.<br>
I work where physics, mathematics and learning systems meet —<br>
turning the governing equations of a system into models that run on real hardware.</p>

{im("d-build")}

{im("domains")}

{im("d-work")}

{rows}

{im("d-path")}

<p align="center"><b>Larsen &amp; Toubro</b> · industry internship, 2026<br>
<sub>EV powertrain simulation · PMSM / BLDC control · BMS architecture · CAN · railway SCADA modelling</sub></p>

<p align="center"><b>AWS Academy</b> · cloud foundations, 2026</p>

{im("d-kit")}

<sub>python · c++ · c · matlab · simulink · sql · bash · dart<br>
pytorch · tensorflow · opencv · scikit-learn · flower<br>
postgresql · docker · streamlit · aws · git · linux · flutter<br>
esp32 · stm32 · raspberry pi · ble · embedded c</sub>

{im("d-motion")}

<img src="https://raw.githubusercontent.com/{U}/Niranjan-crypt/output/github-contribution-grid-snake-dark.svg" width="100%">

{im("footer")}

</div>
'''
open(f"{ROOT}/README.md", "w", encoding="utf-8").write(readme)

wf = f"{ROOT}/.github/workflows"
os.makedirs(wf, exist_ok=True)
open(f"{wf}/snake.yml", "w").write('''name: Generate Contribution Snake

on:
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch:
  push:
    branches:
      - main

permissions:
  contents: write

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - name: Generate contribution graph
        uses: Platane/snk@v3
        with:
          github_user_name: niranjan-crypt
          outputs: |
            dist/github-contribution-grid-snake.svg
            dist/github-contribution-grid-snake-dark.svg?palette=github-dark

      - name: Deploy SVGs
        uses: crazy-max/ghaction-github-pages@v4
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
''')
print("built", ROOT)
