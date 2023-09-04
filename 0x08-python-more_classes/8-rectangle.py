#!/usr/bin/python3
"""A class Rectangle that defines a rectangle."""


class Rectangle:
    """Represent a rectangle.

    Attributes:
        number_of_instances: The number of rectangle instances.
        print_symbol: The symbol used for string representation."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle."""

        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the triangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the triangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the rectangle with the greater area.

        Arguments:
            rect_1 (Rectangle): The first rectangle
            rect_2 (Rectangle): The second rectangle
        Raises:
            TypeError: if either rect_1 or rect_2 is not a Rectangle."""

        if not isinstance(rect_1, Rectangle)
        raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle)
        raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):
        """Returns the printable representation of the rectangle.
        Represents the rectangle with character #."""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for itr in range(self.__height):
            [rect.append(str(self.print_symbol))
                for index in range(self.__width)]
            if itr != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Returns the string representation of the rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print a message whenever a rectangle is deleted."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
