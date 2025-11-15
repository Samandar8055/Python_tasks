""" Lesson 1 Home work

Tasks :
1. Given a side of square. Find its perimeter and area. 
2. Given diameter of circle. Find its length. 
3. Given two numbers a and b. Find their mean. 
4. Given two numbers an and b. Find their sum, product and square of each number. 
5. Give formulas for each task 
""" 
# Task 1

side= int(input ('Enter the side length:'))

Perimeter = side*4
Area = side** 2

print('Perimeter:',Perimeter)
print('Area:',Area)

# Task 2

DofCircle  = int(input ('Enter the diameter of length:'))

lenght = DofCircle * 3.14

print('Lenght:',lenght)

#Task 3

a = int(input ('Enter the length of a:'))
b = int(input ('Enter the length of b:'))

Mean= (a + b) /2

print('Mean:',Mean)

# Task 4
a = int(input ('Enter the length of a:'))
b = int(input ('Enter the length of b:'))

Sum = a + b
Product = a * b
squares = a ** 2 and b ** 2

print('Sum', Sum)
print('Product', Product)
print('Square of each a and b',squares)

