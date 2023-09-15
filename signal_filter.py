# -*- coding: utf-8 -*-
"""
Dibuat oleh Soekilerr a.k.a AFM
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
time_values = np.linspace(0, 10, 1000)
signal_data = np.sin(2 * np.pi * time_values) + 0.5 * np.random.normal(size=len(time_values))

def apply_moving_average_filter(data, window_size):
    window = np.ones(window_size) / float(window_size)
    filtered_data = np.convolve(data, window, "same")
    return filtered_data

window_size = 20
filtered_signal = apply_moving_average_filter(signal_data, window_size)

plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(time_values, signal_data, label="Noisy Signal", color="blue")  # Mengubah warna menjadi biru
plt.title("Noisy Signal")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(time_values, filtered_signal, label="Filtered Signal", color="orange")  # Mengubah warna menjadi orange
plt.title("Filtered Signal")
plt.grid(True)

plt.tight_layout()
plt.show()
