# 4. Dice Roll Monte Carlo Simulation (np.random)
# Tasks:
# Use np.random.randint() to simulate rolling two 6-sided dice 10,000 times (create two 1D arrays of length 10,000 with values from 1 to 6).
# Add the two arrays together to get the sum of each roll.
# Calculate the experimental probability (percentage) of rolling a 7 using np.mean(sums == 7) * 100 (it should be very close to the theoretical 16.67%).
import numpy as np

#Simulating the rolling of two 6-sided dice 10,000 times
die1 = np.random.randint(1, 7, size=10000)
die2 = np.random.randint(1, 7, size=10000)

# Finding the sums of each roll
sums = die1 + die2

#Printing rolls and sums
print(die1)
print(die2)
print(sums)

# Calculate probability of getting 7
prob_7 = np.mean(sums == 7) * 100

print(f"Experimental probability:", prob_7, "%")
print("Theoretical probability:  16.67%")