phone_book = {}


def add_contact(name, number):
    if name in phone_book:
        print(f"{name} already exists, do you want to replace it with {
              number} (yes/no)")
        response = input()  # Get user input for the decision
        if response.lower() == 'yes':  # Get user input for the new number
            phone_book[name] = number
            print(f"Updated {name} with the new number {number}.")
        else:
            print(f"No changes made.")
    else:
        phone_book[name] = number
        print(f"Added {name} with number {number} to the phonebook.")


def del_contact(name):
    if name in phone_book:
        del phone_book[name]
        print(f"{name} deleted successfully.")
    else:
        print(f"{name} not found in phonebook.")


def find_contact(name):
    if name in phone_book:
        user_num = phone_book.get(name)
        print(f'{name}, {user_num}')
    else:
        print('contact not found')


def change_contact(phone_book, name, new_number):
    if name in phone_book:
        phone_book[name] = new_number
        print("Contact updated successfully.")
    else:
        print("Contact not found.")


def display_contacts(phone_book):
    if phone_book:
        for name, number in phone_book.items():
            print(f"{name}: {number}")
    else:
        print("No contacts in phone book.")


def contact():
    while True:
        print('\nWelcome to the Phone Book App')
        print('1. add contact')
        print('2. delete contact')
        print('3. find contact')
        print('4. change contact')
        print('5. display contact')
        print('6. exit')

        choice = input(
            'Pick the number of your desired choice from the above ')

        if choice == '1':
            name = input('Enter name here: ')
            number = int(input('Enter number here '))
            add_contact(name, number)
        elif choice == '2':
            name = input('Enter name to delete here ')
            del_contact(name)
        elif choice == '3':
            name = input('Search for name here ')
            find_contact(name)
        elif choice == '4':
            name = input('Enter the name to update here ')
            number = int(input('Enter number here '))
            change_contact(phone_book, name, number)
        elif choice == '5':
            display_contacts(phone_book)
        elif choice == '6':
            # Exit message before breaking the loop
            print("Exiting phonebook.")
            break
        else:
            print("Invalid option. Please try again.")


contact()
