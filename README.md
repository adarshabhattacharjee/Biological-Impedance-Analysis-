# Biological-Impedance-Analysis
1. Introduction
Every living cell in the body has electrical properties. Biological tissues can conduct electrical signals depending on the condition of cells. This concept is the foundation of Bioelectrical Impedance Analysis, a non-invasive technique used to study tissue health by passing a small alternating electrical current through it and measuring its resistance to that current.

This report explains Python code that models and visualises the electrical behaviour of both healthy and cancerous tissue, using a simplified but realistic electrical circuit model. The goal is to show how the two types of tissue respond differently across a range of frequencies which can be used for early cancer detection.
2. Background & Motivation
•	Why Does Tissue Have Electrical Properties?
All biological cells are surrounded by a thin membrane that acts like a tiny barrier. This membrane is semi-permeable, it controls what goes in and out of the cell. Electrically speaking, this membrane behaves like a combination of a resistor (which slows down current) and a capacitor (which stores charge temporarily). The fluid inside and outside cells also conducts electricity.

When cancer develops, cells change structurally. They tend to pack more tightly, their membranes lose some integrity, and the balance of fluids shifts. All of this changes how electricity flows through the tissue.
•	The Equivalent Circuit Model
For a single biological cell, the standard model is:

•	Rs (Series Resistance): Represents the resistance of the fluid surrounding the cells (extracellular fluid). It is the baseline resistance the current encounters regardless of frequency.
•	Rm (Membrane Resistance): Represents how well the cell membrane resists the flow of current. In healthy tissue, membranes are intact, so this value is higher. In cancer, membranes are compromised, so Rm is lower.
•	Cm (Membrane Capacitance): Represents the ability of the cell membrane to store electrical charge. Cancerous cells often have altered membrane structures, changing this value.

Together, Rm and Cm are connected in parallel (like two paths for electricity to take), and Rs is connected in series (in the main path). 
3. Code Walkthrough 
•	Setting Up the Frequency Range
The first step in the code creates a range of 200 frequency values from 100 Hz to 1,000,000 Hz (1 MHz). This wide range is chosen deliberately because tissue behaves very differently at low vs. high frequencies. At low frequencies, current mostly flows around cells; at high frequencies, it penetrates through the membranes. Sweeping across this range is like testing the tissue at many different electrical speeds to get a complete picture.
•	Assigning Circuit Parameters
The code defines two sets of circuit values — one for healthy tissue and one for cancerous tissue:


Parameter	Healthy Tissue	Cancer Tissue
Rs (Series Resistance)	100 Ω	100 Ω
Rm (Membrane Resistance)	1000 Ω	500 Ω
Cm (Membrane Capacitance)	1.0 μF	1.54 μF

The key insight here is that cancerous tissue has a lower membrane resistance (500 vs. 1000 ohms) because cancer cells have disrupted membranes that are more leaky. It also has a higher capacitance (1.54 vs. 1.0 microfarads), consistent with altered cell membrane structure and increased cell density observed in tumours.
4. Plots and Observations
•	Nyquist Plot 
The Nyquist plot is a classic way to visualise impedance data. For each frequency, the code plots the real part of impedance on the horizontal axis and the negative imaginary part on the vertical axis. The resulting curve is typically a semicircle.

 
Figure 1: Nyquist Plot comparing healthy and cancerous tissue impedance

Key Observations:
•	The healthy tissue curve (blue) forms a larger semicircle, reaching further to the right on the real axis. This is because its higher membrane resistance (1000 Ω) means it opposes current flow more strongly.
•	The cancer tissue curve (red) forms a smaller, shorter semicircle — reflecting the lower membrane resistance (500 Ω) of compromised cell membranes.
•	Both semicircles start at Rs = 100 Ω on the left (the extracellular fluid resistance, which is the same for both), but differ in how far they extend.
•	The diameter of the semicircle is directly related to Rm — a visual, intuitive way to spot tissue differences at a glance.

•	Bode Plot 
While the Nyquist plot compresses all frequencies into one curve, the Bode plot explicitly shows how impedance changes across the frequency range. It has two panels: one showing the magnitude (size) of impedance and one showing the phase angle (timing difference between voltage and current).

 
Figure 2: Bode Plot showing magnitude and phase across frequency for both tissue types

Key Observations:
•	Magnitude 
At low frequencies, healthy tissue has a much higher impedance compared to cancer tissue. This is the clearest frequency range for distinguishing the two. As frequency increases, both converge toward Rs = 100 Ω, because at very high frequencies, the capacitor acts as a short circuit and only the series resistance remains.
•	Phase 
At mid-range frequencies, both tissues show a negative phase, meaning current lags behind voltage, a signature of capacitive behaviour. The peak phase dip and its location shift between healthy and cancerous tissue due to differing Cm values, providing an additional distinguishing feature.
•	Clinical relevance
Low-frequency measurements are particularly valuable for detecting cancer because the contrast between tissue types is greatest there.

•	Sensitivity Plot
The third plot isolates one variable, membrane resistance, and shows how the Nyquist curve changes as Rm is reduced from 1000 Ω (healthy) down to 500 Ω and 200 Ω (increasingly diseased or necrotic tissue).

 
Figure 3: Nyquist sensitivity analysis showing the effect of varying membrane resistance

Key Observations:
•	As Rm decreases, the semicircle shrinks. This directly shows that more damaged or cancerous tissue produces a smaller, more compressed impedance response.
•	The starting point on the real axis remains fixed at Rs = 100 Ω for all three curves, confirming that the extracellular fluid is unchanged — only the membrane properties vary.
5. Clinical Significance
The simulation demonstrates a fundamental principle that underlies real-world clinical tools: different tissues have measurably different electrical signatures, and those signatures can be captured through frequency-swept impedance measurements. This has practical relevance in several areas:

•	Intraoperative margin assessment: 
During cancer surgery, surgeons need to know whether they have removed all the tumour. Impedance probes can provide rapid, real-time feedback about tissue type.
•	Non-invasive screening: 
Wearable or handheld impedance devices are being researched for breast, skin, and colorectal cancer screening without the need for biopsies.
•	Monitoring treatment response
As tumours respond to chemotherapy or radiation, their electrical properties change. Impedance measurements could track this over time.
6. Limitations of the Model
While this simulation is instructive, it is a simplification. Real tissue is far more complex:
•	The model uses a single-shell circuit (one Rs, one Rm, one Cm). Real tissue contains multiple layers — cell interiors, membranes, extracellular matrix — each with their own properties.
•	Biological tissues are heterogeneous and anisotropic. The model assumes uniformity.
•	The parameter values used (e.g., Rm = 1000 Ω for healthy, 500 Ω for cancerous) are illustrative. Actual values vary by tissue type, individual, hydration status, and measurement conditions.
•	The model does not account for electrode effects, contact impedance, or noise, all of which must be addressed in a real measurement system.
7. Conclusion
This Python simulation provides a clear, accessible demonstration of how electrical impedance spectroscopy can differentiate between healthy and cancerous tissue. By modelling each tissue type as a simple Rs-Rm-Cm circuit and sweeping across frequencies from 100 Hz to 1 MHz, the code generates three types of visualisations — Nyquist plots, Bode plots, and sensitivity analyses — each offering a different lens through which to understand the underlying electrical differences.

The key takeaway is that cancerous tissue, with its lower membrane resistance and higher capacitance, produces a distinctly smaller and shifted impedance response. This difference is most pronounced at low frequencies and is clearly visible in all three plots. While the model is a simplification, it faithfully captures the essential physics and provides a strong conceptual foundation for more advanced bioimpedance research and clinical applications.

As cancer detection methods continue to evolve, bioelectrical impedance spectroscopy stands out as a promising, non-invasive, and low-cost complement to conventional diagnostic approaches. This simulation is a first step in understanding and quantifying the electrical language of cells.
