# Contact Management System
# Week 3 Project - Functions & Dictionaries
# Name: Your Name

import json
import re
import csv
from datetime import datetime

DATA_FILE = "contacts_data.json"

# ---------------- VALIDATION FUNCTIONS ----------------

def validate_phone(phone):
    digits = re.sub(r"\D", "", phone)
    if 10 <= len(digits) <= 15:
        return True, digits
    return False, None

def validate_email(email):
    if email == "":
        return True
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# ---------------- FILE HANDLING ----------------

def load_contacts():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("✅ No existing contacts file found. Starting fresh.")
        return {}

def save_contacts(contacts):
    with open(DATA_FILE, "w") as file:
        json.dump(contacts, file, indent=4)
    print("✅ Contacts saved successfully.")

# ---------------- CRUD OPERATIONS ----------------

def add_contact(contacts):
    print("\n--- ADD NEW CONTACT ---")
    name = input("Enter contact name: ").strip()

    if not name:
        print("Name cannot be empty!")
        return

    if name in contacts:
        print("Contact already exists!")
        return

    while True:
        phone = input("Enter phone number: ")
        valid, cleaned = validate_phone(phone)
        if valid:
            break
        print("Invalid phone number!")

    while True:
        email = input("Enter email (optional): ").strip()
        if validate_email(email):
            break
        print("Invalid email format!")

    address = input("Enter address (optional): ").strip()
    group = input("Enter group (Friends/Work/Family/Other): ").strip() or "Other"

    contacts[name] = {
        "phone": cleaned,
        "email": email,
        "address": address,
        "group": group,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }

    print(f"✅ Contact '{name}' added successfully!")
    save_contacts(contacts)

def search_contact(contacts):
    term = input("Enter name to search: ").lower()
    found = False

    for name, info in contacts.items():
        if term in name.lower():
            found = True
            print("\n------------------------")
            print(f"Name   : {name}")
            print(f"Phone  : {info['phone']}")
            print(f"Email  : {info['email']}")
            print(f"Group  : {info['group']}")

    if not found:
        print("No contact found.")

def update_contact(contacts):
    name = input("Enter contact name to update: ").strip()

    if name not in contacts:
        print("Contact not found!")
        return

    print("Leave field empty to keep old value.")

    phone = input("New phone number: ")
    if phone:
        valid, cleaned = validate_phone(phone)
        if valid:
            contacts[name]["phone"] = cleaned

    email = input("New email: ")
    if email and validate_email(email):
        contacts[name]["email"] = email

    address = input("New address: ")
    if address:
        contacts[name]["address"] = address

    group = input("New group: ")
    if group:
        contacts[name]["group"] = group

    contacts[name]["updated_at"] = datetime.now().isoformat()
    print("✅ Contact updated successfully!")
    save_contacts(contacts)

def delete_contact(contacts):
    name = input("Enter contact name to delete: ").strip()

    if name not in contacts:
        print("Contact not found!")
        return

    confirm = input("Are you sure? (y/n): ").lower()
    if confirm == "y":
        del contacts[name]
        print("✅ Contact deleted.")
        save_contacts(contacts)

def display_all_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return

    print("\n--- ALL CONTACTS ---")
    for name, info in contacts.items():
        print("\n------------------------")
        print(f"Name  : {name}")
        print(f"Phone : {info['phone']}")
        print(f"Email : {info['email']}")
        print(f"Group : {info['group']}")

# ---------------- EXTRA FEATURES ----------------

def export_to_csv(contacts):
    with open("contacts_export.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone", "Email", "Address", "Group"])

        for name, info in contacts.items():
            writer.writerow([
                name,
                info["phone"],
                info["email"],
                info["address"],
                info["group"]
            ])

    print("✅ Contacts exported to contacts_export.csv")

def show_statistics(contacts):
    print("\n--- CONTACT STATISTICS ---")
    print(f"Total Contacts: {len(contacts)}")

    groups = {}
    for info in contacts.values():
        grp = info["group"]
        groups[grp] = groups.get(grp, 0) + 1

    for grp, count in groups.items():
        print(f"{grp}: {count}")

# ---------------- MENU SYSTEM ----------------

def main_menu():
    print("\n" + "=" * 50)
    print("      CONTACT MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add New Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. View All Contacts")
    print("6. Export to CSV")
    print("7. View Statistics")
    print("8. Exit")

# ---------------- MAIN FUNCTION ----------------

def main():
    contacts = load_contacts()

    while True:
        main_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            display_all_contacts(contacts)
        elif choice == "6":
            export_to_csv(contacts)
        elif choice == "7":
            show_statistics(contacts)
        elif choice == "8":
            save_contacts(contacts)
            print("\nThank you for using Contact Management System!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
