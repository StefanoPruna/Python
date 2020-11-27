def fahrenheitToCelcius(temp):
    assert type(temp) in (int, float)
    assert temp >= -459.67 #Under absolute zero
    return (temp - 32) / 1.8

#assert abs(orientedObject1.fahrenheitToCelcius(68) - 20) < epsilon

if __name__ == "__main__": #We can call this script with the temp.py script
    print(fahrenheitToCelcius(-500))

    #check the temp.py file for more assert I didn't implement here