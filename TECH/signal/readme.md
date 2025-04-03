# Modulated Audio Signal Processing Task

## Objective
In this task, you will work with a modulated audio signal and apply signal processing techniques to extract and clean the original audio. The goal is to implement a bandpass filter to remove unwanted noise and interference while recovering the original signal.

## Steps to Follow

### 1. Clone the Repository & Navigate to the Signals Folder
Clone the given repository and navigate to the folder containing the modulated audio signal.

### 2. Analyze & Demodulate the Modulated Audio Signal
- The original audio has been modulated using simple Amplitude Modulation (AM) with a sine wave of frequency `Fc`.
- Use Fast Fourier Transform (FFT) to determine the carrier frequency `Fc`.
- Demodulate the signal to recover the original audio.
- Plot and visualize all intermediate signals during this process.

### 3. Apply Bandpass Filtering & Noise Reduction
- Design and implement a bandpass filter to isolate the desired frequency range.
- Compare the filtered audio waveform with the noisy (unfiltered) waveform.

### 4. Final Submission
Submit the following:
1. All relevant graphs and plots:
   - FFT analysis
   - Demodulation steps
   - Filtered vs. noisy signals
2. The filtered audio file (cleaned version of the signal).
3. A brief README file explaining your approach (which software used) and code implementation.

## Software Requirements
You may use one of the following for this task:
- Python (NumPy, SciPy, Matplotlib)
- Scilab
- MATLAB

<img width="641" alt="image" src="https://github.com/user-attachments/assets/570db25c-0f10-4c0e-b744-42fea14e8c7e" />
