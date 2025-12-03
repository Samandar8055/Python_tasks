# lesson-7

## Lesson 7 (functions )
 
# task 1
def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True   # <-- You forgot this line
is_prime(7)

# task 2

k = input("enter your number: ")

def digit_sum(k):
    digits = map(int, k)   # convert each character into an integer
    return sum(digits)

print(digit_sum(k))

# Task 3

def powers_of_two(N):
    k = 1  # 2**0 = 1, lekin biz 2 dan boshlaymiz
    while k <= N:
        print(k, end=" ")
        k *= 2

powers_of_two(20)        


