<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Niranjan Krishnakumar | Cyber-Physical & Deep Learning Research</title>
  <meta name="description" content="Portfolio of Niranjan Krishnakumar — Electrical & Computer Engineer specializing in Hyperspectral 3D-CNNs, Cyber-Physical Digital Twins, PINNs, and Mathematical Optimization." />

  <!-- Google Fonts: Space Grotesk, Inter, and Fira Code -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;600;700;800&display=swap" rel="stylesheet" />

  <!-- Three.js from CDN -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

  <style>
    /* ==========================================================================
       1. GLOBAL RESET & FUTURISTIC THEME VARIABLES
       ========================================================================== */
    :root {
      --bg-void: #050811;
      --bg-surface: #0a0f1d;
      --bg-card: rgba(14, 22, 41, 0.75);
      --bg-card-hover: rgba(20, 32, 60, 0.85);
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-accent: rgba(0, 242, 254, 0.35);
      --border-accent-glow: rgba(0, 242, 254, 0.6);
      --text-main: #f1f5f9;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --cyan-bright: #00f2fe;
      --cyan-glow: #06b6d4;
      --emerald-neon: #10b981;
      --indigo-glow: #6366f1;
      --font-display: 'Space Grotesk', -apple-system, sans-serif;
      --font-body: 'Inter', -apple-system, sans-serif;
      --font-mono: 'Fira Code', monospace;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html {
      scroll-behavior: smooth;
      background-color: var(--bg-void);
      color: var(--text-main);
      font-family: var(--font-body);
      overflow-x: hidden;
    }

    body {
      position: relative;
      background: radial-gradient(circle at 50% 0%, #0d162d 0%, #050811 70%);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      cursor: default;
    }

    /* Selection */
    ::selection {
      background: var(--cyan-bright);
      color: #050811;
    }

    /* Custom Scrollbar */
    ::-webkit-scrollbar {
      width: 6px;
    }
    ::-webkit-scrollbar-track {
      background: var(--bg-void);
    }
    ::-webkit-scrollbar-thumb {
      background: rgba(0, 242, 254, 0.25);
      border-radius: 3px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: var(--cyan-bright);
    }

    /* Custom Cursor */
    .cursor-dot {
      width: 8px;
      height: 8px;
      background-color: var(--cyan-bright);
      position: fixed;
      top: 0;
      left: 0;
      border-radius: 50%;
      pointer-events: none;
      z-index: 9999;
      transform: translate(-50%, -50%);
      transition: transform 0.1s ease-out;
      box-shadow: 0 0 12px var(--cyan-bright);
    }
    .cursor-outline {
      width: 32px;
      height: 32px;
      border: 1.5px solid rgba(0, 242, 254, 0.4);
      position: fixed;
      top: 0;
      left: 0;
      border-radius: 50%;
      pointer-events: none;
      z-index: 9998;
      transform: translate(-50%, -50%);
      transition: transform 0.15s ease-out, width 0.2s, height 0.2s, border-color 0.2s;
    }
    body:hover .cursor-dot { opacity: 1; }

    /* ==========================================================================
       2. THREE.JS 3D CANVAS BACKGROUND
       ========================================================================== */
    #canvas3d {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: 0;
      pointer-events: none;
      opacity: 0.75;
    }

    .grid-overlay {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: 1;
      pointer-events: none;
      background-image: 
        linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
      background-size: 64px 64px;
      mask-image: radial-gradient(ellipse at 50% 50%, rgba(0,0,0,0.8) 0%, transparent 80%);
    }

    /* ==========================================================================
       3. NAVIGATION BAR
       ========================================================================== */
    .nav-container {
      position: fixed;
      top: 1.5rem;
      left: 50%;
      transform: translateX(-50%);
      z-index: 100;
      width: 90%;
      max-width: 1100px;
    }
    .nav-glass {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0.75rem 1.75rem;
      background: rgba(10, 15, 29, 0.75);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid var(--border-subtle);
      border-radius: 9999px;
      box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.7);
    }
    .nav-brand {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      font-family: var(--font-display);
      font-weight: 700;
      font-size: 1.05rem;
      letter-spacing: -0.02em;
      color: var(--text-main);
      text-decoration: none;
    }
    .nav-brand-dot {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: var(--cyan-bright);
      box-shadow: 0 0 10px var(--cyan-bright);
      animation: pulse 2s infinite ease-in-out;
    }
    @keyframes pulse {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.4; transform: scale(0.85); }
    }
    .nav-links {
      display: flex;
      align-items: center;
      gap: 1.5rem;
      list-style: none;
    }
    .nav-link {
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.85rem;
      font-weight: 500;
      transition: color 0.2s, text-shadow 0.2s;
    }
    .nav-link:hover {
      color: var(--cyan-bright);
      text-shadow: 0 0 8px rgba(0, 242, 254, 0.5);
    }
    .nav-badge-btn {
      font-family: var(--font-mono);
      font-size: 0.75rem;
      padding: 0.4rem 0.9rem;
      border-radius: 9999px;
      background: rgba(0, 242, 254, 0.08);
      border: 1px solid var(--border-accent);
      color: var(--cyan-bright);
      text-decoration: none;
      transition: all 0.2s;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
    }
    .nav-badge-btn:hover {
      background: var(--cyan-bright);
      color: #050811;
      box-shadow: 0 0 15px rgba(0, 242, 254, 0.4);
    }

    /* ==========================================================================
       4. MAIN WRAPPER & SECTIONS LAYOUT
       ========================================================================== */
    main {
      position: relative;
      z-index: 2;
      width: 100%;
      max-width: 1240px;
      margin: 0 auto;
      padding: 0 1.5rem;
    }

    section {
      padding: 6rem 0;
    }

    .section-eyebrow {
      font-family: var(--font-mono);
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.15em;
      color: var(--cyan-bright);
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }
    .section-eyebrow::before {
      content: "";
      display: inline-block;
      width: 18px;
      height: 2px;
      background: var(--cyan-bright);
    }

    .section-title {
      font-family: var(--font-display);
      font-size: clamp(2rem, 4vw, 3.2rem);
      font-weight: 700;
      letter-spacing: -0.03em;
      line-height: 1.15;
      margin-bottom: 1.5rem;
      color: #ffffff;
    }

    .section-title span.glow {
      background: linear-gradient(135deg, #00f2fe 0%, #10b981 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .section-desc {
      color: var(--text-muted);
      font-size: 1.05rem;
      max-width: 750px;
      margin-bottom: 3rem;
      line-height: 1.7;
    }

    /* ==========================================================================
       5. HERO SECTION
       ========================================================================== */
    .hero-section {
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      padding-top: 8rem;
      padding-bottom: 4rem;
    }

    .status-pill {
      display: inline-flex;
      align-items: center;
      gap: 0.6rem;
      background: rgba(16, 185, 129, 0.08);
      border: 1px solid rgba(16, 185, 129, 0.3);
      padding: 0.35rem 0.9rem;
      border-radius: 9999px;
      font-family: var(--font-mono);
      font-size: 0.75rem;
      color: #34d399;
      margin-bottom: 2rem;
      width: fit-content;
      backdrop-filter: blur(8px);
    }
    .status-dot-inner {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: #10b981;
      box-shadow: 0 0 8px #10b981;
    }

    .hero-name {
      font-family: var(--font-display);
      font-size: clamp(2.8rem, 7.5vw, 6.2rem);
      font-weight: 800;
      letter-spacing: -0.04em;
      line-height: 1.02;
      margin-bottom: 1.25rem;
      text-transform: uppercase;
      background: linear-gradient(180deg, #ffffff 40%, rgba(255, 255, 255, 0.5) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .hero-typing-box {
      font-family: var(--font-mono);
      font-size: clamp(1rem, 2.2vw, 1.45rem);
      color: var(--cyan-bright);
      margin-bottom: 2rem;
      min-height: 2.2rem;
      display: flex;
      align-items: center;
    }
    .cursor-blink {
      display: inline-block;
      width: 2px;
      height: 1.3em;
      background-color: var(--cyan-bright);
      margin-left: 4px;
      animation: blink 0.8s infinite;
    }
    @keyframes blink {
      0%, 100% { opacity: 1; }
      50% { opacity: 0; }
    }

    .hero-manifesto {
      font-size: clamp(1.05rem, 1.5vw, 1.2rem);
      color: var(--text-muted);
      max-width: 820px;
      line-height: 1.75;
      margin-bottom: 2.5rem;
      border-left: 2px solid var(--border-accent);
      padding-left: 1.5rem;
    }

    .hero-actions {
      display: flex;
      flex-wrap: wrap;
      gap: 1.25rem;
      align-items: center;
      margin-bottom: 4rem;
    }

    .btn-primary {
      font-family: var(--font-mono);
      font-size: 0.9rem;
      font-weight: 600;
      color: #050811;
      background: var(--cyan-bright);
      border: none;
      padding: 0.9rem 1.8rem;
      border-radius: 8px;
      text-decoration: none;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.6rem;
      box-shadow: 0 0 25px rgba(0, 242, 254, 0.4);
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .btn-primary:hover {
      transform: translateY(-2px);
      box-shadow: 0 0 35px rgba(0, 242, 254, 0.7);
      background: #38bdf8;
    }

    .btn-secondary {
      font-family: var(--font-mono);
      font-size: 0.9rem;
      color: var(--text-main);
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-subtle);
      padding: 0.9rem 1.8rem;
      border-radius: 8px;
      text-decoration: none;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.6rem;
      transition: all 0.25s;
    }
    .btn-secondary:hover {
      background: rgba(255, 255, 255, 0.08);
      border-color: var(--border-accent);
      color: var(--cyan-bright);
    }

    /* Live Telemetry Ticker */
    .telemetry-strip {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 1rem;
      padding-top: 2rem;
      border-top: 1px solid var(--border-subtle);
    }
    .telemetry-item {
      display: flex;
      flex-direction: column;
      gap: 0.25rem;
    }
    .telemetry-num {
      font-family: var(--font-display);
      font-size: 1.85rem;
      font-weight: 700;
      color: #ffffff;
      letter-spacing: -0.02em;
    }
    .telemetry-label {
      font-family: var(--font-mono);
      font-size: 0.75rem;
      color: var(--text-dim);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    /* ==========================================================================
       6. INTERACTIVE TECHNICAL DOMAINS
       ========================================================================== */
    .domains-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(270px, 1fr));
      gap: 1.5rem;
      margin-top: 2rem;
    }
    .domain-card {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 14px;
      padding: 2rem;
      position: relative;
      overflow: hidden;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      backdrop-filter: blur(12px);
      cursor: pointer;
    }
    .domain-card::before {
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 3px;
      background: linear-gradient(90deg, transparent, var(--cyan-bright), transparent);
      opacity: 0;
      transition: opacity 0.3s;
    }
    .domain-card:hover {
      transform: translateY(-5px);
      border-color: var(--border-accent);
      background: var(--bg-card-hover);
      box-shadow: 0 15px 35px -10px rgba(0, 242, 254, 0.15);
    }
    .domain-card:hover::before {
      opacity: 1;
    }
    .domain-icon {
      width: 48px;
      height: 48px;
      border-radius: 10px;
      background: rgba(0, 242, 254, 0.08);
      border: 1px solid rgba(0, 242, 254, 0.2);
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 1.5rem;
      color: var(--cyan-bright);
    }
    .domain-title {
      font-family: var(--font-display);
      font-size: 1.25rem;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 0.75rem;
    }
    .domain-desc {
      color: var(--text-muted);
      font-size: 0.9rem;
      line-height: 1.6;
      margin-bottom: 1.25rem;
    }
    .domain-tags {
      display: flex;
      flex-wrap: wrap;
      gap: 0.4rem;
    }
    .domain-tag {
      font-family: var(--font-mono);
      font-size: 0.7rem;
      padding: 0.25rem 0.6rem;
      border-radius: 4px;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--border-subtle);
      color: var(--text-dim);
    }

    /* ==========================================================================
       7. SELECTED FLAGSHIP PROJECTS
       ========================================================================== */
    .filter-bar {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      margin-bottom: 2.5rem;
    }
    .filter-btn {
      font-family: var(--font-mono);
      font-size: 0.8rem;
      padding: 0.5rem 1rem;
      border-radius: 6px;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.2s;
    }
    .filter-btn.active, .filter-btn:hover {
      background: rgba(0, 242, 254, 0.1);
      border-color: var(--cyan-bright);
      color: var(--cyan-bright);
    }

    .projects-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
      gap: 2rem;
    }
    .project-card {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 16px;
      padding: 2.25rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
      overflow: hidden;
    }
    .project-card:hover {
      border-color: var(--border-accent);
      transform: translateY(-4px);
      box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.7);
    }
    .project-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 1.25rem;
    }
    .project-badge {
      font-family: var(--font-mono);
      font-size: 0.7rem;
      padding: 0.3rem 0.7rem;
      border-radius: 9999px;
      background: rgba(0, 242, 254, 0.08);
      border: 1px solid rgba(0, 242, 254, 0.25);
      color: var(--cyan-bright);
    }
    .project-index {
      font-family: var(--font-mono);
      font-size: 0.75rem;
      color: var(--text-dim);
    }
    .project-title {
      font-family: var(--font-display);
      font-size: 1.4rem;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 0.9rem;
      line-height: 1.3;
    }
    .project-desc {
      color: var(--text-muted);
      font-size: 0.92rem;
      line-height: 1.65;
      margin-bottom: 1.5rem;
      flex-grow: 1;
    }
    .project-math {
      background: rgba(0, 0, 0, 0.4);
      border: 1px dashed var(--border-subtle);
      border-radius: 8px;
      padding: 0.8rem 1rem;
      font-family: var(--font-mono);
      font-size: 0.78rem;
      color: #38bdf8;
      margin-bottom: 1.5rem;
      overflow-x: auto;
    }
    .project-footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      padding-top: 1.25rem;
      border-top: 1px solid var(--border-subtle);
    }
    .project-btn-deep {
      background: none;
      border: none;
      font-family: var(--font-mono);
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--cyan-bright);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.4rem;
      transition: color 0.2s, transform 0.2s;
    }
    .project-btn-deep:hover {
      color: #ffffff;
      transform: translateX(3px);
    }
    .project-github-link {
      color: var(--text-muted);
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 0.4rem;
      font-family: var(--font-mono);
      font-size: 0.8rem;
      transition: color 0.2s;
    }
    .project-github-link:hover {
      color: #ffffff;
    }

    /* ==========================================================================
       8. RESEARCH & PEER-REVIEWED PUBLICATIONS
       ========================================================================== */
    .publications-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 1.5rem;
      margin-top: 2rem;
    }
    .pub-card {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 16px;
      padding: 2.25rem;
      display: grid;
      grid-template-columns: 1fr auto;
      gap: 2rem;
      align-items: center;
      transition: border-color 0.3s;
    }
    .pub-card:hover {
      border-color: var(--border-accent);
    }
    .pub-tag {
      font-family: var(--font-mono);
      font-size: 0.72rem;
      padding: 0.3rem 0.75rem;
      border-radius: 4px;
      background: rgba(99, 102, 241, 0.1);
      border: 1px solid rgba(99, 102, 241, 0.3);
      color: #818cf8;
      display: inline-block;
      margin-bottom: 0.75rem;
    }
    .pub-title {
      font-family: var(--font-display);
      font-size: 1.35rem;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 0.5rem;
      line-height: 1.35;
    }
    .pub-venue {
      font-family: var(--font-body);
      font-size: 0.9rem;
      color: var(--cyan-bright);
      margin-bottom: 1rem;
    }
    .pub-abstract {
      font-size: 0.92rem;
      color: var(--text-muted);
      line-height: 1.65;
      max-width: 850px;
      margin-bottom: 1.25rem;
    }
    .pub-actions {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
      min-width: 170px;
    }

    /* ==========================================================================
       9. INTERACTIVE TERMINAL
       ========================================================================== */
    .terminal-box {
      background: #020409;
      border: 1px solid rgba(0, 242, 254, 0.25);
      border-radius: 12px;
      box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.9);
      overflow: hidden;
      font-family: var(--font-mono);
    }
    .terminal-header {
      background: #090d18;
      padding: 0.75rem 1.25rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--border-subtle);
    }
    .terminal-dots {
      display: flex;
      gap: 6px;
    }
    .dot-red { width: 10px; height: 10px; border-radius: 50%; background: #ef4444; }
    .dot-yellow { width: 10px; height: 10px; border-radius: 50%; background: #f59e0b; }
    .dot-green { width: 10px; height: 10px; border-radius: 50%; background: #10b981; }
    .terminal-title {
      font-size: 0.75rem;
      color: var(--text-dim);
    }
    .terminal-body {
      padding: 1.5rem;
      min-height: 280px;
      max-height: 420px;
      overflow-y: auto;
      font-size: 0.85rem;
      line-height: 1.6;
    }
    .term-line {
      margin-bottom: 0.5rem;
    }
    .term-line.cyan { color: var(--cyan-bright); }
    .term-line.emerald { color: var(--emerald-neon); }
    .term-line.muted { color: var(--text-dim); }
    .term-input-row {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      margin-top: 1rem;
    }
    .term-prompt {
      color: var(--emerald-neon);
      font-weight: 600;
    }
    .term-input {
      background: transparent;
      border: none;
      outline: none;
      font-family: var(--font-mono);
      font-size: 0.85rem;
      color: #ffffff;
      flex-grow: 1;
    }

    /* ==========================================================================
       10. TIMELINE / ENGINEERING JOURNEY
       ========================================================================== */
    .timeline {
      position: relative;
      padding-left: 2rem;
      border-left: 2px solid var(--border-subtle);
      margin-top: 2rem;
    }
    .timeline-item {
      position: relative;
      margin-bottom: 3rem;
    }
    .timeline-item::before {
      content: "";
      position: absolute;
      left: -2rem;
      top: 0.25rem;
      width: 14px;
      height: 14px;
      border-radius: 50%;
      background: #050811;
      border: 3px solid var(--cyan-bright);
      transform: translateX(-50%);
      box-shadow: 0 0 10px var(--cyan-bright);
    }
    .timeline-year {
      font-family: var(--font-mono);
      font-size: 0.8rem;
      color: var(--cyan-bright);
      margin-bottom: 0.35rem;
    }
    .timeline-title {
      font-family: var(--font-display);
      font-size: 1.25rem;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 0.5rem;
    }
    .timeline-desc {
      color: var(--text-muted);
      font-size: 0.95rem;
      line-height: 1.6;
      max-width: 700px;
    }

    /* ==========================================================================
       11. MODAL DIALOG FOR TECHNICAL DEEP-DIVES
       ========================================================================== */
    .modal-overlay {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(5, 8, 17, 0.85);
      backdrop-filter: blur(16px);
      z-index: 1000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
    }
    .modal-overlay.active {
      display: flex;
    }
    .modal-content {
      background: #0b1120;
      border: 1px solid var(--border-accent);
      border-radius: 16px;
      width: 100%;
      max-width: 780px;
      max-height: 85vh;
      overflow-y: auto;
      padding: 2.5rem;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.9);
      position: relative;
    }
    .modal-close {
      position: absolute;
      top: 1.5rem;
      right: 1.5rem;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      width: 36px;
      height: 36px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 1.2rem;
      transition: all 0.2s;
    }
    .modal-close:hover {
      background: rgba(255, 255, 255, 0.1);
      color: #ffffff;
    }
    .modal-title {
      font-family: var(--font-display);
      font-size: 1.75rem;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 0.5rem;
    }
    .modal-meta {
      font-family: var(--font-mono);
      font-size: 0.8rem;
      color: var(--cyan-bright);
      margin-bottom: 1.75rem;
    }
    .modal-section-h {
      font-family: var(--font-display);
      font-size: 1.1rem;
      font-weight: 600;
      color: #e2e8f0;
      margin-top: 1.5rem;
      margin-bottom: 0.5rem;
      border-bottom: 1px solid var(--border-subtle);
      padding-bottom: 0.35rem;
    }
    .modal-p {
      color: var(--text-muted);
      font-size: 0.95rem;
      line-height: 1.7;
      margin-bottom: 1rem;
    }

    /* ==========================================================================
       12. FOOTER
       ========================================================================== */
    footer {
      border-top: 1px solid var(--border-subtle);
      padding: 4rem 0 3rem;
      margin-top: 4rem;
    }
    .footer-content {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 2rem;
    }
    .footer-quote {
      font-family: var(--font-display);
      font-size: 1.15rem;
      color: #ffffff;
      max-width: 500px;
    }
    .footer-links {
      display: flex;
      gap: 1.5rem;
    }
    .footer-link {
      color: var(--text-muted);
      text-decoration: none;
      font-family: var(--font-mono);
      font-size: 0.85rem;
      transition: color 0.2s;
    }
    .footer-link:hover {
      color: var(--cyan-bright);
    }

    /* Responsive */
    @media (max-width: 768px) {
      .nav-links { display: none; }
      .pub-card { grid-template-columns: 1fr; }
      .hero-actions { flex-direction: column; align-items: stretch; }
      .projects-grid { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>

  <!-- Custom Glowing Cursor Elements -->
  <div class="cursor-dot" id="cursorDot"></div>
  <div class="cursor-outline" id="cursorOutline"></div>

  <!-- Background 3D Canvas -->
  <canvas id="canvas3d"></canvas>
  <div class="grid-overlay"></div>

  <!-- Top Glass Navigation Bar -->
  <header class="nav-container">
    <nav class="nav-glass">
      <a href="#hero" class="nav-brand">
        <span class="nav-brand-dot"></span>
        <span>NIRANJAN.AI</span>
      </a>

      <ul class="nav-links">
        <li><a href="#domains" class="nav-link">Domains</a></li>
        <li><a href="#projects" class="nav-link">Flagship Systems</a></li>
        <li><a href="#research" class="nav-link">Research</a></li>
        <li><a href="#terminal" class="nav-link">Terminal</a></li>
        <li><a href="#journey" class="nav-link">Milestones</a></li>
      </ul>

      <a href="mailto:niranjankrishnakumar2005@gmail.com" class="nav-badge-btn">
        <span>GET IN TOUCH</span>
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
      </a>
    </nav>
  </header>

  <!-- Main Content Wrapper -->
  <main>

    <!-- 1. HERO SECTION -->
    <section class="hero-section" id="hero">
      <div class="status-pill">
        <span class="status-dot-inner"></span>
        <span>RESEARCHING HYPERSPECTRAL 3D-CNNs & SILICON TELEMETRY</span>
      </div>

      <h1 class="hero-name">NIRANJAN<br/>KRISHNAKUMAR</h1>

      <!-- Dynamic Typing Specialization Box -->
      <div class="hero-typing-box">
        <span id="typedText"></span><span class="cursor-blink"></span>
      </div>

      <p class="hero-manifesto">
        "Operating at the convergence of high-dimensional sensor physics, machine learning representations, and embedded silicon execution. Rather than treating AI as an isolated mathematical abstraction, I engineer physical systems where failure is mathematically bounded."
      </p>

      <div class="hero-actions">
        <a href="#projects" class="btn-primary">
          <span>EXPLORE FLAGSHIP SYSTEMS</span>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
        </a>

        <a href="https://doi.org/10.1109/EPREC66546.2026.11412040" target="_blank" rel="noreferrer" class="btn-secondary">
          <span>IEEE EPREC-2026 PUBLICATION</span>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
        </a>
      </div>

      <!-- Live Telemetry Bar -->
      <div class="telemetry-strip">
        <div class="telemetry-item">
          <span class="telemetry-num">1200+</span>
          <span class="telemetry-label">Hyperspectral Bands (400–1000 nm)</span>
        </div>
        <div class="telemetry-item">
          <span class="telemetry-num">R² = 0.9994</span>
          <span class="telemetry-label">PINN Solar MPPT Correlation</span>
        </div>
        <div class="telemetry-item">
          <span class="telemetry-num">&lt; 5 ms</span>
          <span class="telemetry-label">ESP32 BLE 5.0 Kinematic Latency</span>
        </div>
        <div class="telemetry-item">
          <span class="telemetry-num">2</span>
          <span class="telemetry-label">Peer-Reviewed IEEE Publications</span>
        </div>
      </div>
    </section>

    <!-- 2. INTERACTIVE TECHNICAL DOMAINS -->
    <section id="domains">
      <div class="section-eyebrow">RESEARCH ARCHITECTURE</div>
      <h2 class="section-title">Core <span class="glow">Technical Pillars</span></h2>
      <p class="section-desc">
        Bridging bare-metal microcontroller registers to non-convex optimization and high-dimensional deep tensor spaces.
      </p>

      <div class="domains-grid">
        <!-- Domain 1 -->
        <div class="domain-card">
          <div class="domain-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>
          </div>
          <h3 class="domain-title">Computer Vision & Spectral AI</h3>
          <p class="domain-desc">
            Hyperspectral datacubes (400–1000 nm), 3D-CNN feature fusion, ArcFace deep metric loss on $S^{127}$, and Explainable AI (Spectral SHAP, Grad-CAM++).
          </p>
          <div class="domain-tags">
            <span class="domain-tag">PyTorch</span>
            <span class="domain-tag">3D-CNN</span>
            <span class="domain-tag">ArcFace</span>
            <span class="domain-tag">OpenCV</span>
          </div>
        </div>

        <!-- Domain 2 -->
        <div class="domain-card">
          <div class="domain-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8h1a4 4 0 0 1 0 8h-1"></path><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"></path><line x1="6" y1="1" x2="6" y2="4"></line><line x1="10" y1="1" x2="10" y2="4"></line><line x1="14" y1="1" x2="14" y2="4"></line></svg>
          </div>
          <h3 class="domain-title">Cyber-Physical Silicon</h3>
          <p class="domain-desc">
            Dual-core ESP32 register programming, low-latency FreeRTOS tasks, BLE 5.0 GATT kinematic streaming, and interactive 3D glTF digital twin rendering.
          </p>
          <div class="domain-tags">
            <span class="domain-tag">ESP32</span>
            <span class="domain-tag">FreeRTOS</span>
            <span class="domain-tag">BLE 5.0</span>
            <span class="domain-tag">Three.js</span>
          </div>
        </div>

        <!-- Domain 3 -->
        <div class="domain-card">
          <div class="domain-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
          </div>
          <h3 class="domain-title">Power Grid Metaheuristics</h3>
          <p class="domain-desc">
            PTDF DC-OPF sensitivity modeling ($C = A \cdot B$) on IEEE transmission grids solved via tri-hybrid heuristics (Orca, Krill Herd, Spotted Hyena).
          </p>
          <div class="domain-tags">
            <span class="domain-tag">IEEE EPREC</span>
            <span class="domain-tag">DC-OPF</span>
            <span class="domain-tag">OOA-KHA-SHO</span>
            <span class="domain-tag">MATLAB</span>
          </div>
        </div>

        <!-- Domain 4 -->
        <div class="domain-card">
          <div class="domain-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20"></path><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>
          </div>
          <h3 class="domain-title">PINNs & DSP Analytics</h3>
          <p class="domain-desc">
            Embedding semiconductor diode equations into neural architectures, 300-state 2D Markov stochastic weather generation, and harmonic analysis (FFT/THD).
          </p>
          <div class="domain-tags">
            <span class="domain-tag">PINNs</span>
            <span class="domain-tag">Markov Chains</span>
            <span class="domain-tag">FFT / THD</span>
            <span class="domain-tag">Python</span>
          </div>
        </div>
      </div>
    </section>

    <!-- 3. SELECTED PROJECTS SHOWCASE -->
    <section id="projects">
      <div class="section-eyebrow">ENGINEERING REPOSITORY</div>
      <h2 class="section-title">Selected <span class="glow">Flagship Systems</span></h2>
      <p class="section-desc">
        Curated systems built with first-principles physical rigor and verifiable empirical performance.
      </p>

      <!-- Filter Tabs -->
      <div class="filter-bar">
        <button class="filter-btn active" onclick="filterProjects('all', this)">All Disciplines</button>
        <button class="filter-btn" onclick="filterProjects('vision', this)">Computer Vision & AI</button>
        <button class="filter-btn" onclick="filterProjects('silicon', this)">Embedded & Wearables</button>
        <button class="filter-btn" onclick="filterProjects('energy', this)">Energy & Optimization</button>
      </div>

      <div class="projects-grid" id="projectsGrid">
        
        <!-- PROJECT 1 -->
        <article class="project-card" data-category="vision">
          <div>
            <div class="project-header">
              <span class="project-badge">VISION & SPECTRAL AI</span>
              <span class="project-index">[01]</span>
            </div>
            <h3 class="project-title">Hyperspectral Face ID & Explainable AI</h3>
            <p class="project-desc">
              Resolves RGB facial anti-spoofing vulnerabilities by processing subsurface biological tissue reflectance across 1200+ contiguous bands (400–1000 nm). Built with a 3D-CNN feature extractor and Additive Angular Margin loss (ArcFace on $S^{127}$ hypersphere).
            </p>
            <div class="project-math">
              Loss: L_ArcFace = -log( e^(s*cos(θ_yi + m)) / Σ e^(s*cos(θ_j)) )
            </div>
          </div>
          <div class="project-footer">
            <button class="project-btn-deep" onclick="openDeepDive('hyperspectral')">
              <span>TECHNICAL DOSSIER</span>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
            </button>
            <a href="https://github.com/niranjan-crypt/Hyperspectral-Face-Identification-XAI" target="_blank" class="project-github-link">
              <span>GitHub</span>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
            </a>
          </div>
        </article>

        <!-- PROJECT 2 -->
        <article class="project-card" data-category="silicon">
          <div>
            <div class="project-header">
              <span class="project-badge">EMBEDDED SILICON & TWINS</span>
              <span class="project-index">[02]</span>
            </div>
            <h3 class="project-title">KinoSync: Smart Glove & 3D Digital Twin</h3>
            <p class="project-desc">
              ESP32 dual-core teleoperation wearable sampling 5-channel continuous flex kinematics and streaming over custom BLE 5.0 GATT services (&lt;5 ms latency) to a synchronized 3D glTF digital twin.
            </p>
            <div class="project-math">
              Kinematics: θ_j(t) = f(ADC_raw) · K_calib | BLE MTU: 247 bytes @ 50 Hz
            </div>
          </div>
          <div class="project-footer">
            <button class="project-btn-deep" onclick="openDeepDive('kinosync')">
              <span>TECHNICAL DOSSIER</span>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
            </button>
            <a href="https://github.com/niranjan-crypt/KinoSync-Cyber-Physical-Smart-Glove-Telemetry-3D-Digital-Twin-System" target="_blank" class="project-github-link">
              <span>GitHub</span>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
            </a>
          </div>
        </article>

        <!-- PROJECT 3 -->
        <article class="project-card" data-category="energy">
          <div>
            <div class="project-header">
              <span class="project-badge">ENERGY AI & OPTIMIZATION</span>
              <span class="project-index">[03]</span>
            </div>
            <h3 class="project-title">Power Transmission Congestion Optimization</h3>
            <p class="project-desc">
              Published at IEEE EPREC-2026. Solves constrained DC-OPF sensitivity matrices on IEEE 14-bus and 30-bus networks using a novel tri-hybrid metaheuristic (OOA, KHA, SHO) with zero avoidable load shedding.
            </p>
            <div class="project-math">
              PTDF Sensitivity: ΔP_ij = Σ (PTDF_ij-k · ΔP_Gk)  |  C = A · B
            </div>
          </div>
          <div class="project-footer">
            <button class="project-btn-deep" onclick="openDeepDive('congestion')">
              <span>TECHNICAL DOSSIER</span>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
            </button>
            <a href="https://doi.org/10.1109/EPREC66546.2026.11412040" target="_blank" class="project-github-link">
              <span>DOI Paper</span>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
            </a>
          </div>
        </article>

        <!-- PROJECT 4 -->
        <article class="project-card" data-category="energy">
          <div>
            <div class="project-header">
              <span class="project-badge">PHYSICS-INFORMED ML</span>
              <span class="project-index">[04]</span>
            </div>
            <h3 class="project-title">Physics-Informed Solar MPPT Controller</h3>
            <p class="project-desc">
              Accepted at IEEE SPICES-2026. Embeds 6 semiconductor diode features into an Artificial Neural Network for single-step zero-oscillation Maximum Power Point Tracking. Validated via a 300-state 2D Markov weather simulator.
            </p>
            <div class="project-math">
              Diode PINN: I = I_ph - I_0 [ exp((V + I*R_s) / (n*V_t)) - 1 ] - (V + I*R_s) / R_sh
            </div>
          </div>
          <div class="project-footer">
            <button class="project-btn-deep" onclick="openDeepDive('mppt')">
              <span>TECHNICAL DOSSIER</span>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
            </button>
            <a href="https://github.com/niranjan-crypt/Physics-Informed-ANN-Based-MPPT-with-Markov-Chain-Based-Dynamic-Validation-for-Photovoltaic-Systems" target="_blank" class="project-github-link">
              <span>GitHub</span>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
            </a>
          </div>
        </article>

      </div>
    </section>

    <!-- 4. RESEARCH & PUBLICATIONS SECTION -->
    <section id="research">
      <div class="section-eyebrow">ACADEMIC OUTPUT</div>
      <h2 class="section-title">Peer-Reviewed <span class="glow">Research</span></h2>
      <p class="section-desc">
        Formal mathematical publications presenting novel sensitivity formulations and physics-informed architectures.
      </p>

      <div class="publications-grid">
        
        <!-- Paper 1 -->
        <div class="pub-card">
          <div>
            <span class="pub-tag">IEEE EPREC-2026 PUBLISHED</span>
            <h3 class="pub-title">Hybrid Optimization for Congestion Management in Deregulated Power Systems</h3>
            <p class="pub-venue">6th International Conference on Electric Power and Renewable Energy (EPREC-2026), IIT Bhilai • Published by IEEE</p>
            <p class="pub-abstract">
              Formulated a constrained DC Optimal Power Flow sensitivity framework ($C = A \cdot B$) on IEEE 14-bus and 30-bus transmission networks. Engineered a novel tri-hybrid metaheuristic combining Orca Optimization Algorithm (OOA), Krill Herd Algorithm (KHA), and Spotted Hyena Optimizer (SHO) with dynamic diversification to relieve transmission line overloads with minimal generator redispatch deviation and zero avoidable load shedding.
            </p>
            <div class="domain-tags">
              <span class="domain-tag">DOI: 10.1109/EPREC66546.2026.11412040</span>
              <span class="domain-tag">PTDF DC-OPF</span>
              <span class="domain-tag">OOA-KHA-SHO</span>
            </div>
          </div>
          <div class="pub-actions">
            <a href="https://doi.org/10.1109/EPREC66546.2026.11412040" target="_blank" class="btn-primary" style="font-size: 0.8rem; padding: 0.7rem 1.2rem;">
              <span>READ DOI PAPER</span>
            </a>
            <a href="https://github.com/niranjan-crypt/Hybrid-Optimization-for-Congestion-Management-in-Deregulated-Power-Systems" target="_blank" class="btn-secondary" style="font-size: 0.8rem; padding: 0.7rem 1.2rem;">
              <span>VIEW SOURCE</span>
            </a>
          </div>
        </div>

        <!-- Paper 2 -->
        <div class="pub-card">
          <div>
            <span class="pub-tag">IEEE SPICES-2026 ACCEPTED</span>
            <h3 class="pub-title">Physics-Informed ANN-Based MPPT with Markov-Chain Dynamic Validation for Photovoltaic Systems</h3>
            <p class="pub-venue">IEEE International Conference on Signal Processing, Informatics, Communication and Energy Systems • Published by IEEE</p>
            <p class="pub-abstract">
              Embedded 6 physically derived semiconductor diode features into an Artificial Neural Network, enabling single-step zero-oscillation Maximum Power Point Tracking (MPPT). Stress-tested via a 300-state 2D Markov chain stochastic weather simulator, demonstrating $R^2 = 0.9994$, &gt;99.5% dynamic tracking efficiency, and settling times under 5 ms in hardware simulations.
            </p>
            <div class="domain-tags">
              <span class="domain-tag">Diode PINN</span>
              <span class="domain-tag">2D Markov Weather</span>
              <span class="domain-tag">R² = 0.9994</span>
            </div>
          </div>
          <div class="pub-actions">
            <a href="https://github.com/niranjan-crypt/Physics-Informed-ANN-Based-MPPT-with-Markov-Chain-Based-Dynamic-Validation-for-Photovoltaic-Systems" target="_blank" class="btn-primary" style="font-size: 0.8rem; padding: 0.7rem 1.2rem;">
              <span>VIEW PREPRINT</span>
            </a>
          </div>
        </div>

      </div>
    </section>

    <!-- 5. INTERACTIVE TERMINAL EMULATOR -->
    <section id="terminal">
      <div class="section-eyebrow">COMMAND INTERFACE</div>
      <h2 class="section-title">Interactive <span class="glow">System Shell</span></h2>
      <p class="section-desc">
        Direct telemetry shell to interrogate research credentials, inspect hardware telemetry, or navigate sections.
      </p>

      <div class="terminal-box">
        <div class="terminal-header">
          <div class="terminal-dots">
            <span class="dot-red"></span>
            <span class="dot-yellow"></span>
            <span class="dot-green"></span>
          </div>
          <div class="terminal-title">niranjan@silicon-lab: ~/system_shell</div>
          <div style="width: 40px;"></div>
        </div>

        <div class="terminal-body" id="termOutput">
          <div class="term-line muted">Initializing Cyber-Physical Kernel v3.8.4... [OK]</div>
          <div class="term-line muted">Loaded IEEE EPREC-2026 PTDF Sensitivity Tensor... [OK]</div>
          <div class="term-line cyan">Welcome to Niranjan Krishnakumar's Research Shell.</div>
          <div class="term-line">Type <span class="cyan">help</span> to list available commands (e.g. <span class="cyan">about</span>, <span class="cyan">projects</span>, <span class="cyan">research</span>, <span class="cyan">contact</span>).</div>
        </div>

        <div style="padding: 0 1.5rem 1.5rem;">
          <div class="term-input-row">
            <span class="term-prompt">niranjan@cyber:~$</span>
            <input type="text" class="term-input" id="termInput" placeholder="Type 'help' and press Enter..." autocomplete="off" />
          </div>
        </div>
      </div>
    </section>

    <!-- 6. ENGINEERING TIMELINE -->
    <section id="journey">
      <div class="section-eyebrow">CHRONOLOGY</div>
      <h2 class="section-title">Engineering <span class="glow">Milestones</span></h2>

      <div class="timeline">
        <div class="timeline-item">
          <div class="timeline-year">2026 — PRESENT</div>
          <h3 class="timeline-title">Peer-Reviewed IEEE Publications & Research</h3>
          <p class="timeline-desc">
            Published author at IEEE EPREC-2026 (IIT Bhilai) for grid congestion optimization and accepted researcher at IEEE SPICES-2026 for physics-informed solar neural controllers.
          </p>
        </div>

        <div class="timeline-item">
          <div class="timeline-year">JUNE 2026</div>
          <h3 class="timeline-title">Industry Intern — Larsen & Toubro (L&T), Chennai</h3>
          <p class="timeline-desc">
            Engineered simulation models of EV powertrains and Battery Management Systems (BMS) to evaluate PMSM/BLDC motor-control behavior, DC–DC converter operation, CAN-bus communication, and railway SCADA automation.
          </p>
        </div>

        <div class="timeline-item">
          <div class="timeline-year">FEBRUARY 2026</div>
          <h3 class="timeline-title">AWS Academy Graduate — Cloud Foundations</h3>
          <p class="timeline-desc">
            Certified in scalable cloud compute, network topologies, IAM security architectures, and relational storage via verifiable Credly badge.
          </p>
        </div>

        <div class="timeline-item">
          <div class="timeline-year">2023 — 2027 (EXPECTED)</div>
          <h3 class="timeline-title">B.Tech in Electrical & Computer Engineering (ELC)</h3>
          <p class="timeline-desc">
            Amrita Vishwa Vidyapeetham, Coimbatore. Rigorous training across analog signal conditioning, electromagnetics, embedded silicon, computer vision, and deep learning representations.
          </p>
        </div>
      </div>
    </section>

  </main>

  <!-- Technical Deep-Dive Modal Window -->
  <div class="modal-overlay" id="deepDiveModal" onclick="closeModalOnOverlay(event)">
    <div class="modal-content">
      <button class="modal-close" onclick="closeModal()">&times;</button>
      <div id="modalBody"></div>
    </div>
  </div>

  <!-- Footer -->
  <footer>
    <div style="max-width: 1240px; margin: 0 auto; padding: 0 1.5rem;">
      <div class="footer-content">
        <div>
          <div class="footer-quote">
            "Operating at the intersection where physical hardware, applied mathematics, and artificial intelligence converge."
          </div>
          <div style="color: var(--text-dim); font-size: 0.8rem; font-family: var(--font-mono); margin-top: 0.5rem;">
            &copy; 2026 Niranjan Krishnakumar. All rights reserved.
          </div>
        </div>

        <div class="footer-links">
          <a href="https://github.com/niranjan-crypt" target="_blank" class="footer-link">GitHub</a>
          <a href="https://doi.org/10.1109/EPREC66546.2026.11412040" target="_blank" class="footer-link">IEEE EPREC</a>
          <a href="https://www.credly.com/badges/eaed5b78-e6d1-426e-8be1-6a1c66f2bc7e" target="_blank" class="footer-link">Credly</a>
          <a href="mailto:niranjankrishnakumar2005@gmail.com" class="footer-link">Email</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- ==========================================================================
       JAVASCRIPT: THREE.JS BACKGROUND, TYPING, TERMINAL & INTERACTIONS
       ========================================================================== -->
  <script>
    /* 1. Custom Mouse Glowing Cursor */
    const cursorDot = document.getElementById('cursorDot');
    const cursorOutline = document.getElementById('cursorOutline');

    window.addEventListener('mousemove', (e) => {
      const posX = e.clientX;
      const posY = e.clientY;
      cursorDot.style.left = `${posX}px`;
      cursorDot.style.top = `${posY}px`;

      cursorOutline.animate({
        left: `${posX}px`,
        top: `${posY}px`
      }, { duration: 400, fill: "forwards" });
    });

    /* 2. Interactive Three.js 3D Wireframe Cyber-Sphere with Particles */
    const canvas = document.getElementById('canvas3d');
    const renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(55, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.z = 24;

    // Particle Cloud
    const particleCount = 1800;
    const geometry = new THREE.BufferGeometry();
    const positions = new Float32Array(particleCount * 3);
    const colors = new Float32Array(particleCount * 3);

    const color1 = new THREE.Color('#00f2fe');
    const color2 = new THREE.Color('#6366f1');

    for (let i = 0; i < particleCount * 3; i += 3) {
      const radius = 10 + Math.random() * 8;
      const theta = Math.random() * Math.PI * 2;
      const phi = Math.acos((Math.random() * 2) - 1);

      positions[i] = radius * Math.sin(phi) * Math.cos(theta);
      positions[i + 1] = radius * Math.sin(phi) * Math.sin(theta);
      positions[i + 2] = radius * Math.cos(phi);

      const mixedColor = color1.clone().lerp(color2, Math.random());
      colors[i] = mixedColor.r;
      colors[i + 1] = mixedColor.g;
      colors[i + 2] = mixedColor.b;
    }

    geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));

    const material = new THREE.PointsMaterial({
      size: 0.12,
      vertexColors: true,
      transparent: true,
      opacity: 0.85
    });

    const particleSystem = new THREE.Points(geometry, material);
    scene.add(particleSystem);

    // Inner Cyber-Wireframe Icosahedron
    const sphereGeo = new THREE.IcosahedronGeometry(7.5, 2);
    const sphereMat = new THREE.MeshBasicMaterial({
      color: 0x06b6d4,
      wireframe: true,
      transparent: true,
      opacity: 0.18
    });
    const wireSphere = new THREE.Mesh(sphereGeo, sphereMat);
    scene.add(wireSphere);

    // Mouse Interaction
    let mouseX = 0;
    let mouseY = 0;
    window.addEventListener('mousemove', (e) => {
      mouseX = (e.clientX / window.innerWidth) * 2 - 1;
      mouseY = -(e.clientY / window.innerHeight) * 2 + 1;
    });

    window.addEventListener('resize', () => {
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
    });

    // Animation Loop
    function animate() {
      requestAnimationFrame(animate);

      particleSystem.rotation.y += 0.0012;
      particleSystem.rotation.x += 0.0006;
      wireSphere.rotation.y -= 0.0018;

      // Subtle mouse parallax
      camera.position.x += (mouseX * 2.5 - camera.position.x) * 0.05;
      camera.position.y += (-mouseY * 2.5 - camera.position.y) * 0.05;
      camera.lookAt(scene.position);

      renderer.render(scene, camera);
    }
    animate();

    /* 3. Typing Effect in Hero Section */
    const typingPhrases = [
      "Hyperspectral 3D-CNNs & Metric Learning",
      "Published Author @ IEEE EPREC-2026",
      "Cyber-Physical ESP32 Silicon & BLE 5.0 GATT",
      "Physics-Informed Neural Solar MPPT (SPICES-2026)",
      "High-Dimensional Sensor Physics & Digital Twins"
    ];

    let phraseIdx = 0;
    let charIdx = 0;
    let isDeleting = false;
    const typedTextEl = document.getElementById('typedText');

    function typeLoop() {
      const currentPhrase = typingPhrases[phraseIdx];

      if (isDeleting) {
        typedTextEl.textContent = currentPhrase.substring(0, charIdx - 1);
        charIdx--;
      } else {
        typedTextEl.textContent = currentPhrase.substring(0, charIdx + 1);
        charIdx++;
      }

      let typingSpeed = isDeleting ? 40 : 80;

      if (!isDeleting && charIdx === currentPhrase.length) {
        typingSpeed = 2000; // Pause at end
        isDeleting = true;
      } else if (isDeleting && charIdx === 0) {
        isDeleting = false;
        phraseIdx = (phraseIdx + 1) % typingPhrases.length;
        typingSpeed = 400;
      }

      setTimeout(typeLoop, typingSpeed);
    }
    typeLoop();

    /* 4. Project Filter Logic */
    function filterProjects(category, btnEl) {
      document.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
      btnEl.classList.add('active');

      const cards = document.querySelectorAll('.project-card');
      cards.forEach(card => {
        if (category === 'all' || card.getAttribute('data-category') === category) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
    }

    /* 5. Interactive Terminal Logic */
    const termInput = document.getElementById('termInput');
    const termOutput = document.getElementById('termOutput');

    termInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        const val = termInput.value.trim().toLowerCase();
        termInput.value = '';

        // Add user command line
        const cmdLine = document.createElement('div');
        cmdLine.className = 'term-line';
        cmdLine.innerHTML = `<span class="term-prompt">niranjan@cyber:~$</span> ${val}`;
        termOutput.appendChild(cmdLine);

        // Process Command
        let response = '';
        if (val === 'help') {
          response = `Available commands:
  • <span class="cyan">about</span>       - Print executive background & philosophy
  • <span class="cyan">projects</span>    - List flagship engineering systems
  • <span class="cyan">research</span>    - Display IEEE publications & DOI links
  • <span class="cyan">contact</span>     - Display email & communication coordinates
  • <span class="cyan">clear</span>       - Clear shell console output`;
        } else if (val === 'about') {
          response = `<span class="emerald">Niranjan Krishnakumar</span> — Electrical & Computer Engineering undergraduate at Amrita Vishwa Vidyapeetham ('27). Operating at the nexus of sensor physics, 3D deep metric embeddings, and embedded silicon.`;
        } else if (val === 'projects') {
          response = `Flagship Systems:
  1. Hyperspectral Face ID & XAI (3D-CNN, ArcFace, Spectral SHAP)
  2. KinoSync Smart Glove (ESP32, BLE 5.0 GATT, 3D glTF Twin)
  3. Power Grid Congestion Optimization (Tri-hybrid OOA-KHA-SHO)
  4. Physics-Informed Solar MPPT (Diode PINN + 2D Markov Simulator)`;
        } else if (val === 'research') {
          response = `Publications:
  • IEEE EPREC-2026: Hybrid Optimization for Congestion Management (DOI: 10.1109/EPREC66546.2026.11412040)
  • IEEE SPICES-2026: Physics-Informed ANN-Based MPPT with Markov-Chain Validation`;
        } else if (val === 'contact') {
          response = `Email: <span class="cyan">niranjankrishnakumar2005@gmail.com</span>
GitHub: <a href="https://github.com/niranjan-crypt" target="_blank" style="color: #00f2fe;">github.com/niranjan-crypt</a>`;
        } else if (val === 'clear') {
          termOutput.innerHTML = '';
          return;
        } else {
          response = `Command not recognized: "${val}". Type <span class="cyan">help</span> for valid commands.`;
        }

        const resLine = document.createElement('div');
        resLine.className = 'term-line';
        resLine.innerHTML = response;
        termOutput.appendChild(resLine);

        termOutput.scrollTop = termOutput.scrollHeight;
      }
    });

    /* 6. Deep Dive Modal Content */
    const deepDiveData = {
      hyperspectral: {
        title: "Hyperspectral Face Identification & Explainable AI",
        meta: "Computer Vision • Deep Metric Learning • Subsurface Biometrics",
        content: `
          <h4 class="modal-section-h">Problem Formulation</h4>
          <p class="modal-p">Conventional RGB biometric verification systems fail against high-resolution 2D photo printouts, 3D silicone masks, and variable chromatic lighting. By sampling 1200+ contiguous spectral bands from 400 nm to 1000 nm, biological tissue reveals distinct chemical and melanin absorption profiles that synthetic spoofs cannot replicate.</p>
          <h4 class="modal-section-h">Architecture & Methodology</h4>
          <p class="modal-p">A spectral-spatial 3D-CNN simultaneously convolves across spatial dimensions and the continuous wavelength axis. Embeddings are projected onto a 128-dimensional unit hypersphere ($S^{127}$) using Additive Angular Margin Loss (ArcFace) with margin $m=0.5$ and scale factor $s=64$. Explainability is enforced using Spectral SHAP feature attributions and Grad-CAM++ activation maps.</p>
          <h4 class="modal-section-h">Verification & Results</h4>
          <p class="modal-p">Benchmarked with metaheuristic band reduction from 1200+ channels down to 15 optimal bands, achieving real-time inference on edge silicon (Raspberry Pi 4) with zero false accepts against silicone mask spoofs.</p>
        `
      },
      kinosync: {
        title: "KinoSync: Cyber-Physical Smart Glove & 3D Digital Twin",
        meta: "ESP32 FreeRTOS • BLE 5.0 GATT • Continuous Kinematics",
        content: `
          <h4 class="modal-section-h">Embedded Architecture</h4>
          <p class="modal-p">A dual-core ESP32 microcontroller executes two deterministic FreeRTOS threads: Core 0 handles high-speed ADC sampling across 5 analog flex sensors through operational amplifiers; Core 1 operates the low-latency Bluetooth Low Energy (BLE 5.0) GATT telemetry stack.</p>
          <h4 class="modal-section-h">Real-Time Teleoperation & Digital Twin</h4>
          <p class="modal-p">Continuous joint angles are packed into custom 247-byte MTU BLE packets broadcast at 50 Hz. A Three.js / Flutter 3D glTF robotic hand twin subscribes to notifications, calculating forward kinematic joint matrices in real time with sub-5ms round-trip latency.</p>
        `
      },
      congestion: {
        title: "Congestion Management via Tri-Hybrid Metaheuristics",
        meta: "IEEE EPREC-2026 • Constrained DC-OPF • Power Transfer Distribution",
        content: `
          <h4 class="modal-section-h">Mathematical Model</h4>
          <p class="modal-p">Formulated a constrained DC-OPF sensitivity framework ($C = A \cdot B$) on IEEE 14-bus and 30-bus transmission networks. Overloaded line flows are mathematically relieved via generator active power redispatch ($\Delta P_G$).</p>
          <h4 class="modal-section-h">Tri-Hybrid Optimization Algorithm</h4>
          <p class="modal-p">Engineered a tri-hybrid optimizer merging the fast global exploration of the Orca Optimization Algorithm (OOA), the spatial flocking dynamics of the Krill Herd Algorithm (KHA), and the encircling entrapment mechanics of the Spotted Hyena Optimizer (SHO). Stagnation is mitigated via Cauchy mutation diversification, achieving zero avoidable load shedding.</p>
        `
      },
      mppt: {
        title: "Physics-Informed ANN-Based Solar MPPT",
        meta: "IEEE SPICES-2026 • Semiconductor Diode Equations • 2D Markov Weather",
        content: `
          <h4 class="modal-section-h">Physics-Guided Neural Architecture</h4>
          <p class="modal-p">Standard MPPT algorithms (Perturb & Observe) suffer from continuous oscillations around the Maximum Power Point. We embedded 6 physically derived semiconductor diode features directly into an Artificial Neural Network, enabling single-step deterministic tracking without oscillatory loss.</p>
          <h4 class="modal-section-h">2D Stochastic Markov Validation</h4>
          <p class="modal-p">The controller was subjected to a 300-state 2D Markov chain simulating stochastic solar irradiance transitions and thermal transients. Achieved $R^2 = 0.9994$, settling times under 5 ms, and dynamic tracking efficiency exceeding 99.5%.</p>
        `
      }
    };

    function openDeepDive(key) {
      const modal = document.getElementById('deepDiveModal');
      const body = document.getElementById('modalBody');
      const data = deepDiveData[key];

      body.innerHTML = `
        <h3 class="modal-title">${data.title}</h3>
        <div class="modal-meta">${data.meta}</div>
        <div>${data.content}</div>
      `;
      modal.classList.add('active');
    }

    function closeModal() {
      document.getElementById('deepDiveModal').classList.remove('active');
    }

    function closeModalOnOverlay(e) {
      if (e.target.id === 'deepDiveModal') {
        closeModal();
      }
    }
  </script>
</body>
</html>
