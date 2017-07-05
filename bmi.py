
# Import numpy
import numpy as np

# Build an array of my recent weigh in data

np_weight = np.array([64.4, 64.7, 64.5, 64.4, 64.1, 63.9, 65.5, 64.6, 64.8, 64.8, 64.9, 65.0, 64.1, 63.7])

# Calculate the BMI against each of these
height = 1.68

np_bmi = np_weight / height ** 2

print (np_bmi)

import csv

with open('responses-noNAN.csv') as csvfile:
    next(csvfile)
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV)

    student_weights = []
    student_heights = []

    for row in readCSV:
    	student_heights.append(row[-9])
    	student_weights.append(row[-8])


np_student_heights = np.array(student_heights)
np_student_heights = np_student_heights.astype(np.int)

np_student_weights = np.array(student_weights)
np_student_weights = np_student_weights.astype(np.int)

np_student_bmi = 10000 * np_student_weights/np_student_heights ** 2
print(np_student_bmi)
	


# Correlation of BMI with age, gender, spending on healthy eating etc

print(np.shape(np_student_bmi))






#genfromtxt("world_alcohol.csv", skip_header = 1, delimiter = ",", dtype = "U75")
