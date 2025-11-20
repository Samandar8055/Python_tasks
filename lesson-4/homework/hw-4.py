# task 1 dictionery
my_dict = {1: 10, 2: 5, 3: 7, 4: 1}


# Task 2

number = {0: 10, 1: 20}
add= number.update({2:30})

print(number)
# task 3

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

dicthree = dic1 | dic2 | dic3

print(dicthree)
# task 4
n = int(input("Enter a number: "))

result = {}

for x in range(1, n + 1):
    result[x] = x * x

print(result)



#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# task 5
n = 15

result = {}

for x in range(1, n + 1):
    result[x] = x * x

print(result)

# Task 1 set
fist_set = {'ali', 'vali','mali'}
print(type(fist_set))
# Task 2
name = {'ali', 'vali','mali'}
second_name= {'brown','will','mark'}
full_na = name | second_name
print(full_na)
# Task 3
animal = {'wolf','lion','giraf','horse'}
add = animal.add('tiger')
print(animal)
# task 4
animal = {'wolf','lion','giraf','horse', 'tiger'}
re = animal.discard('wolf')
print(animal)
# Task 5
animal = {'wolf','lion','giraf','horse', 'tiger'}
if 'wolf' in animal:
    animal.remove('wolf')
else:
    print(animal)   


print(animal)

