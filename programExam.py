lions = []
dingoes = [1,2,3,4,5,6,7]
for i in dingoes:
    aver = sum(dingoes) / i
kangaroos = [10, 5, 3, 7, 5]
for k in kangaroos:
    avg = sum(kangaroos) / k

def analyseSightings(sightings):
    if sightings == lions:
        print("No data to analyse")
    elif sightings == dingoes:
        print("Maximum sighted in one day: " + str(max(dingoes)))
        print("Minimum sighted in one day: " + str(min(dingoes)))
        print("Average sighted for all days: " + str(aver))
    elif sightings == kangaroos:
        print("Maximum sighted in one day: " + str(max(kangaroos)))
        print("Minimum sighted in one day: " + str(min(kangaroos)))
        print("Average sighted for all days: " + str(avg))


print("Lions: ")
analyseSightings(lions)
print("Dingoes: ")
analyseSightings(dingoes)
print("Kangaroos: ")
analyseSightings(kangaroos)