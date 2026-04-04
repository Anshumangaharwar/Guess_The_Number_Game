def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")

    with open("contacts.txt", "a") as file:
        file.write(f"{name},{phone}\n")

    print("Contact Added Successfully!")


def view_contacts():
    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()

            if not contacts:
                print("No Contacts Found!")
                return

            print("\n--- Contact List ---")
            for contact in contacts:
                name, phone = contact.strip().split(",")
                print(f"Name: {name} | Phone: {phone}")

    except FileNotFoundError:
        print("No Contacts Found!")


while True:
    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")