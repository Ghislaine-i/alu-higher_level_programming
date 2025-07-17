#!/usr/bin/python3
"""
This module defines a Student class with serialization and deserialization capabilities.
"""

class Student:
    """
    Represents a student with first name, last name, and age.
    Provides methods to convert to/from dictionary representation.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): A list of strings specifying which attributes
                                    to retrieve. If None or not a list, all
                                    public instance attributes are retrieved.

        Returns:
            dict: A dictionary containing the specified attributes and their values.
        """
        # Get all public instance attributes of the object
        obj_dict = self.__dict__
        
        # If attrs is a list of strings, filter the attributes
        if type(attrs) is list:
            filtered_dict = {}
            for attr_name in attrs:
                # Check if the attribute exists in the object's dictionary
                if attr_name in obj_dict:
                    filtered_dict[attr_name] = obj_dict[attr_name]
            return filtered_dict
        else:
            # Otherwise, return all public instance attributes
            return obj_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with values from a dictionary.

        Args:
            json (dict): A dictionary where keys are attribute names and
                         values are the corresponding attribute values.
                         Assumed to be a valid dictionary.
        """
        # Iterate through the key-value pairs in the provided dictionary
        for key, value in json.items():
            # Set the attribute on the current instance
            # This will create the attribute if it doesn't exist, or update it if it does.
            setattr(self, key, value)

