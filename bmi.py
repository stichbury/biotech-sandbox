
# Import numpy
import numpy as np

# Build an array of my recent weigh-in data
np_weight = np.array([64.4, 64.7, 64.5, 64.4, 64.1, 63.9, 65.5, 64.6, 64.8, 64.8, 64.9, 65.0, 64.1, 63.7])

# Calculate the BMI against each of these
height = 1.68

np_bmi = np_weight / height ** 2

print (np_bmi)

# -------------------------------------------
# TO DO - work out how to manage NaN values and use original responses.csv (so I can put this in a Kaggle notebook)
# What I've done to the data so far: remove NaN values for age, height and weight, spending on healthy eating, healthy lifestyle, active & passive sports. 
# Fixed one value of height from 62 to 162 (probably was a typo, otherwise an outlier)

np_responses = np.genfromtxt("responses-noNAN.csv", skip_header = 1, delimiter = ",", dtype = "U75")
np_student_weights = np_responses[:,-8]
np_student_heights = np_responses[:,-9]

np_student_heights = np_student_heights.astype(np.int)
np_student_weights = np_student_weights.astype(np.int)


np_student_bmi = 10000 * np_student_weights/np_student_heights ** 2
print(np_student_bmi)	

# Visualisation of BMI with age, gender, spending on healthy eating etc

import matplotlib.pyplot as plt

# First, age

np_student_ages = np_responses[:,-10]
np_student_ages = np_student_ages.astype(np.int)

plt.scatter(np_student_ages, np_student_bmi)
plt.show()


# Build a column of data that combines
# -11: Spending on healthy eating
# 75: Living a healthy lifestyle
# 53: Passive sport
# 54: Active sport

np_healthperception = np_responses[:,-11]
np_healthperception_int = np_healthperception.astype(np.int)

np_healthperception = np_responses[:,75]
np_healthperception_int = np_healthperception_int + np_healthperception.astype(np.int)

np_healthperception = np_responses[:,53]
np_healthperception_int = np_healthperception_int + np_healthperception.astype(np.int)

np_healthperception = np_responses[:,54]
np_healthperception_int = np_healthperception_int + np_healthperception.astype(np.int)

plt.scatter(np_healthperception_int, np_student_bmi)
plt.show()
