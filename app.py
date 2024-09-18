
def add_contact(contact_list):
    name = input("Enter the name of the contact: ")
    number = input("Enter the phone number of the contact (no spaces): ")
    email = input("Enter the email of the contact: ")
    additional_info = input("Enter any additional info e.g., address, birthday, etc. (optional): ")
    id = len(contact_list)+1
    contact_list[id] = {'name': name, 'number': number, 'email': email, 'additional_info': additional_info}
    print('Contact added successfully!')

def edit_contact(contact_list):
    name = input("Enter the name of the contact you'd like to edit: ")
    # Find the contact by name
    contact_id = None
    for id, contact in contact_list.items():
        if contact['name'] == name:
            contact_id = id
            break

    if contact_id is None:
        print(f"No contact found with the name {name}.")
        return

    field = input("Enter the field you'd like to edit (name, number, email, additional_info): ")
    if field in contact_list[contact_id]:
        new_value = input(f"Enter the new {field}: ")
        contact_list[contact_id][field] = new_value
        print('Contact edited successfully!')
    else:
        print(f"Invalid field: {field}")


def delete_contact(contact_list):
    name = input("Enter the name of the contact you'd like to delete: ")
    contact_id = None
    for id, contact in contact_list.items():
        if contact['name'] == name:
            contact_id = id
            break

    if contact_id is None:
        print(f"No contact found with the name {name}.")
        return

    del contact_list[contact_id]
    print('Contact deleted successfully!')


def view_contacts(contact_list):
    if not contact_list:
        print("No contacts found.")
    for id, contact in contact_list.items():
        print(f"ID: {id}")
        print(f"Name: {contact['name']}")
        print(f"Number: {contact['number']}")
        print(f"Email: {contact['email']}")
        print(f"Additional Info: {contact['additional_info']}")

def search_contact(contact_list):
    name = input("Enter the name of the contact you'd like to search for: ")
    found = False
    for id, contact in contact_list.items():
        if contact['name'] == name:
            print(f"ID: {id}")
            print(f"Name: {contact['name']}")
            print(f"Number: {contact['number']}")
            print(f"Email: {contact['email']}")
            print(f"Additional Info: {contact['additional_info']}")
            found = True
            break
    if not found:
        print(f"No contact found with the name {name}.")



def main():
    contact_list = {}

    while True:
        try:
            selection = int(input('''
Welcome to the Contact Management System! 
Menu:
1. Add a new contact
2. Edit an existing contact
3. Delete a contact
4. Search for a contact
5. Display all contacts
6. Export contacts to a text file
7. Quit
Please enter the number of your selection: '''))
            if selection == 1:
                add_contact(contact_list)
            elif selection == 2:
                edit_contact(contact_list)
            elif selection == 3:
                delete_contact(contact_list)  
            elif selection == 4:
                search_contact(contact_list)  
            elif selection == 5:
                view_contacts(contact_list)
            elif selection == 6:
                print('Exporting contacts to a text file...')
                with open('contacts.txt', 'w') as file:
                    for id, contact in contact_list.items():
                        file.write(f"ID: {id}\n")
                        file.write(f"Name: {contact['name']}\n")
                        file.write(f"Number: {contact['number']}\n")
                        file.write(f"Email: {contact['email']}\n")
                        file.write(f"Additional Info: {contact['additional_info']}\n")
                        file.write('\n')
                print("Contacts exported successfully!")
            elif selection == 7:
                break
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Invalid selection. Please enter a number.")
if __name__ == "__main__":
    main()