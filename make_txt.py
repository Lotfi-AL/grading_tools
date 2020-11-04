import os
from pathlib import Path
# This script will go through each folder in your root and make a retting.txt file
# with the file content of the grading guide
# You should copy the content of the grading guide and put it into a assignment_number.txt file


def get_project_root() -> Path:
    return Path(__file__).parent.parent


get_project_root()
print(get_project_root())
rootdir = "."
liste = []
rootFileName = "ass8.txt"
if (True):
    with open(rootFileName) as f:
        for line in f:
            liste.append(line)
for subdir, dirs, files in os.walk(rootdir):
    for i in range(len(dirs)):
        with open(dirs[i]+"/retting.txt", 'w+') as f:
            for line in liste:
                f.write(line)
