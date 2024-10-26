class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        address = input("Enter address: ")
        
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print(f"Contact {name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("Contact List:")
            for contact in self.contacts:
                print(contact)

    def search_contact(self):
        search_term = input("Enter name or phone number to search: ").lower()
        results = [contact for contact in self.contacts if search_term in contact.name.lower() or search_term in contact.phone]
        
        if results:
            print("Search Results:")
            for contact in results:
                print(contact)
        else:
            print("No matching contacts found.")

    def update_contact(self):
        search_term = input("Enter the name of the contact to update: ").lower()
        for contact in self.contacts:
            if search_term == contact.name.lower():
                print(f"Found contact: {contact}")
                contact.name = input("Enter new name (leave blank to keep current): ") or contact.name
                contact.phone = input("Enter new phone (leave blank to keep current): ") or contact.phone
                contact.email = input("Enter new email (leave blank to keep current): ") or contact.email
                contact.address = input("Enter new address (leave blank to keep current): ") or contact.address
                print(f"Contact {contact.name} updated successfully!")
                return
        print("Contact not found.")

    def delete_contact(self):
        search_term = input("Enter the name of the contact to delete: ").lower()
        for contact in self.contacts:
            if search_term == contact.name.lower():
                self.contacts.remove(contact)
                print(f"Contact {contact.name} deleted successfully!")
                return
        print("Contact not found.")

    def menu(self):
        while True:
            print("\n--- Contact Manager ---")
            print("1. Add Contact")
            print("2. View Contact List")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")
            choice = input("Choose an option (1-6): ")

            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.update_contact()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                print("Exiting the Contact Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manager = ContactManager()
    manager.menu()
