## Lesson-10 Classes (Library Project)
#Exercies -1
#Task - 1

'''Homework 1. ToDo List Application

Define Task Class:
Create a Task class with attributes such as task title, description, due date, and status..
'''

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = "Incomplete"

    def mark_complete(self):
        self.status = "Complete"

    def __str__(self):
        return f"Title: {self.title} | Due: {self.due_date} | Status: {self.status}"
 


# Task 2
'''2. Define ToDoList Class:
    - Create a ToDoList class that manages a list of tasks.
    - Include methods to add a task, mark a task as complete, list all tasks, and display incomplete tasks.'''
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully.")

    def mark_task_complete(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_complete()
            print("Task marked as complete.")
        else:
            print("Invalid task number.")

    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")

    def list_incomplete_tasks(self):
        found = False
        for i, task in enumerate(self.tasks):
            if task.status == "Incomplete":
                print(f"{i}. {task}")
                found = True
        if not found:
            print("No incomplete tasks.")


# Task 3

def main():
    todo_list = ToDoList()

    while True:
        print("\n--- ToDo List Menu ---")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. List Incomplete Tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            task = Task(title, description, due_date)
            todo_list.add_task(task)

        elif choice == "2":
            todo_list.list_all_tasks()
            index = int(input("Enter task number to mark complete: "))
            todo_list.mark_task_complete(index)

        elif choice == "3":
            todo_list.list_all_tasks()

        elif choice == "4":
            todo_list.list_incomplete_tasks()

        elif choice == "5":
            print("Exiting application.")
            break

        else:
            print("Invalid choice. Try again.")

# task 4
if __name__ == "__main__":
    main()            

#Exercies -2
#Task - 1
#Homework 2. Simple Blog System
'''Define Post Class:
    - Create a Post class with attributes like title, content, and author.'''

class Post:
    def __init__(self, title,content,author):
        self.title = title
        self.content = content
        self.author = author
        

#task -2 
'''2. Define Blog Class:
    - Create a Blog class that manages a list of posts.
    - Include methods to add a post, list all posts, and display posts by a specific author.'''  
class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self,post):
        self.posts.append(post) 

    def list_all_psots(self):
        if not self.posts:
            print("No posts available.")
            return
        
        for post in self.posts:
            print(post)
    def show_posts_by_author(self,post,author_name):
        found = False
        for post in self.posts:
            if post.author.lower() == author_name.lower():
                print(post)
                found = True

        if not found:
            print("No posts found for this author.") 
                         
# Task 3
'''3. Create Main Program:
    - Develop a CLI to interact with the Blog system.
    - Include options to add posts, list all posts, and display posts by a specific author.'''
def main():
    blog = Blog()

    while True:
        print("\n--- Blog Menu ---")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Display Posts by Author")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")

            post = Post(title, content, author)
            blog.add_post(post)

        elif choice == "2":
            blog.list_all_posts()

        elif choice == "3":
            author = input("Enter author name: ")
            blog.display_posts_by_author(author)

        elif choice == "4":
            print("Exiting Blog System.")
            break

        else:
            print("Invalid choice. Try again.")


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
        print("Post added successfully.")

    def list_all_posts(self):
        if not self.posts:
            print("No posts available.")
            return
        for i, post in enumerate(self.posts):
            print(f"{i}. {post}")

    def display_posts_by_author(self, author):
        found = False
        for post in self.posts:
            if post.author.lower() == author.lower():
                print(post)
                found = True
        if not found:
            print("No posts found for this author.")

    def delete_post(self, index):
        if 0 <= index < len(self.posts):
            deleted = self.posts.pop(index)
            print(f"Deleted post: {deleted.title}")
        else:
            print("Invalid post number.")

    def edit_post(self, index, title, content, author):
        if 0 <= index < len(self.posts):
            self.posts[index].title = title
            self.posts[index].content = content
            self.posts[index].author = author
            print("Post updated successfully.")
        else:
            print("Invalid post number.")

    def display_latest_posts(self, count=3):
        if not self.posts:
            print("No posts available.")
            return
        print("Latest posts:")
        for post in self.posts[-count:]:
            print(post)

# task 5

blog = Blog()

post1 = Post("Python", "Learn Python", "Alex")
post2 = Post("AI", "Intro to AI", "Alex")
post3 = Post("Web", "HTML Basics", "John")
post4 = Post("ML", "Machine Learning", "Alex")

blog.add_post(post1)
blog.add_post(post2)
blog.add_post(post3)
blog.add_post(post4)

print("\nAll Posts:")
blog.list_all_posts()

print("\nLatest Posts:")
blog.display_latest_posts(2)

print("\nEditing post 1:")
blog.edit_post(1, "AI Updated", "Advanced AI", "Alex")

print("\nDeleting post 2:")
blog.delete_post(2)

print("\nPosts by Alex:")
blog.display_posts_by_author("Alex")

# ecercies 3
# task 1

'''1. Define Account Class:
    - Create an Account class with attributes like account number, account holder name, and balance.'''

class Account:
    def __init__(self,account_number:int, account_holder_name, balance:int):
        self.account_number= account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

        '''- Include methods to add an account, check balance, deposit money, and withdraw money.'''

class Bank:
    def __init__(self):
        self.accounts = []  

    def add_account(self,account):
        self.accounts.append(account)
        print("Account is added sucessfuly")  

    def check_balance(self, balance):
        print(f'You balance is {balance}')

    def deposit_money(self,balance):
        deposit = int(input("Enetr you amount to deposit:"))
        print(f'Your {deposit} amount is made sucessfult! Your current balance is {balance + deposit}')
    def withdraw_money(self, balance):
        withdraw = int(input("Enetr you amount to withdraw:"))
        print(f'Your {withdraw} protses is made sucessfult! Your current balance is {balance - withdraw}')



class Account:
    def __init__(self, account_number, account_holder_name, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def __str__(self):
        return f"Account: {self.account_number} | Holder: {self.account_holder_name} | Balance: {self.balance}"



class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print("Account added successfully.")

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def check_balance(self, account_number):
        account = self.find_account(account_number)
        if account:
            print(f"Current balance: {account.balance}")
        else:
            print("Account not found.")

    def deposit_money(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.deposit(amount)
            print("Deposit successful.")
        else:
            print("Account not found.")

    def withdraw_money(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")


def main():
    bank = Bank()

    while True:
        print("\n--- Banking System Menu ---")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            acc_number = int(input("Enter account number: "))
            name = input("Enter account holder name: ")
            balance = int(input("Enter initial balance: "))
            account = Account(acc_number, name, balance)
            bank.add_account(account)

        elif choice == "2":
            acc_number = int(input("Enter account number: "))
            bank.check_balance(acc_number)

        elif choice == "3":
            acc_number = int(input("Enter account number: "))
            amount = int(input("Enter deposit amount: "))
            bank.deposit_money(acc_number, amount)

        elif choice == "4":
            acc_number = int(input("Enter account number: "))
            amount = int(input("Enter withdraw amount: "))
            bank.withdraw_money(acc_number, amount)

        elif choice == "5":
            print("Exiting Banking System.")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
