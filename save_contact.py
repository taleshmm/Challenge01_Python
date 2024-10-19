def save_new_contact():
    name = input("Name -> ").capitalize()
    phone = input("Phone number -> ")
    email = input("Email Address -> ").lower()
    bookmark = input("Would you like add as Bookmarck? y/n -> ").lower()
    
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "bookmark": True if bookmark == "y" else False         
               }
    
    return contact