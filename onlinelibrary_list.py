#LIST TO DO:
#PRODUCE A LIST OF DIFFERENT CATEGORIES, SORTED FROM THE ONE WITH THE HIGHEST AVERAGE TO THE ONE WITH THE LOWEST
#ADD READ_DATA AND GET_AVERAGE_DICTIONARY FUNCTIONS
#ADD COMMENTS
#INCLUDE AND CREATE A README.MD FILE
#SUBMIT IT AS A SINGLE .TGZ FILE NAMED a3.tgz

def read_data(filename):
    pass  # TODO: Implement this correctly

def get_average_dictionary(readings):
    pass  # TODO: Implement this correctly

def getData():
    try:
        file_in = open("onlinelibrary.txt")
        for averages in file_in:
            print(averages)
    except PermissionError:
        print("you don't have permission to read the file")
    except IOError:
        print("I/O error reading file")


FILENAME = "onlinelibrary.txt"

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