FM Signal Visualization Simulator
📌 Project Description

The FM Signal Visualization Simulator is an educational simulation project that demonstrates the generation and visualization of a Frequency Modulated (FM) signal. The project generates the message signal, carrier signal, and FM signal and displays their corresponding waveforms and frequency spectrum.

It is designed to help students understand the basic concepts of frequency modulation, modulation index, carrier frequency, message frequency, and frequency deviation.

🎯 Objectives
Generate a sinusoidal message signal.
Generate a high-frequency carrier signal.
Generate an FM-modulated signal.
Calculate the FM modulation index.
Visualize the message, carrier, and FM signals.
Analyze the frequency spectrum of the FM signal.
Provide an interactive HTML-based simulation output.
Verify the FM signal parameters using a testbench.
📐 FM Theory

The FM signal can be represented as:

𝑠
(
𝑡
)
=
𝐴
𝑐
cos
⁡
(
2
𝜋
𝑓
𝑐
𝑡
+
𝛽
sin
⁡
(
2
𝜋
𝑓
𝑚
𝑡
)
)

where:

𝐴
𝑐
 = Carrier amplitude
𝑓
𝑐
 = Carrier frequency
𝑓
𝑚
 = Message frequency
𝛽
 = FM modulation index

The modulation index is:

𝛽
=
Δ
𝑓
𝑓
𝑚

where 
Δ
𝑓
 is the frequency deviation.

⚙️ Default Parameters
Parameter	Value
Carrier frequency	10 kHz
Message frequency	1 kHz
Carrier amplitude	1 V
Message amplitude	1 V
Frequency deviation	5 kHz
Sampling frequency	200 kHz
Simulation time	5 ms
Modulation index	5
✨ Features
Message signal visualization
Carrier signal visualization
FM signal visualization
Frequency-domain spectrum
Modulation-index calculation
Interactive HTML output
Automated testbench
Easy-to-modify simulation parameters
🛠️ Technologies Used
Python
NumPy
Matplotlib
HTML5
JavaScript
CSS
Python unittest
📂 Project Structure
FM-Signal-Visualization-Simulator/
│
├── README.md
├── requirements.txt
│
├── src/
│   └── fm_signal_simulator.py
│
├── testbench/
│   └── test_fm_signal.py
│
└── simulation/
    └── fm_simulation.html

▶️ Installation

Install Python 3.x and then install the required libraries:

pip install -r requirements.txt

▶️ Run the Simulator

From the project root directory:

python src/fm_signal_simulator.py


The program generates the FM waveforms and frequency spectrum.

🧪 Run the Testbench

Run:

python -m unittest testbench/test_fm_signal.py


The testbench verifies:

Signal length
Modulation index
Signal amplitude
Basic FM signal generation
Input parameter validity
🌐 HTML Simulation

Open:

simulation/fm_simulation.html


in a web browser.

The HTML simulation provides an interactive visualization
