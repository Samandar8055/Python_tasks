"""
Homework: Modules, Packages, and Virtual Environment

1. Virtual Environment (EXPLANATION):
-----------------------------------
A virtual environment is created using:
    python -m venv venv
    source venv/bin/activate  (Linux/Mac)
    venv\\Scripts\\activate   (Windows)

Packages can be installed using:
    pip install numpy pandas

This file demonstrates modules and packages programmatically.
"""

import os
import math

# ===============================
# 2. CREATE CUSTOM MODULES
# ===============================

# math_operations.py
with open("math_operations.py", "w") as f:
    f.write("""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
""")

# string_utils.py
with open("string_utils.py", "w") as f:
    f.write("""
def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
""")

# ===============================
# 3. CREATE CUSTOM PACKAGES
# ===============================

# geometry package
os.makedirs("geometry", exist_ok=True)

with open("geometry/__init__.py", "w") as f:
    f.write("from .circle import calculate_area, calculate_circumference")

with open("geometry/circle.py", "w") as f:
    f.write("""
import math

def calculate_area(radius):
    return math.pi * radius * radius

def calculate_circumference(radius):
    return 2 * math.pi * radius
""")

# file_operations package
os.makedirs("file_operations", exist_ok=True)

with open("file_operations/__init__.py", "w") as f:
    f.write("from .file_reader import read_file\nfrom .file_writer import write_file")

with open("file_operations/file_reader.py", "w") as f:
    f.write("""
def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()
""")

with open("file_operations/file_writer.py", "w") as f:
    f.write("""
def write_file(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)
""")

# ===============================
# 4. TEST EVERYTHING
# ===============================

import math_operations
import string_utils
from geometry import calculate_area, calculate_circumference
from file_operations import write_file, read_file

print("Math Operations:")
print("Add:", math_operations.add(5, 3))
print("Subtract:", math_operations.subtract(5, 3))
