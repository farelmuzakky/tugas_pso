#!/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def customFastFourierTransform(data):
    length = len(data)
    
    if length == 1:
        return data
    else:
        # Implementing a recursive approach
        even_F = customFastFourierTransform(data[::2])
        odd_F = customFastFourierTransform(data[1::2])
        
        # Frequency factor
        factor = np.exp(-2j * np.pi * np.arange(length) / length)
        
        # Build the FFT array
        FFT_result = np.concatenate([
            even_F + factor[:int(length/2)] * odd_F,
            even_F + factor[int(length/2):] * odd_F
            ])
        
        return FFT_result

# Identification
print("Name: Ahnaf Farel Muzakky")
print("NRP: 5009201003")

# Generate an array with linear spacing
X_values = np.arange(0, 1, 1.0/128)

# Generate a sine function
Y_values = np.sin(2 * np.pi * X_values)

# Create an array with random noise of the same length as X
Random_noise = np.random.rand(len(X_values))

# Add noise to the sine wave
Noisy_Y = Y_values + Random_noise

# Perform FFT on both signals
FFT_Y = np.abs(customFastFourierTransform(Y_values))
FFT_Noisy_Y = np.abs(customFastFourierTransform(Noisy_Y))

# Plot the results with different colors
figure, axes = plt.subplots(2, 2)
axes[0, 0].plot(X_values, Y_values, color='blue')
axes[0, 1].plot(FFT_Y, color='green')
axes[1, 0].plot(X_values, Noisy_Y, color='red')
axes[1, 1].plot(FFT_Noisy_Y, color='purple')

plt.show()