# this .py file includes functions for adding people to the list
# .py icludes functions for saving the list to a csv file and reading from a csv file.


from person import Person
from FamilyTree import FamilyTree
import csv


def save_csv(family_tree):
    """Saves the family tree to a CSV file."""
    with open("family_tree.csv", "w") as file:
        writer = csv.writer(file, lineterminator="\n")  # lineterminator eliminates the empty line
        writer.writerow(["Name", "Date of Birth", "Gender", "Death Day"])  # writing rows to the csv file
        for member in family_tree.members:
            birth_day, birth_month, birth_year = member.get_birthday()  # converting into variables
            if not member.is_alive():
                death_day, death_month, death_year = member.get_death_day()
                death = f"{death_day}/{death_month}/{death_year}"
            else:
                death = "Alive"
            writer.writerow([
                member.name,
                f"{birth_day}/{birth_month}/{birth_year}",
                member._gender,
                death
            ])


def read_csv(path = "family_tree.csv"):
    """Reads a CSV file and adds the people to the family tree."""
    family_tree = FamilyTree()
    with open("family_tree.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row.
        for row in reader:
            name, date_of_birth, gender, death_day = row
            date_of_birth = int(date_of_birth.replace("/", ""))  # replacing '/' with an empty string
            try:
                death_day = int(death_day.replace("/", ""))  # replacing '/' with an empty string
            except:
                death_day = -1
            # adding the person to the family tree
            family_tree.add_member(Person(name, date_of_birth, gender, death_day))
    return family_tree



# Adds a person to the family tree using the function 'add_member' from the FamilyTree class.

# family_tree = FamilyTree()

# family_tree.add_member(Person("Cornelia Emmersohn", 24_07_1982, "Female", -1))
# family_tree.add_member(Person("Otto Emmersohn", 19_05_1980, "Male", -1))
#
# family_tree.add_member(Person("Ara Song", 2_02_1948, "Female", 3_02_1972))
# family_tree.add_member(Person("John Winchester", 11_01_1947, "Male", 27_11_1995))
# family_tree.add_member(Person("Amy Wong", 12_11_1932, "Female", -1))
# family_tree.add_member(Person("Bo Chen", 23_08_1932, "Male", 9_11_2001))
# family_tree.add_member(Person("Andra Kaur", 30_10_1934, "Female", 23_05_2012))
# family_tree.add_member(Person("Kanan Khan", 23_01_1923, "Male", 30_05_2022))
#
# family_tree.add_member(Person("Emma Desposito", 5_07_1900, "Female", 17_03_2000))
# family_tree.add_member(Person("Nico Romano", 22_05_1897, "Male", 27_04_1964))
#
# family_tree.add_member(Person("Anna Romano", 12_01_1930, "Female", 6_02_1998))
# family_tree.add_member(Person("Deniele Bruno", 11_08_1928, "Male", 25_10_2024))
# family_tree.add_member(Person("Ada Hoffman", 28_02_1931, "Female", 4_03_1987))
# family_tree.add_member(Person("Gunther Emmersohn", 14_03_1928, "Male", 28_05_1957))
#
# family_tree.add_member(Person("Sam Song", 12_06_1969, "Male", -1))
# family_tree.add_member(Person("Emma Chen", 14_04_1970, "Female", -1))
# family_tree.add_member(Person("David Martinez", 23_05_1957, "Male", 12_07_1980))
# family_tree.add_member(Person("Lucy Chen", 14_04_1959, "Female", -1))
# family_tree.add_member(Person("Josh Khan", 26_08_1957, "Male", -1))
# family_tree.add_member(Person("Isabella Bruno", 19_03_1950, "Female", -1))
# family_tree.add_member(Person("Bernard Emmersohn", 31_10_1948, "Male", 16_04_2002))
# family_tree.add_member(Person("Zakk Emmersohn", 31_10_1956, "Male", -1))
#
# family_tree.add_member(Person("Chan Soun", 11_04_1988, "Male", -1))
# family_tree.add_member(Person("An Chen", 24_12_1991, "Female", -1))
# family_tree.add_member(Person("Aki Chen", 21_07_1995, "Male", 22_07_1995))
# family_tree.add_member(Person("Guozhi Chen", 16_08_2009, "Male", 19_03_2019))
# family_tree.add_member(Person("Harold Stokes", 18_03_1982, "Male", -1))
# family_tree.add_member(Person("Lina Chen", 18_11_1979, "Female", -1))
# family_tree.add_member(Person("Adeline Chen", 18_11_1979, "Female", 1_01_2014))
# family_tree.add_member(Person("Karl Emmersohn", 19_05_1985, "Male", -1))
#
# family_tree.add_member(Person("Jessica Vegas", 21_02_2000, "Female", -1))
# family_tree.add_member(Person("Shelby Emmersohn", 23_09_2001, "Male", -1))
# family_tree.add_member(Person("Melina Emmersohn", 7_03_2008, "Female", -1))

family_tree = read_csv()  # reads the csv file and adds the people from there to the family_tree variable
# print(family_tree.members)  # to make sure it works

# Adds a spouse and parent-child relationship between people using the functions from the FamilyTree class.

family_tree.add_spouse_relationship("Ara Song", "John Winchester")
family_tree.add_parent_relationship(["Sam Song"], "Ara Song", "John Winchester")

family_tree.add_spouse_relationship("Amy Wong", "Bo Chen")
family_tree.add_parent_relationship(["Emma Chen", "Lucy Chen"], "Amy Wong", "Bo Chen")

family_tree.add_spouse_relationship("Andra Kaur", "Kanan Khan")
family_tree.add_parent_relationship(["Josh Khan"], "Andra Kaur", "Kanan Khan")

family_tree.add_spouse_relationship("Emma Desposito", "Nico Romano")
family_tree.add_parent_relationship(["Anna Romano"], "Emma Desposito", "Nico Romano")

family_tree.add_spouse_relationship("Anna Romano", "Deniele Bruno")
family_tree.add_parent_relationship(["Isabella Bruno"], "Anna Romano", "Deniele Bruno")

family_tree.add_spouse_relationship("Ada Hoffman", "Gunther Emmersohn")
family_tree.add_parent_relationship(["Bernard Emmersohn", "Zakk Emmersohn"], "Ada Hoffman", "Gunther Emmersohn")


family_tree.add_spouse_relationship("Sam Song", "Emma Chen")
family_tree.add_parent_relationship(["An Chen", "Aki Chen", "Guozhi Chen"], "Sam Song", "Emma Chen")

family_tree.add_spouse_relationship("David Martinez", "Lucy Chen")
family_tree.add_spouse_relationship("Josh Khan", "Lucy Chen")
family_tree.add_parent_relationship(["Lina Chen", "Adeline Chen", "Cornelia Emmersohn"], "Josh Khan", "Lucy Chen")

family_tree.add_spouse_relationship("Isabella Bruno", "Bernard Emmersohn")
family_tree.add_parent_relationship(["Otto Emmersohn", "Karl Emmersohn"], "Isabella Bruno", "Bernard Emmersohn")

family_tree.add_spouse_relationship("Chan Soun", "An Chen")

family_tree.add_spouse_relationship("Harold Stokes", "Lina Chen")

family_tree.add_spouse_relationship("Cornelia Emmersohn", "Otto Emmersohn")
family_tree.add_parent_relationship(["Shelby Emmersohn", "Melina Emmersohn"], "Cornelia Emmersohn", "Otto Emmersohn")

family_tree.add_spouse_relationship("Jessica Vegas", "Shelby Emmersohn")


# save_csv(family_tree)