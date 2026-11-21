# Gradebook Analyzer (2D Arrays + axis Aggregations)
# Scenario: Create a 2D array representing 4 students (rows) and their scores across 3 exams (columns):
# python
# scores = np.array([
#     [85, 90, 88],
#     [72, 78, 70],
#     [95, 92, 96],
#     [60, 65, 70]
# ])
# Use code with caution.
#
# Tasks:
# Print the .shape of the array.
# Calculate the average score per student (hint: use axis=1).
# Calculate the highest score on each exam (hint: use axis=0).
# Apply a 5-point curve to everyone's 3rd exam only using array slicing (scores[:, 2]).
from unicodedata import decimal

#importing numpy into file
import numpy as np
#making numpy array
scores = np.array([[85, 90, 88],
                   [72, 78, 70],
                   [95, 92, 96],
                   [60, 65, 70]])
#printing shape of scores array
print(scores.shape)
#printing each student's average score
print(np.round(np.mean(scores, axis=1), 1))
#printing the highest score for each test
print(np.round(np.amax(scores, axis=0)))
#printing the curved score for the third test
scores[:, 2] += 5
print(scores)
