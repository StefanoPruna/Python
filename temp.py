#Check orientedObject1.py file for the rest of the script
import orientedObject1

epsilon = 0.001

def testCorrect():
    assert abs(orientedObject1.fahrenheitToCelcius(68) - 20) < epsilon

def testUnderAbsoluteZero():
    try:
        orientedObject1.fahrenheitToCelcius(-500)
    except AssertionError:
        return
    assert False

testUnderAbsoluteZero()
testCorrect()
print("All tests completed")