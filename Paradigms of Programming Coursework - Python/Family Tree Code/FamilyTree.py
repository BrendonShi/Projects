# this .py file contains a FamilyTree class that is responsible for all members of the family tree
# includes a list of members and methods for adding members and relationships
# contains method for finding a branch


from relationship import ParentRelationship, ChildRelationship, SpouseRelationship


class FamilyTree:
    members = []  # list of all members of the family tree

    def add_member(self, member):
        """Adds a member to the family tree."""
        self.members.append(member)

    def add_relationship(self, relationship_type, person1_name, person2_name):
        """Adds a relationship between two people."""
        person1 = self.find_person_by_name(person1_name)
        person2 = self.find_person_by_name(person2_name)
        if person1 is None or person2 is None:
            print(f"{person1_name} or {person2_name} do not exist")
            return

        relationship = relationship_type(person1, person2)
        person1.add_relationship(relationship)

    def add_spouse_relationship(self, person1_name, person2_name):
        """Adds a spouse relationship between two people."""
        self.add_relationship(SpouseRelationship, person1_name, person2_name)
        self.add_relationship(SpouseRelationship, person2_name, person1_name)

    def find_person_by_name(self, name):
        """Finds a person by name."""
        for person in self.members:
            if person.name == name:
                return person
        return None

    def add_parent_relationship(self, children, parent1, parent2):
        """Adds parent-child relationships between children and two parents."""
        for child in children:
            self.add_relationship(ParentRelationship, parent1, child)
            self.add_relationship(ParentRelationship, parent2, child)
            self.add_relationship(ChildRelationship, child, parent1)
            self.add_relationship(ChildRelationship, child, parent2)

    def get_branch(self, person, visited=None):
        """Loop that goes through whole family branch to add people to the list.
        Using “visited” prevents an endless loop of adding people to this list,
        and if a person is already on the list when you view it again, they will not be added."""
        first_person = False
        if visited is None:
            visited = []
            first_person = True
        if person in visited:
            return []
        visited.append(person)
        members = [person]
        for parent in person.find_parents():
            members.extend(self.get_branch(parent, visited))
        if not first_person:
            for child in person.find_children():
                members.extend(self.get_branch(child, visited))
            for spouse in person.find_spouse():
                members.extend(self.get_branch(spouse, visited))
        else:
            for child in person.find_children():
                members.append(child)
        return members

    def get_birthday_calendar(self, members):
        """Returns sorted birthday calendar."""
        birthday_calendar = {}
        for member in members:
            day, month, year = member.get_birthday()
            birthday = (day, month)
            if birthday in birthday_calendar:
                birthday_calendar[birthday].append(member)
            else:
                birthday_calendar[birthday] = [member]
        birthday_calendar = dict(sorted(birthday_calendar.items(), key=lambda x: (x[0][1], x[0][0])))
        return birthday_calendar

    def average_age_per_person(self):
        """Calculates the average age per person."""
        total_members = len(self.members)
        total_age = sum(person.get_age() for person in self.members)  # adding all ages
        average_age = total_age // total_members
        return average_age

    def average_age_at_death(self):
        """Calculates the average age at death."""
        dead_members = [person for person in self.members if person.is_alive()]  # a loop for adding people if alive
        total_age = sum(person.get_age() for person in dead_members)  # finding sum of ages of dead members
        average_age = total_age // len(dead_members)
        return average_age

    def total_children_count(self):
        """Calculate the total number of children."""
        total_children = sum(len(person.find_children()) for person in self.members)
        return total_children

    def average_children_per_person(self):
        """Calculate the average number of children per person."""
        total_members = len(self.members)
        if total_members == 0:
            return 0
        total_children = self.total_children_count()
        # Use 'total_children_count' to get the total number of children
        average_children = total_children // total_members
        # Calculate the average
        return average_children