# 3. Synthetic Data & Matrix Reshaping (arange + reshape)
# Tasks:
# Generate a 1D array of numbers from 1 to 24 using np.arange().
# Reshape it into a 4 x 6 2D matrix.
# Slice out the bottom-right 2 x 3 corner of that matrix.
# Replace all odd numbers in that 2 x 3 slice with -1
# imported numpy into file
import numpy as np
# arranged array
array = np.arange(1, 25)
print("Array arranged", array)
print(array.ndim)
#array reshaped in 4*6 shape
print("Array reshaped in 4*6 matrix", array.reshape(4,6))
#sliced 2*3 corner
corner = (array.reshape(4,6)[2:, 3:])
print("The 2*3 sliced corner numbers",corner)
#replaced all odd numbers in corner splice to -1
corner[corner % 2 == 1] = -1
print("All odd numbers in 2*3 slice replaced with -1", corner)
