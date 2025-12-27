## Jsone Homework
# Task 1
'''write a Python script that reads the students.jon JSON file and prints details of each student.'''

import json

with open('students.json') as f:
    data = json.load(f)

print(data['students'])    
# task 2
import requests

API = "2fc238b675895e88462d309fd97c0ad5"   # <-- put your API key here
city = "Tashkent"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}"

params = {
    "q": city,
    "appid": API,
    "units": "metric"   # Celsius
}

response = requests.get(url, params=params)
data = response.json()

# Print weather details
print("City:", data["name"])
print("Temperature:", data["main"]["temp"], "°C")
print("Feels like:", data["main"]["feels_like"], "°C")
print("Humidity:", data["main"]["humidity"], "%")
print("Weather:", data["weather"][0]["description"])

# Task 3 try
import json

FILE_NAME = "books.json"

def load_books():
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_books(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def add_book():
    data = load_books()

    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = int(input("Enter year: "))

    new_id = max(book["id"] for book in data["books"]) + 1

    new_book = {
        "id": new_id,
        "title": title,
        "author": author,
        "year": year
    }

    data["books"].append(new_book)
    save_books(data)
    print("✅ Book added successfully")

def update_book():
    data = load_books()
    book_id = int(input("Enter book ID to update: "))

    for book in data["books"]:
        if book["id"] == book_id:
            book["title"] = input("New title: ")
            book["author"] = input("New author: ")
            book["year"] = int(input("New year: "))
            save_books(data)
            print("✅ Book updated")
            return

    print("❌ Book not found")

def delete_book():
    data = load_books()
    book_id = int(input("Enter book ID to delete: "))

    data["books"] = [book for book in data["books"] if book["id"] != book_id]
    save_books(data)
    print("✅ Book deleted")

while True:
    print("\n1. Add book")
    print("2. Update book")
    print("3. Delete book")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        update_book()
    elif choice == "3":
        delete_book()
    elif choice == "4":
        break
    else:
        print("❌ Invalid choice")

# task 4 
import requests



search_key = 'The God father'
url = f"http://www.omdbapi.com/?apikey={key}&s={search_key}"
key= '9d7c246e'



req = requests.get(url)

check= req.status_code

print(check)
req.json()
