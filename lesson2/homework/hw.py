#Homework Lesson-2 

# Task 1
Name = str(input('What is your name:'))
Year = int(input ('when were you born:'))

age = 2025 - Year
print('Name:', Name)
print('Age:', age)
# Task 2
txt = 'MsaatmiazDBMW'
print(txt[-3:])

# Task 3

txt = 'MsaatmiaTeslazD'
print(txt[8:13])
# Task 4

txt = "I'am John. I am from London"

print(txt[-6:])
# Task 5
string = str(input('Enter your str text:'))
print(string[::-1])
# Task 6

txt = str(input('Enter your str:'))
vowels = "aeiouAEIOU"
count = 0

for vowels in txt:
    if vowels in txt:
        count +=1
print('Number of vowels are',count)        

# Task 7 
lists = list(map(int, input().split(',')))


print('Max value is ',max(lists))

# Task 8

txt = str(input("Enter your txt:"))

if txt == txt[::-1]:
    print(txt, "is palindrome")
else :
    print(txt,'is not palindrome ')    

# Task 9

email = input("Enter your email: ")

domain = email.split("@")[1]

print("Domain:", domain)

# Task 10

import random
import string

length = int(input("Enter password length: "))

# All characters allowed in the password
chars = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = "".join(random.choice(chars) for _ in range(length))

print("Generated Password:", password)

