# Functions and Methods in Python: A Beginner's Guide

When you start learning Python, you'll frequently hear two terms: **Functions** and **Methods**. While they look and act very similarly, there is a fundamental difference in how they are used.

This guide will break down both concepts clearly with simple examples.

---

## 1. What is a Function?

A **function** is a reusable block of code that performs a specific task. You can think of it as a mini-program inside your larger program. You give it an input, it does some work, and often gives you an output.

Functions are standalone. This means you call them by their name and pass data directly into the parentheses.

### A. Built-in Functions

Python comes with many functions ready to use out of the box. You have probably used some of these already!

```python
# Examples of Built-in Functions

# 1. print(): Outputs text to the console
print("Hello, World!")

# 2. len(): Returns the length of an item
name = "Anoop"
print(len(name))  # Output: 5

# 3. type(): Tells you the data type of a variable
age = 25
print(type(age))  # Output: <class 'int'>

# 4. dir(): Shows all valid functions and methods for an object
print(dir(str))
```

### B. User-Defined Functions

You can also create (define) your own custom functions using the `def` keyword.

```python
# Defining our own function
def greet_user(username):
    print(f"Hello, {username}! Welcome to Python.")

# Calling the function
greet_user("Anoop")
```

---

## 2. What is a Method?

A **method** is exactly like a function, but with one major difference: **it is attached to a specific object or data type.**

Because a method belongs to an object (like a string, a list, or an integer), you call it slightly differently. You use a "dot" (`.`) after the object's name to use it.

### A. String Methods

String methods can _only_ be called on strings.

```python
course = "Python Programming"

# .upper() is a method belonging to strings
print(course.upper())  # Output: PYTHON PROGRAMMING

# .replace() is another string method
print(course.replace("Python", "AI"))  # Output: AI Programming
```

_Note: You cannot use `.upper()` on a number, because numbers don't understand the `upper()` method!_

### B. List Methods

List methods can _only_ be called on lists.

```python
numbers = [1, 2, 3]

# .append() is a method to add items to the end of a list
numbers.append(4)
print(numbers)  # Output: [1, 2, 3, 4]

# .pop() is a list method to remove the last item
numbers.pop()
print(numbers)  # Output: [1, 2, 3]
```

---

## 3. The Core Difference: Function vs. Method

Here is the easiest way to remember the difference:

| Feature            | Function                                     | Method                         |
| :----------------- | :------------------------------------------- | :----------------------------- |
| **How to call it** | `function_name(data)`                        | `object.method_name(data)`     |
| **Dependency**     | Standalone; doesn't need an object to exist. | Attached to a specific object. |
| **Example**        | `len(course)`                                | `course.upper()`               |

### A Side-by-Side Comparison

Let's look at getting the length of a list (using a function) vs. adding to a list (using a method).

```python
my_list = [10, 20, 30]

# FUNCTION: We pass the list inside the parentheses
list_length = len(my_list)

# METHOD: We call it directly ON the list using a dot
my_list.append(40)
```

## Summary

- If it stands alone by its name (e.g., `print()`, `len()`, `dir()`, `type()`), it is a **Function**.
- If it requires a dot (`.`) tied to your specific variable to do its job (e.g., `name.upper()`, `my_list.append()`), it is a **Method**.
