# this .py file is created in order to embed the main functions of the application, which transport functions from other .py files

from list import family_tree


def find_spouse(family_tree, name):
    """Output spouse of a person."""
    spouse = family_tree.find_person_by_name(name).find_spouse()
    if spouse:
        print("\nSpouse:")
        print(*[f"{spouse.name}" for spouse in spouse], sep='\n')  # Print the names of the spouse separated(sep='\n') by a newline.
    else:
        print("\nNo spouse found.")


def print_parents(family_tree, name):
    """Output parents of a person."""
    parents = family_tree.find_person_by_name(name).find_parents()
    if parents:
        print("\nParents:")
        print(*[f"{parent.name}" for parent in parents], sep='\n')  # Print the names of the parents separated(sep='\n') by a newline.
    else:
        print("\nNo parents found.")


def find_children(family_tree, name):
    """Output children of a person."""
    children = family_tree.find_person_by_name(name).find_children()
    if children:
        print("\nChildren:")
        print(*[f"{child.name}" for child in children], sep='\n')  # Print the names of the children separated(sep='\n') by a newline.
    else:
        print("\nNo children found.")


def find_siblings(family_tree, name):
    """Output siblings of a person."""
    siblings = family_tree.find_person_by_name(name).find_siblings()
    if siblings:
        print("\nSiblings:")
        print(*[f"{sibling.name}" for sibling in siblings], sep='\n')  # Print the names of the siblings separated(sep='\n') by a newline.
    else:
        print("No siblings found.")


def find_cousins(family_tree, name):
    """Output cousins of a person."""
    cousins = family_tree.find_person_by_name(name).find_cousins()  # Variable for cousins, created to record cousins.
    if cousins:
        print("\nCousins:")
        print(*[f"{cousin.name}" for cousin in cousins], sep='\n')  # Print the names of the siblings separated(sep='\n') by a newline.
    else:
        print("No cousins found.")


def find_birthday(family_tree, name):
    """Output birthday of a person."""
    birthday = family_tree.find_person_by_name(name).get_birthday()
    if birthday:
        print(f"\nBirthday: {birthday[0]}/{birthday[1]}/{birthday[2]}")  # Outputs birthday if is known.
    else:
        print("No birthday found.")


def family_birthdays_in_branch(family_tree, name):
    """Output birthdays of all people in a branch."""
    person = family_tree.find_person_by_name(name)  # creates a variable for person
    branch = family_tree.get_branch(person)
    for member in branch:
        day, month, year = member.get_birthday()  # Variable for day, month, year - helps to display birthdays individually.
        print(f"Person: {member.name}")
        print(f"Birthday: {day}/{month}/{year}")
        print("")


def find_sorted_birthdays_calendar(family_tree, name):
    """Output birthdays calendar sorted by month and day only."""
    person = family_tree.find_person_by_name(name)  # creates a variable for person
    branch = family_tree.get_branch(person)
    calendar = family_tree.get_birthday_calendar(branch)
    for date in calendar:
        print(f"Day: {date[0]}/{date[1]}")  # Prints the day and month of birth using the selected values in the array.
        for member in calendar[date]:  # Prints the member's name in members of branch.
            print(f"Name: {member.name}")
        print("")


def find_immediate_family_members(family_tree, name):
    """Output immediate family members of a person."""
    person = family_tree.find_person_by_name(name)  # creates a variable for person
    parents, spouse, children, siblings = person.immediate_family_members()  # Search for a family members and assign to a variables
    if parents:
        print("\nParents:")
        print(*[f"{parent.name}" for parent in parents], sep='\n')  # Print the names of the parents separated by a newline.
    if spouse:
        print("\nSpouse:")
        print(*[f"{spouse.name}" for spouse in spouse], sep='\n')
    if children:
        print("\nChildren:")
        print(*[f"{children.name}" for children in children], sep='\n')
    if siblings:
        print("\nSiblings:")
        print(*[f"{siblings.name}" for siblings in siblings], sep='\n')


def extended_family_members(family_tree, name):
    """Output extended family members of a person."""
    person = family_tree.find_person_by_name(name)  # creates a variable for person
    extended_family = person.extended_family_members()  # variable for extended family
    if extended_family:
        print("\nExtended Family:")
        print(*[f"{member.name}" for member in extended_family], sep='\n')
    else:
        print("No extended family found.")


def number_of_children(family_tree, name):
    """Output number of children of a person."""
    children = family_tree.find_person_by_name(name).number_of_children()
    if children:
        print(f"\nNumber of children: {children}")
    else:
        print("No children found.")


def find_grandchildren(family_tree, name):
    """Output grandchildren of a person."""
    person = family_tree.find_person_by_name(name)  # creates a variable for person
    grandchildren = person.find_grandchildren()
    if grandchildren:
        print("\nGrandchildren:")
        print(*[f"Name: {grandchild.name}" for grandchild in grandchildren], sep='\n')
    else:
        print("No grandchildren found.")


def find_grandparents(family_tree, name):
    """Output grandparents of a person."""
    person = family_tree.find_person_by_name(name)  # creates a variable for person
    grandparents = person.find_grandparents()
    if grandparents:
        print("\nGrandparents:")
        print(*[f"{grandparent.name}" for grandparent in grandparents], sep='\n')
    else:
        print("No grandparents found.")


def average_age(family_tree):
    """Return average age of all people in the family."""
    return f"\nAverage age: {family_tree.average_age_per_person()}"


def average_age_at_death(family_tree):
    """Return average age at death of all people in the family."""
    return f"\nAverage age at death: {family_tree.average_age_at_death()}"


def average_children(family_tree):
    """Return average number of children per person."""
    return f"\nAverage children per person: {family_tree.average_children_per_person()}"


# array of options for the first/start menu
# lambda is used to call functions that were written above
start_options = [
    ["Find information by person", lambda: use_options()],
    ["Find the information of all recorded people", lambda: family_menu()],
    ["Exit", lambda: exit()],
]


# this array contains the options used to find family relationships associated with the selected person
member_options = [
    ["Find spouse", lambda name: find_spouse(family_tree, name)],
    ["Find parents", lambda name: print_parents(family_tree, name)],
    ["Find children", lambda name: find_children(family_tree, name)],
    ["Find siblings", lambda name: find_siblings(family_tree, name)],
    ["Find cousins", lambda name: find_cousins(family_tree, name)],
    ["Find birthday", lambda name: find_birthday(family_tree, name)],
    ["Family birthdays", lambda name: family_birthdays_in_branch(family_tree, name)],
    ["Find sorted birthdays calendar", lambda name: find_sorted_birthdays_calendar(family_tree, name)],
    ["Find immediate family members", lambda name: find_immediate_family_members(family_tree, name)],
    ["Extended family members(alive)", lambda name: extended_family_members(family_tree, name)],
    ["Find number of children", lambda name: number_of_children(family_tree, name)],
    ["Find grandchildren", lambda name: find_grandchildren(family_tree, name)],
    ["Find grandparents", lambda name: find_grandparents(family_tree, name)],
    ["Enter name again", lambda name: use_options()],
    ["Exit to main menu", lambda name: start_menu()],
]


# array contains the options wich calculates averages per person
family_options = [
    ["Average age per person", lambda: print(average_age(family_tree))],
    ["Average age at death", lambda: print(average_age_at_death(family_tree))],
    ["Average children per person", lambda: print(average_children(family_tree))],
    ["Exit to main menu", lambda: start_menu()],
]


def start_menu():
    """Outputs first menu options."""
    while True:
        print("\nOptions: ")
        for i, option in enumerate(start_options, 1):  # loop for each option in the enumarated array
            print(f"{i}. {option[0]}")  # prints the enumarated options(1 - number; and 2 - option)
        try:  # try this code
            command = int(input("\nEnter command: "))
            # the number entered cannot be greater than the maximum number of option counts, or not an integer
            if command > len(start_options) or not isinstance(command, int):
                print("Invalid command")
                continue
        except ValueError:  # if something is wrong in the previous code in 'try' - this code will be executed
            print("Invalid command")
            continue
        start_options[command - 1][1]()  # using the number entered to call the function from the array above


def use_options():
    """Outputs second menu options."""
    member_list = [member.name for member in family_tree.members]
    print("\nWelcome to Otto's and Cornelia's Family Tree, please select a person: ")
    print(*member_list, sep='\n')  # prints the separated array of member list
    name = input("\nEnter name: ")
    if family_tree.find_person_by_name(name):  # if a person exists
        while True:
            print(f"\nOptions: ")
            for i, option in enumerate(member_options):  # loop for each option in the enumarated array
                print(f"{i + 1}. {option[0]}")  # print the enumarated options(1 - number; and 2 - option)
            try:  # try this code
                command = int(input("\nEnter command: "))
                # the number entered cannot be greater than the maximum number of option counts, or not an integer
                if command > len(member_options) or not isinstance(command, int):
                    print("Invalid command")
                    continue
            except ValueError:  # if something is wrong in the previous code in 'try' - this code will be executed
                print("Invalid command")
                continue
            member_options[int(command) - 1][1](name)  # using the number entered to call the function from the array above
    else:
        print("Person not found.")
        start_menu()


def family_menu():
    """Outputs third menu options."""
    while True:
        print("\nOptions: ")
        for i, option in enumerate(family_options):  # loop for each option in the enumarated array
            print(f"{i + 1}. {option[0]}")  # print the enumarated options(1 - number; and 2 - option)
        try:  # try this code
            command = input("\nEnter command: ")
            # the number entered cannot be greater than the maximum number of option counts
            if int(command) > len(family_options):
                print("Invalid command")
                continue
        except ValueError:  # if something is wrong in the previous code in 'try' - this code will be executed
            print("Invalid command")
            continue
        family_options[int(command) - 1][1]()  # using the number entered to call the function from the array above

family_tree.find_person_by_name("Otto Emmersohn")
start_menu()  # calling the start menu function