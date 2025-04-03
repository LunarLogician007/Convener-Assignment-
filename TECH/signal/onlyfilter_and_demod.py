import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Load the audio file
file_path = "signal/modulated_noisy_audio.wav"
sample_rate, audio_data = wav.read(file_path)

# Convert to mono if stereo
if len(audio_data.shape) > 1:
    audio_data = np.mean(audio_data, axis=1)

# Plot the original waveform
plt.figure(figsize=(12, 4))
plt.plot(audio_data[:sample_rate], alpha=0.7)
plt.title("Original Modulated Noisy Audio Waveform")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

# Compute and plot the original frequency spectrum
fft_spectrum = np.fft.fft(audio_data)
frequencies = np.fft.fftfreq(len(fft_spectrum), 1/sample_rate)
plt.figure(figsize=(12, 4))
plt.plot(frequencies[:len(frequencies)//2], np.abs(fft_spectrum[:len(frequencies)//2]))
plt.title("Frequency Spectrum of Modulated Noisy Audio")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid()
plt.show()

# Generate the carrier wave
carrier_freq = 10000  # 10 kHz
t = np.arange(len(audio_data)) / sample_rate
carrier_wave = np.sin(2 * np.pi * carrier_freq * t)

# Multiply the modulated signal by the carrier to shift it back to baseband
demodulated_signal = audio_data * carrier_wave

# Compute and plot the frequency spectrum after demodulation
demod_fft_spectrum = np.fft.fft(demodulated_signal)
plt.figure(figsize=(12, 4))
plt.plot(frequencies[:len(frequencies)//2], np.abs(demod_fft_spectrum[:len(demod_fft_spectrum)//2]))
plt.title("Frequency Spectrum After Demodulation")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid()
plt.show()

# Design a low-pass filter to remove high-frequency noise
def lowpass_filter(signal, cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return filtfilt(b, a, signal)

# Apply low-pass filter (cutoff at 4 kHz, assuming speech or music signal)
filtered_signal = lowpass_filter(demodulated_signal, 4000, sample_rate)

# Compute and plot the frequency spectrum after filtering
filtered_fft_spectrum = np.fft.fft(filtered_signal)
plt.figure(figsize=(12, 4))
plt.plot(frequencies[:len(frequencies)//2], np.abs(filtered_fft_spectrum[:len(filtered_fft_spectrum)//2]))
plt.title("Frequency Spectrum After Filtering")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid()
plt.show()

# Save the processed audio
output_path = "demodulated_filtered_audio.wav"
wav.write(output_path, sample_rate, filtered_signal.astype(np.int16))

# Plot the refined demodulated waveform
plt.figure(figsize=(12, 4))
plt.plot(filtered_signal[:sample_rate], alpha=0.7)
plt.title("Refined Demodulated and Filtered Audio Waveform")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

print(f"Demodulated audio saved as {output_path}")
