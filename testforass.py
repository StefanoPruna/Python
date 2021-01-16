import os
import collections, functools, operator
from statistics import mean


FILENAME = open("onlinelibrary.txt", "r")

def read_data(filename):
    readings = {}
    for line in FILENAME:
        (k, v) = line.strip().split(",")
        if k in readings:
            readings[k].append(v)
        else:
            readings[k] = [v]
    return readings
        
   
readings = read_data("readings.txt")
print(readings)
FILENAME.close()

def get_average_dictionary(readings):
    averages = {}
    for k in readings:
        values = sum([ int(v) / 2 for v in readings[k] ])
        averages.update({k: values })
    return averages


averages = get_average_dictionary(readings)
print(averages)


if __name__ == "__main__":
    try:
        readings = read_data(FILENAME)
        averages = get_average_dictionary(readings)

        # Loops through the keys in averages, sorted from that with the largest associated value in averages to the lowest - see https://docs.python.org/3.5/library/functions.html#sorted for details
        for category in sorted(averages, key = averages.get, reverse = True):
            print(category, averages[category])

    except (IOError, ValueError):
        print("Error reading {}".format(FILENAME))
        print("Please ensure the file exists and matches the required format")
        print("(each line should begin with a day name, followed by a comma, followed by a reading value)")