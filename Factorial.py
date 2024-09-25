# Python 3 program to find
# factorial of given number
def factorial(n):
	
	# single line to find factorial
	return 1 if (n==1 or n==0) else n * factorial(n - 1)

# Driver Code
num = int(input("Enter a number here:"))
print("Factorial of given number is:",factorial(num))


#2nd method to find factorial
import math

n=int(input("Enter a Number Here:"))

f= math.factorial(n)
print(f)