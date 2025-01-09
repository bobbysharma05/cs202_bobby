'''Write recursive functions for the following:
1. Find the factorial of an input positive integer.
2. Find the sum of first N positive integers.
3. Display the Fibonacci series till N terms.'''

#Part1
def Fact(a):
    if a==1 or a==0:
        return 1
    else:
        return Fact(a-1)*a
    
n = int(input("n = "))
print(Fact(n))

#Part2
def Sum(a):
    if a==0:
        return 0
    else:
        return Sum(a-1)+a
    
n = int(input("n = "))
print(Sum(n))

#Part3
def Fibo(a):
    if a==0 or a==1:
        return 1
    else:
        return Fibo(a-1)+Fibo(a-2)
    
n = int(input("n= "))
print(Fibo(n))