import unittest

from list import family_tree
from relationship import ChildRelationship


class TestFamilyTree(unittest.TestCase):

    def test_find_person_by_name(self):
        person = family_tree.find_person_by_name("Cornelia Emmersohn")
        self.assertEqual(person.name, "Cornelia Emmersohn")

    def test_get_relationship(self):
        self.parent1 = family_tree.find_person_by_name("Cornelia Emmersohn")
        self.child = family_tree.find_person_by_name("Shelby Emmersohn")
        self.relationship = ChildRelationship(self.parent1, self.child)
        self.assertEqual(self.parent1, self.relationship.person1)
        self.assertEqual(self.child, self.relationship.person2)

    def test_find_spouse(self):
        persons_spouse = family_tree.find_person_by_name("Cornelia Emmersohn").find_spouse()
        self.assertEqual(persons_spouse, [family_tree.find_person_by_name("Otto Emmersohn")])

    def test_find_parents(self):
        parents = family_tree.find_person_by_name("Cornelia Emmersohn").find_parents()
        self.assertEqual(parents, [family_tree.find_person_by_name("Josh Khan"),
                                   family_tree.find_person_by_name("Lucy Chen")])

    def test_find_siblings(self):
        siblings = family_tree.find_person_by_name("Cornelia Emmersohn").find_siblings()
        self.assertEqual(siblings, [family_tree.find_person_by_name("Lina Chen"),
                                    family_tree.find_person_by_name("Adeline Chen")])

    def test_find_children(self):
        children = family_tree.find_person_by_name("Cornelia Emmersohn").find_children()
        self.assertEqual(children, [family_tree.find_person_by_name("Shelby Emmersohn"),
                                    family_tree.find_person_by_name("Melina Emmersohn")])

    def test_find_cousins(self):
        cousins = family_tree.find_person_by_name("Cornelia Emmersohn").find_cousins()
        self.assertEqual(cousins, [family_tree.find_person_by_name("An Chen"),
                                   family_tree.find_person_by_name("Aki Chen"),
                                   family_tree.find_person_by_name("Guozhi Chen")])

    def test_find_grandchildren(self):
        grandchildren = family_tree.find_person_by_name("Amy Wong").find_grandchildren()
        self.assertEqual(grandchildren, [family_tree.find_person_by_name("An Chen"),
                                         family_tree.find_person_by_name("Aki Chen"),
                                         family_tree.find_person_by_name("Guozhi Chen"),
                                         family_tree.find_person_by_name("Lina Chen"),
                                         family_tree.find_person_by_name("Adeline Chen"),
                                         family_tree.find_person_by_name("Cornelia Emmersohn")])

    def test_find_grandparents(self):
        grandparents = family_tree.find_person_by_name("Cornelia Emmersohn").find_grandparents()
        self.assertEqual(grandparents, [family_tree.find_person_by_name("Andra Kaur"),
                                        family_tree.find_person_by_name("Kanan Khan"),
                                        family_tree.find_person_by_name("Amy Wong"),
                                        family_tree.find_person_by_name("Bo Chen")])

    def test_immediate_family_members(self):
        person = family_tree.find_person_by_name("Cornelia Emmersohn")
        immediate_family = person.immediate_family_members()
        self.assertEqual(immediate_family, ([family_tree.find_person_by_name("Josh Khan"),
                                            family_tree.find_person_by_name("Lucy Chen")],
                                            [family_tree.find_person_by_name("Otto Emmersohn")],
                                            [family_tree.find_person_by_name("Shelby Emmersohn"),
                                            family_tree.find_person_by_name("Melina Emmersohn")],
                                            [family_tree.find_person_by_name("Lina Chen"),
                                            family_tree.find_person_by_name("Adeline Chen")]))

    def test_extended_family_members(self):
        person = family_tree.find_person_by_name("Cornelia Emmersohn")
        extended_family = person.extended_family_members()
        self.assertEqual(extended_family, [family_tree.find_person_by_name("Josh Khan"),
                                           family_tree.find_person_by_name("Lucy Chen"),
                                           family_tree.find_person_by_name("Otto Emmersohn"),
                                           family_tree.find_person_by_name("Shelby Emmersohn"),
                                           family_tree.find_person_by_name("Melina Emmersohn"),
                                           family_tree.find_person_by_name("Lina Chen"),
                                           family_tree.find_person_by_name("Emma Chen"),
                                           family_tree.find_person_by_name("An Chen")
                                           ])

    def test_number_of_children(self):
        person1 = family_tree.find_person_by_name("Cornelia Emmersohn")
        self.assertEqual(person1.number_of_children(), 2)
        person2 = family_tree.find_person_by_name("Sam Song")
        self.assertEqual(person2.number_of_children(), 3)

    def test_get_age(self):
        current_age_years = family_tree.find_person_by_name("Melina Emmersohn").get_age()
        self.assertEqual(current_age_years, 16)

    def test_get_birthday(self):
        person = family_tree.find_person_by_name("Melina Emmersohn")
        birthday = person.get_birthday()
        self.assertEqual(birthday, (7, 3, 2008))

    def test_is_alive(self):
        person1 = family_tree.find_person_by_name("Cornelia Emmersohn")
        person2 = family_tree.find_person_by_name("Otto Emmersohn")
        person3 = family_tree.find_person_by_name("Kanan Khan")
        person4 = family_tree.find_person_by_name("Andra Kaur")
        self.assertEqual(person1.is_alive(), True)
        self.assertEqual(person2.is_alive(), True)
        self.assertEqual(person3.is_alive(), False)
        self.assertEqual(person4.is_alive(), False)

    def test_average_age_per_person(self):
        self.assertEqual(family_tree.average_age_per_person(), 50)

    def test_average_age_at_death(self):
        self.assertEqual(family_tree.average_age_at_death(), 48)

    def test_total_children(self):
        self.assertEqual(family_tree.total_children_count(), 36)

    def test_average_children_per_person(self):
        self.assertEqual(family_tree.average_children_per_person(), 1)

    def test_get_birthday_calendar(self):
        person = family_tree.find_person_by_name("Cornelia Emmersohn")
        members = family_tree.get_branch(person)
        birthdays = family_tree.get_birthday_calendar(members)
        self.assertEqual(birthdays, {(2, 2): [family_tree.find_person_by_name("Ara Song")],
                                            (7, 3): [family_tree.find_person_by_name("Melina Emmersohn")],
                                            (11, 1): [family_tree.find_person_by_name("John Winchester")],
                                            (11, 4): [family_tree.find_person_by_name("Chan Soun")],
                                            (12, 6): [family_tree.find_person_by_name("Sam Song")],
                                            (12, 11): [family_tree.find_person_by_name("Amy Wong")],
                                            (14, 4): [family_tree.find_person_by_name("Lucy Chen"),
                                                      family_tree.find_person_by_name("Emma Chen")],
                                            (16, 8): [family_tree.find_person_by_name("Guozhi Chen")],
                                            (18, 3): [family_tree.find_person_by_name("Harold Stokes")],
                                            (18, 11): [family_tree.find_person_by_name("Lina Chen"),
                                                       family_tree.find_person_by_name("Adeline Chen")],
                                            (21, 7): [family_tree.find_person_by_name("Aki Chen")],
                                            (23, 1): [family_tree.find_person_by_name("Kanan Khan")],
                                            (23, 5): [family_tree.find_person_by_name("David Martinez")],
                                            (23, 8): [family_tree.find_person_by_name("Bo Chen")],
                                            (23, 9): [family_tree.find_person_by_name("Shelby Emmersohn")],
                                            (24, 7): [family_tree.find_person_by_name("Cornelia Emmersohn")],
                                            (24, 12): [family_tree.find_person_by_name("An Chen")],
                                            (26, 8): [family_tree.find_person_by_name("Josh Khan")],
                                            (30, 10): [family_tree.find_person_by_name("Andra Kaur")]})


if __name__ == "__main__":
    unittest.main()