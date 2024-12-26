import numpy as np
import matplotlib.pyplot as plt

# Parameter
speed = 8                   # Kecepatan suara (m/s)
jarak = 10                   # Waktu tempuh (detik)
sampling_rate = 17     # Frekuensi sampling (Hz)
frequency = 20               # Frekuensi sinyal (Hz)

# Model matematis sensor ultrasonik
def ultrasonic2_signal(speed, jarak, sampling_rate, frequency):
    ultrasonic = (speed * jarak) / 2  # Hitung jarak berdasarkan model21
    t = np.linspace(0, ultrasonic, int(sampling_rate * ultrasonic), endpoint=False)  # Waktu sampling
    signal = np.sin(2 * np.pi * frequency * t)  # Sinyal sinusoidal
    return t, signal  # Kembalikan waktu dan sinyal

# Hitung sinyal
t, signal = ultrasonic2_signal(speed, jarak, sampling_rate, frequency)

# Plot sinyal
plt.figure(figsize=(10, 5))
plt.plot(t, signal, label="Ultrasonic Signal")  # Gunakan hasil t dan signal
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("Sensor Ultrasonik")
plt.legend()
plt.grid()
plt.show()
