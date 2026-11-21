
# 1. Temperature Converter & Anomaly Filter (Vectorization + Boolean Masking)
# Scenario: You have a week of daily Celsius temperatures recorded by a weather sensor: [18.5, 21.0, 29.5, 31.2, 19.8, 27.4, 33.0].
# Tasks:
# Convert the list into a NumPy array.
# Convert all temperatures to Fahrenheit in one line using the formula \(F = C \times 1.8 + 32\).
# Use boolean filtering to extract only the temperatures above 85°F and print how many hot days occurred.

import numpy as np
temperatures = np.array([18.5, 21.0, 29.5, 31.2, 19.8, 27.4, 33.0])
fahrenheit = temperatures * 1.8 + 32
hotDay = fahrenheit[fahrenheit > 85]
print("The hot days are:", hotDay)
print("The number of hot days are", hotDay.size)