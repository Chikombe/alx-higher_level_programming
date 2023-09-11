0x0A. Python - Inheritance

This project focuses on the concept of inheritance in Python.

Inheritance is a fundamental concept in object-oriented programming (OOP) that allows you to create new classes that are based on existing classes, inheriting their attributes and methods. 

This project provides hands-on experience with inheritance, helping you understand its significance and how to implement it effectively in Python.

Project Goals
The primary goals of this project are as follows:

To gain a solid understanding of inheritance and its importance in object-oriented programming.

To practice creating and using classes in Python.

To implement inheritance hierarchies to model relationships between different objects.

File Descriptions
The project includes several Python scripts, each addressing a specific aspect of inheritance. Here is a brief description of each script:

0-lookup.py: Defines a function lookup(obj) that returns the list of available attributes and methods of an object.

1-my_list.py: Defines a class MyList that inherits from the list class and adds a new method, print_sorted, to print the list in ascending order.

2-is_same_class.py: Defines a function is_same_class(obj, a_class) that checks if an object is an instance of a given class.

3-is_kind_of_class.py: Defines a function is_kind_of_class(obj, a_class) that checks if an object is an instance of a class or a class that inherited from the specified class.

4-inherits_from.py: Defines a function inherits_from(obj, a_class) that checks if an object inherits from a given class.

5-base_geometry.py: Defines an empty class BaseGeometry.

6-base_geometry.py: Defines a class BaseGeometry with a method area() that raises an exception.

7-base_geometry.py: Extends the BaseGeometry class with a method integer_validator() to validate the value of a given attribute.

8-rectangle.py: Defines a class Rectangle that inherits from BaseGeometry and adds attributes and methods specific to rectangles.

9-rectangle.py: Extends the Rectangle class by adding a __str__ method to provide a human-readable string representation of the rectangle.

10-square.py: Defines a class Square that inherits from Rectangle and adds attributes and methods specific to squares.

11-square.py: Extends the Square class by adding a __str__ method to provide a human-readable string representation of the square.

tests/: Contains unit tests for each script to verify the correctness of the implementations.
