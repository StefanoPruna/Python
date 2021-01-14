def add(map, k, v):
    map.append((k, v))#adding values to the list
    return map #adding a value into the list is constant time 

def get(map, target):
    for key, val in map:
        if key == target: #print(get(map, 2))
            return val #this is a linear search to go through all items in the list
    raise KeyError

map = []
map = add(map, 1, 2) #= map, k(ey), v(al)
map = add(map, 2, 4)
print(map)
print(get(map, 2))

#To improve the linear search by using the hash function built-in Python to become a logarithmic search:
def findMap(maps, k):
    index = hash(k) % len(maps) #add the items in one of the 100 lists, constant time and so linear search
    return maps[index]

def add(maps, k, v):
    map = findMap(maps, k) 
    map.append((k, v))
    return maps

def get(map, target): #now the list is 100 times smaller, therefore even if it's still linear search, now is 100 times faster
    map = findMap(maps, target)
    for key, val in map:
        if key == target:
            return val
    raise KeyError

maps = []
for i in range(100): #creates 100 separate lists 
    maps.append([])

map = add(maps, 1, 2) #they are two different lists, so the linear search is faster
map = add(maps, 2, 4)
print(get(maps, 2))
        
#to improve it even more, we use the hashtable method:
def resize(maps, n):
    newMaps =[]
    for i in range(2* n):
        newMaps.append([])
    c = 0
    for map in maps: #go through all the maps
        for k, v in map: #go through all the values of the lists
            add(newMaps, c, k, v)
            c = c + 1
    return newMaps

def findMap(maps, k):
    index = hash(k) % len(maps)
    return maps[index]

def add(maps, n, k, v): #we add n the number of hidden maps
    if n == len(maps):
        maps = resize(maps, n) #if the list is to big, resize it
    map = findMap(maps, k) #otherwise we find the correct map
    map.append((k, v))
    return maps

def get(map, target): #stay the same finding the target
    map = findMap(maps, target)
    for key, val in map:
        if key == target:
            return val
    raise KeyError

maps = [[]] #single list to begin with

maps = add(maps, 0, 1, 2) #then we add to maps 0, 1, 2
maps = add(maps, 1, 2, 4) #then we add the 4
print(get(maps, 2))