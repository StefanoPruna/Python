yourAge = input("How old are you? ")
yourAge = int(yourAge)
beforeHundred = int(100 - yourAge)

if yourAge >= 100:
    print("You have already turned 100!")
elif yourAge <= 0:
    print("Try again after you are born!")
else:
    print("You will be 100 in " + str(beforeHundred) + "years!")

