def solution():
    # write your code in Python 3.6
    N = input("Insert the number: ")
    N = int(N)
    b = []
    a = []
    gap = 0
    while(N>0):
        d=N%2
        b.append(d)
        N=N//2
    b.reverse()
    # for i in b:
    #     print(i,end="")

    a.append(b)
    # print(b)
    for z in b:
        if z == 0:
            gap +=1
            
        
    print(gap)

solution()