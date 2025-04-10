# this file includes the Person class and the methods that belong to it


from relationship import ChildRelationship, ParentRelationship, SpouseRelationship


# class Person is used to initialize a person's details
# Encapsulation implemented
class Person:
    def __init__(self, name: str, birthday: int, gender: str, death_day: int):  # initialize the person's attributes
        self._name = name
        self._birthday = birthday
        self._gender = gender
        self._death_day = death_day

        self._relationship = []

    def __str__(self):  # returns a string representation of a person
        return self._name

    def __repr__(self):  # helps to represent the relationship and understand the object
        return self._name

    # appends the relationship to the list
    def add_relationship(self, relationship):
        self._relationship.append(relationship)

    # decorator for the name, using for accessing the name of the person without calling the method
    @property
    def name(self):
        return self._name

    def get_relationships(self):
        """Return relationships for each person in the list."""
        return self._relationship

    def find_parents(self):
        """Return parents of the selected person."""
        parents = []
        for relationship in self._relationship:
            if isinstance(relationship, ChildRelationship):  # if the relationship is a child relationship
                parents.append(relationship.person2)
        return parents

    def find_siblings(self):
        """Return siblings of the selected person.
        finds siblings through parents' children"""
        siblings = []
        parents = self.find_parents()  # variable for parents, using 'find_parents' function
        for parent in parents:
            for relationship in parent.get_relationships():  # loop for relationships in parents, using 'get_relationships' function
                if not isinstance(relationship, ParentRelationship):  # if the relationship is not a parent relationship
                    continue
                if relationship.person2 != self and relationship.person2 not in siblings:
                    siblings.append(relationship.person2)
        return siblings

    def find_children(self):
        """Return children of the selected person."""
        children = []
        for relationship in self._relationship:
            if isinstance(relationship, ParentRelationship):  # if the relationship is a parent relationship
                children.append(relationship.person2)
        return children

    def find_cousins(self):
        """Return cousins of the selected person.
        Loop, that goes through parents, then siblings of parents and find their children"""
        cousins = []
        parents = self.find_parents()
        for parent in parents:
            siblings = parent.find_siblings()
            for sibling in siblings:
                children = sibling.find_children()
                for child in children:
                    cousins.append(child)
        return cousins

    def find_spouse(self):
        """Return spouses of the selected person."""
        spouse = []  # adds spouse to the array
        for relationship in self._relationship:
            if isinstance(relationship, SpouseRelationship):  # if the relationship is a spouse relationship
                spouse.append(relationship.person2)
        return spouse

    def get_birthday(self):
        """Return birthday of the selected person."""
        birth_day, birth_month, birth_year = self.get_date(self._birthday)
        return birth_day, birth_month, birth_year

    def get_death_day(self):
        """Return death day of the selected person if person is no longer alive."""
        if self._death_day == -1:
            return "Person is still alive."
        else:
            death_day, death_month, death_year = self.get_date(self._death_day)
            return death_day, death_month, death_year

    # static method: a method that belongs to a class, but not associated with a class object
    @staticmethod
    def get_date(date):
        """Converts a date to integers"""
        day = int(str(date)[-8:-6])
        month = int(str(date)[-6:-4])
        year = int(str(date)[-4:])
        return day, month, year

    def find_grandchildren(self):
        """Return a list of grandchildren (Person objects) of the current person.
        Loop, that goes through children of parents and find their children."""
        grandchildren = []
        for child in self.find_children():
            grandchildren.extend(child.find_children())
        return grandchildren

    def find_grandparents(self):
        """Adding grandparents to the list
        using loop that goes through parents of parents"""
        grandparents = []
        for parent in self.find_parents():
            grandparents.extend(parent.find_parents())
        return grandparents

    def immediate_family_members(self):
        """Saving people in immediate family members: parents, spouse, children and siblings."""
        parents = self.find_parents()
        spouse = self.find_spouse()
        children = self.find_children()
        siblings = self.find_siblings()
        return parents, spouse, children, siblings

    def number_of_children(self):
        """Return the number of children of the selected person."""
        return len(self.find_children())

    def is_alive(self):
        """Check if selected person is alive"""
        if self._death_day == -1:  # if instead of the date of death there is '-1' in the list, the person is alive
            return True
        else:
            return False

    def extended_family_members(self):
        """Return a list of extended family members of selected person."""
        extended_family = []  # list for all extended family members
        relations = [
            self.find_parents(),
            self.find_spouse(),
            self.find_children(),
            self.find_siblings(),
            [sibling for parent in self.find_parents() for sibling in parent.find_siblings()],  # adding siblings of parents
            self.find_cousins()
        ]

        for relation_list in relations:
            for relation in relation_list:
                if relation.is_alive():
                    extended_family.append(relation)  # adds member to extended family
        return extended_family

    #static method returns current day, month, and year to be able to calculate average age in other functions
    @staticmethod
    def current_datetime():
        """Using datetime module to get current date and convert it to int"""
        import datetime
        date_time = datetime.datetime.now()
        current_day = int(str(date_time.day))
        current_month = int(str(date_time.month))
        current_year = int(str(date_time.year))
        return current_day, current_month, current_year

    def get_age(self):
        """Return age of the selected person.
        Using current date/date of death and date of birth to calculate age of person."""
        current_day, current_month, current_year = self.current_datetime()  # converting into variables
        birth_day, birth_month, birth_year = self.get_birthday()  # converting into variables
        if self.is_alive():  # if the person is alive - the current date is subtracted by the date of birth.
            current_age_years = current_year - birth_year
            if (birth_month > current_month) or (birth_month == current_month and birth_day > current_day):
                current_age_years -= 1
        else:  # if the person is dead - the date of death is subtracted by the date of birth
            death_day, death_month, death_year = self.get_death_day()
            current_age_years = death_year - birth_year
            if (birth_month > death_month) or (birth_month == death_month and birth_day > death_day):
                current_age_years -= 1
        return current_age_years