# Task 1

fruits= ['mango','kiwi','apple','cherry','banana']
print(fruits[2])


# Task 2

numbers = [1,2,3,4,5,6,7]
number2= [8,9,10,11,12,13]

numbers.extend(number2)
print(numbers)
# Task 3

numbers = [1,11,3,422,52,64,7,18,9,150,131,112,132,140,155]
first = numbers[0]
last = numbers[-1]
middle = numbers[8]

new_list = []
new_list.append(first)
new_list.append(last)
new_list.append(middle)

# 2nd method
new_list2 = [first,last, middle]

print(new_list)
print(new_list2)
# Task 4
movies = ['Art','Harry-Poter','Thegotfather','tatris','Monoco']
t = tuple(movies)
print(type(t))

# task 5 

cities = ['London','Moscow','Paris','New-York','Bukhares']

if 'Paris' in cities:
    print('Yes')
else:
    print('No')    
# task 6

d_number = [12,22,14,56,65,24,76,12,44,884,46]

# method 1
duplicate_list= d_number.copy()
print(duplicate_list)

# method 2
m_list = d_number * 2
print(m_list)

# Task 7
s_number = [12,22,14,56,65,24,76,12,44,884,46]

#methid 1
s_number[0]=46
s_number[-1]=12

#method 2
s_number[0], s_number[-1] = s_number[-1], s_number[0]

print(s_number)
# Task 8 
## 8. Slice a Tuple
#Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.

numbers = (12,23,11,1,3,53,231,122,334,65,3432,11)
s= numbers[2:7]
print(s)

# Task 9 
colors = ['red','yellow', 'pink', 'blue', 'purple','black','light-yellow','green','blue']
n= colors.count('blue')
print(n)
# Task 10

animals = ('wolf','lion','bird','giraf','snake')
i = animals.index('lion')

print(i)
print(type(animals))

# Task 11

s_numbers=(122,22,13,422,12,431,11245)
z_numbers =(2,4,76,99,65,3,34,54,23,111)

s_number += z_numbers
print(type(s_number))
# task 12
animals = ('wolf','lion','bird','giraf','snake')
numbers =[12,22,12,31,41,3331,311554,452,133]

length_a= len(animals)
length_n = len(numbers)
print(length_a)
print(length_n)
# task 13
t_numbers = (12,2,11,41,88,91)

l_number = list(t_numbers)
print(type(l_number))
# task 14
tuple_numbers= (12,22,14,54,775,886,445,23,12,430,89,93,61)

min_tuple_n= min(tuple_numbers)
max_tuple_n = max(tuple_numbers)

print(min_tuple_n)
print(max_tuple_n)
# Task 15
r_animals = ('wolf','lion','bird','giraf','snake')
reverse_a = r_animals[::-1]

print(reverse_a)

