# grading_tools
Tools to automate some of the process of grading assignments via blackboard

The process is -> cd to root folder.

1. python unzip-all.py
2. Manually delete all the redundant zip files and .txt files
3. python make_grading_files.py
4. Fill the grading.txt files as you grade
5. When finished with the grading
6. python collect_grading.py
7. import grading.csv to spreadsheet for grading overview.
8. manually fill out the gradings in blackboard for a quality check.


# unzip-all.py

**Will unzip all the zips in your root folder.** 

You can then easily delete all the redundant txt files and zip files by selecting them in file explorer and deleting. They will be sorted at the top or bottom and by themselves

# make_grading_files.py

This script will go through each folder in your root and make a **grading.txt** file, with the content of the grading guide, You should copy the content of the grading guide and put it into an assignment_number.txt file as shown in assignment_5.txt.


# collect_grading.py

**Script will collect the gradings of each assignment and save them in a **grading.csv** file.**

Script is placed in root folder of the gradebook.
Will go through every folder and find the file named grading.txt and get the last line of that file.
The file should look like **assignment_5.txt**
Important part is to have a **value, i.e 90, on the last line** of the file and by itself. 

The other part of the script will make a retting.csv with the grading on each line
This can then be imported into another spreadsheet where the values are held

Keep in mind that most likely your folders will be sorted on the username while blackboard will have some other order.

To paste it into the google sheet you will most likely have to select all the rows and select sort based on column "c", or the column that holds the username. Then you click on file, import, upload and select the grading.csv. Make sure you have selected the rights cells and click replace data at selected cell. 

