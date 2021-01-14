def read_data(filename):
    readings = read_data("onlinelibrary.txt")
    print(readings)

def get_average_dictionary(readings):
    pass  # TODO: Implement this correctly

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