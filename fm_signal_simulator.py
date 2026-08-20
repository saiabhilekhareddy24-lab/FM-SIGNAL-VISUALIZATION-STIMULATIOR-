import numpy as np
import matplotlib.pyplot as plt

---------------------------------------------------------
FM Signal Visualization Simulator
---------------------------------------------------------

def generate_fm_signal(
carrier_frequency=10_000,
message_frequency=1_000,
carrier_amplitude=1.0,
message_amplitude=1.0,
frequency_deviation=5_000,
sampling_frequency=200_000,
duration=0.005
):
"""
Generate message, carrier and FM signals.
"""

if carrier_frequency <= 0:
    raise ValueError("Carrier frequency must be positive.")

if message_frequency <= 0:
    raise ValueError("Message frequency must be positive.")

if sampling_frequency <= 2 * carrier_frequency:
    raise ValueError(
        "Sampling frequency must be greater than twice "
        "the carrier frequency."
    )

if duration <= 0:
    raise ValueError("Duration must be positive.")

# Time vector
t = np.arange(0, duration, 1 / sampling_frequency)

# Modulation index
beta = frequency_deviation / message_frequency

# Message signal
message = message_amplitude * np.sin(
    2 * np.pi * message_frequency * t
)

# Carrier signal
carrier = carrier_amplitude * np.sin(
    2 * np.pi * carrier_frequency * t
)

# FM signal
fm_signal = carrier_amplitude * np.sin(
    2 * np.pi * carrier_frequency * t
    + beta * np.sin(2 * np.pi * message_frequency * t)
)

return t, message, carrier, fm_signal, beta


def calculate_spectrum(signal, sampling_frequency):
"""
Calculate single-sided magnitude spectrum.
"""

n = len(signal)

fft_signal = np.fft.fft(signal)
frequencies = np.fft.fftfreq(
    n,
    d=1 / sampling_frequency
)

magnitude = np.abs(fft_signal) / n

positive = frequencies >= 0

return frequencies[positive], magnitude[positive]


def main():

# Simulation parameters
fc = 10_000          # Carrier frequency
fm = 1_000           # Message frequency
Ac = 1.0             # Carrier amplitude
Am = 1.0             # Message amplitude
delta_f = 5_000      # Frequency deviation
fs = 200_000         # Sampling frequency
duration = 0.005     # Simulation duration

# Generate signals
t, message, carrier, fm_signal, beta = generate_fm_signal(
    fc,
    fm,
    Ac,
    Am,
    delta_f,
    fs,
    duration
)

# Calculate spectrum
frequencies, magnitude = calculate_spectrum(
    fm_signal,
    fs
)

# Print simulation information
print("=" * 50)
print("FM SIGNAL VISUALIZATION SIMULATOR")
print("=" * 50)

print(f"Carrier Frequency     : {fc / 1000:.2f} kHz")
print(f"Message Frequency     : {fm / 1000:.2f} kHz")
print(f"Frequency Deviation   : {delta_f / 1000:.2f} kHz")
print(f"Modulation Index      : {beta:.2f}")
print(f"Sampling Frequency    : {fs / 1000:.2f} kHz")
print(f"Simulation Duration   : {duration * 1000:.2f} ms")

# Create figure
fig, axes = plt.subplots(4, 1, figsize=(12, 10))

# Message signal
axes[0].plot(
    t * 1000,
    message,
    color="blue"
)
axes[0].set_title("Message Signal")
axes[0].set_xlabel("Time (ms)")
axes[0].set_ylabel("Amplitude")
axes[0].grid(True)

# Carrier signal
axes[1].plot(
    t * 1000,
    carrier,
    color="green"
)
axes[1].set_title("Carrier Signal")
axes[1].set_xlabel("Time (ms)")
axes[1].set_ylabel("Amplitude")
axes[1].grid(True)

# FM signal
axes[2].plot(
    t * 1000,
    fm_signal,
    color="red"
)
axes[2].set_title(
    f"FM Signal (Modulation Index = {beta:.2f})"
)
axes[2].set_xlabel("Time (ms)")
axes[2].set_ylabel("Amplitude")
axes[2].grid(True)

# Frequency spectrum
axes[3].plot(
    frequencies / 1000,
    magnitude,
    color="purple"
)
axes[3].set_xlim(0, 25)
axes[3].set_title("FM Frequency Spectrum")
axes[3].set_xlabel("Frequency (kHz)")
axes[3].set_ylabel("Magnitude")
axes[3].grid(True)

plt.tight_layout()

# Save output
plt.savefig(
    "fm_simulation_output.png",
    dpi=300
)

plt.show()


if name == "main":
main()
