# def solution(A):
#     # write your code in Python 3.6
#     A.sort(reverse=False)
#     #print(A)
#     numbers = list(range(-1000000, 1000000))
#     for i in numbers:
#         if i not in A and i <= 0:
#             break  


# solution([1,3,4,6,1,2])

# def solution(s):
#     c = s[0]
#     if c.isupper():    # please fix condition
#         print("upper")
#     elif c.lower():  # please fix condition
#         print ("lower")
#     elif c[0] == int:  # please fix condition
#         print("digit")
#     else:
#         print("other")


# solution(2)

# def solution(S):
#     N = list(range(1, 1000000))
#     array = []
#     for char in S:
#         if S.count(char) > 1:
#             array.append(char)
    
#     print(array)


# solution("abba")

# def solution(N):
#     result = 0
#     int(x) 
#     for x in str(N):
#         print(x)
#     while N > 0:
#         num = N % 10
#         result = result + num
#         N = int(N/10)
    
#     print(result)

def rangeLetters(start, stop):
    for x in range(ord(start), ord(stop)):
        yield chr(x)

def solution(S):
    array = S.split()
    for i in array:
        if len(i) > 1:
            for x in rangeLetters("a", "z"):
                M = S.replace("?", str(x))
                if M == M[::-1]:
                    print(M)
                else:
                    print("NO")
                    break


solution("?aya?")