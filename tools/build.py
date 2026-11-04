"""Profile README generator.  Edit ROWS / DOMAINS / copy below, then run:  python3 tools/build.py ."""
import os, sys, io, re, math, random, base64
from functools import lru_cache
from xml.sax.saxutils import escape as E, unescape as UE
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "lib"))
from fontTools import subset
from fontTools.ttLib import TTFont
random.seed(11)
ROOT = sys.argv[1] if len(sys.argv) > 1 else "/mnt/user-data/outputs/profile4"
A = f"{ROOT}/assets"
os.makedirs(A, exist_ok=True)
U = "niranjan-crypt"
SITE = f"https://{U}.github.io"

# ------------------------------------------------------------------ fonts (embedded into every SVG, subset to the glyphs used)
FONTS = {
    "NK Sans": {
        400: "Inter-Regular.woff2",
        500: "Inter-Medium.woff2",
        700: "InterDisplay-Bold.woff2",
        800: "InterDisplay-ExtraBold.woff2",
    },
    "NK Mono": {
        400: "jetbrains-mono-latin-400-normal.woff2",
        700: "jetbrains-mono-latin-700-normal.woff2",
    },
}
MONO = "font-family:'NK Mono','JetBrains Mono','SF Mono',Menlo,Consolas,monospace"
SANS = "font-family:'NK Sans','Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif"
TAGLINE = "font-family:'NK Sans','Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif"


@lru_cache(None)
def subset_b64(fn, chars):
    opts = subset.Options(); opts.flavor = "woff2"; opts.layout_features = ["kern"]; opts.notdef_outline = True
    font = subset.load_font(os.path.join(HERE, "fonts", fn), opts)
    sub = subset.Subsetter(opts); sub.populate(text=chars); sub.subset(font)
    buf = io.BytesIO(); font.flavor = "woff2"; font.save(buf)
    return base64.b64encode(buf.getvalue()).decode()


def embed(s):
    txt = "".join(re.sub(r"<[^>]+>", "", t) for t in re.findall(r"<text[^>]*>(.*?)</text>", s, re.S))
    chars = "".join(sorted(set(UE(txt)) | set(" .·-")))
    faces = ""
    for fam, ws in FONTS.items():
        if f"'{fam}'" not in s: continue
        for wgt, fn in ws.items():
            st = "italic" if "italic" in fn else "normal"
            faces += f"@font-face{{font-family:'{fam}';font-weight:{wgt};font-style:{st};src:url(data:font/woff2;base64,{subset_b64(fn, chars)}) format('woff2')}}"
    return s.replace("<style>", "<style>" + faces, 1)


@lru_cache(None)
def _font(fn):
    return TTFont(os.path.join(HERE, "fonts", fn))


def advances(fn, text, size):
    f = _font(fn); cm = f.getBestCmap(); hm = f["hmtx"]; upm = f["head"].unitsPerEm
    return [hm[cm[ord(c)]][0] * size / upm if ord(c) in cm else size * .6 for c in text]


# ------------------------------------------------------------------ palette + shared svg helpers
BLUE, ELEC, LIME, LIME2 = "#A8C9C8", "#8FB5B4", "#CDCBCA", "#F4F3F2"   # powder, deep powder, chrome silver, bright chrome
DUSTC = ["#fff", "#fff", BLUE, LIME]


def svg(w, h, body, defs="", css="", fade_x=.06, fade_y=0.0, mask=True):
    fx = fy = ""; o = c = ""
    if mask:
        fx = (f'<linearGradient id="fx"><stop offset="0" stop-color="#000"/><stop offset="{fade_x}" stop-color="#fff"/><stop offset="{1-fade_x}" stop-color="#fff"/><stop offset="1" stop-color="#000"/></linearGradient>'
              f'<mask id="mx" maskUnits="userSpaceOnUse" x="0" y="0" width="{w}" height="{h}"><rect width="{w}" height="{h}" fill="url(#fx)"/></mask>')
        o, c = '<g mask="url(#mx)">', "</g>"
        if fade_y:
            fy = (f'<linearGradient id="fy" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#000"/><stop offset="{fade_y}" stop-color="#fff"/><stop offset="{1-fade_y}" stop-color="#fff"/><stop offset="1" stop-color="#000"/></linearGradient>'
                  f'<mask id="my" maskUnits="userSpaceOnUse" x="0" y="0" width="{w}" height="{h}"><rect width="{w}" height="{h}" fill="url(#fy)"/></mask>')
            o += '<g mask="url(#my)">'; c += "</g>"
    out = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'
           f'<defs>{fx}{fy}{defs}</defs><style>{css}</style>{o}{body}{c}</svg>')
    return embed(out)


LG = (f'<linearGradient id="lg" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="1200" y2="0">'
      f'<stop offset="0" stop-color="{BLUE}" stop-opacity="0"/><stop offset=".25" stop-color="{BLUE}" stop-opacity=".9"/>'
      f'<stop offset=".5" stop-color="{ELEC}"/><stop offset=".8" stop-color="{LIME}" stop-opacity=".95"/>'
      f'<stop offset="1" stop-color="{LIME2}" stop-opacity="0"/></linearGradient>')
SPLINE = 'calcMode="spline" keyTimes="0;.33;.66;1" keySplines=".45 0 .55 1;.45 0 .55 1;.45 0 .55 1"'
EASE = 'calcMode="spline" keyTimes="0;.5;1" keySplines=".45 0 .55 1;.45 0 .55 1"'


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


# ------------------------------------------------------------------ copy (edit freely)
NAME = "NIRANJAN KRISHNAKUMAR"
TAGLINES = ["physics-informed intelligence", "vision that explains itself", "learning that stays private", "algorithms that meet hardware"]
ROWS = [  # (index, title, description, right label, link)
    ("01", "Physics-Informed MPPT", "Diode-physics features + 300-state Markov weather drive a neural tracker · R² 0.9994", "IEEE SPICES 2026", None),
    ("02", "Congestion Management", "Tri-hybrid OOA · KHA · SHO optimizer over a DC-OPF sensitivity framework", "IEEE EPREC 2026", "https://doi.org/10.1109/EPREC66546.2026.11412040"),
    ("03", "Hyperspectral Face ID", "1,200+ bands · PUMA band selection · 3D-CNN + ArcFace · SHAP / LIME / Grad-CAM++", "COMPUTER VISION", f"https://github.com/{U}/Hyperspectral-Face-Identification-XAI"),
    ("04", "Federated Text AI", "Flower + FedAvg · resource-aware clients · Fernet-encrypted LSTM next-word prediction", "PRIVATE LEARNING", f"https://github.com/{U}/Privacy-Preserving-Federated-Learning-FL-System-for-Text-Prediction"),
    ("05", "IntelliPQ", "FFT · THD · IEEE 1159 / 519 rules + 1D-CNN / BiLSTM with neuro-symbolic arbitration", "POWER QUALITY", f"https://github.com/{U}/IntelliPQ-AI-Based-Power-Quality-Monitoring-Fault-Detection"),
    ("06", "CommerceIQ", "1.5M-record ETL · star-schema warehouse · 22 quality checks · 5.35× faster queries", "DATA ENGINEERING", f"https://github.com/{U}/CommerceIQ"),
    ("··", "All repositories", "Smart glove, MRI segmentation, transmission-fault vision, formal verification and more", "GITHUB", f"https://github.com/{U}?tab=repositories"),
]
DOMAINS = [
    ("Physics-informed AI", "governing equations as features", "MPPT · DC-OPF · Markov validation"),
    ("Vision & explainability", "hyperspectral · 3D-CNN · ArcFace", "SHAP · LIME · Grad-CAM++"),
    ("Private learning", "federated LSTM · Flower · FedAvg", "encrypted, resource-aware clients"),
    ("Power & embedded", "power quality · EV · BMS · SCADA", "ESP32 · STM32 · edge AI"),
]


# ------------------------------------------------------------------ hero
def hero():
    W, H = 1200, 520
    blobs = ""
    for cx, cy, rx, ry, col, op, tx, ty, dur in [(280, 120, 330, 85, "#6E9593", .34, 160, 30, 19), (760, 150, 360, 95, "#3A4B4A", .55, -170, 20, 23),
                                                 (1000, 100, 260, 70, BLUE, .22, -120, 40, 17), (560, 190, 300, 60, LIME, .09, 100, -20, 21)]:
        blobs += (f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{col}" opacity="{op}"><animateTransform attributeName="transform" type="translate" '
                  f'values="0 0;{tx} {ty};0 0" dur="{dur}s" repeatCount="indefinite" {EASE}/></ellipse>')
    dust = ""
    for _ in range(34):
        x, y, r = random.randint(30, 1170), random.randint(30, 400), round(random.uniform(.6, 1.5), 1)
        d, b = random.uniform(4, 9), random.uniform(0, 8)
        dust += (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{random.choice(DUSTC)}" opacity=".1"><animate attributeName="opacity" values=".08;.7;.08" dur="{d:.1f}s" begin="-{b:.1f}s" repeatCount="indefinite"/>'
                 f'<animateTransform attributeName="transform" type="translate" values="0 0;{random.randint(-18,18)} {random.randint(-24,-6)};0 0" dur="{d*2:.1f}s" repeatCount="indefinite"/></circle>')
    # name: every letter placed from real font metrics, then rises in with a stagger
    size, track, y = 66, 5.5, 238
    adv = advances(FONTS["NK Sans"][800], NAME, size)
    x = 600 - (sum(adv) + track * (len(NAME) - 1)) / 2
    letters = ""
    for i, (c, a) in enumerate(zip(NAME, adv)):
        cx = x + a / 2; x += a + track
        if c != " ":
            letters += f'<text class="ch" style="animation-delay:{.25 + i*.04:.2f}s;{SANS}" x="{cx:.1f}" y="{y}" text-anchor="middle" font-size="{size}" font-weight="800" fill="#FFFFFF">{c}</text>'
    tl = "".join(f'<text class="tg" style="animation-delay:{i*4}s;{TAGLINE}" x="600" y="316" text-anchor="middle" font-size="28" font-weight="400" letter-spacing="1.2" fill="{BLUE}">{E(t)}</text>' for i, t in enumerate(TAGLINES))
    defs = (LG + f'<linearGradient id="bm"><stop offset="0" stop-color="{LIME}" stop-opacity="0"/><stop offset=".5" stop-color="{LIME}"/><stop offset="1" stop-color="{LIME}" stop-opacity="0"/></linearGradient>'
            '<filter id="bl" x="-30%" y="-100%" width="160%" height="300%"><feGaussianBlur stdDeviation="55"/></filter>'
            '<filter id="bl2" x="-5%" y="-50%" width="110%" height="200%"><feGaussianBlur stdDeviation="5"/></filter>')
    css = (".ch{animation:rise 1.2s cubic-bezier(.2,.8,.2,1) backwards}.sm{animation:rise 2s .8s cubic-bezier(.2,.8,.2,1) backwards}"
           "@keyframes rise{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:none}}"
           ".tg{opacity:0;animation:cy 16s infinite}@keyframes cy{0%{opacity:0;transform:translateY(10px)}7%,22%{opacity:1;transform:none}29%,100%{opacity:0;transform:translateY(-8px)}}")
    body = (f'<rect width="{W}" height="{H}" fill="#080808"/><g filter="url(#bl)">{blobs}</g>{dust}'
            f'<g id="wv">{waves(16, 350, 9, 26)}</g><use href="#wv" filter="url(#bl2)" opacity=".7"/>'
            f'<rect y="330" width="260" height="190" fill="url(#bm)" opacity=".13"><animateTransform attributeName="transform" type="translate" values="-300 0;1300 0" dur="11s" repeatCount="indefinite"/></rect>'
            f'<text class="sm" x="600" y="148" text-anchor="middle" style="{MONO}" font-size="12" letter-spacing="6" fill="#888894">ELECTRICAL &amp; COMPUTER ENGINEERING · B.TECH 2027</text>'
            f'<g>{letters}</g>'
            f'<path d="M420 270H780" stroke="url(#lg)" stroke-width="1.5" stroke-dasharray="360" stroke-dashoffset="360"><animate attributeName="stroke-dashoffset" from="360" to="0" dur="1.8s" begin="1.4s" fill="freeze"/></path>{tl}')
    return svg(W, H, body, defs, css, fade_x=.08, fade_y=.12)


# ------------------------------------------------------------------ pill buttons
def pill(label, accent=False, delay=0):
    h = 46; r = h / 2; w = round(len(label) * 11.4 + 78)
    col = LIME if accent else BLUE
    path = f"M{r} 1H{w-r}A{r-1} {r-1} 0 0 1 {w-r} {h-1}H{r}A{r-1} {r-1} 0 0 1 {r} 1Z"
    defs = (f'<linearGradient id="pg" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="{w}" y2="0"><stop offset="0" stop-color="{BLUE}"/><stop offset="1" stop-color="{LIME}"/></linearGradient>'
            '<filter id="pf" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3"/></filter>')
    body = (f'<path d="{path}" fill="#0C0D0E" fill-opacity=".75" stroke="{col}" stroke-opacity=".38"/>'
            f'<g><animateMotion dur="6s" begin="{delay}s" repeatCount="indefinite" path="{path}"/><circle r="6" fill="{col}" opacity=".6" filter="url(#pf)"/><circle r="2.4" fill="#fff"/></g>'
            f'<text x="{w/2 - 8}" y="28.5" text-anchor="middle" style="{MONO}" font-size="12" letter-spacing="3" fill="#F4F4F5">{E(label)}</text>'
            f'<text x="{w - 28}" y="29" text-anchor="middle" style="{MONO}" font-size="13" fill="{col}">↗</text>')
    return svg(w, h, body, defs, mask=False)


# ------------------------------------------------------------------ pipeline: equations -> intelligence -> silicon
def pipeline():
    W, H = 1200, 390
    X0, Y0, PW, PH = 70, 250, 250, 165
    states = [(1.0, .95), (.60, .80), (.82, .90)]
    ds, fs, peaks = [], [], []
    for s, vx in states:
        pts, best = [], (0, 0, -1)
        for k in range(61):
            v = k / 60
            p = s * v * (1 - v ** 9) / .697
            x, y = X0 + v * vx * PW, Y0 - p * PH
            pts.append(f"{x:.1f} {y:.1f}")
            if Y0 - y > best[2]: best = (x, y, Y0 - y)
        ds.append("M" + " L".join(pts)); fs.append("M" + " L".join(pts) + f" L{X0 + vx*PW:.1f} {Y0} L{X0} {Y0}Z"); peaks.append(best)
    def cyc(seq): return ";".join(str(round(v, 1)) for v in [*seq, seq[0]])
    dv = lambda a: ";".join([a[0], a[1], a[2], a[0]])
    defs = (LG + f'<linearGradient id="cv" gradientUnits="userSpaceOnUse" x1="{X0}" y1="0" x2="{X0+PW}" y2="0"><stop offset="0" stop-color="{BLUE}"/><stop offset="1" stop-color="{LIME}"/></linearGradient>'
            '<filter id="pf" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="3"/></filter>')
    css = ".fl{animation:fl 1.4s linear infinite}@keyframes fl{to{stroke-dashoffset:-28}}"
    b = f'<text x="600" y="36" text-anchor="middle" style="{MONO}" font-size="11" letter-spacing="8" fill="#6B6B75">FROM EQUATIONS TO SILICON</text>'
    # stage 1 · physics
    b += ''.join(f'<path d="M{X0} {Y0 - g*41}H{X0+PW}" stroke="#1D2022" stroke-dasharray="2 6"/>' for g in (1, 2, 3))
    b += f'<path d="M{X0} {Y0}H{X0+PW+14}M{X0} {Y0}V{Y0-PH-18}" stroke="#3A3E40" stroke-width="1.4"/>'
    b += f'<text x="{X0+PW+16}" y="{Y0+16}" style="{MONO}" font-size="11" fill="#6B6B75">V</text><text x="{X0-18}" y="{Y0-PH-14}" style="{MONO}" font-size="11" fill="#6B6B75">P</text>'
    b += (f'<path d="{fs[0]}" fill="{BLUE}" opacity=".07"><animate attributeName="d" values="{dv(fs)}" dur="9s" repeatCount="indefinite" {SPLINE}/></path>'
          f'<path d="{ds[0]}" fill="none" stroke="url(#cv)" stroke-width="2.2" stroke-linecap="round"><animate attributeName="d" values="{dv(ds)}" dur="9s" repeatCount="indefinite" {SPLINE}/></path>')
    px, py = [p[0] for p in peaks], [p[1] for p in peaks]
    anim = lambda attr, seq: f'<animate attributeName="{attr}" values="{cyc(seq)}" dur="9s" repeatCount="indefinite" {SPLINE}/>'
    b += (f'<line x1="{px[0]:.1f}" x2="{px[0]:.1f}" y1="{py[0]:.1f}" y2="{Y0}" stroke="{LIME}" stroke-opacity=".5" stroke-dasharray="3 4">{anim("x1", px)}{anim("x2", px)}{anim("y1", py)}</line>'
          f'<circle cx="{px[0]:.1f}" cy="{py[0]:.1f}" r="11" fill="{LIME}" opacity=".35" filter="url(#pf)">{anim("cx", px)}{anim("cy", py)}</circle>'
          f'<circle cx="{px[0]:.1f}" cy="{py[0]:.1f}" r="4.5" fill="{LIME}">{anim("cx", px)}{anim("cy", py)}</circle>'
          f'<text x="{px[0]+12:.1f}" y="{py[0]-10:.1f}" style="{MONO}" font-size="11" font-weight="700" fill="{LIME}">MPP{anim("x", [p + 12 for p in px])}{anim("y", [p - 10 for p in py])}</text>')
    # stage 2 · intelligence
    xs, counts, cyy = [470, 550, 630, 710], [3, 5, 5, 2], 160
    pos = [[(x, cyy + (i - (n - 1) / 2) * 38) for i in range(n)] for x, n in zip(xs, counts)]
    for l in range(3):
        for (x1, y1) in pos[l]:
            for (x2, y2) in pos[l + 1]:
                b += f'<path d="M{x1} {y1:.0f}L{x2} {y2:.0f}" stroke="{BLUE}" stroke-opacity=".16"/>'
    for l in range(3):
        for k in range(5):
            (x1, y1), (x2, y2) = random.choice(pos[l]), random.choice(pos[l + 1])
            b += (f'<circle r="2.4" fill="{LIME}"><animateMotion dur="2.4s" begin="-{random.uniform(0, 2.4):.2f}s" repeatCount="indefinite" path="M{x1} {y1:.0f}L{x2} {y2:.0f}"/>'
                  f'<animate attributeName="opacity" values="0;1;1;0" dur="2.4s" begin="0s" repeatCount="indefinite"/></circle>')
    for l, layer in enumerate(pos):
        for (x, y) in layer:
            b += (f'<circle cx="{x}" cy="{y:.0f}" r="7.5" fill="#0C0D0E" stroke="{BLUE}" stroke-width="1.4"/>'
                  f'<circle cx="{x}" cy="{y:.0f}" r="3" fill="{BLUE}"><animate attributeName="fill" values="{BLUE};{LIME};{BLUE}" dur="3.2s" begin="{l*.5}s" repeatCount="indefinite"/>'
                  f'<animate attributeName="r" values="2.6;4.8;2.6" dur="3.2s" begin="{l*.5}s" repeatCount="indefinite"/></circle>')
    # stage 3 · hardware
    cx, cy2 = 1000, 160
    for k in range(3):
        y = 140 + k * 20
        b += f'<path d="M905 {y}H958" stroke="#2B2F31" stroke-width="1.5"/><circle r="2.2" fill="{LIME}"><animateMotion dur="1.8s" begin="-{k*.5}s" repeatCount="indefinite" path="M905 {y}H958"/></circle>'
    b += (f'<circle cx="{cx}" cy="{cy2}" r="88" fill="none" stroke="{LIME}" stroke-opacity=".55" stroke-dasharray="3 10"><animateTransform attributeName="transform" type="rotate" from="0 {cx} {cy2}" to="360 {cx} {cy2}" dur="26s" repeatCount="indefinite"/></circle>'
          f'<circle cx="{cx}" cy="{cy2}" r="74" fill="none" stroke="{BLUE}" stroke-opacity=".45" stroke-dasharray="1 7"><animateTransform attributeName="transform" type="rotate" from="360 {cx} {cy2}" to="0 {cx} {cy2}" dur="38s" repeatCount="indefinite"/></circle>')
    for i in range(5):
        o = 972 + i * 14
        b += f'<path d="M{o} 120v-11M{o} 200v11M960 {o-852}h-11M1040 {o-852}h11" stroke="{BLUE}" stroke-width="2" stroke-linecap="round"/>'
    b += (f'<rect x="960" y="120" width="80" height="80" rx="11" fill="#0C0D0E" stroke="{BLUE}" stroke-width="1.6"/>'
          f'<rect x="976" y="136" width="48" height="48" rx="7" fill="{BLUE}" opacity=".14" stroke="{LIME}" stroke-width="1.2"><animate attributeName="opacity" values=".12;.45;.12" dur="2.2s" repeatCount="indefinite"/></rect>'
          f'<text x="1000" y="165" text-anchor="middle" style="{MONO}" font-size="13" font-weight="700" fill="{LIME}">MCU</text>'
          f'<circle cx="1033" cy="193" r="2" fill="{LIME}"><animate attributeName="opacity" values="1;.1;1" dur="1.2s" repeatCount="indefinite"/></circle>')
    # connectors
    for x1, x2 in [(345, 448), (728, 898)]:
        b += (f'<path d="M{x1} 160H{x2-8}" class="fl" stroke="{LIME}" stroke-opacity=".8" stroke-width="1.6" stroke-dasharray="6 8"/>'
              f'<path d="M{x2-9} 154L{x2} 160L{x2-9} 166" fill="none" stroke="{LIME}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>')
    # captions
    for x, t, s1, s2 in [(195, "PHYSICS", "diode-physics features", "Markov-chain weather"), (590, "INTELLIGENCE", "ANN · CNN · LSTM", "federated · explainable"), (1000, "HARDWARE", "ESP32 · STM32 · Pi 4", "INT8 edge inference")]:
        b += (f'<text x="{x}" y="304" text-anchor="middle" style="{MONO}" font-size="12.5" font-weight="700" letter-spacing="5" fill="{LIME}">{t}</text>'
              f'<text x="{x}" y="328" text-anchor="middle" style="{MONO}" font-size="11.5" fill="#8A8A93">{s1}</text>'
              f'<text x="{x}" y="348" text-anchor="middle" style="{MONO}" font-size="11.5" fill="#55555F">{s2}</text>')
    return svg(W, H, b, defs, css, fade_x=.04)


# ------------------------------------------------------------------ dividers, rows, domains, footer
def divider(label=""):
    W, H = 1200, 70
    ds = [wave_d(35, 7, 700, j * 2.1) for j in range(3)]
    gw = len(label) * 14 + 56
    defs = LG + (f'<mask id="gp" maskUnits="userSpaceOnUse" x="0" y="0" width="{W}" height="{H}"><rect width="{W}" height="{H}" fill="#fff"/><rect x="{600 - gw/2}" y="0" width="{gw}" height="{H}" fill="#000"/></mask>' if label else "")
    txt = f'<text x="600" y="40" text-anchor="middle" style="{MONO}" font-size="11" letter-spacing="5" fill="{LIME}" opacity=".9">{E(label.upper())}</text>' if label else ""
    body = (f'<path d="{ds[0]}" fill="none" stroke="url(#lg)" stroke-width="1" opacity=".75" mask="url(#gp)"><animate attributeName="d" values="{";".join([ds[0], ds[1], ds[2], ds[0]])}" dur="14s" repeatCount="indefinite" {SPLINE}/></path>{txt}')
    return svg(W, H, body, defs, fade_x=.1)


def row(idx, title, desc, tag, last=False, delay=0):
    W, H = 1200, 122
    defs = (f'<linearGradient id="sw" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="320" y2="0"><stop offset="0" stop-color="{BLUE}" stop-opacity="0"/><stop offset=".5" stop-color="{BLUE}"/><stop offset="1" stop-color="{LIME}" stop-opacity="0"/>'
            f'<animateTransform attributeName="gradientTransform" type="translate" values="-320 0;1200 0" dur="7s" begin="{delay}s" repeatCount="indefinite"/></linearGradient>')
    line = lambda y: f'<path d="M0 {y}H1200" stroke="#26282A"/><path d="M0 {y}H1200" stroke="url(#sw)" stroke-width="1.5"/>'
    body = (f'{line(1)}{line(H-1) if last else ""}'
            f'<text x="28" y="66" style="{MONO}" font-size="13" fill="#55555F">{E(idx)}</text>'
            f'<text x="92" y="62" style="{SANS}" font-size="32" font-weight="500" letter-spacing=".3" fill="#F4F4F5">{E(title)}</text>'
            f'<text x="92" y="93" style="{MONO}" font-size="13" fill="#8A8A93">{E(desc)}</text>'
            f'<text x="1120" y="58" text-anchor="end" style="{MONO}" font-size="12" letter-spacing="3" fill="{LIME}" opacity=".92">{E(tag)}</text>'
            f'<text x="1172" y="72" text-anchor="end" style="{MONO}" font-size="24" fill="{BLUE}">→<animateTransform attributeName="transform" type="translate" values="0 0;7 0;0 0" dur="3.2s" repeatCount="indefinite" {EASE}/></text>')
    return svg(W, H, body, defs, fade_x=.04)


def domains():
    W, H = 1200, 250
    xs = [150, 450, 750, 1050]
    c1 = "M0 70 C150 40 300 100 450 70 S750 40 900 70 S1100 90 1200 60"
    c2 = "M0 60 C150 95 300 45 450 70 S750 100 900 65 S1100 40 1200 75"
    body = f'<path d="{c1}" fill="none" stroke="url(#lg)" stroke-width="1.2"><animate attributeName="d" values="{c1};{c2};{c1}" dur="12s" repeatCount="indefinite" {EASE}/></path>'
    for i, ((t, l1, l2), x) in enumerate(zip(DOMAINS, xs)):
        d = i * 1.1
        body += (f'<circle cx="{x}" cy="70" r="14" fill="none" stroke="{BLUE}"><animate attributeName="r" values="6;30;6" dur="5s" begin="{d}s" repeatCount="indefinite"/><animate attributeName="opacity" values=".7;0;.7" dur="5s" begin="{d}s" repeatCount="indefinite"/></circle>'
                 f'<circle cx="{x}" cy="70" r="4.5" fill="{LIME}"/>'
                 f'<text x="{x}" y="140" text-anchor="middle" style="{SANS}" font-size="22" font-weight="500" letter-spacing=".3" fill="#F4F4F5">{E(t)}</text>'
                 f'<text x="{x}" y="172" text-anchor="middle" style="{MONO}" font-size="12" fill="#8A8A93">{E(l1)}</text>'
                 f'<text x="{x}" y="194" text-anchor="middle" style="{MONO}" font-size="12" fill="#55555F">{E(l2)}</text>')
    return svg(W, H, body, LG, fade_x=.04)


def footer():
    W, H = 1200, 300
    body = (f'{waves(14, 150, 9, 24, op=(.08, .5))}'
            f'<text x="600" y="106" text-anchor="middle" style="{TAGLINE}" font-size="30" font-weight="400" letter-spacing=".5" fill="#EDEDF0">understand the system. engineer the intelligence.</text>'
            f'<text x="600" y="140" text-anchor="middle" style="{MONO}" font-size="11" letter-spacing="6" fill="#55555F">NIRANJAN KRISHNAKUMAR · COIMBATORE</text>')
    return svg(W, H, body, LG, fade_x=.08, fade_y=.2)


# ------------------------------------------------------------------ write assets
from toolkit import toolkit_svg

def w(name, s): open(f"{A}/{name}.svg", "w", encoding="utf-8").write(s)

_w, _h, _b, _d = toolkit_svg()
w("toolkit", svg(_w, _h, _b, _d, fade_x=.03, fade_y=.03))
w("hero", hero()); w("pipeline", pipeline()); w("domains", domains()); w("footer", footer())
w("pill-portfolio", pill("PORTFOLIO", True, 0)); w("pill-repos", pill("REPOSITORIES", False, -2)); w("pill-paper", pill("IEEE PAPER", False, -4))
for n, lab in [("d-build", "what i build"), ("d-work", "selected work"), ("d-path", "path"), ("d-kit", "toolkit")]:
    w(n, divider(lab))
for i, (idx, t, d, tag, _) in enumerate(ROWS):
    w(f"row{i+1}", row(idx, t, d, tag, last=i == len(ROWS) - 1, delay=i * .9))

# ------------------------------------------------------------------ README
im = lambda n, href=None: (f'<a href="{href}"><img src="assets/{n}.svg" width="100%"></a>' if href else f'<img src="assets/{n}.svg" width="100%">')
pl = lambda n, href: f'<a href="{href}"><img src="assets/{n}.svg" height="46"></a>'
rows = "\n".join(im(f"row{i+1}", r[4]) for i, r in enumerate(ROWS))
readme = f'''<div align="center">

{im("hero")}

{pl("pill-portfolio", SITE)}&nbsp;&nbsp;{pl("pill-repos", f"https://github.com/{U}?tab=repositories")}&nbsp;&nbsp;{pl("pill-paper", "https://doi.org/10.1109/EPREC66546.2026.11412040")}

<br><br>

<p align="center">Final-year Electrical &amp; Computer Engineering student at Amrita Vishwa Vidyapeetham, Coimbatore.<br>
I build intelligence that respects physics — from governing equations to models that run on real hardware.<br>
<sub>IEEE EPREC 2026 (published) &nbsp;·&nbsp; IEEE SPICES 2026 (accepted)</sub></p>

{im("pipeline")}

{im("d-build")}

{im("domains")}

{im("d-work")}

{rows}

{im("d-path")}

<p align="center"><b>Larsen &amp; Toubro</b> &nbsp;·&nbsp; industry internship, 2026<br>
<sub>EV powertrain simulation · PMSM / BLDC motor control · DC-DC converters · BMS architecture · CAN · railway SCADA modelling</sub></p>

<p align="center"><b>AWS Academy</b> &nbsp;·&nbsp; cloud foundations, 2026<br>
<sub>cloud architecture · compute &amp; storage · networking · security</sub></p>

{im("d-kit")}

{im("toolkit")}

<p align="center"><sub>open to research collaborations &nbsp;·&nbsp; ML roles &nbsp;·&nbsp; data engineering challenges</sub></p>

{im("footer")}

</div>
'''
open(f"{ROOT}/README.md", "w", encoding="utf-8").write(readme)
print("built", ROOT)
