# Homework 6
# Homework Lesson 6
# Task 1
txt = input("enter the txt: ")

vowels = "aeiouAEIOU"
result = ""
count = 0

for i in range(len(txt)):
    result += txt[i]
    count += 1

    # every third character → time to place underscore
    if count == 3:
        # cannot place underscore at the end
        if i == len(txt) - 1:
            break

        # if vowel → shift underscore to next character
        if txt[i] in vowels:
            result += txt[i + 1] + "_"
            # skip one character (already added)
            txt = txt[:i+1] + txt[i+2:]
        else:
            result += "_"

        count = 0

print(result)

# task 2
'''The provided code stub reads an integer, n, 
from STDIN. For all non-negative integers i where 0 <= i < n, print i^2'''

n = int(input("enter your number "))


for i in range(n):
    print(i * i)

 ## Task N3. Loop-Based Exercises
# Exercise 1:

first_natural=1

for i in range(first_natural,11):
    print(i)


#  Exercise 2:

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#  Exercise 3:

given_number= int(input("enter your number: "))
total_sum= 0 

for i in range(1, given_number+1):
    total_sum +=i
print('Sum',total_sum)
# exercis 4

given_number= int(input("enter your number: "))
multiplication = 0

for i in range(1,given_number):
    print(i * 2)    
# Exercise 5
numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    print(i)
    
# Exercise 6: Count the total number of digits in a number

num = input("Enter a number: ")
print("Total digits:", len(num))

# Exercise 7:
for i in range(5, 0, -1):          # start from 5 down to 1
    for j in range(i, 0, -1):      # print numbers from i down to 1
        print(j, end=" ")
    print()                         # move to next line

# Exercise 8:
list1 = [10, 20, 30, 40, 50]

for i in range(len(list1) - 1, -1, -1):
    print(list1[i])

# Exercise 9: Display numbers from -10 to -1 using a for loop

for i in range(-10,0):
    print(i)
# Exercise 10: Display message “Done” after successful loop execution
for i in range(0,5):
    print(i)
print("Done!")
# Exercise 11: Print all prime numbers within a range -  non
for i in range(25,50):
    if i % i==1  and i / 1==i:
        print(i)
# Exercise 12: Display Fibonacci series up to 10 terms
terms = 10
a, b = 0, 1

print("Fibonacci sequence:")

for _ in range(terms):
    print(a, end="  ")
    a, b = b, a + b

# Exercise : 13
num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"{num}! = {factorial}")

## 4. Return Uncommon Elements of Lists
list1 = [1, 1, 2]
list2 = [2, 3, 4]

# Elements not common
result = []

# Add elements from list1 that are not in list2
for item in list1:
    if item not in list2:
        result.append(item)
    else:
        list2.remove(item)  # remove one occurrence to handle duplicates

# Add remaining elements from list2
result.extend(list2)

print(result)
