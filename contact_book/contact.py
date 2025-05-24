contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts to display.\n")
        return
    print("\nContact List:")
    for idx, c in enumerate(contacts, start=1):
        print(f"{idx}. {c['name']} - {c['phone']}")
    print()

def search_contact():
    keyword = input("Enter name or phone to search: ").lower()
    found = False
    for c in contacts:
        if keyword in c['name'].lower() or keyword in c['phone']:
            print(f"\nName: {c['name']}\nPhone: {c['phone']}\nEmail: {c['email']}\nAddress: {c['address']}\n")
            found = True
    if not found:
        print("No contact found.\n")

def update_contact():
    name = input("Enter the name of the contact to update: ").lower()
    for c in contacts:
        if c['name'].lower() == name:
            c['phone'] = input("Enter new phone number: ")
            c['email'] = input("Enter new email: ")
            c['address'] = input("Enter new address: ")
            print("Contact updated.\n")
            return
    print("Contact not found.\n")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").lower()
    for i, c in enumerate(contacts):
        if c['name'].lower() == name:
            del contacts[i]
            print("Contact deleted.\n")
            return
    print("Contact not found.\n")

def main():
    while True:
        print("=== Contact Manager ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")

main()
