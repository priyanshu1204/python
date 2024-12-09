"""
import tkinter as tk
import json
import re

phonebook ={}

def add_contact(name , phone):
    if not re.fullmatch(r'[A-Za-z0-9_]+', name ):
        return 'Invalid name'
    if not re.fullmatch(r'\d{10}', phone):
        return 'invalid phone number'
    phonebook[name] = phone
    with open ('phonebook.json', 'w') as f:
        json.dump(phonebook , f)

def view_contact():
    with open('phonebook.json', 'r')as f:
        phonebook1 = json.load(f)
    return phonebook1

root = tk.Tk()

add_contact_button = tk.Button(root , text ='Add Contact', command= lambda: add_contact(input("Name"), input("phone number")))
add_contact_button.pack()


view_contact_button = tk.Button(root , text= "View Contacts", command= view_contact())
view_contact_button.pack()

root.mainloop()
"""

import tkinter as tk
import json
import re
import os

# Ensure phonebook.json exists
if not os.path.exists('phonebook.json'):
    with open('phonebook.json', 'w') as f:
        json.dump({}, f)


# Add a contact to the phonebook
def add_contact(name, phone):
    if not re.fullmatch(r'[A-Za-z0-9_]+', name):
        status_label.config(text="Invalid name! Use letters, numbers, or underscores.")
        return
    if not re.fullmatch(r'\d{10}', phone):
        status_label.config(text="Invalid phone number! Use exactly 10 digits.")
        return

    # Load existing contacts
    with open('phonebook.json', 'r') as f1:
        phonebook = json.load(f1)

    # Add the new contact
    phonebook[name] = phone
    with open('phonebook.json', 'w') as f1:
        json.dump(phonebook, f1)

    status_label.config(text="Contact added successfully!")


# View all contacts
def view_contacts():
    try:
        with open('phonebook.json', 'r') as f2:
            phonebook = json.load(f2)

        # Display contacts
        contacts_display.delete(1.0, tk.END)  # Clear previous contents
        for name, phone in phonebook.items():
            contacts_display.insert(tk.END, f"{name}: {phone}\n")
    except json.JSONDecodeError:
        contacts_display.insert(tk.END, "Error loading contacts!")


# Create the main GUI
root = tk.Tk()
root.title("Phonebook")

# Input fields for adding contacts
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

phone_label = tk.Label(root, text="Phone Number:")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

# Add Contact button
add_contact_button = tk.Button(root, text="Add Contact",
                               command=lambda: add_contact(name_entry.get(), phone_entry.get()))
add_contact_button.pack()

# View Contacts button
view_contacts_button = tk.Button(root, text="View Contacts", command=view_contacts)
view_contacts_button.pack()

# Display area for contacts
contacts_display = tk.Text(root, height=10, width=50)
contacts_display.pack()

# Status label for messages
status_label = tk.Label(root, text="")
status_label.pack()

# Run the application
root.mainloop()
