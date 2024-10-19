from change_bookmark import change_bookmar_contact
from delete_contact import delete_contact
from edit_contact import edit_contact_by_id
from save_contact import save_new_contact
from view_bookmarks import show_contacts_are_bookmark
from view_contact import view_contacts

contacts = []

while True:
    print("Welcome to your contacts, what would you like to do?")
    print("1 - Save a new Contact")
    print("2 - Show contacts")
    print("3 - Edit a Contact")
    print("4 - Show bookmark contacts")
    print("5 - Mark/UnMark a Favorite Contact")
    print("6- Delete a Contact")
    print("0 - Exit")
    
    try:
        choice_user = int(input("\nEnter your option: "))
      
        if choice_user == 1:
            creating_contact = save_new_contact()
            contacts.append(creating_contact)
            print("\nContact save successful")
        elif choice_user == 2:
            view_contacts(contacts)
        elif choice_user == 3:
            new_list_contact = edit_contact_by_id(contacts)
            contacts = new_list_contact
            print("\nContact edited with success")
        elif choice_user == 4:
            show_contacts_are_bookmark(contacts)
        elif choice_user == 5: 
            new_bookmark_contact = change_bookmar_contact(contacts)
            contacts = new_bookmark_contact
        elif choice_user == 6:
            contacts = delete_contact(contacts)
        elif choice_user == 0:
            break
    except ValueError as e:
        print("Please, enter a valid number")
    except Exception as e:
        print(f"An error occurred, check your choice: {e}")

    