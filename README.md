
---

## 🎖️ Published Peer-Reviewed Research

<table width="100%">
  <tr>
    <td style="padding: 18px; border: 1px solid #30363d; border-radius: 8px;">
      <div align="right">
        <a href="https://doi.org/10.1109/EPREC66546.2026.11412040">
          <img src="https://img.shields.io/badge/IEEE%20Xplore-DOI%3A%2010.1109%2FEPREC66546.2026.11412040-00629B?style=flat-square&logo=ieee&logoColor=white" alt="DOI" />
        </a>
        <img src="https://img.shields.io/badge/Status-Presented%20%26%20Published-2ea44f?style=flat-square" alt="Published" />
      </div>
      <h3>⚡ <a href="https://github.com/niranjan-crypt/Hybrid-Optimization-for-Congestion-Management-in-Deregulated-Power-Systems">Hybrid Optimization for Congestion Management in Deregulated Power Systems</a></h3>
      <p>
        <strong>6th International Conference on Electric Power and Renewable Energy (EPREC-2026)</strong><br>
        <em>Department of Electrical Engineering, Indian Institute of Technology (IIT) Bhilai, India</em><br>
        <strong>Publisher:</strong> IEEE &nbsp;|&nbsp; <strong>Author:</strong> Niranjan Krishnakumar &nbsp;|&nbsp; <strong>License:</strong> MIT
      </p>
      <ul>
        <li><strong>Sensitivity Matrix Modeling:</strong> Formulated nodal active power injections and line power flows via the Power Transfer Distribution Factor (PTDF) sensitivity matrix:
          $$\mathbf{C} = \mathbf{A} \cdot \mathbf{B}$$
          where $\mathbf{B} \in \mathbb{R}^{N \times 1}$ is the bus injection vector, $\mathbf{A} \in \mathbb{R}^{M \times N}$ is the PTDF sensitivity matrix, and $\mathbf{C} \in \mathbb{R}^{M \times 1}$ represents active line flows across $M$ transmission branches.</li>
        <li><strong>Hierarchical Multi-Objective Formulation:</strong> Structured hard physical constraints (line capacity $|C_i| \le C_{i,\max}$, generator physical limits, power balance $\sum B_i = 0$ with $10^{10}$ penalty), strictly minimizing shedded load ($10^7$ penalty), generator redispatch deviation ($10^5$), and economic rescheduling costs ($0.1$).</li>
        <li><strong>Tri-Hybrid Metaheuristic Architecture:</strong> Synthesized an adaptive probability-guided metaheuristic combining:
          <ul>
            <li><strong>Orca Optimization Algorithm (OOA):</strong> Time-decaying coordinated pursuit exploitation.</li>
            <li><strong>Krill Herd Algorithm (KHA):</strong> Multi-dimensional foraging and biological exploration.</li>
            <li><strong>Spotted Hyena Optimizer (SHO):</strong> Encirclement and social hierarchy mechanism.</li>
          </ul>
        </li>
        <li><strong>Two-Stage SciPy SLSQP Polishing:</strong> Post-processed metaheuristic solutions with Sequential Least Squares Programming (SLSQP) for tight constraint satisfaction and sub-megawatt precision.</li>
      </ul>
      <p>
        <a href="https://github.com/niranjan-crypt/Hybrid-Optimization-for-Congestion-Management-in-Deregulated-Power-Systems">
          <img src="https://img.shields.io/badge/View_Repository-181717?style=flat-square&logo=github&logoColor=white" alt="Repo" />
        </a>
      </p>
    </td>
  </tr>
</table>

---

## 🚀 Featured Flagship Projects

### 1. 🦾 [KinoSync: Cyber-Physical Smart Glove & 3D Digital Twin Platform](https://github.com/niranjan-crypt/KinoSync-Cyber-Physical-Smart-Glove-Telemetry-3D-Digital-Twin-System)
> *Real-time Cyber-Physical System (CPS) bridging ESP32 hardware telemetry to an interactive 3D skeletal digital twin.*

<p align="left">
  <img src="https://img.shields.io/badge/Hardware-ESP32-E7352C?style=flat-square&logo=espressif&logoColor=white" />
  <img src="https://img.shields.io/badge/Protocol-BLE_5.0-007AFF?style=flat-square&logo=bluetooth&logoColor=white" />
  <img src="https://img.shields.io/badge/Client-Flutter_3.x-02569B?style=flat-square&logo=flutter&logoColor=white" />
  <img src="https://img.shields.io/badge/3D_Engine-glTF_/_model__viewer-6366F1?style=flat-square" />
  <img src="https://img.shields.io/badge/Biometrics-PPG_Pulse_Sensor-E11D48?style=flat-square" />
</p>

* **Real-Time 3D Digital Twin:** Renders an interactive 3D hand rig (`Hand_Animation_Final.glb`) with multi-finger skeletal animations (`Thumb_Flex`, `Index_Flex`, `Middle_Flex`, `Ring_Flex`, `Little_Flex`) updated continuously via BLE packet streams.
* **Continuous Joint Kinematics:** Converts raw sensor impedance into biomechanical joint flexion angles:
  $$\theta = \text{flexPercent} \times 0.9 \quad (0\% \to 0^\circ, \ 100\% \to 90^\circ)$$
* **Dominant-Finger Hysteresis Filter:** Implemented a $+12\%$ threshold hysteresis state filter to eliminate high-frequency animation jitter and isolate primary intentional finger motions.
* **Biometric PPG & Clinical Logger:** Integrated photoplethysmography (PPG) pulse visualizer for live BPM tracking, synchronized heartbeat animations, and local storage for up to 50 rehabilitation sessions with $\Delta\%$ flexion delta evaluation.

---

### 2. 👁️ [Hyperspectral Human Face Identification & Explainable AI (XAI)](https://github.com/niranjan-crypt/Hyperspectral-Face-Identification-XAI)
> *Anti-spoofing biometrics via 1200+ contiguous spectral bands (400–1000 nm), 3D-CNN feature fusion, and Edge AI deployment.*

<p align="left">
  <img src="https://img.shields.io/badge/TensorFlow-2.15+-FF6F00?style=flat-square&logo=tensorflow&logoColor=white" />
  <img src="https://img.shields.io/badge/Architecture-Spectral--Spatial_3D--CNN-9333EA?style=flat-square" />
  <img src="https://img.shields.io/badge/Loss-ArcFace_on_S^127-10B981?style=flat-square" />
  <img src="https://img.shields.io/badge/XAI-Spectral_SHAP_%2B_Grad--CAM++-3B82F6?style=flat-square" />
  <img src="https://img.shields.io/badge/Edge_Deploy-Raspberry_Pi_4-C51A4A?style=flat-square&logo=raspberrypi&logoColor=white" />
</p>

* **Subsurface Biometric Signatures:** Samples 1200+ contiguous narrow-band channels across 400–1000 nm (VIS to NIR) to capture invariant subsurface tissue characteristics (melanin, oxygenated/deoxygenated hemoglobin, and hydration), providing absolute immunity against 2D photos, 4K screen replays, 3D silicone masks, and generative deepfakes.
* **Metaheuristic Band Selection:** Engineered a 6-component multi-objective fitness formulation:
  $$\max_{B} \; F(B) = \gamma \mathcal{J}_{\text{Fisher}}(B) + \delta \mathcal{C}(B) + \lambda \mathcal{D}(B) - \eta \mathcal{R}(B) - \xi \mathcal{S}(B) + \zeta \Phi(B)$$
  Optimized via PSO, GA, and GWO to compress 1200+ bands into an optimal 5–20 channel subset without loss of discriminative entropy.
* **Unit Hyperspherical Metric Space ($\mathbb{S}^{127}$):** Developed **UISM-Net** (MobileNetV2 backbone with $L_2$-normalized embedding projection on $\mathbb{S}^{127}$) trained with Additive Angular Margin Loss (**ArcFace**):
  $$\mathcal{L}_{\text{ArcFace}} = -\frac{1}{N} \sum_{i=1}^N \log \frac{e^{s \cdot \cos(\theta_{y_i} + m)}}{e^{s \cdot \cos(\theta_{y_i} + m)} + \sum_{j \neq y_i} e^{s \cdot \cos(\theta_j)}}$$
* **Dual-Domain XAI & Edge Deployment:** Auditable biometrics through **Spectral SHAP** (band importance attribution) and **Spatial Grad-CAM++ / LIME** (facial landmark saliency). Quantized (FP16/INT8 TFLite) for Raspberry Pi 4 Model B achieving $<50\text{ms}$ edge inference latency under $<3\text{W}$ power envelope.

---

### 3. ⚡ [IntelliPQ: AI-Based Power Quality Monitoring & Fault Intelligence](https://github.com/niranjan-crypt/IntelliPQ-AI-Based-Power-Quality-Monitoring-Fault-Detection)
> *Smart grid disturbance diagnosis combining Digital Signal Processing (DSP), IEEE Standards, and Deep Learning.*

<p align="left">
  <img src="https://img.shields.io/badge/Compliance-IEEE_1159_%7C_519-F59E0B?style=flat-square" />
  <img src="https://img.shields.io/badge/AI_Model-1D--CNN_%2B_Bidirectional_LSTM-06B6D4?style=flat-square" />
  <img src="https://img.shields.io/badge/Analytics-DSP_/_FFT_Spectrum-8B5CF6?style=flat-square" />
  <img src="https://img.shields.io/badge/Framework-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" />
</p>

* **Full DSP Analytics Engine:** Real-time computation of Fast Fourier Transform (FFT) harmonic spectrum, Total Harmonic Distortion (THD), RMS voltage, peak amplitude, and crest factor.
* **Neuro-Symbolic Arbitration Layer:** Arbitrates between a deterministic rule engine (strict IEEE 1159 voltage sags/swells and IEEE 519 harmonic thresholds) and a deep temporal classifier (1D-CNN + BiLSTM) to eliminate false alarms and validate critical anomalies.
* **Prescriptive Engineering Remedies:** Translates raw diagnostic flags directly into actionable utility procedures (e.g., active harmonic filter tuning, AVR compensation, or capacitor bank de-energization).
* **Automated Compliance Auditing:** Generates downloadable official diagnostic certificates (`.txt`) and synchronized waveform records (`.csv`).

---

### 4. ☀️ [Physics-Informed ANN & Markov Chain MPPT for Solar Photovoltaic Systems](https://github.com/niranjan-crypt/ANN-MARKOV)
> *Eliminating steady-state tracking oscillations in solar PV using semiconductor physics feature embedding and stochastic weather simulation.*

<p align="left">
  <img src="https://img.shields.io/badge/Platform-MATLAB_/_Simulink-ED8B00?style=flat-square&logo=mathworks&logoColor=white" />
  <img src="https://img.shields.io/badge/Model-Physics--Informed_Neural_Net_(PINN)-10B981?style=flat-square" />
  <img src="https://img.shields.io/badge/Stochastics-2D_Markov_Chain_(300_States)-6366F1?style=flat-square" />
  <img src="https://img.shields.io/badge/Regularization-Bayesian_(`trainbr`)-EC4899?style=flat-square" />
</p>

* **Semiconductor Physics Feature Engineering:** Directly maps ambient $(G, T)$ to optimal maximum power points $(V_{mpp}, I_{mpp})$ in a single step without perturbational oscillations by constructing 6 domain features:
  $$\mathbf{X} = \left[ G, \, T, \, \ln(G), \, \sqrt{G}, \, (T - T_{\text{ref}})^2, \, \frac{G}{G_{\text{ref}}}(T - T_{\text{ref}}) \right]$$
  where $\ln(G)$ embeds the logarithmic diode equation ($V_{oc} \propto \frac{nkT}{q} \ln \frac{I_{ph}}{I_0}$).
* **Rigorous Statistical Overfitting Validation:** Enforced group-based cluster partitioning, Bayesian Regularization (`trainbr`), two-sample $t$-test evaluation ($p \ge 0.05$), and Cohen's $d$ effect size verification ($d < 0.2$).
* **2D Markov Stochastic Weather Generator:** Discretized $(T, G)$ space into 300 discrete states ($15 \text{ temperature} \times 20 \text{ irradiance bins}$) to generate realistic diurnal transitions and rapid cloud shading transients for dynamic benchmark testing.
* **Simulink Co-Simulation:** Benchmarked against Newton-Raphson 5-parameter single-diode P&O and InC controllers across DC-DC boost converters and Hybrid Energy Storage Systems (HESS).

---

### 5. 🔍 [Hybrid Computer Vision & Deep Learning for Power Transmission Infrastructure Fault Detection](https://github.com/niranjan-crypt/Hybrid-Computer-Vision-and-Deep-Learning-for-Automated-Power-Transmission-Fault-Detection)
> *Autonomous aerial inspection and multi-class anomaly detection on high-voltage transmission lines.*

<p align="left">
  <img src="https://img.shields.io/badge/Vision-OpenCV_&_Scikit--Image-5C3EE8?style=flat-square&logo=opencv&logoColor=white" />
  <img src="https://img.shields.io/badge/Classifiers-SVM_|_Random_Forest_|_KNN-F7931E?style=flat-square" />
  <img src="https://img.shields.io/badge/Deep_Learning-AlexNet_|_VGG16_|_GoogLeNet_|_ResNet50-EE4C2C?style=flat-square" />
</p>

* **Defect-Specific Classical Pipelines:**
  * *Insulator Disc Defects:* Circular Hough Transform & multi-scale template matching for broken/missing glass disc isolation.
  * *Metallic Corrosion:* HSV color space thresholding combined with mathematical morphological operations.
  * *Foreign Encroachment:* Contour geometry and texture segmentation for bird nest and debris detection.
* **Dual-Paradigm Benchmarking:** Extracted handcrafted spatial-texture features (GLCM, LBP, HOG, Canny, color moments) trained against classical classifiers, compared directly against deep transfer learning backbones (AlexNet, VGG16, InceptionV3, ResNet50).

---

### 6. 🚗 [TOC-AV: Formal Verification System for Autonomous Vehicles](https://github.com/niranjan-crypt/Computation-and-Compiler-design)
> *Theory of Computation & Automata formal verification applied to safety-critical autonomous parking maneuvers.*

<p align="left">
  <img src="https://img.shields.io/badge/Theory-Formal_Automata_Verification-3B82F6?style=flat-square" />
  <img src="https://img.shields.io/badge/Stack-JavaScript_ES6_%2B_Canvas-F7DF1E?style=flat-square&logo=javascript&logoColor=black" />
  <img src="https://img.shields.io/badge/Scope-DFA_|_NFA_|_PDA_|_CFG_|_Timed_Automata-10B981?style=flat-square" />
</p>

* **Safety-Critical State Modeling:** Formally proves correctness of the autonomous parking lifecycle:
  $$\text{SEARCH}^+ \to \text{STOP} \to \text{REVERSE} \to \text{ALIGN} \to \text{PARK}$$
* **Mathematical Automata Implementation:**
  * *DFA 5-Tuple Formulation:* $M = (Q, \Sigma, \delta, q_0, F)$ over states $\{q_0, q_1, q_2, q_3, q_4, q_E\}$ with asynchronous emergency obstacle interruptions (`OBSTACLE` $\to q_E$, `CLEAR` $\to q_1$).
  * *Subset Construction:* Visualized dynamic $\epsilon$-closure mappings and NFA-to-DFA conversion.
  * *Timed Automata:* Measures deterministic reaction latency ($\Delta T$) between obstacle detection and deceleration.
  * *Context-Free Grammar & PDA:* Validates command grammar in Chomsky Normal Form (CNF) via a Pushdown Automaton.

---

## 🛠️ Technical Arsenal

<div align="center">

### Programming & Scientific Computing
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![C++](https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)
![C](https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=black)
![MATLAB](https://img.shields.io/badge/MATLAB-ED8B00?style=for-the-badge&logo=mathworks&logoColor=white)
![Dart](https://img.shields.io/badge/Dart-0175C2?style=for-the-badge&logo=dart&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white)

### AI, Machine Learning & Computer Vision
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

### Cyber-Physical Systems, Embedded & Hardware
![ESP32](https://img.shields.io/badge/ESP32-E7352C?style=for-the-badge&logo=espressif&logoColor=white)
![Raspberry Pi](https://img.shields.io/badge/Raspberry_Pi_4-C51A4A?style=for-the-badge&logo=raspberrypi&logoColor=white)
![BLE](https://img.shields.io/badge/Bluetooth_LE_5.0-0082FC?style=for-the-badge&logo=bluetooth&logoColor=white)
![Simulink](https://img.shields.io/badge/Simulink-E16726?style=for-the-badge&logo=mathworks&logoColor=white)
![Sensors](https://img.shields.io/badge/Telemetry_%26_Biometrics-10B981?style=for-the-badge)

### Software Engineering, Mobile & Cloud
![Flutter](https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

</div>

---

## 📈 GitHub Metrics & Activity

<div align="center">
  <table border="0">
    <tr>
      <td>
        <img src="https://github-readme-stats.vercel.app/api?username=niranjan-crypt&show_icons=true&theme=radical&hide_border=true&title_color=7C3AED&icon_color=06B6D4" alt="GitHub Stats" />
      </td>
      <td>
        <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=niranjan-crypt&layout=compact&theme=radical&hide_border=true&title_color=7C3AED" alt="Top Languages" />
      </td>
    </tr>
  </table>
  <br>
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=niranjan-crypt&theme=radical&hide_border=true&ring=7C3AED&fire=06B6D4&currStreakNum=7C3AED" alt="Streak Stats" />
</div>

---

## 🤝 Connect & Collaborate

<p align="center">
  <a href="mailto:niranjankrishnakumar2005@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-niranjankrishnakumar2005%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail" />
  </a>
  &nbsp;
  <a href="https://github.com/niranjan-crypt">
    <img src="https://img.shields.io/badge/GitHub-niranjan--crypt-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
  </a>
  &nbsp;
  <a href="https://doi.org/10.1109/EPREC66546.2026.11412040">
    <img src="https://img.shields.io/badge/IEEE_Publication-EPREC--2026-00629B?style=for-the-badge&logo=ieee&logoColor=white" alt="IEEE" />
  </a>
</p>

<p align="center">
  <em>"Engineering at the convergence of mathematical optimization, physics-informed AI, and real-time physical systems."</em>
</p>
