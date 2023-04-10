# https://golookup.com/

# The goal is to write a scraper that searches for input name & location, covering the following outcomes:
# find results
# no results found
# error

# imports
from models.demographics import Name, Location, Person
from scraper import scrape_person

# main
if __name__ == '__main__':
    # greeting
    print("Welcome!")
    print()

    # get name
    print("What is the name of the person you wish to search?")
    while True:
        try:
            print("First: ")
            first = Name(name=input())
        except ValueError as e:
            print("First name must be at least 1 character. Please re-enter first name.")
            continue
        break
    while True:
        try:
            print("Last: ")
            last = Name(name=input())
        except ValueError as e:
            print("Last name must be at least 1 character. Please re-enter last name.")
            continue
        break
    print()

    # get location
    print("What is this person's location?")
    while True:
        try:
            print("State: ")
            location = Location(state=input())
        except ValueError as e:
            print("Must enter \"All States\", \"District of Columbia\" or a valid US state with proper spacing and "
                  "capitalization. Please re-enter state.")
            continue
        break
    print()

    # save person
    person = Person(first_name=first, last_name=last, location=location)

    # scrape person & inform user of delay
    print("Your data will be ready in about 45 seconds.")
    print()
    result = scrape_person(person=person)

    # display results
    print(result)
