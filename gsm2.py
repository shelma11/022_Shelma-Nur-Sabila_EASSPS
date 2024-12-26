import numpy as np
import matplotlib.pyplot as plt

# Parameter iterasi
A = 1              # Amplitudo awal
fc = 10            # Frekuensi pembawa (Hz)
duration = 1       # Durasi sinyal (detik)
sampling_rate = 1000  # Frekuensi sampel (Hz)
iterations = 100    # Jumlah iterasi
gi = lambda x: 0.9 * x + 0.1  # Fungsi g_i sebagai contoh

# Waktu diskret
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Inisialisasi nilai awal
v = np.zeros(len(t))
v[0] = A  # Nilai awal

# Iterasi berdasarkan model matematis
for k in range(1, len(t)):
    v[k] = gi(v[k-1])  # Update nilai berdasarkan fungsi g_i

# Sinyal berbasis model
s = v * np.cos(2 * np.pi * fc * t)

# Plot sinyal
plt.figure(figsize=(10, 6))

# Plot sinyal akhir
plt.subplot(1, 1, 1)
plt.plot(t, s, label='Sinyal Sensor', color='green')
plt.title('Sinyal Berdasarkan Dinamika Model')
plt.xlabel('Waktu (s)')
plt.ylabel('Amplitudo')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
