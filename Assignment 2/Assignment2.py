# Program Name: Assignment2.py
# Course: IT3883 / Section W01
# Student Name: Jaxon Evans
# Assignment Number: Assignment 2
# Due Date: 02/18/2026
# Purpose: We have the students grades as an input and calculate their averages
# We then display them from highest to lowest using our formula
# Resources Used: Python review modules and previous python assignments

data = []
# input student's grades file
file = input("File: ")
f = open(file, "r")
for line in f:
    #divides the names and grades
    parts = line.split()
    name = parts[0]
    total = 0
    i = 1
    while i < len(parts):
        total = total + int(parts[i])
        i = i + 1
    #total scores
    scores = len(parts) - 1
    #average formula
    avg = total / scores
    data.append([name, avg])
f.close()
# helps rank the order based on grades
i = 0
while i < len(data):
    j = 0
    while j < len(data) - 1:
        if data[j][1] < data[j + 1][1]:
            temp = data[j]
            data[j] = data[j + 1]
            data[j + 1] = temp
        j = j + 1
    i = i + 1

# results time
i = 0
while i < len(data):
    print(data[i][0], format(data[i][1], ".2f"))
    i = i + 1
