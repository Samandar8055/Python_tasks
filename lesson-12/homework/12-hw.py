##  Thread Lesson-12 Hw
# task 1

'''Write a Python program that checks whether a given range of numbers contains prime numbers.
 Divide the range among multiple threads to parallelize the prime checking process. 
 Each thread should be responsible for checking a subset of the range,
 and the main program should print the list of prime numbers found.'''


import threading

# Prime checker
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


# Thread task
def check_primes(start, end, primes):
    for num in range(start, end):
        if is_prime(num):
            with lock:
                primes.append(num)


# Input
start_range = 1
end_range = 50
num_threads = 5

# Shared data
primes = []
lock = threading.Lock()
threads = []

step = (end_range - start_range) // num_threads

# Create threads
for i in range(num_threads):
    start = start_range + i * step
    end = start + step

    if i == num_threads - 1:
        end = end_range  # last thread takes rest

    t = threading.Thread(target=check_primes, args=(start, end, primes))
    threads.append(t)
    t.start()

# Wait for all threads
for t in threads:
    t.join()

# Output
print("Prime numbers found:")
print(sorted(primes))



'''Exercise 2: Threaded File Processing

Write a program that reads a large text file containing lines of text.
Implement a threaded solution to count the occurrence of each word in the file.
Each thread should process a portion of the file, 
and the main program should display a summary of word occurrences across all threads.'''

import threading

# Thread function
def count_words(lines_chunk, global_count):
    local_count = {}

    for line in lines_chunk:
        words = line.lower().split()
        for word in words:
            local_count[word] = local_count.get(word, 0) + 1

    # Merge safely
    with lock:
        for word, count in local_count.items():
            global_count[word] = global_count.get(word, 0) + count


# Read file
with open("threating.txt", "r") as f:
    lines = f.readlines()

num_threads = 4
threads = []
global_word_count = {}
lock = threading.Lock()

chunk_size = len(lines) // num_threads

# Create threads
for i in range(num_threads):
    start = i * chunk_size
    end = start + chunk_size

    if i == num_threads - 1:
        end = len(lines)  # last thread takes remaining lines

    t = threading.Thread(
        target=count_words,
        args=(lines[start:end], global_word_count)
    )
    threads.append(t)
    t.start()

# Wait for all threads
for t in threads:
    t.join()

# Display result
print("Word occurrences:")
for word, count in sorted(global_word_count.items()):
    print(f"{word}: {count}")
   
