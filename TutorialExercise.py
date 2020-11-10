hours = input("How many hours did you work?")
hours = int(hours)
rate = input("How much do you get paid per hour? ")
rate = int(rate)
pay = int(hours * rate)
if hours < 10:
    pay = rate + 1
elif hours > 100:
    pay = rate + 5
print("Your pay with bonus is of: " + str(pay))