# this file contains the Relationship class as a parent class and three subclasses
# designed to represent connections between people


from abc import ABC, abstractmethod


class Relationship(ABC):
    """Parent class. Represents a relationship between people."""
    def __init__(self, person1, person2):  # initializes two people for a relationship
        self.person1 = person1
        self.person2 = person2

    # The decorator that exposes only essential information and functionalities, hiding complex details
    @abstractmethod
    def __str__(self):  # returns a string representation of the relationship
        return f"{self.person1} in relationship with {self.person2}"

    # the decorator that exposes only essential information and functionalities, hiding complex details
    @abstractmethod
    def __repr__(self):  # helps to represent the relationship and understand the object
        return f"{self.person1} in relationship with {self.person2}"


class SpouseRelationship(Relationship):
    """Child class of 'relationship'. Represents a spouse relationship between two people."""
    def __init__(self, person1, person2):
        super().__init__(person1, person2)  # super() is used to use the parent constructor

    def __str__(self):  # returns a string representation of the relationship
        return f"{self.person1} is in marriage with {self.person2}"

    def __repr__(self):  # helps to represent the relationship and understand the object
        return f"{self.person1} is in marriage with {self.person2}"


class ParentRelationship(Relationship):
    """Child class of 'relationship'. Represents a parent relationship between people."""
    def __init__(self, person1, person2):
        super().__init__(person1, person2)  # super() is used to use the parent constructor

    def __str__(self):  # returns a string representation of the relationship
        return f"{self.person1} is a parent of {self.person2}"

    def __repr__(self):  # helps to represent the relationship and understand the object
        return f"{self.person1} is a parent of {self.person2}"


class ChildRelationship(Relationship):# child class for child relationship
    def __init__(self, person1, person2):
        super().__init__(person1, person2)  # super() is used to use the parent constructor

    def __str__(self):  # returns a string representation of the relationship
        return f"{self.person1} is a child of {self.person2}"

    def __repr__(self):  # helps to represent the relationship and understand the object
        return f"{self.person1} is a child of {self.person2}"