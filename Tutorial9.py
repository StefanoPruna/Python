class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def  __str__(self):
        return (self.name, self.age)
    
    def getName(self):
        return (self.name)

    def getAge(self):
        return (self.age)

    def setName(self, newName):
        self.newName = newName

    def setAge(self, newAge):
        self.newAge = newAge

    def isOlderThan(self, other):
        return True

alice = Person("Alice", 18)
bob = Person("Bob", 19)
if bob.isOlderThan(alice):
    print("{0} is older than {1}".format(bob.getName(), alice.getName()))
else:
    print("{0} is older than {1}".format(alice.getName(), bob.getName()))
