import numpy as np
import matplotlib.pyplot as plt

# Parameter
e0 = 8.85e-12                          # Permitivitasi vakum (F/m)
A = 1e-4                               # Luas permukaan sensor (m^2)
d = 1e-3                               # Jarak pelat sensor (m)
time = np.linspace(0, 10, 100)         # Waktu diskrit (0-10 detik, 100 titik)

# Model matematis sensor kelembapan
def humidity2_signal(e0, A, d, t):
    # Model sinyal kelembapan dalam bentuk diskrit
    humidity = (e0 * A / d) * (1 + 0.5 * np.random.uniform(0.8, 1.2, size=len(t)))  
    return humidity

# Hitung sinyal kelembapan
humidity_signal = humidity2_signal(e0, A, d, time)

# Plot sinyal diskrit
plt.figure(figsize=(10, 5))
plt.stem(time, humidity_signal, linefmt="b-", markerfmt="bo", basefmt="r-", label="Humidity Signal (Diskrit)")
plt.xlabel("Time (s)")
plt.ylabel("Signal (arbitrary units)")
plt.title("Sensor Humidity")
plt.legend()
plt.grid()
plt.show()
