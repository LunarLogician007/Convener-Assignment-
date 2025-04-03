import numpy as np
import soundfile as sf
import scipy.signal as signal
import matplotlib.pyplot as plt
from pydub import AudioSegment

# Load the audio file
mp3_path = "your_audio_file.mp3"  # Replace with your actual file
wav_path = "converted_audio.wav"

# Convert MP3 to WAV
audio = AudioSegment.from_mp3(mp3_path)
audio.export(wav_path, format="wav")

# Read WAV file
audio_data, fs = sf.read(wav_path)

# Convert to mono if stereo
if len(audio_data.shape) > 1:
    audio_data = np.mean(audio_data, axis=1)

# Define a carrier wave
carrier_freq = 10000  # 10 kHz
T = len(audio_data) / fs

t = np.arange(len(audio_data)) / fs
carrier_wave = np.sin(2 * np.pi * carrier_freq * t)

# Modulate the audio
modulated_audio = audio_data * carrier_wave

# Add strong noise
modulated_noisy_audio = modulated_audio + np.random.normal(0, 0.3, audio_data.shape)

# Bandpass filter to isolate the carrier frequency
def bandpass_filter(data, lowcut, highcut, fs, order=4):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = signal.butter(order, [low, high], btype='band')
    return signal.filtfilt(b, a, data)

filtered_modulated_audio = bandpass_filter(modulated_noisy_audio, carrier_freq - 500, carrier_freq + 500, fs)

# Demodulate (multiply again with the carrier wave)
demodulated_audio = filtered_modulated_audio * carrier_wave

# Lowpass filter to extract original signal
def lowpass_filter(data, cutoff, fs, order=4):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='low')
    return signal.filtfilt(b, a, data)

recovered_audio = lowpass_filter(demodulated_audio, 3000, fs)

# Save processed files
sf.write("modulated_audio.wav", modulated_audio, fs)
sf.write("modulated_noisy_audio.wav", modulated_noisy_audio, fs)
sf.write("recovered_audio.wav", recovered_audio, fs)

# Plot waveforms
plt.figure(figsize=(12, 8))
plt.subplot(4, 1, 1)
plt.plot(audio_data, alpha=0.5)
plt.title("Original Audio")

plt.subplot(4, 1, 2)
plt.plot(modulated_audio, alpha=0.5, color='orange')
plt.title("Modulated Audio (Carrier Wave Applied)")

plt.subplot(4, 1, 3)
plt.plot(modulated_noisy_audio, alpha=0.5, color='r')
plt.title("Noisy Modulated Audio")

plt.subplot(4, 1, 4)
plt.plot(recovered_audio, alpha=0.5, color='g')
plt.title("Recovered Audio (After Demodulation & Filtering)")

plt.tight_layout()
plt.show()
