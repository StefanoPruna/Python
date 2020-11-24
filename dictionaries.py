bookCategories = {"Book": "Chemistry", "Book2": "Computer", "Book2": "Computer", "Book4": "Biology", "Book5": "Arts", "Book5": "test"}
result = {}
for book in bookCategories:
    if book in result:
        print("duplicate")
    else:
        print("no duplicate")
    #print(bookCategories)
"""
bookCategories["Book"] = "Book0" #Now the first index has been changed to Book0 from Book
bookCategories["Book6"] = 50
print(bookCategories["Book"])
"""
def countTotal():
    available = {"pen": 3, "pencil": 5, "eraser": 2, "paper": 10}
    result = {}
    for count in available:
        result[count] = result.get(countTotal, 0) + 1
    return result

print(countTotal())

#How I have done
def countTotal2():
    available = {"pen": 3, "pencil": 5, "eraser": 2, "paper": 10}
    total = sum(available.values())
    print(total)    

countTotal2()

#How the tutorial has done
available = {"pen": 3, "pencil": 5, "eraser": 2, "paper": 10}
total = 0
for key in available:
    total += available[key]
    
print(total)