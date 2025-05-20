"""Homework Projects:
Homework 1. ToDo List Application

Define Task Class:
Create a Task class with attributes such as task title, description, due date, and status.
Define ToDoList Class:
Create a ToDoList class that manages a list of tasks.
Include methods to add a task, mark a task as complete, list all tasks, and display incomplete tasks.
Create Main Program:
Develop a simple CLI to interact with the ToDoList.
Include options to add tasks, mark tasks as complete, list all tasks, and display only incomplete tasks.
Test the Application:
Create instances of tasks and test the functionality of your ToDoList."""

class Task:
    def __init__(self, title, description, due_date, status):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
        

class ToDoList:
    