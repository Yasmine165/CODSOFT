# Contact Management System

# Global dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact():
    print("\n======= Add New Contact =======")
    name = input("Enter the name: ").strip()
    if name in contacts:
        print(f"Contact '{name}' already exists.")
        return
    
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    address = input("Enter address: ").strip()
    
    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    
    print(f"Contact '{name}' added successfully.")

# Function to view all contacts
def view_contacts():
    print("\n======= Contact List =======")
    if not contacts:
        print("No contacts found.")
    else:
        for name, info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
            print("------------------------")

# Function to search for a contact by name or phone number
def search_contact():
    print("\n======= Search Contact =======")
    query = input("Enter a name or phone number to search: ").strip().lower()
    
    found = False
    for name, info in contacts.items():
        if query in name.lower() or query == info['phone']:
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
            print("------------------------")
            found = True
    
    if not found:
        print("No matching contacts found.")

# Function to update a contact
def update_contact():
    print("\n======= Update Contact =======")
    name = input("Enter name of the contact to update: ").strip()
    
    if name in contacts:
        print(f"Updating contact '{name}'. Enter new details:")
        phone = input(f"Enter the new phone number ({contacts[name]['phone']}): ").strip()
        email = input(f"Enter a new email address ({contacts[name]['email']}): ").strip()
        address = input(f"Enter new address ({contacts[name]['address']}): ").strip()
        
        # Update contact details
        contacts[name]['phone'] = phone if phone else contacts[name]['phone']
        contacts[name]['email'] = email if email else contacts[name]['email']
        contacts[name]['address'] = address if address else contacts[name]['address']
        
        print(f"Contact '{name}' updated successfully.")
    else:
        print(f"Contact '{name}' not found.")

# Function to delete a contact
def delete_contact():
    print("\n======= Delete Contact =======")
    name = input("Enter name of the contact to delete: ").strip()
    
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

# Function to display the main menu
def display_menu():
    print("\n======= Contact Management System =======")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    print("==========================================")

# Main function to run the contact management system
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

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
            print("Thank you for using the Contact Management System. Goodbye!")
            break
        else:
            print("Your choice is Invalid. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
