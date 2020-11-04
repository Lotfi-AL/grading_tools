# grading_tools
Tools to automate some of the process of grading assignments via blackboard

# unzip-all.py

Will unzip all the zips in your root folder. You can then easily delete all the redundant txt files and zip files by selecting them in file explorer and deleting. They will be sorted at the top or bottom and by themselves


# Collect_grading.py

Script is placed in root folder of the gradebook.
Will go through every folder and find the file named retting.txt and get the last line of that file.
The file should look #### assignment_5.txt

, something like this:
...
...
...
90


# the last line should hold the grading given to that specific assignment.
# The other part of the script will make a retting.csv with the grading on each line
# This can then be imported into another spreadsheet where the values are held
# Keep in mind that most likely your folders will be in alphabetical order on the username
# while blackboard will have some other order
# To paste it into the google sheet you will most likely have to select all the rows and select order based on column "c"
# or the column that holds the username.
