# 📒 Contact Book (Python CLI App)

from validator_collection import validators, checkers, errors
from tabulate import tabulate


# File name where contacts will be stored
CONTACTS_FILE = "contacts.txt"

# In-memory contact list (works as app database during runtime)
contact_book = []


# Function to add a new contact with validation
def add_new_contact():
    while True:
        try:
            # --- Get Name (must not be empty & must be unique) ---
            while True:
                name = input("\n📝 Enter name of the new contact: ").strip()
                if not name:  # name must not be blank
                    print("⚠️ Name cannot be empty. Please try again.\n")
                    continue
                if any(contact["name"].lower() == name.lower() for contact in contact_book):
                    # Check if name exists already (case-insensitive)
                    print("⚠️ A contact with this name already exists. Please try again.\n")
                    continue
                break

            # Get Phone (must be exactly 10 digits & unique)
            while True:
                phone = input(f"📱 Enter phone number of {name}: ").strip()
                if not phone.isdigit() or len(phone) != 10:
                    print("⚠️ Phone number must be exactly 10 digits. Please try again.\n")
                    continue
                phone = int(phone)
                if any(contact["phone"] == phone for contact in contact_book):
                    # No duplicate phone allowed
                    print("⚠️ Phone number already exists. Please try again.\n")
                    continue
                break

            # Get Email (validate proper format & ensure it’s unique)
            while True:
                email = input(f"✉️ Enter email of {name}: ").strip()
                try:
                    # Validate email format
                    email = validators.email(email)
                    if not checkers.is_email(email):
                        print("⚠️ Invalid email format. Please try again.\n")
                        continue
                    if any(contact["email"].lower() == email.lower() for contact in contact_book):
                        print("⚠️ Email already exists. Please try again.\n")
                        continue
                    break
                except (errors.EmptyValueError, errors.InvalidEmailError):
                    print("⚠️ Invalid email. Please try again.\n")
                    continue

            # Add the validated contact to the in-memory list
            contact_book.append({"name": name, "phone": phone, "email": email})
            print("\n✅ Contact added successfully!\n")
            break

        except Exception as e:
            # Catch any other unexpected issue
            print(f"❌ An unexpected error occurred: {e}. Please try again.\n")


# Function to display all available contacts
def view_all_contacts():
    if not contact_book:
        print("\n📭 No contacts found.\n")
        return

    # Convert dictionary data into tabular format
    table_data = []
    for contact in contact_book:
        row = [contact["name"], contact["phone"], contact["email"]]
        table_data.append(row)

    headers = ['👤 Name', '📱 Phone', '✉️ Email']
    print("\n📒 ----- Contact Book -----\n")

    # Tabulate neatly with borders
    print(tabulate(table_data, headers=headers, tablefmt='grid', colalign=("left", "left", "left")))
    print("\n")


# Function to search a contact by name
def search():
    name = input("\n🔍 Enter name to search: ").strip().lower()
    found = []

    # Match entered name (case-insensitive search)
    for contact in contact_book:
        if name == contact["name"].lower():
            found.append([contact["name"], contact["phone"], contact["email"]])

    if found:
        print("\n✅ ----- Contact Found -----\n")
        headers = ['👤 Name', '📱 Phone', '✉️ Email']
        print(tabulate(found, headers=headers, tablefmt='grid', colalign=("left", "left", "left")))
        print("\n")
    else:
        print("❌ No matching contact found.\n")


# Function to delete a contact by name
def delete_a_contact():
    name = input("\n❌ Enter name to delete: ").strip().lower()

    for i, contact in enumerate(contact_book):
        if name == contact["name"].lower():
            del contact_book[i]  # Removes contact from list
            print("\n🗑️ Contact deleted successfully.\n")
            return
    print("❌ No matching contact found.\n")


# Function to save all contacts into file
def save_contacts():
    with open(CONTACTS_FILE, 'w') as f:
        for contact in contact_book:
            f.write(f"{contact['name']},{contact['phone']},{contact['email']}\n")
    print("💾 Contacts saved to file.\n")


# Function to load contacts from file when app starts
def load_contacts():
    try:
        with open(CONTACTS_FILE, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue  # Ignore empty lines
                parts = line.split(',')
                if len(parts) == 3:
                    name, phone, email = parts
                    contact_book.append({
                        "name": name,
                        "phone": int(phone),
                        "email": email
                    })
    except FileNotFoundError:
        # No saved contact file present
        print("\n📂 No contacts file found. Starting with empty contact book.\n")
    except Exception as e:
        print(f"\n⚠️ Error loading contacts: {e}. Starting with empty contact book.\n")


# Program starts here
if __name__ == "__main__":
    # Load contacts at the beginning
    load_contacts()

    # Continuous loop until user exits
    while True:
        try:
            # Display Menu Options
            user_choice = int(input(
                "📒 ----- Contact Book Menu -----\n"
                "1️⃣  Add New Contact\n"
                "2️⃣  View All Contacts\n"
                "3️⃣  Search by Name\n"
                "4️⃣  Delete a Contact\n"
                "5️⃣  Exit 🚪\n\n"
                "👉 Choose one: "
            ))
        except ValueError:
            # Ensure choice is a valid number
            print("\n⚠️ Please enter a number from 1 to 5.\n")
            continue

        # Perform operation based on user menu choice
        if user_choice == 1:
            add_new_contact()
            save_contacts()
        elif user_choice == 2:
            view_all_contacts()
        elif user_choice == 3:
            search()
        elif user_choice == 4:
            delete_a_contact()
            save_contacts()
        elif user_choice == 5:
            print("\n👋 Exiting the contact book. Goodbye!\n")
            break
        else:
            print("\n⚠️ Invalid choice. Please enter a number from 1 to 5.\n")
