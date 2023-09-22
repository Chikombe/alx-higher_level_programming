#!/usr/bin/python3

"""Defines a base model class."""
import json
import csv
import turtle


class Base:
    """A representation of the base model.

    This class will be the “base” of all other classes in this project.

    Private Class Attribute:
        __nb_objects(int): Number of bases instantiated.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new Base.

        Args:
        id(int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON list of dictionaries that is serialized.

        Args:
            list_dictionaries(list): A list of directionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the JSON string that is deserialized.

        Args:
            json_string(str): A json string representation of a list of dicts.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves the JSON list of directories that is serialized.

        Args:
            list_objs(list): A list of Base instances that are inherited.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        """Return instances created from a dictionary representation.

        Args:
            **dictionary(dict): A dictionary containing
            attributes to initialize.
        """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1)
        else:
            raise ValueError("Invalid class name")
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of classes loaded from a file.

        Reads from '<cls.__name__>.json'.

        Returns:
            If the file does not exist - an empty list
            otherwise a list of classes that are instantiated.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError as e:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves objects to csv file.

        Args:
            list_objs(list): A list of inherited base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Loads lists from csv file.

        Read from '<cls.__name__>.csv'.

        Returns:
            If the file does not exist - an empty list
            otherwise a list of classes that are instantiated.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles(list): A list of rectangle objects to draw.
            list_squares(list): A list of square objects to draw.
        """
        t = turle.Turtle()
        t.scree.bgcolour("#b7312c")
        t.pensize(3)
        t.shape("turtle")

        t.colour("#ffffff")
        for rect in list_rectangle:
            t.showturtle()
            t.up()
            t.goto(rect.x, rect.y)
            t.down()
            for i in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)
            t.hideturtle()

        t.colour("#b5e3d8")
        for sq in list_squares:
            t.showturtle()
            t.up()
            t.goto(sq.x, sq.y)
            t.down()
            for i in range(2):
                t.forward(sq.width)
                t.left(90)
                t.forward(sq.height)
                t.left(90)
            t.hideturtle()

        t.exitonclick()
