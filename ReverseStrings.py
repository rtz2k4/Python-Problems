#Reverse a string using Stack


def reversebyStack(str):
    stack = [] 

    for i in range(len(str)):
        stack.append(str[i])

    for i in range (len(str)):
        str[i] = stack.pop()

#Reverse a string using two pointers
        
def reverseStr(str):
    n = len(str)

    i, j = 0, n-1

    while i<j:
        str[i], str[j] = str[j], str[i] 
        i += 1
        j -= 1

#Reverse a string using recursion
#The recursive alg to reverse a string works by
#swapping the first and last characters until
#the middle of the string is reached.
#This process is performed through recursive calls
#Characters at positions i and n-i-1 are swapped 
# and i is incremented
        

def recursiveRev(str, i=0):
    n = len(str)
    if n == n // 2:
        return
    str[i], str[n-i-1] = str[n-i-1], str[i]

    recursiveRev(str, i+1)


#There's also an inbuilt method in python to reverse a string
# For example str = Example, reverseStr = str[::-1]