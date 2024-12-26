import numpy as np
import matplotlib.pyplot as plt

# Parameter model matematis
R1 = 1000  # Resistor 1 (ohm)
R2 = 2000  # Resistor 2 (ohm)
C = 1e-6   # Kapasitor (farad)

# Menghitung frekuensi berdasarkan persamaan
f = 1.44 / ((R1 + 2 * R2) * C)
print(f"Frekuensi osilasi: {f:.2f} Hz")

# Parameter untuk sinyal
duration = 0.01  # Durasi sinyal (detik)
sampling_rate = 10000  # Frekuensi sampling (Hz)
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)  # Waktu diskret

# Membuat gelombang persegi
sinyal = 0.5 * (1 + np.sign(np.sin(2 * np.pi * f * t)))  # Gelombang persegi (0 dan 1)

# Plot sinyal
plt.figure(figsize=(10, 5))
plt.plot(t, sinyal, drawstyle='steps-post', label=f'Gelombang Persegi dengan f = {f:.2f} Hz', color='blue')
plt.title('Gelombang Persegi Berdasarkan Model Matematis')
plt.xlabel('Waktu (s)')
plt.ylabel('Amplitudo')
plt.grid(True)
plt.legend()
plt.show()
