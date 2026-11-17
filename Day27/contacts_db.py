import sqlite3

# Connect to database
conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT,
    email TEXT
)
""")

conn.commit()


# 1. Add Contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    cursor.execute(
        "INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)",
        (name, phone, email)
    )

    conn.commit()
    print("Contact added successfully!")


# 2. View Contacts
def view_contacts():
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()

    if contacts:
        for contact in contacts:
            print(contact)
    else:
        print("No contacts found!")


# 3. Search Contact
def search_contact():
    name = input("Enter name to search: ")

    cursor.execute(
        "SELECT * FROM contacts WHERE name LIKE ?",
        ('%' + name + '%',)
    )

    contacts = cursor.fetchall()

    if contacts:
        for contact in contacts:
            print(contact)
    else:
        print("Contact not found!")


# 4. Update Contact
def update_contact():
    contact_id = input("Enter contact ID: ")

    cursor.execute(
        "SELECT * FROM contacts WHERE id = ?",
        (contact_id,)
    )

    contact = cursor.fetchone()

    if contact:
        name = input("Enter new name: ")
        phone = input("Enter new phone: ")
        email = input("Enter new email: ")

        cursor.execute(
            "UPDATE contacts SET name = ?, phone = ?, email = ? WHERE id = ?",
            (name, phone, email, contact_id)
        )

        conn.commit()
        print("Contact updated successfully!")
    else:
        print("Contact not found!")


# 5. Delete Contact
def delete_contact():
    contact_id = input("Enter contact ID: ")

    cursor.execute(
        "DELETE FROM contacts WHERE id = ?",
        (contact_id,)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")


# Main Menu
while True:
    print("\n===== CONTACTS APP =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")

conn.close()