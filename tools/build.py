"""Profile README generator. Edit ROWS / DOMAINS below, then run:  python3 tools/build.py ."""
import os, sys, math, random
from xml.sax.saxutils import escape as E

random.seed(11)
DUSTC = ["#fff", "#fff", "#00E5FF", "#C6FF00"]
ROOT = sys.argv[1] if len(sys.argv) > 1 else "/mnt/user-data/outputs/profile3"
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
      '<stop offset="0" stop-color="#00E5FF" stop-opacity="0"/><stop offset=".25" stop-color="#00E5FF" stop-opacity=".9"/>'
      '<stop offset=".5" stop-color="#2F7BFF"/><stop offset=".8" stop-color="#C6FF00" stop-opacity=".95"/>'
      '<stop offset="1" stop-color="#E4FF4D" stop-opacity="0"/></linearGradient>')
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
    for cx, cy, rx, ry, col, op, tx, ty, dur in [(280, 120, 330, 85, "#0AA8FF", .20, 160, 30, 19), (760, 150, 360, 95, "#2F5BFF", .26, -170, 20, 23),
                                                 (1000, 100, 260, 70, "#00E5FF", .20, -120, 40, 17), (560, 190, 300, 60, "#C6FF00", .10, 100, -20, 21)]:
        blobs += (f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{col}" opacity="{op}"><animateTransform attributeName="transform" type="translate" '
                  f'values="0 0;{tx} {ty};0 0" dur="{dur}s" repeatCount="indefinite" calcMode="spline" keyTimes="0;.5;1" keySplines=".45 0 .55 1;.45 0 .55 1"/></ellipse>')
    dust = ""
    for _ in range(34):
        x, y, r = random.randint(30, 1170), random.randint(30, 400), round(random.uniform(.6, 1.5), 1)
        d, b = random.uniform(4, 9), random.uniform(0, 8)
        dust += (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{random.choice(DUSTC)}" opacity=".1"><animate attributeName="opacity" values=".08;.7;.08" dur="{d:.1f}s" begin="-{b:.1f}s" repeatCount="indefinite"/>'
                 f'<animateTransform attributeName="transform" type="translate" values="0 0;{random.randint(-18,18)} {random.randint(-24,-6)};0 0" dur="{d*2:.1f}s" repeatCount="indefinite"/></circle>')
    tl = "".join(f'<text class="tg" style="animation-delay:{i*4}s;{MONO}" x="600" y="300" text-anchor="middle" font-size="15" letter-spacing="4" fill="#C6FF00">{E(t)}</text>' for i, t in enumerate(TAGLINES))
    defs = (LG + '<linearGradient id="bm"><stop offset="0" stop-color="#C6FF00" stop-opacity="0"/><stop offset=".5" stop-color="#C6FF00"/><stop offset="1" stop-color="#C6FF00" stop-opacity="0"/></linearGradient><filter id="bl" x="-30%" y="-100%" width="160%" height="300%"><feGaussianBlur stdDeviation="55"/></filter>'
            '<linearGradient id="sh" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="1200" y2="0"><stop offset="0" stop-color="#D4D8DE"/><stop offset=".36" stop-color="#D4D8DE"/><stop offset=".5" stop-color="#F7FFC2"/><stop offset=".64" stop-color="#D4D8DE"/><stop offset="1" stop-color="#D4D8DE"/><animateTransform attributeName="gradientTransform" type="translate" values="-1200 0;1200 0" dur="9s" repeatCount="indefinite"/></linearGradient>')
    css = (".nm{animation:up 2.4s .2s cubic-bezier(.2,.7,.2,1) backwards}.sm{animation:up 2.4s .8s cubic-bezier(.2,.7,.2,1) backwards}"
           "@keyframes up{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:none}}"
           ".tg{opacity:0;animation:cy 16s infinite}@keyframes cy{0%{opacity:0}6%,22%{opacity:.9}28%,100%{opacity:0}}")
    body = (f'<rect width="{W}" height="{H}" fill="#000"/><g filter="url(#bl)">{blobs}</g>{dust}{waves(16, 350, 9, 26)}<rect y="330" width="260" height="190" fill="url(#bm)" opacity=".13"><animateTransform attributeName="transform" type="translate" values="-300 0;1300 0" dur="11s" repeatCount="indefinite"/></rect>'
            f'<text class="sm" x="600" y="150" text-anchor="middle" style="{MONO}" font-size="12" letter-spacing="7" fill="#71717A">ELECTRICAL &amp; COMPUTER ENGINEERING · B.TECH 2027</text>'
            f'<text class="nm" x="600" y="236" text-anchor="middle" style="{SANS}" font-size="54" font-weight="300" letter-spacing="11" fill="url(#sh)">NIRANJAN KRISHNAKUMAR</text>{tl}')
    return svg(W, H, body, defs, css, fade_x=.08, fade_y=.12)


def divider(label=""):
    W, H = 1200, 70
    ds = [wave_d(35, 7, 700, j * 2.1) for j in range(3)]
    gw = len(label) * 14 + 56
    defs = LG + (f'<mask id="gp" maskUnits="userSpaceOnUse" x="0" y="0" width="{W}" height="{H}"><rect width="{W}" height="{H}" fill="#fff"/><rect x="{600 - gw/2}" y="0" width="{gw}" height="{H}" fill="#000"/></mask>' if label else "")
    txt = f'<text x="600" y="40" text-anchor="middle" style="{MONO}" font-size="11" letter-spacing="5" fill="#C6FF00" opacity=".85">{E(label.upper())}</text>' if label else ""
    body = (f'<path d="{ds[0]}" fill="none" stroke="url(#lg)" stroke-width="1" opacity=".75" mask="url(#gp)"><animate attributeName="d" values="{";".join([ds[0], ds[1], ds[2], ds[0]])}" dur="14s" repeatCount="indefinite" {SPLINE}/></path>{txt}')
    return svg(W, H, body, defs, fade_x=.1)


def row(idx, title, desc, tag, last=False, delay=0):
    W, H = 1200, 118
    defs = ('<linearGradient id="sw" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="320" y2="0"><stop offset="0" stop-color="#00E5FF" stop-opacity="0"/><stop offset=".5" stop-color="#00E5FF"/><stop offset="1" stop-color="#C6FF00" stop-opacity="0"/>'
            f'<animateTransform attributeName="gradientTransform" type="translate" values="-320 0;1200 0" dur="7s" begin="{delay}s" repeatCount="indefinite"/></linearGradient>')
    line = lambda y: f'<path d="M0 {y}H1200" stroke="#27272A"/><path d="M0 {y}H1200" stroke="url(#sw)" stroke-width="1.5"/>'
    body = (f'<rect width="{W}" height="{H}" fill="#000" opacity=".0"/>{line(1)}{line(H-1) if last else ""}'
            f'<text x="28" y="64" style="{MONO}" font-size="13" fill="#52525B">{E(idx)}</text>'
            f'<text x="92" y="60" style="{SANS}" font-size="33" font-weight="300" letter-spacing="1" fill="#F4F4F5">{E(title)}</text>'
            f'<text x="92" y="90" style="{MONO}" font-size="13" fill="#71717A">{E(desc)}</text>'
            f'<text x="1120" y="56" text-anchor="end" style="{MONO}" font-size="12" letter-spacing="3" fill="#C6FF00" opacity=".9">{E(tag)}</text>'
            f'<text x="1172" y="70" text-anchor="end" style="{SANS}" font-size="26" fill="#00E5FF">→<animateTransform attributeName="transform" type="translate" values="0 0;7 0;0 0" dur="3.2s" repeatCount="indefinite" calcMode="spline" keyTimes="0;.5;1" keySplines=".45 0 .55 1;.45 0 .55 1"/></text>')
    return svg(W, H, body, defs, fade_x=.04)


def domains():
    W, H = 1200, 250
    xs = [150, 450, 750, 1050]
    c1 = "M0 70 C150 40 300 100 450 70 S750 40 900 70 S1100 90 1200 60"
    c2 = "M0 60 C150 95 300 45 450 70 S750 100 900 65 S1100 40 1200 75"
    body = f'<path d="{c1}" fill="none" stroke="url(#lg)" stroke-width="1.2"><animate attributeName="d" values="{c1};{c2};{c1}" dur="12s" repeatCount="indefinite" calcMode="spline" keyTimes="0;.5;1" keySplines=".45 0 .55 1;.45 0 .55 1"/></path>'
    for i, ((t, l1, l2), x) in enumerate(zip(DOMAINS, xs)):
        d = i * 1.1
        body += (f'<circle cx="{x}" cy="70" r="14" fill="none" stroke="#00E5FF"><animate attributeName="r" values="6;30;6" dur="5s" begin="{d}s" repeatCount="indefinite"/><animate attributeName="opacity" values=".7;0;.7" dur="5s" begin="{d}s" repeatCount="indefinite"/></circle>'
                 f'<circle cx="{x}" cy="70" r="4.5" fill="#C6FF00"/>'
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


# ------------------------------------------------------------------ FACE (particles that assemble, hold, dissolve)
def _lens(cx, cy, w, h, n=14):
    us = [-1 + 2 * i / (n - 1) for i in range(n)]
    return [(cx + w * u, cy - h * (1 - u * u)) for u in us] + [(cx + w * u, cy + .8 * h * (1 - u * u)) for u in us[1:-1]]


def _arc(f, n):
    return [f(i / (n - 1)) for i in range(n)]


LM = [(-.40, -.12), (-.12, -.12), (.12, -.12), (.40, -.12), (-.26, -.12), (.26, -.12), (0, .27), (-.12, .22), (.12, .22),
      (-.2, .48), (.2, .48), (0, .48), (0, .84), (-.46, .5), (.46, .5), (0, -.55), (-.26, -.30), (.26, -.30)]
EDGES = [(0, 4), (4, 1), (2, 5), (5, 3), (4, 5), (1, 6), (2, 6), (7, 6), (8, 6), (7, 9), (8, 10), (9, 11), (11, 10), (9, 12), (10, 12),
         (13, 9), (14, 10), (13, 12), (14, 12), (15, 16), (15, 17), (16, 4), (17, 5), (0, 13), (3, 14), (6, 11)]


def face_geometry():
    rnd = random.Random(3)
    P = []
    add = lambda pts, k="c": P.extend((x, y, k) for x, y in pts)
    N = 120
    add([(.62 * math.cos(th) * (1 - .28 * max(0, -math.sin(th)) ** 2), -.85 * math.sin(th)) for th in [2 * math.pi * i / N for i in range(N)]])
    for sc in (1.09, 1.19):
        add([(.62 * math.cos(math.radians(a)) * sc, -.85 * math.sin(math.radians(a)) * sc) for a in range(12, 169, 5)])
    for sx in (-1, 1):
        add(_lens(sx * .26, -.12, .14, .055))
        add([(sx * .26 + .045 * math.cos(2 * math.pi * i / 9), -.12 + .045 * math.sin(2 * math.pi * i / 9)) for i in range(9)])
        add(_arc(lambda t: (sx * .26 - .17 + .34 * t, -.25 - .045 * math.sin(math.pi * t)), 10))
        add(_arc(lambda t: (sx * (.05 + .07 * t), -.05 + .27 * t), 8))
        add(_arc(lambda t: (sx * (.16 + .06 * t), .25 + .25 * t), 8))
        add(_arc(lambda t: (sx * (.64 + .07 * math.sin(math.pi * t)), -.12 + .3 * t), 10))
        add(_arc(lambda t: (sx * (.30 - .02 * t), .75 + .3 * t), 8))
    add(_arc(lambda t: (-.12 + .24 * t, .22 + .06 * (1 - (2 * t - 1) ** 2)), 10))
    add(_arc(lambda t: (-.2 + .4 * t, .48 - .045 * (1 - abs(2 * t - 1) ** 1.5)), 14))
    add(_arc(lambda t: (-.2 + .4 * t, .485 + .008 * (1 - (2 * t - 1) ** 2)), 12))
    add(_arc(lambda t: (-.17 + .34 * t, .50 + .06 * (1 - (2 * t - 1) ** 2)), 14))
    n = 0
    while n < 70:
        x, y = rnd.uniform(-.55, .55), rnd.uniform(-.75, .75)
        if (x / .55) ** 2 + (y / .75) ** 2 < 1:
            P.append((x, y, "d")); n += 1
    add(LM, "l")
    return P


def face_svg():
    W, H, CX, CY, S = 1200, 540, 600, 270, 240
    rnd = random.Random(5)
    parts = ""
    for x, y, k in face_geometry():
        px, py = CX + x * S, CY + y * S - 12
        ang, dist = rnd.uniform(0, 6.283), rnd.uniform(260, 620)
        sx, sy = dist * math.cos(ang), dist * math.sin(ang)
        dx, dy = rnd.uniform(30, 260), rnd.uniform(-300, -40)
        r = {"c": rnd.uniform(1, 1.9), "d": rnd.uniform(.7, 1.2), "l": 3}[k]
        col = "#FFFFFF" if k == "l" else ("#C6FF00" if k == "d" else "#00E5FF")
        op = .35 if k == "d" else .95
        parts += (f'<circle class="p" cx="{px:.1f}" cy="{py:.1f}" r="{r:.1f}" fill="{col}" opacity="{op}" '
                  f'style="--sx:{sx:.0f}px;--sy:{sy:.0f}px;--dx:{dx:.0f}px;--dy:{dy:.0f}px;--o:{op};animation-delay:{rnd.uniform(0, 1):.2f}s"/>')
    pos = lambda i: (CX + LM[i][0] * S, CY + LM[i][1] * S - 12)
    mesh = "".join(f'<line class="an" x1="{pos(a)[0]:.1f}" y1="{pos(a)[1]:.1f}" x2="{pos(b)[0]:.1f}" y2="{pos(b)[1]:.1f}" stroke="url(#lg)" stroke-width=".9" stroke-opacity=".6"/>' for a, b in EDGES)
    rings = "".join(f'<circle class="an" cx="{pos(i)[0]:.1f}" cy="{pos(i)[1]:.1f}" r="4" fill="none" stroke="#00E5FF" stroke-opacity=".8"><animate attributeName="r" values="4;15;4" dur="3s" begin="{i*.17:.2f}s" repeatCount="indefinite"/></circle>' for i in range(len(LM)))
    notes = (f'<g class="an"><text x="150" y="252" style="{SANS}" font-size="34" font-weight="300" fill="#F4F4F5">1,200+</text>'
             f'<text x="150" y="278" style="{MONO}" font-size="11" letter-spacing="4" fill="#00E5FF">SPECTRAL BANDS</text><path d="M150 296H340" stroke="url(#lg)"/>'
             f'<text x="1050" y="252" text-anchor="end" style="{SANS}" font-size="34" font-weight="300" fill="#F4F4F5">XAI</text>'
             f'<text x="1050" y="278" text-anchor="end" style="{MONO}" font-size="11" letter-spacing="4" fill="#00E5FF">SHAP · LIME · GRAD-CAM++</text><path d="M860 296H1050" stroke="url(#lg)"/></g>')
    scan = '<g class="scan"><rect x="330" y="-22" width="540" height="44" fill="url(#sb)"/><path d="M330 0H870" stroke="#00E5FF" stroke-opacity=".9"/></g>'
    defs = (LG + '<linearGradient id="sb" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#00E5FF" stop-opacity="0"/><stop offset="1" stop-color="#00E5FF" stop-opacity=".28"/></linearGradient>'
            '<filter id="bl" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="60"/></filter>')
    css = ("@keyframes pf{0%{transform:translate(var(--sx),var(--sy));opacity:0;animation-timing-function:cubic-bezier(.16,.8,.2,1)}"
           "26%{transform:translate(0,0);opacity:var(--o);animation-timing-function:linear}"
           "64%{transform:translate(0,0);opacity:var(--o);animation-timing-function:cubic-bezier(.5,0,.9,.5)}"
           "90%,100%{transform:translate(var(--dx),var(--dy));opacity:0}}"
           ".p{animation:pf 16s infinite backwards}"
           "@keyframes an{0%,28%{opacity:0}37%,58%{opacity:1}66%,100%{opacity:0}}.an{opacity:0;animation:an 16s infinite}"
           "@keyframes sc{0%,30%{opacity:0;transform:translateY(60px)}33%,57%{opacity:1}60%,100%{opacity:0;transform:translateY(500px)}}.scan{opacity:0;animation:sc 16s linear infinite}"
           "@keyframes gl{0%{opacity:0}30%,64%{opacity:.16}92%,100%{opacity:0}}.gl{opacity:0;animation:gl 16s infinite}")
    body = (f'<rect width="{W}" height="{H}" fill="#000"/><ellipse class="gl" cx="600" cy="270" rx="250" ry="300" fill="#0AA8FF" filter="url(#bl)"/>'
            f'{mesh}{parts}{rings}{scan}{notes}')
    return svg(W, H, body, defs, css, fade_x=.1, fade_y=.12)


# ------------------------------------------------------------------ TOOLKIT (animated glyph per domain)
KIT = [
    ("Languages", ["Python · C++ · C", "MATLAB · SQL · Bash", "Dart · Flutter", "Embedded C"]),
    ("Learning", ["ANN · CNN · LSTM", "1D / 3D-CNN · BiLSTM", "Transfer learning", "Random Forest", "Federated · FedAvg", "PyTorch · TensorFlow", "scikit-learn · Flower"]),
    ("Vision & XAI", ["OpenCV · Hyperspectral", "ArcFace · PUMA bands", "HOG · GLCM · LBP", "Hough · Otsu", "SHAP · LIME", "Grad-CAM++"]),
    ("Data & cloud", ["PostgreSQL · MySQL", "Pandas · NumPy", "Plotly · Streamlit", "Docker · Compose", "AWS · CI/CD", "Git · GitHub · Linux", "Fernet · PBKDF2"]),
    ("Embedded", ["ESP32 · STM32", "Arduino · RPi 4", "BLE 5.0 · GATT", "Firmware · PPG", "INT8 · Edge AI", "Digital twins"]),
    ("Power & theory", ["DC-OPF · PTDF · MPPT", "THD · FFT · DSP", "PMSM · BLDC · BMS", "CAN · SCADA · Simulink", "PSO · GA · OOA · KHA", "SHO · PUMA · Markov", "Automata · Timed · CFG"]),
]


sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from toolkit import toolkit_svg as _tk


w("face", face_svg())
_w, _h, _b, _d = _tk()
w("toolkit", svg(_w, _h, _b, _d, fade_x=.03, fade_y=.03))

w("hero", hero()); w("domains", domains()); w("footer", footer())
for n, lab in [("d-build", "what i build"), ("d-work", "selected work"), ("d-path", "path"), ("d-kit", "toolkit")]:
    w(n, divider(lab))
for i, (idx, t, d, tag, _) in enumerate(ROWS):
    w(f"row{i+1}", row(idx, t, d, tag, last=i == len(ROWS) - 1, delay=i * .9))

im = lambda n, href=None: (f'<a href="{href}"><img src="assets/{n}.svg" width="100%"></a>' if href else f'<img src="assets/{n}.svg" width="100%">')
rows = "\n".join(im(f"row{i+1}", r[4]) for i, r in enumerate(ROWS))
readme = f'''<div align="center">

{im("hero")}

<sub><a href="https://{U}.github.io">portfolio</a> &nbsp;·&nbsp; <a href="https://github.com/{U}?tab=repositories">repositories</a> &nbsp;·&nbsp; <a href="https://doi.org/10.1109/EPREC66546.2026.11412040">ieee paper</a></sub>

{im("face")}

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

{im("toolkit")}

{im("footer")}

</div>
'''
open(f"{ROOT}/README.md", "w", encoding="utf-8").write(readme)

print("built", ROOT)
