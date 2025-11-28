# Task 1
year = int(input("Enter the year:"))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year,' is a  leap year')
else:
    print(year,' is not a  leap year') 


# Task 2

n = int(input("Enter your number:"))

if n%2 != 0:
    print(n,'is weird')
elif n%2 == 0 and 2<=n>=5:
    print('Not Weird')
elif n%2 == 0 and 6<=n>=20:
    print('Weird')  
elif n%2 == 0 and n>20:  
    print('Not Weird')   

# Task 3

# Solution 1
a = int(input('Enter the number:'))
b = int(input('Enter the number:'))

for x in range(a,b):
    if x % 2== 0:
         print(x)
   

# Solusion 2

a = int(input('Enter the number: '))
b = int(input('Enter the number: '))

start = a + (a % 2)      # if a is odd → next even; if even → a
evens = list(range(start, b + 1, 2))

print(*evens, sep="\n")
