## Homework 13 fatetime and re

# task 1
'''Age Calculator: Ask the user to enter their birthdate. 
Calculate and print their age in years, months, and days.'''

from datetime import date
from dateutil.relativedelta import relativedelta

# Ask user for birthdate
birth_year = int(input("Enter birth year (YYYY): "))
birth_month = int(input("Enter birth month (MM): "))
birth_day = int(input("Enter birth day (DD): "))

# Create date object for birthdate
birth_date = date(birth_year, birth_month, birth_day)

# Get today's date
today = date.today()

# Calculate difference
age = relativedelta(today, birth_date)

# Print result
print(f"\nYour age is:")
print(f"{age.years} years, {age.months} months, and {age.days} days")
print(birth_date)


# TASK 2 
'''Days Until Next Birthday: Similar to the first exercise, but this time,
 calculate and print the number of days remaining until the user's next birthday.'''

import datetime 

birth_year = int(input("Enter birth year (YYYY): "))
birth_month = int(input("Enter birth month (MM): "))
birth_day = int(input("Enter birth day (DD): "))

birth_date = datetime.date(birth_year, birth_month, birth_day)

left = datetime.date.today() - birth_date


print(birth_date)
print(f'{left} ,left till your next birthday')








# task 3 try
'''Meeting Scheduler: Ask the user to enter the current date and time, 
as well as the duration of a meeting in hours and minutes. 
Calculate and print the date and time when the meeting will end.'''
from datetime import datetime, timedelta

while True:
    current_datetime_str = input("Enter current date and time (YYYY-MM-DD HH:MM): ")
    try:
        current_datetime = datetime.strptime(current_datetime_str, "%Y-%m-%d %H:%M")
        break
    except ValueError:
        print("❌ Invalid format. Please use YYYY-MM-DD HH:MM")

while True:
    try:
        hours = int(input("Enter meeting duration hours: "))
        minutes = int(input("Enter meeting duration minutes: "))
        if hours < 0 or minutes < 0:
            raise ValueError
        break
    except ValueError:
        print("❌ Please enter valid non-negative numbers.")

# Create time delta
meeting_duration = timedelta(hours=hours, minutes=minutes)

# Calculate end time
end_datetime = current_datetime + meeting_duration

# Output result
print("\nMeeting will end at:")
print(end_datetime.strftime("%Y-%m-%d %H:%M"))



# Task 4 try again
'''Timezone Converter: Create a program that allows the user 
to enter a date and time along with their current timezone, 
and then convert and print the date and time in another timezone of their choice.'''

from datetime import datetime
import pytz

# Ask user for date and time
datetime_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")

# Ask for timezones
from_tz_str = input("Enter your current timezone (e.g. America/New_York): ")
to_tz_str = input("Enter target timezone (e.g. Europe/London): ")

try:
    # Parse input datetime (naive)
    naive_datetime = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")

    # Get pytz timezone objects
    from_tz = pytz.timezone(from_tz_str)
    to_tz = pytz.timezone(to_tz_str)

    # Localize naive datetime to source timezone
    source_datetime = from_tz.localize(naive_datetime)

    # Convert to target timezone
    target_datetime = source_datetime.astimezone(to_tz)

    # Output result
    print("\nConverted date and time:")
    print(target_datetime.strftime("%Y-%m-%d %H:%M (%Z)"))

except Exception as e:
    print("❌ Error:", e)


# Task 5 non

from datetime import datetime
import time

# Ask user for future date and time
future_time_str = input("Enter future date and time (YYYY-MM-DD HH:MM:SS): ")

try:
    # Convert input string to datetime
    future_time = datetime.strptime(future_time_str, "%Y-%m-%d %H:%M:%S")

    while True:
        now = datetime.now()
        remaining_time = future_time - now

        # If countdown finished
        if remaining_time.total_seconds() <= 0:
            print("\n⏰ Countdown finished!")
            break

        # Convert remaining time to days, hours, minutes, seconds
        days = remaining_time.days
        hours, remainder = divmod(remaining_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Print countdown (overwrite same line)
        print(
            f"\rTime remaining: {days}d {hours}h {minutes}m {seconds}s",
            end=""
        )

        time.sleep(1)

except ValueError:
    print("❌ Invalid format. Use YYYY-MM-DD HH:MM:SS")


# Task 6

import re

emails= str(input("enter your email:Ex:**@gmail.com"))

try:
    x = re.findall("^@gmail.com", emails)
    print(f"{emails} is valid email")

except:
    print(f"{emails} is not valid email, pls try again!")    




# task 7 try

'''Phone Number Formatter: Create a program that takes a phone number as
 input and formats it according to a standard format. 
For example, convert "1234567890" to "(123) 456-7890".'''



import re

phone_number = input("Enter a 10-digit phone number: ")

# Regex pattern for 10 digits
pattern = r"^(\d{3})(\d{3})(\d{4})$"

match = re.match(pattern, phone_number)

if match:
    formatted_number = f"({match.group(1)}) {match.group(2)}-{match.group(3)}"
    print("Formatted phone number:", formatted_number)
else:
    print("❌ Invalid phone number. Please enter exactly 10 digits.")



 # task 8 
'''Password Strength Checker: Implement a password strength checker. Ask the user to input a
 password and check if it meets certain criteria (e.g., minimum length,
 contains at least one uppercase letter,
 one lowercase letter, and one digit).'''
import re

password= input("enter your password:")

# Criteria checks using regex
length_ok = len(password) >= 8
upper_ok = re.search(r"[A-Z]", password)
lower_ok = re.search(r"[a-z]", password)
digit_ok = re.search(r"\d", password)

if length_ok and upper_ok and lower_ok and digit_ok:
    print("✅ Password is strong")
else:
    print("❌ Password is weak")
    print("Requirements:")
    if not length_ok:
        print("- At least 8 characters")
    if not upper_ok:
        print("- At least one uppercase letter")
    if not lower_ok:
        print("- At least one lowercase letter")
    if not digit_ok:
        print("- At least one digit")


# Task 9 
import re

text = '''Word Finder: Develop a program that finds all occurrences of a specific word in a given text.
 Ask the user to input a word, 
and then search for and print all occurrences of that word in a sample text.'''

searchh = input("Enter your word to serach")

searched =re.findall(searchh,text)

print(searched)



# task 10
'''Date Extractor: Write a program that extracts dates from a given text. 
Ask the user to input a text, and then identify and print all the dates present in the text.'''

import re

text = input("Enter text: ")

# Regex pattern for multiple date formats
date_pattern = r"""
\b(
    \d{4}-\d{2}-\d{2} |        # YYYY-MM-DD
    \d{2}/\d{2}/\d{4}          # DD/MM/YYYY or MM/DD/YYYY
)\b
"""

# Find all dates
dates = re.findall(date_pattern, text, re.VERBOSE)

if dates:
    print("\nDates found:")
    for date in dates:
        print("-", date)
else:
    print("\nNo dates found.")
