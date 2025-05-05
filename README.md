# assignment06

# 🐍 Python OOP Assignments Summary

This repository contains 21 object-oriented programming (OOP) assignments in Python. Each task focuses on a key concept including classes, objects, inheritance, decorators, exception handling, and more. Below is a summary of each topic and what the assignment covers.

---

## 📘 Table of Contents

1. [Using `self`](#1-using-self)
2. [Using `cls`](#2-using-cls)
3. [Public Variables and Methods](#3-public-variables-and-methods)
4. [Class Variables and Class Methods](#4-class-variables-and-class-methods)
5. [Static Variables and Static Methods](#5-static-variables-and-static-methods)
6. [Constructors and Destructors](#6-constructors-and-destructors)
7. [Access Modifiers](#7-access-modifiers-public-private-and-protected)
8. [`super()` Function](#8-the-super-function)
9. [Abstract Classes and Methods](#9-abstract-classes-and-methods)
10. [Instance Methods](#10-instance-methods)
11. [Class Methods](#11-class-methods)
12. [Static Methods](#12-static-methods)
13. [Composition](#13-composition)
14. [Aggregation](#14-aggregation)
15. [MRO and Diamond Inheritance](#15-method-resolution-order-mro-and-diamond-inheritance)
16. [Function Decorators](#16-function-decorators)
17. [Class Decorators](#17-class-decorators)
18. [Property Decorators](#18-property-decorators-property-setter-and-deleter)
19. [`callable()` and `__call__()`](#19-callable-and-__call__)
20. [Custom Exception](#20-creating-a-custom-exception)
21. [Custom Iterable Class](#21-make-a-custom-class-iterable)

---

## 1. Using `self`

**Class**: `Student`

* Demonstrates use of `self` to initialize instance variables via a constructor.
* Includes a `display()` method to print student details.

---

## 2. Using `cls`

**Class**: `Counter`

* Uses a class variable and a class method to keep track of the number of objects created using the `cls` keyword.

---

## 3. Public Variables and Methods

**Class**: `Car`

* Public variable `brand` and public method `start()`.
* Demonstrates access from outside the class.

---

## 4. Class Variables and Class Methods

**Class**: `Bank`

* Has a class variable `bank_name`.
* Includes a class method `change_bank_name()` to update it across all instances.

---

## 5. Static Variables and Static Methods

**Class**: `MathUtils`

* A static method `add(a, b)` demonstrates utility function with no dependence on class or instance.

---

## 6. Constructors and Destructors

**Class**: `Logger`

* Prints messages upon object creation and destruction using `__init__` and `__del__`.

---

## 7. Access Modifiers: Public, Private, and Protected

**Class**: `Employee`

* Public variable: `name`
* Protected variable: `_salary`
* Private variable: `__ssn`
* Access demonstration and explanation of visibility.

---

## 8. The `super()` Function

**Classes**: `Person`, `Teacher`

* `Teacher` inherits from `Person`.
* Uses `super()` to call parent constructor and adds its own field `subject`.

---

## 9. Abstract Classes and Methods

**Module**: `abc`
**Classes**: `Shape` (abstract), `Rectangle` (concrete)

* Implements `area()` method in the derived class.

---

## 10. Instance Methods

**Class**: `Dog`

* Instance variables `name` and `breed`.
* Method `bark()` prints a custom message using instance data.

---

## 11. Class Methods

**Class**: `Book`

* Class variable `total_books`.
* Class method `increment_book_count()` increases book count.

---

## 12. Static Methods

**Class**: `TemperatureConverter`

* Static method `celsius_to_fahrenheit(c)` converts Celsius to Fahrenheit.

---

## 13. Composition

**Classes**: `Engine`, `Car`

* Demonstrates composition by passing an `Engine` instance to `Car` and calling its method.

---

## 14. Aggregation

**Classes**: `Department`, `Employee`

* Department holds a reference to an Employee, which exists independently.

---

## 15. Method Resolution Order (MRO) and Diamond Inheritance

**Classes**: `A`, `B`, `C`, `D`

* `B` and `C` inherit from `A`, `D` inherits from both `B` and `C`.
* Demonstrates Python’s MRO by calling overridden `show()`.

---

## 16. Function Decorators

* Defines a decorator `log_function_call` that prints a message before function execution.
* Applies it to a function `say_hello()`.

---

## 17. Class Decorators

* Decorator `add_greeting` adds a `greet()` method to a class.
* Applied to the `Person` class.

---

## 18. Property Decorators: `@property`, `@setter`, and `@deleter`

**Class**: `Product`

* Uses private attribute `_price`.
* Provides getter, setter, and deleter using property decorators.

---

## 19. `callable()` and `__call__()`

**Class**: `Multiplier`

* Implements `__call__()` to make the object callable like a function.

---

## 20. Creating a Custom Exception

**Exception**: `InvalidAgeError`

* Function `check_age()` raises the exception if age < 18.
* Demonstrates `try...except` block.

---

## 21. Make a Custom Class Iterable

**Class**: `Countdown`

* Implements `__iter__()` and `__next__()` to count down from a start value to 0 in a for-loop.

---

## ✅ How to Run

```bash
python app.py
```

(Replace `app.py` with your actual file names for each topic.)

