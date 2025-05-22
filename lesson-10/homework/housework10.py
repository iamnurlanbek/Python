""" Task 1"""

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = False
        
        
class ToDoList:
    def __init__(self):
        self.task_lists = []
        
    def add_task(self, task):
        self.task_lists.append(task)
        
    def all_tasks(self):
        for task in self.task_lists:
            print(f"{task.title} - {'Bajarilgan ✅' if task.status else 'Bajarilmagan ❌'}")
            
    def mark_task_completed(self, title):
        for task in self.task_lists:
            if task.title == title:
                task.status = True
                
    def show_completed_tasks(self):
        for task in self.task_lists:
            if task.status:
                print(F"{task.title} - Bajarildi 👌")
                
    def show_incompleted_tasks(self):
        for task in self.task_lists:
            if not task.status:
                print(f"{task.title} - Bajarilmadi ✖️")

                
                
task1 = Task('Kitob o\'qish', ' 2 soat', '2025-05-21')
task2 = Task('Zalga borish', ' 1 soat', '2025-05-22')
task3 = Task('Ishga borish', ' 7 soat', '2025-05-20')

todo = ToDoList()

todo.add_task(task1)
todo.add_task(task2)
todo.add_task(task3)

todo.mark_task_completed('Zalga borish')

todo.show_incompleted_tasks()
todo.show_completed_tasks()
print()
todo.all_tasks()


""" Task 2"""
class Account:
    def __init__(self, account_number, account_holder_name, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance
        
class Bank:
    def __init__(self):
        self.accounts = []
        
    def add_account(self, account):
        self.accounts.append(account)
    
    def check_balance(self, acc_number):
        for account in self.accounts:
            if account.account_number == acc_number:
                result =  f"Account Number: {account.account_number}, Account Holder: {account.account_holder_name.title()}, Balance: {account.balance}$"
                return result
            
    def deposit(self, account_number, amount):
        if amount <= 0:
            print(f"The amount should be positive.")
            return 
        
        for account in self.accounts:
            if account.account_number == account_number:
                account.balance += amount
                print(f"{account.account_number} - account has been credited with {amount}$. Current balance: {account.balance}$")
                return 
                
        print(f"{account_number} account number is not available.")
            
    
    def withdraw(self, account_number, amount):
        if amount <= 0:
            print("The amount should be positive.")
            return 
        
        for account in self.accounts:
            if account.account_number == account_number and amount > account.balance:
                print("Insufficient funds in the account.")
                return 
            
            elif account.account_number == account_number:
                account.balance -= amount
                print(f"{amount}$ has been withdrawn from your account. Current balance: {account.balance}$")
                return
            
        print(f"{account_number} account number is not available.")
        
    def transfer(self, from_account_number, to_account_number, amount):
        if amount <= 0:
            print("The amount should be positive.")
            return 
        
        from_account = None
        to_account = None
        
        for account in self.accounts:
            if account.account_number == from_account_number:
                from_account = account
                
            if account.account_number == to_account_number:
                to_account = account
                
        if from_account is None:
            print(f"{from_account_number} account number is not available.")
            return
        
        if to_account is None:
            print(f"{to_account_number} account number is not available.")
            return
        
        if from_account.balance < amount:
            print("Insufficient funds in the account.")
            return
        
        if from_account == to_account:
            print("Transfer must involve two different account numbers.")
            return
        
        from_account.balance -= amount
        to_account.balance += amount
        print(f"{amount}$ successfully transferred from account {from_account_number} to {to_account_number}.")
        print(f"New balance - {from_account_number}: {from_account.balance}$, {to_account_number}: {to_account.balance}$")
                
    
account1 = Account(125, 'alex', 50000)
account2 = Account(124, 'linda', 20000)

bank = Bank()

bank.add_account(account1)
bank.add_account(account2)

print(bank.check_balance(125))
print(bank.check_balance(124))
print()
bank.deposit(125, 5000)
bank.deposit(124, 5000)
bank.deposit(126, 5000)
print()
bank.withdraw(125, 6000)
bank.withdraw(124, 6000)
bank.withdraw(126, 6000)
print()
print(bank.check_balance(125))
print(bank.check_balance(124))
print()
bank.transfer(124, 125, 9999)
print()
bank.transfer(125, 125, 9999)


""" Task 3 """

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

class Blog:
    def __init__(self):
        self.posts = []
        
    def add_post(self, new_post):
        self.posts.append(new_post)
        
    def show_all_posts(self):
        for post in self.posts:
            print(f"Post Title: {post.title.title()}\nContent: {post.content.capitalize()}\nAuthor: {post.author.title()}\n")
        
    def showpostbyauthor(self, author):
        for post in self.posts:
            if post.author == author:
                print(f"Post by {author.title()}\n Title: {post.title.title()}\nContent: {post.content.title()}")
                return    
                    
        print("No content found for this author.")
        
    def delete_post(self, title, author):
        for post in self.posts:
            if post.title == title and post.author == author:
                self.posts.remove(post)
                print(f"Post '{title}' by {author} deleted successfully.")
                return
            
        return f"No post found with title '{title}' by {author}"
    
    
    def edit_post(self, new_title, new_content, author):
        for post in self.posts:
            if post.author == author:
                post.title = new_title
                post.content = new_content
                print(f"Content and Title successfully edited")
                return
                
    def show_latest_post(self):
        if self.posts:
            last_post = self.posts[-1]
            print(f"Title: {last_post.title}\nContent: {last_post.content}\nAuthor: {last_post.author}")
        else:
            print("No posts available.")
            

                
                
post1 = Post('The Power of Consistency', "Success doesn't come from what you do occasionally, it comes from what you do consistently.", 'James Clear')
post2 = Post('Keep Moving Forward', "It does not matter how slowly you go, as long as you do not stop.", 'Confucius')
post3 = Post('Believe in Yourself',"Don’t let the noise of others’ opinions drown out your own inner voice.", 'Steve Jobs')

blog = Blog()

blog.add_post(post1)
blog.add_post(post2)
blog.add_post(post3)

blog.show_all_posts()
blog.showpostbyauthor('Steve Jobs')
print()
blog.showpostbyauthor('Adam Smith')
print()
blog.delete_post('The Power of Consistency', 'James Clear')
print()
blog.show_all_posts()
blog.edit_post('Happiness', 'Happiness never lays its finger on its pulse', 'James Clear')
print()
blog.show_all_posts()
blog.show_latest_post()

    
