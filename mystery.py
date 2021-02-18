def mystery(num1, num2):
    #From the two values checks if num1 is bigger than num2 and then return/recall itself, but with the values swapped
    if num1 > num2: 
        return mystery(num2, num1) #So now num1 is 11 and num2 is 13, thus it will move to the next if
                                    #Second time we call it num1 is 12 and num2 is 13; move to the next if
                                    #Third time num1 is 13 and num2 is 13, move to the next if
    if num1 == num2: #third time they are the same value of 13, thus retun num1, 13 and print num2 13 and it will finish, because we don't call the mystery function anymore
        print(num2)
        return num1 #if we don't put this return, it will go into an inifinite loop
    #if we divide num2 by 2, do we get zero? First time it's 13/2, so no; Second time is the same, 13/2, so no
    if num2 % 2 == 0:
        return mystery(num1, num2 - 1) #if yes, we recall the mystery function, but with num2 -1(We never call this line)
    return mystery(num1 + 1, num2)     #Otherwise, we recall the mystery function, but with num1 + 1; first time num1 is 12, num3 is 13; go back to the start
                                       #Second time num1 becomes 13 and num3 is 13; go back to the start


mystery(13, 11)