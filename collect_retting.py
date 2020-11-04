import os
from pathlib import Path
import csv

# Script is placed in root folder of the gradebook.
# Will go through every folder and find the file named retting.txt and get the last line of that file.
# The file should look like this:
# ...
# ...
# ...
# 90
# the last line should hold the grading given to that specific assignment.
# The other part of the script will make a retting.csv with the grading on each line
# This can then be imported into another spreadsheet where the values are held
# Keep in mind that most likely your folders will be in alphabetical order on the username
# while blackboard will have some other order
# To paste it into the google sheet you will most likely have to select all the rows and select order based on column "c"
# or the column that holds the username.

rootdir = "."
grades = []
grades_doublecheck = []
grading_file_name = "grading.txt"


for subdir, dirs, files in os.walk(rootdir):
    try:
        with open(subdir+"/"+grading_file_name, "r") as f:
            full_file = [x for x in f]
            # your grading value should be on the last line and alone
            val = full_file[len(full_file)-1]
            grades_doublecheck.append((val, subdir))
            grades.append(val)
    except:
        pass

# Check that the folder names are correct with the grading
for grade, name in grades_doublecheck:
    print(grade, name)

# Check that the length is the same amount of assignments you grade
print(len(grades))

with open("grading.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for grade in grades:
        writer.writerow([grade]*1)
