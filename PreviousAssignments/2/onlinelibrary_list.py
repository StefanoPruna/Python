import os

#Open the text file in read mode
FILENAME = open("onlinelibrary.txt", "r")

#Function 1: loops the file that we opened, assigned each category as a key of "readings" dictionary and combines the values of the same category together as a list
def read_data(filename):
    readings = {}
    for line in FILENAME:  
        (k, v) = line.strip().split(",")
        if k in readings:
            readings[k].append(v)
        else:
            readings[k] = [v]
    return readings
        
#Calling the function 1, print the "readings" dictionary and close the opened file  
readings = read_data("readings.txt")
print(readings)
FILENAME.close()

#Function 2: provides the average of each category from the "readings" dictionary      
def get_average_dictionary(readings):
    averages = {}
    for k in readings:
        values = sum([ int(v) / 2 for v in readings[k] ])
        averages.update({k: values })
    return averages

#Calling the function 2 and print the new dictionary with the average results
averages = get_average_dictionary(readings)
print(averages)
    
if __name__ == "__main__":
    try:
        readings = read_data(FILENAME)
        averages = get_average_dictionary(readings)

        #Loops through the keys in averages, sorted from that with the largest associated value in averages to the lowest - see https://docs.python.org/3.5/library/functions.html#sorted for details
        for category in sorted(averages, key = averages.get, reverse = True):
            print(category, averages[category])

    except (IOError, ValueError):
        print("Error reading {}".format(FILENAME))
        print("Please ensure the file exists and matches the required format")
        print("(each line should begin with a day name, followed by a comma, followed by a reading value)")