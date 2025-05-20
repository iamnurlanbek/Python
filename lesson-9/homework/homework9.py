# # Homework:

# # Object-Oriented Programming (OOP) Exercises

""" 1. Circle Class
 Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter."""
# from math import pi
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
          
#     def get_area(self):
#         return f"Area of circle: {self.radius ** 2 * pi:.2f} m²."
    
#     def get_perimeter(self):
#         return f"Perimeter of circle: {2 * pi * self.radius:.2f} m."

# circle = Circle(5)
# print(circle.get_area())
# print(circle.get_perimeter())
 

"""## 2. Person Class
Write a Python program to create a Person class. Include attributes like name, country, and date of birth. Implement a method to determine the person's age.
"""
# from datetime import datetime
# class Person:
#     def __init__(self, name, country, date_of_birth):
#         self.name = name
#         self.country = country
#         self.date_of_birth = date_of_birth
        
        
#     def get_age(self):
#         today = datetime.now()
#         age = today.year - self.date_of_birth.year
        
#         if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
#             age -= 1
#         return f"{self.name.capitalize()} from {self.country.capitalize()}, he/she is {age} years old."

# per1 = datetime(2001, 8, 12)
# per2 = datetime(2008, 1, 30)
# person1 = Person('jack', 'england', per1)
# person2 = Person('ann', 'spain', per2)
# print(person1.get_age())
# print(person2.get_age())






"""3. Calculator Class
Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.
"""

# class Calculator:
#     def __init__(self, number1, number2):
#         self.number1 = number1
#         self.number2 = number2
        
#     def add(self):
#         return f"Addition: {self.number1 + self.number2}"
    
#     def multiply(self):
#         return f"Multiplication: {self.number1 * self.number2}"
    
#     def substract(self):
#         return f"Subtraction: {self.number1 - self.number2}"
    
#     def division(self):  
#         try:
#             result = self.number1 / self.number2
#             return f"Division: {result}"
#         except ZeroDivisionError:
#             return "Error: Division by zero is not allowed"
        
#     def power(self):
#         return f"Power: {self.number1 ** self.number2}"
    

# test = Calculator(10,)
# print(test.add())
# print(test.multiply())
# print(test.substract())
# print(test.division())
# print(test.power())




"""## 4. Shape and Subclasses
Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. 
Implement subclasses for different shapes like Circle, Triangle, and Square.
"""
# from abc import ABC, abstractmethod
# from math import pi
# class Shape(ABC):
    
#     @abstractmethod
#     def area(self):
#         pass
    
#     @abstractmethod
#     def perimeter(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius:int):
#         self.radius = radius
        
#     def area(self):
#         return f"Perimeter of circle: {2 * pi * self.radius:.2f}m²"
    
#     def perimeter(self):
#         return f"Area of circle: {pi * self.radius**2:.2f}m"
    
# class Triangle(Shape):
#     def __init__(self, side1:int, main_side:int, side3:int, height:int):
#         self.side1 = side1
#         self.main_side = main_side
#         self.side3 = side3
#         self.height = height
        
#     def area(self):
#         return f"Area of triangle: {self.main_side * self.height * 1/2}m²"
    
#     def perimeter(self):
#         return f"Perimeter of triangle: {self.side1 + self.main_side + self.side3}m"
    
# class Square(Shape):
#     def __init__(self, side:int):
#         self.side = side
        
#     def area(self):
#         return f"Area of square: {self.side ** 2}m²"
    
#     def perimeter(self):
#         return f"Perimeter of square: {4 * self.side}m"
    

# circle = Circle(5)
# triangle = Triangle(8, 12, 9, 7)
# square = Square(5)

# shapes = [Circle(5), Triangle(8, 12, 9, 7), Square(5)]
# for shape in shapes:
#     print(shape.area())
#     print(shape.perimeter())
#     print('----------------------')
    






"""## 5. Binary Search Tree Class
Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.
"""
# class Node:
#     def __init__(self, value):
#         self.value = value  
#         self.left = None    
#         self.right = None   

# class BinarySearchTree:
#     def __init__(self):
#         self.root = None  

#     def insert(self, value):
#         if self.root is None:
#             self.root = Node(value)
#         else:
#             self._insert_recursive(self.root, value)

#     def _insert_recursive(self, current, value):
#         if value < current.value:
#             if current.left is None:
#                 current.left = Node(value)
#             else:
#                 self._insert_recursive(current.left, value)
#         else:
#             if current.right is None:
#                 current.right = Node(value)
#             else:
#                 self._insert_recursive(current.right, value)

#     def search(self, value):
#         return self._search_recursive(self.root, value)

#     def _search_recursive(self, current, value):
#         if current is None:
#             return False
#         elif value == current.value:
#             return True
#         elif value < current.value:
#             return self._search_recursive(current.left, value)
#         else:
#             return self._search_recursive(current.right, value)


# bst = BinarySearchTree()


# bst.insert(50)
# bst.insert(30)
# bst.insert(70)
# bst.insert(20)
# bst.insert(40)


# print(bst.search(30)) 
# print(bst.search(60))  





"""## 6. Stack Data Structure
Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.
"""

# class Stack:
#     def __init__(self, lists=None):
#         if lists is None:
#             self.lists = []
#         else:
#             self.lists = lists
      
#     def show(self):
#         return self.lists
        
#     def push(self, newvalue):
#         self.lists.append(newvalue)
        
#     def pop(self):
#         if len(self.lists) == 0:
#             return f"List is empty, nothing to pop"
#         else:
#             return self.lists.pop()
    
# stack = Stack()
# print(stack.show())
# stack.push(100)
# stack.push(True)
# stack.push(False)
# print(stack.show())
# stack.pop()
# print(stack.show())



"""## 7. Linked List Data Structure
Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting, and deleting nodes.
"""

# class Node:
#     def __init__(self, data):
#         self.data = data  
#         self.next = None      



# class LinkedList:
#     def __init__(self):
#         self.head = None   

   
#     def insert(self, data):
#         new_node = Node(data)  
#         if self.head is None:   
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next: 
#                 current = current.next
#             current.next = new_node  

  
#     def delete(self, data):
#         current = self.head
#         prev = None
#         while current:
#             if current.data == data:
#                 if prev is None:
#                     self.head = current.next  
#                 else:
#                     prev.next = current.next  
#                 return True 
#             prev = current
#             current = current.next
#         return False  

   
#     def display(self):
#         current = self.head
#         if current is None:
#             print("List is empty.")
#             return
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")  



# my_list = LinkedList()
# my_list.insert(10)
# my_list.insert(20)
# my_list.insert(30)

# print("Initial list:")
# my_list.display()

# print("\nAfter deleting 20:")
# my_list.delete(20)
# my_list.display()

# print("\nAfter deleting 10:")
# my_list.delete(10)
# my_list.display()

# print("\nAfter deleting 30:")
# my_list.delete(30)
# my_list.display()





"""## 8. Shopping Cart Class
Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.
"""

# class ShoppingCart:
#     def __init__(self):
#         self.items = {}
        
    
#     def add_item(self, name, price):
#         new_item = self.items[name] = price
#         print(f"Added to cart: {name}")
#         return new_item
    
#     def remove_item(self, name):
#         if name not in self.items:
#             print(f"{name} is not available in the cart.")
#         else:
#             removed_item = self.items.pop(name)
#             print(f"Removed from cart: {name}")
#             return removed_item

    
#     def get_total_price(self):
#         total_price = 0
#         for price in self.items.values():
#             total_price += price
#         return f"Total Price: {total_price}$"
            
    
#     def show(self):
#         return self.items
    
        
# card = ShoppingCart()
# card.add_item('apple', 1500)
# card.add_item('grape', 1000)
# card.add_item('melon', 2600)
# card.add_item('watermelon', 4000)
# card.add_item('kiwi', 1800)
# card.add_item('banana', 4530)
# print('-----------------')
# card.remove_item('apple')
# card.remove_item('watermelon')
# card.remove_item('apple')
# print('-----------------')
# print(card.get_total_price())
# print('-----------------')
# print('Items in the cart')
# print(card.show())




"""## 9. Stack with Display
Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping, and displaying elements.
"""

# class Stack:
#     def __init__(self, elemets=None):
#         if elemets is None:
#             self.elements = []
#         else:
#             self.elements = elemets
            
#     def push(self, element):
#         self.elements.append(element)
        
#     def pop(self):
#         if len(self.elements) == 0:
#             return f"List is empty, nothing to pop"
#         else:
#             return self.elements.pop()
    
#     def display(self):
#         return f"Elements:{self.elements}"

# stack = Stack()
# print(stack.display())
# stack.push(100)
# stack.push(200)
# stack.push(300)
# stack.push(400)
# stack.push(500)
# print(stack.display())
# stack.pop()
# stack.pop()
# stack.pop()
# print(stack.display())



"""## 10. Queue Data Structure
Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.
"""
# class Queue:
#     def __init__(self):
#         self.queues = []
        
#     def enqueue(self, queue):
#         self.queues.append(queue)
        
#     def dequeue(self):
#         return self.queues.pop(0)
    
#     def show(self):
#         return self.queues
    
# queue = Queue()
# queue.enqueue('ali')
# queue.enqueue('salim')
# queue.enqueue(True)
# queue.enqueue(58)
# print(queue.show())
# queue.dequeue()
# queue.dequeue()
# print(queue.show())



"""## 11. Bank Class
# Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.
"""

# class Bank:
#     def __init__(self):
#         self.accounts = {}
        
#     def create_account(self, name:str, balance:int):
#         new_account = self.accounts[name] = balance
#         print(f"Added new account: {name.title()}:{balance}$")
#         return new_account
    
#     def check_balance(self, name:str):
#         if name in self.accounts:
#             return (f"{name.title()}'s balance: {self.accounts[name]}$")
#         else:
#             return (f'{name.title()} was not found.')
        
    
#     def deposit(self, name:str, amount:int):
#         if amount < 0:
#             return "The balance must not be less than zero."
#         else:
#             self.accounts[name] += amount
#             return (f"A deposit of {amount} was made to {name.title()}'s account.")
            
            
#     def withdraw(self, name:str, amount:int):
#         if amount > self.accounts[name]:
#             return 'Your account does not have enough balance.'
            
#         elif  amount < 0:
#             return "The balance must not be less than zero."
        
#         else:
#             self.accounts[name] -= amount
#             return (f'You successfully withdrew {amount}. Your balance: {self.accounts[name]}$')
            
#     def show_acoounts(self):
#         print('Show all customers in the bank.')
#         for name, balance in self.accounts.items():
#             print(f"Name: {name.title()}\nBalance: {balance}$\n")
    

# account = Bank()
# account.create_account('ali', 5000)
# account.create_account('salim', 7000)
# account.create_account('linda', 550)
# account.create_account('tom', 9999)
# account.create_account('john', 1500)
# print('---------------------')
# print(account.check_balance('ali'))
# print(account.check_balance('lucy'))
# print('---------------------')
# print(account.deposit('ali',6000))
# print(account.deposit('ali',-5000))
# print('---------------------')
# print(account.check_balance('ali'))
# print(account.withdraw('ali',-5000))
# print(account.withdraw('ali',55000))
# print(account.withdraw('ali',5000))
# print('---------------------')
# account.show_acoounts()




            
        
