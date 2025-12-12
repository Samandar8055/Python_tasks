## Lesson 8 (Parctises)
# Task 1
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    
    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: You cannot divide a number by zero!")

# task 2
user_input = input("Enter an integer: ")

try:
    number = int(user_input)
    print("You entered:", number)

except ValueError:
    print("Invalid input! You must enter a valid integer.") 
# task 3

filename = input("Enter the filename to open: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("File content:\n", content)

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")

# Task 4

a = input("Enter a number a: ")
b = input("Enter a number b: ")

try:
    # Try to convert inputs to float
    a = float(a)
    b = float(b)
    print("You entered:", a, b)

except ValueError:
    # Raise TypeError if conversion fails
    raise TypeError("Error: Both inputs must be numeric!")

# Task 5
# Write a Python program that opens a file and handles 
# a PermissionError exception if there is a permission issue.



try:
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)

except PermissionError:
    print("PermissionError: You do not have permission to open this file.")
except FileNotFoundError:
    print(" There is no error")



# task 6

'''Write a Python program that executes an operation on a list and handles an
 IndexError exception if the index is out of range.
'''
try:
   nam= ['Alex','Bob', 'Jhon','Marta']
   i = nam[0]
   print(i)

except IndexError:
  print("there is error while indexing")


# task 7

'''Write a Python program that prompts the user to input a number and handles 
a KeyboardInterrupt exception if the user cancels the input.'''

try:
    num = int(input("enter your number :"))
    print(num)
except KeyboardInterrupt:
    print(KeyboardInterrupt," occured")    


# task 8

'''Write a Python program that executes division and handles 
an ArithmeticError exception if there is an arithmetic error.
'''
try:
    a= 7
    b=0
    c = 7/0
    print(c)
except ArithmeticError:
    print("arithmetic error occured")    

# Task 9
'''Write a Python program that opens a file and handles a UnicodeDecodeError exception 
if there is an encoding issue.'''

try: 
    with open('exercies.txt','r') as f:
        f.read()
except UnicodeDecodeError:
    print(UnicodeDecodeError, 'occured')        
# task 10
'''Write a Python program that executes a list operation and handles 
an AttributeError exception if the attribute does not exist.'''

my_list = [1, 2, 3, 4]

try:
    my_list.push(5)  # ❌ lists don't have 'push' method
except AttributeError as e:
    print("AttributeError occurred:", e)

## File Input/Output Exercises
# task 1
with open('exercies.txt','r') as f:
    f.read()

# task 2
n = 5
with open('exercies.txt', 'r') as f:
    print(f.read(n))
# task 3
with open('exercies.txt', 'a') as f:
    f.write("Please, add this text to existing file")

with open("exercies.txt") as f:
    ff=f.read()
    print(ff)
# Task 4
with open('exercies.txt') as f:
    readd = f.readlines()
    print(readd[-1])
# task 5
with open('exercies.txt') as f:
    r= list(f.readlines())
    print(r)
# Task 6
'''Write a Python program to read a file line by line and store it into a variable.'''
with open('exercies.txt') as f:
    var = f.readlines()
    print(var)
# task 7
'''Write a Python program to read a file line by line and store it into an array.'''

# task 8
# Write a Python program to find the longest words.

with open('exercies.txt', 'r') as f:
    words = f.read().split()   # split the entire file into words

# Find the longest length
max_length = max(len(word) for word in words)

# Find all words with that length
longest_words = []
for word in words:
    if len(word) == max_length:
        longest_words.append(word)


print("Longest word(s):", longest_words)
print("Length:", max_length)

# task 9 
'''Write a Python program to count the number of lines in a text file.'''

with open('exercies.txt', 'r') as z:
    re = z.readlines()
    print(len(re))
# task 10
from collections import Counter
'''Write a Python program to count the frequency of words in a file.'''
with open ('exercies.txt','r') as x:
    words = x.read().split()



fequent = Counter(words).most_common()
print(fequent[0])
# Task 11
'''Write a Python program to get the file size of a plain file.'''

import os

file_path = 'exercies.txt'

try:
    file_size = os.path.getsize(file_path)
    print(f"File size: {file_size} bytes")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except PermissionError:
    print(f"Error: Insufficient permissions to access '{file_path}'.")

# Task 11
import os 

file = 'exercies.txt'
size = os.path.getsize(file)
print(size)
# Task 12
animals =['wolf','lion','tiger','horse']

with open('exercies.txt', 'w') as f:
    for item in animals:
        f.write(item + '\n')


with open('exercies.txt','r') as z:
    x = z.read()

print(x)

    

    
# task 13
'''Write a Python program to copy the contents of a file to another file.'''

with open('exercies.txt', 'r') as f:
    data = f.read()

with open('second.txt','a') as d:
    d.write(data)

with open('second.txt','r') as z:
    for i in z:
        print(i.strip())        
# task 14
'''Write a Python program to combine each line 
from the first file with the corresponding line in the second file.'''
# task 15

import random

file_name = "exercies.txt"
random_line = None
with open(file_name, "r") as file:
    for i, line in enumerate(file, 1):
        if random.randint(1, i) == 1:
            random_line = line.strip()

print("Random line:", random_line)

# task 16

file = open("second.txt", "r")

print("Is the file closed?", file.closed)  # Should be False

file.close()

print("Is the file closed now?", file.closed)  # Should be True

# task 17
with open('exercies.txt', 'r') as f:
    data = f.read().replace('\n','')

with open('second.txt','a') as d:
    d.write(data)

print("Newline characters removed successfully!") 


# Task 18

with open('exercies.txt' ,'r') as f:
    for i in f:
        print(len(i))
# task 19
import glob

characters = []

# Read all .txt files in the current folder
for filename in glob.glob("*.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
        for ch in text:
            characters.append(ch)

print(characters)

# task 20
import string

# Generate files A.txt to Z.txt
for letter in string.ascii_uppercase:
    filename = f"{letter}.txt"
    with open(filename, "w") as f:
        f.write(f"This is file {letter}.txt")

print("26 files created successfully!")

# task 21

import string

letters_per_line = 5   # change this number to whatever you want

alphabet = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'

with open("alphabet.txt", "w") as f:
    for i in range(0, len(alphabet), letters_per_line):
        line = alphabet[i:i + letters_per_line]
        f.write(line + "\n")

print("File 'alphabet.txt' created successfully.")

