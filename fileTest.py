#This is in reference to the report.txt
try:
    file_in = open("report.txt")
    for line in file_in:
        print(line)
except PermissionError:
    print("you don't have permission to read the file")
except IOError:
    print("I/O error reading file")