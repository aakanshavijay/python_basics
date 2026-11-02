#storing a contact
contacts = {
    "Riya": "9876543210",
    "Aman": "9876501234"
}

name = input("Enter a contact name: ")

if name in contacts:
    print("Phone number:", contacts[name])
else:
    print("Contact not found.")


#interactive 
contacts = {}

while True:
    print("\n--- Contact Book ---")
    print("1. Add contact")
    print("2. Search contact")
    print("3. View all contacts")
    print("4. Delete contact")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        contacts[name] = phone
        print("Contact saved.")

    elif choice == "2":
        name = input("Enter name to search: ")

        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Contact not found.")

    elif choice == "3":
        for name, phone in contacts.items():
            print(name, ":", phone)

    elif choice == "4":
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")