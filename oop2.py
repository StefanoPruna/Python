a = [1, 4, 3]
a.sort(reverse = False) #method, not function 
print(a) 

class myClass:
    x = 5

myVar = myClass()
print(myVar.x)


class Time:
    """ Represents a time of day
    attributes: hour, minute, second """
    def printTime(self):
        print("{:2d}:{:2d}:{:2d}".format(self.hour, self.minute, self.second))
    #or we can use the __str__() function
    def __str__(self):
        return "{:2d}:{:2d}:{:2d}".format(self.hour, self.minute, self.second)

t = Time()
t.hour = 12
t.minute = 20
t.second = 18
#t.printTime()
print(t)

# A better way to code the above is to use __init__() function
# Create a class named Person, use the __init__() function to assign values for name and age:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Loske", 41)

print("My name is", p.name, "and my age is", p.age)

#Objects can also contain methods. Methods in objects are functions that belong to the object
class People:
    def __init__(self, surname, eta):
        self.surname = surname
        self.eta = eta
    
    def  myFunc(self):
        print("My name is " + self.surname)

p2 = People("Loske", 41)
p2.myFunc()
