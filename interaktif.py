import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import Scale

# Inisialisasi parameter global
fs = 1000  # Sampling rate
T = 2      # Durasi sinyal

# Domain waktu
t = np.linspace(0, T, int(fs * T), endpoint=False)
noise_freq = 10
sensor_signal = np.zeros_like(t)
noise_signal = np.zeros_like(t)
result_signal = np.zeros_like(t)
dft_result = np.zeros_like(t)

# Fungsi untuk menghitung sinyal sensor
def generate_sensor(sensor_type):
    global sensor_signal
    if sensor_type == "anemometer":
        A, B, n, f, phi = 5, 2, 2, 2, np.pi / 4
        theta = np.linspace(1, 10, len(t))
        sensor_signal = (A + B * theta**n) * np.sin(2 * np.pi * f * t + phi)
    elif sensor_type == "gsm":
        A, fc = 1, 10
        v = np.zeros(len(t))
        v[0] = A 
        gi = lambda x: 0.9 * x + 0.1 
        for k in range(1, len(t)):
            v[k] = gi(v[k-1])  
        sensor_signal = v * np.cos(2 * np.pi * fc * t)
    elif sensor_type == "humidity":
        c, A, d = 8.85e-12, 1e-4, 1e-3
        sensor_signal = (c * A / d) * (1 + 0.5 * np.random.uniform(0.8, 1.2, size=len(t)))
    elif sensor_type == "raindrop":
        R1, R2, C = 25, 45, 1e-6
        f = 1.44 / ((R1 + 2 * R2) * C)
        period = 1 / f
        sensor_signal = 2 * (t % period) /period - 1
    elif sensor_type == "ultrasonic":
        speed, jarak, freq = 8, 10, 20
        ultrasonic_time = (speed * jarak) / 2
        sensor_signal = np.sin(2 * np.pi * freq * t)
    update_plots()

# Fungsi untuk menghitung noise
def generate_noise(freq):
    global noise_signal
    noise_signal = np.sin(2 * np.pi * freq * t)
    update_plots()

# Fungsi untuk melakukan operasi (penjumlahan/perkalian)
def perform_operation(operation):
    global result_signal
    if operation == "add":
        result_signal = sensor_signal + noise_signal
    elif operation == "multiply":
        result_signal = sensor_signal * noise_signal
    update_plots()

# Fungsi untuk menghitung DFT
def calculate_dft():
    global dft_result
    dft_result = np.abs(np.fft.fft(result_signal))
    update_plots()

# Fungsi untuk memperbarui subplot
def update_plots():
    ax1.clear()
    ax2.clear()
    ax3.clear()
    ax4.clear()

    ax1.plot(t, sensor_signal, label="Sensor Signal", color="cyan")
    ax1.set_title("Sensor Signal", color="black")
    ax1.legend()
    ax1.grid()
    ax1.set_facecolor("pink")

    ax2.plot(t, noise_signal, label="Noise Signal", color="yellow")
    ax2.set_title("Noise Signal", color="black")
    ax2.legend()
    ax2.grid()
    ax2.set_facecolor("pink")

    ax3.plot(t, result_signal, label="Result Signal", color="green")
    ax3.set_title("Result Signal", color="black")
    ax3.legend()
    ax3.grid()
    ax3.set_facecolor("pink")

    ax4.plot(np.fft.fftfreq(len(t), 1 / fs), dft_result, label="DFT Result", color="magenta")
    ax4.set_title("DFT Result", color="black")
    ax4.legend()
    ax4.grid()
    ax4.set_facecolor("pink")

    canvas.draw()

# GUI Setup
root = tk.Tk()
root.title("EAS SPS")
root.state('zoomed')  # Fullscreen mode
root.configure(bg="pink")

# Judul Utama
title_label = tk.Label(root, text="EAS SPS SHELMA NUR SABILA (2042231022)", font=("Helvetica", 20, "bold"), bg="pink", fg="skyblue")
title_label.pack()

# Frame untuk kontrol tombol
toolbar = tk.Frame(root, bg="pink")
toolbar.pack(side=tk.LEFT, fill=tk.Y)

sensor_buttons = ["anemometer", "gsm", "humidity", "raindrop", "ultrasonic"]
for sensor in sensor_buttons:
    btn = tk.Button(toolbar, text=sensor, command=lambda s=sensor: generate_sensor(s), bg="skyblue", fg="white", font=("Helvetica", 12, "bold"))
    btn.pack(pady=5, padx=5)

freq_slider = Scale(toolbar, from_=0, to=100, orient=tk.HORIZONTAL, label="Noise Frequency (Hz)", command=lambda val: generate_noise(int(val)), bg="pink", fg="skyblue")
freq_slider.pack(pady=5, padx=5)

btn_add = tk.Button(toolbar, text="Add", command=lambda: perform_operation("add"), bg="skyblue", fg="white", font=("Helvetica", 12, "bold"))
btn_add.pack(pady=5, padx=5)

btn_multiply = tk.Button(toolbar, text="Multiply", command=lambda: perform_operation("multiply"), bg="skyblue", fg="white", font=("Helvetica", 12, "bold"))
btn_multiply.pack(pady=5, padx=5)

btn_dft = tk.Button(toolbar, text="Calculate DFT", command=calculate_dft, bg="skyblue", fg="white", font=("Helvetica", 12, "bold"))
btn_dft.pack(pady=5, padx=5)

# Frame untuk plot
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))
fig.tight_layout(pad=4.0)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(fill=tk.BOTH, expand=True)

root.mainloop()
