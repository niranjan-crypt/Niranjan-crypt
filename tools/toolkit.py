"""Circuit-board toolkit panel (obsidian / chrome / powder blue) with official brand colours."""
import json, os
from xml.sax.saxutils import escape as E

HERE = os.path.dirname(os.path.abspath(__file__))
SI = json.load(open(os.path.join(HERE, "icons.json")))
BRAND = json.load(open(os.path.join(HERE, "brand.json")))
POWDER, CHROME, BRIGHT = "#A8C9C8", "#CDCBCA", "#F4F3F2"
EDGE, CARD, TRACE = "#2A2D2F", "#0C0D0E", "#26292B"
MONO = "font-family:'NK Mono','JetBrains Mono','SF Mono',Menlo,Consolas,monospace"

# official brand colours; a few are swapped for the brand's lighter palette colour so they stay visible on black
LIGHTER = {"github": "#F0EFEE", "pandas": "#E70488", "numpy": "#4DABCF", "stmicroelectronics": "#3CB4E6", "cplusplus": "#659AD2",
           "flutter": "#54C5F8", "raspberrypi": "#C51A4A", "opencv": "#8B73FF", "dart": "#2BB7F6", "arduino": "#00A3AD", "postgresql": "#5B84F0"}
GLYPH_COLOR = {"matlab": "#E16737", "cloud": "#FF9900", "code": "#3B9CFF"}  # brand colour where the tool has one but no icon in the open set


def brand(key):
    return LIGHTER.get(key) or "#" + BRAND[key]


# 24x24 line glyphs for tools / techniques that have no brand logo
GL = {
    "sql": '<ellipse cx="12" cy="6" rx="7" ry="3"/><path d="M5 6v12c0 1.7 3.1 3 7 3s7-1.3 7-3V6M5 12c0 1.7 3.1 3 7 3s7-1.3 7-3"/>',
    "matlab": '<path d="M2 17c3-1 4-11 7-11 2 0 2 5 4 5s2-4 4-4c1.5 0 2 4 5 10l-7 4z"/><path d="M9 6l4 15M16 7l-3 14"/>',
    "neural": '<circle cx="5" cy="6" r="1.7"/><circle cx="5" cy="12" r="1.7"/><circle cx="5" cy="18" r="1.7"/><circle cx="12" cy="8" r="1.7"/><circle cx="12" cy="16" r="1.7"/><circle cx="19" cy="12" r="1.7"/><path d="M6.5 6.5l4 1.3M6.5 11.5l4-3M6.5 12.5l4 3M6.5 17.5l4-1.3M13.5 8.5l4 3M13.5 15.5l4-3"/>',
    "lstm": '<rect x="5" y="5" width="14" height="14" rx="3.5"/><path d="M9 12h6M12 9v6M2 12h3M19 12h3"/>',
    "transfer": '<path d="M3 8h15l-3.5-3.5M21 16H6l3.5 3.5"/>',
    "forest": '<path d="M12 21v-8M12 13L7 8M12 13l5-5M7 8L4 4M7 8l3-4M17 8l-3-4M17 8l3-4"/><circle cx="4" cy="4" r="1"/><circle cx="10" cy="4" r="1"/><circle cx="14" cy="4" r="1"/><circle cx="20" cy="4" r="1"/>',
    "flower": '<circle cx="12" cy="12" r="2"/>' + "".join(f'<ellipse cx="12" cy="6.2" rx="2.4" ry="3.6" transform="rotate({a} 12 12)"/>' for a in range(0, 360, 60)),
    "etl": '<path d="M3 7h8M3 12h8M3 17h8"/><path d="M14 6l6 6-6 6z"/>',
    "prism": '<path d="M12 3l8 14H4z"/><path d="M1 13h6M16 9l7-3M17 13h6M16 16l7 3"/>',
    "cube": '<path d="M12 3l8 4.5v9L12 21l-8-4.5v-9z"/><path d="M12 12l8-4.5M12 12L4 7.5M12 12v9"/>',
    "face": '<path d="M3 8V4h4M17 4h4v4M21 16v4h-4M7 20H3v-4"/><circle cx="12" cy="12" r="4.5"/><path d="M10.3 11.2v.6M13.7 11.2v.6M10.3 14c1 .9 2.4.9 3.4 0"/>',
    "heat": '<rect x="3" y="3" width="18" height="18" rx="3.5"/><circle cx="12" cy="12" r="3"/><circle cx="12" cy="12" r="6" stroke-dasharray="2 2.2"/>',
    "bars": '<path d="M4 20V12M9 20V5M14 20V9M19 20V3"/>',
    "texture": '<path d="M4 4h16v16H4zM4 9.3h16M4 14.6h16M9.3 4v16M14.6 4v16"/>',
    "hough": '<circle cx="12" cy="12" r="7"/><path d="M12 2v6M12 16v6M2 12h6M16 12h6"/>',
    "swarm": '<circle cx="5" cy="17" r="1.2"/><circle cx="9" cy="8" r="1.2"/><circle cx="13" cy="15" r="1.2"/><circle cx="7" cy="12.5" r="1.2"/><circle cx="17" cy="7" r="2.6"/><path d="M5 17l11-9M9 8l6-1M13 15l4-6"/>',
    "dna": '<path d="M8 3c0 5 8 5 8 9s-8 4-8 9M16 3c0 5-8 5-8 9s8 4 8 9"/><path d="M9.2 6.5h5.6M9.2 17.5h5.6"/>',
    "fish": '<path d="M2.5 12c3-5.5 9.5-5.5 13.5 0-4 5.5-10.500 5.5-13.5 0zM16 12l5.500-4.500v9z"/><circle cx="7.500" cy="11" r=".8"/>',
    "sliders": '<path d="M4 7h16M4 12h16M4 17h16"/><circle cx="9" cy="7" r="2"/><circle cx="15" cy="12" r="2"/><circle cx="8" cy="17" r="2"/>',
    "markov": '<circle cx="5" cy="12" r="2.6"/><circle cx="19" cy="5.500" r="2.6"/><circle cx="19" cy="18.500" r="2.6"/><path d="M7.300 10.800l9.400-4M7.300 13.200l9.400 4M19 8.300v7.400"/>',
    "otsu": '<path d="M2 20c3.500 0 3-13 6.500-13S12 20 14 20M13 20c2 0 2-7 4-7s2 7 5 7"/><path d="M11.500 3v18" stroke-dasharray="2 2.200"/>',
    "grid": '<circle cx="5" cy="6" r="2"/><circle cx="19" cy="6" r="2"/><circle cx="12" cy="19" r="2"/><path d="M7 6h10M6.200 7.800l4.800 9.400M17.800 7.800l-4.800 9.400"/>',
    "automata": '<circle cx="7" cy="12" r="4.200"/><circle cx="7" cy="12" r="2"/><path d="M11.200 12H17M15 9.800L17.200 12 15 14.200"/><circle cx="20" cy="12" r="1.600"/>',
    "chip": '<rect x="6" y="6" width="12" height="12" rx="2"/><path d="M9 3v3M15 3v3M9 18v3M15 18v3M3 9h3M3 15h3M18 9h3M18 15h3M10 12h4"/>',
    "ppg": '<path d="M2 12h5l2.200-6 4 12 2.200-6H22"/>',
    "can": '<path d="M3 9h18M3 15h18M7 9V5M12 9V5M17 9V5M7 15v4M12 15v4M17 15v4"/>',
    "solar": '<circle cx="12" cy="7" r="3"/><path d="M12 1.500v1M5.500 7h-1M19.500 7h-1"/><path d="M5 21l2-7h10l2 7zM12 14v7"/>',
    "fft": '<path d="M3 20h18M6 20v-6M10 20V5M14 20v-9M18 20v-4"/>',
    "sine": '<path d="M2 12c3-9 5-9 8 0s5 9 8 0 2-3 4-3"/><path d="M2 7h20" stroke-dasharray="2 2.200"/>',
    "dsp": '<path d="M3 18h5c3.500 0 3-12 7-12h6"/><path d="M3 21h18" stroke-dasharray="1 3"/>',
    "motor": '<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="2.500"/><path d="M12 4v5.500M12 14.500V20M4 12h5.500M14.500 12H20"/>',
    "battery": '<rect x="3" y="7" width="16" height="10" rx="2"/><path d="M21 10v4M7 10v4M11 10v4"/>',
    "coil": '<path d="M2 15h3c0-6 4-6 4 0 0-6 4-6 4 0 0-6 4-6 4 0h5"/>',
    "scada": '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4M6 13l3-3 3 2 4-4"/>',
    "cloud": '<path d="M7 18a4 4 0 0 1-.5-8A6 6 0 0 1 18 9.500 4.200 4.200 0 0 1 17.500 18z"/>',
    "code": '<path d="M8 6l-6 6 6 6M16 6l6 6-6 6M13.500 4l-3 16"/>',
    "cicd": '<path d="M4 12a8 8 0 0 1 14-5l2 2M20 12a8 8 0 0 1-14 5l-2-2"/><path d="M20 4v5h-5M4 20v-5h5"/>',
    "lock": '<rect x="5" y="11" width="14" height="10" rx="2.500"/><path d="M8 11V8a4 4 0 0 1 8 0v3M12 15v2"/>',
}
# (label, 'si'|'gl', key)
ROWS = [
    ("LANGUAGES", [("Python", "si", "python"), ("C++", "si", "cplusplus"), ("C", "si", "c"), ("MATLAB", "gl", "matlab"), ("Bash", "si", "gnubash"), ("Dart", "si", "dart"), ("SQL", "gl", "sql")]),
    ("MACHINE LEARNING", [("PyTorch", "si", "pytorch"), ("TensorFlow", "si", "tensorflow"), ("scikit-learn", "si", "scikitlearn"), ("ANN·CNN", "gl", "neural"), ("LSTM·BiLSTM", "gl", "lstm"), ("Transfer", "gl", "transfer"), ("Random Forest", "gl", "forest"), ("Flower·FedAvg", "gl", "flower")]),
    ("DATA ENGINEERING", [("PostgreSQL", "si", "postgresql"), ("MySQL", "si", "mysql"), ("Pandas", "si", "pandas"), ("NumPy", "si", "numpy"), ("Plotly", "si", "plotly"), ("Streamlit", "si", "streamlit"), ("Docker", "si", "docker"), ("ETL·ELT", "gl", "etl")]),
    ("VISION & XAI", [("OpenCV", "si", "opencv"), ("Hyperspectral", "gl", "prism"), ("3D-CNN", "gl", "cube"), ("ArcFace", "gl", "face"), ("Grad-CAM++", "gl", "heat"), ("SHAP·LIME", "gl", "bars"), ("HOG·GLCM", "gl", "texture"), ("Hough", "gl", "hough")]),
    ("OPTIMIZATION", [("PSO", "gl", "swarm"), ("GA", "gl", "dna"), ("OOA·KHA·SHO", "gl", "fish"), ("PUMA", "gl", "sliders"), ("Markov", "gl", "markov"), ("Otsu", "gl", "otsu"), ("DC-OPF·PTDF", "gl", "grid"), ("Automata·CFG", "gl", "automata")]),
    ("EMBEDDED", [("ESP32", "si", "espressif"), ("STM32", "si", "stmicroelectronics"), ("Arduino", "si", "arduino"), ("Raspberry Pi", "si", "raspberrypi"), ("BLE 5.0", "si", "bluetooth"), ("Edge AI·INT8", "gl", "chip"), ("PPG", "gl", "ppg"), ("CAN bus", "gl", "can")]),
    ("POWER & SIGNALS", [("MPPT", "gl", "solar"), ("FFT", "gl", "fft"), ("THD·RMS", "gl", "sine"), ("DSP", "gl", "dsp"), ("PMSM·BLDC", "gl", "motor"), ("BMS", "gl", "battery"), ("DC-DC", "gl", "coil"), ("SCADA", "gl", "scada")]),
    ("CLOUD & TOOLS", [("AWS", "gl", "cloud"), ("Git", "si", "git"), ("GitHub", "si", "github"), ("Linux", "si", "linux"), ("VS Code", "gl", "code"), ("CI/CD", "gl", "cicd"), ("Flutter", "si", "flutter"), ("Fernet·PBKDF2", "gl", "lock")]),
]


def toolkit_svg():
    W, PITCH, XP, X0, SPINE, XEND, CYCLE, TRAVEL = 1200, 112, 116, 292, 222, 1180, 8.0, 7.0
    cy0, T, IC = 64, 34, 1.5          # first row y, tile half-size, icon scale (24px glyph -> 36px)
    H = cy0 + (len(ROWS) - 1) * PITCH + 96
    cyN = cy0 + (len(ROWS) - 1) * PITCH
    defs = (f'<pattern id="dp" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="1" fill="{CHROME}" opacity=".08"/></pattern>'
            '<linearGradient id="py" x1="0" y1="0" x2="1" y2="1"><stop offset=".5" stop-color="#4B8BBE"/><stop offset=".5" stop-color="#FFD43B"/></linearGradient>'
            f'<linearGradient id="chr" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{BRIGHT}"/><stop offset=".5" stop-color="{CHROME}"/><stop offset="1" stop-color="#8E8D8C"/></linearGradient>')
    body = (f'<rect width="{W}" height="{H}" fill="url(#dp)"/>'
            f'<path d="M{SPINE} {cy0}V{cyN}" stroke="{TRACE}" stroke-width="1.6"/>'
            f'<g><animateMotion dur="{CYCLE}s" repeatCount="indefinite" path="M{SPINE} {cy0}V{cyN}" keyPoints="0;1;1" keyTimes="0;.7;1" calcMode="linear"/>'
            f'<circle r="9" fill="{POWDER}" opacity=".22"/><circle r="3" fill="{BRIGHT}"/></g>')
    for r, (name, items) in enumerate(ROWS):
        cy, delay = cy0 + r * PITCH, round(r * .7, 2)
        body += (f'<path d="M{SPINE} {cy}H{XEND}" stroke="{TRACE}" stroke-width="1.6"/>'
                 f'<circle cx="{SPINE}" cy="{cy}" r="4.2" fill="{CARD}" stroke="{POWDER}" stroke-width="1.6"/>'
                 f'<circle cx="{XEND}" cy="{cy}" r="3.6" fill="{CARD}" stroke="{EDGE}" stroke-width="1.6"/>'
                 f'<text x="22" y="{cy-3}" style="{MONO}" font-size="12.5" font-weight="700" letter-spacing="2.5" fill="url(#chr)">{E(name)}</text>'
                 f'<text x="22" y="{cy+17}" style="{MONO}" font-size="11" letter-spacing="2" fill="#5F5E5D">{len(items):02d} TOOLS</text>'
                 f'<g opacity="0"><animateMotion dur="{CYCLE}s" begin="{delay}s" repeatCount="indefinite" path="M{SPINE} {cy}H{XEND}" keyPoints="0;1;1" keyTimes="0;.875;1" calcMode="linear"/>'
                 f'<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;.86;.875;1" dur="{CYCLE}s" begin="{delay}s" repeatCount="indefinite"/>'
                 f'<circle r="12" fill="{POWDER}" opacity=".2"/><circle r="3.6" fill="{BRIGHT}"/></g>')
        for j, (label, kind, key) in enumerate(items):
            cx = X0 + j * XP
            f = TRAVEL * (cx - SPINE) / (XEND - SPINE) / CYCLE
            kt = f'0;{f-.045:.3f};{f:.3f};{f+.11:.3f};1'
            anim = lambda attr, a, b: f'<animate attributeName="{attr}" values="{a};{a};{b};{a};{a}" keyTimes="{kt}" dur="{CYCLE}s" begin="{delay}s" repeatCount="indefinite"/>'
            pop = f'<animateTransform attributeName="transform" type="scale" values="1 1;1 1;1.14 1.14;1 1;1 1" keyTimes="{kt}" dur="{CYCLE}s" begin="{delay}s" repeatCount="indefinite"/>'
            if kind == "si":
                col = "url(#py)" if key == "python" else brand(key)
                icon = f'<g transform="translate({-12*IC},{-12*IC}) scale({IC})" fill="{col}"><path d="{SI[key]}"/></g>'
            else:
                col = GLYPH_COLOR.get(key, POWDER)
                icon = f'<g transform="translate({-12*IC},{-12*IC}) scale({IC})" fill="none" stroke="{col}" stroke-width="1.45" stroke-linecap="round" stroke-linejoin="round">{GL[key]}</g>'
            body += (f'<rect x="{cx-T}" y="{cy-T}" width="{2*T}" height="{2*T}" rx="17" fill="{CARD}" stroke="{EDGE}" stroke-width="1.3">{anim("stroke", EDGE, POWDER)}</rect>'
                     f'<rect x="{cx-T}" y="{cy-T}" width="{2*T}" height="{2*T}" rx="17" fill="{POWDER}" opacity="0"><animate attributeName="opacity" values="0;0;.14;0;0" keyTimes="{kt}" dur="{CYCLE}s" begin="{delay}s" repeatCount="indefinite"/></rect>'
                     f'<g transform="translate({cx},{cy})"><g>{pop}{icon}</g></g>'
                     f'<text x="{cx}" y="{cy+T+19}" text-anchor="middle" style="{MONO}" font-size="12.5" fill="#A3A2A1">{E(label)}</text>')
    return W, H, body, defs
