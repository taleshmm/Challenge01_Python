def edit_contact_by_id(datas):
    user_option = int(input("\nWhich contact do you want edit? -> "))
    index = user_option - 1
    ct_to_edit = datas[index]

    new_name = input(f"Old Name: {ct_to_edit["name"]} -- New Name: ")
    new_phone = input(f"Old Phone: {ct_to_edit["phone"]} -- New Phone: ")
    new_email = input(f"Old Email: {ct_to_edit["email"]} -- New Email: ")
    is_bookmark = "\nThis contact is bookmarked" if ct_to_edit["bookmark"]  else "This contact isn't bookmarked"
    change_bookmark = input(f"{is_bookmark}. Would you like to change? y/n -> ").lower()
    
    ct_to_edit["name"] = new_name if new_name != "" else ct_to_edit["name"]
    ct_to_edit["phone"] = new_phone if new_phone != "" else ct_to_edit["phone"]
    ct_to_edit["email"] = new_email if new_email != "" else ct_to_edit["email"]
    
    if change_bookmark == "y":
        ct_to_edit["bookmark"] = not ct_to_edit["bookmark"]
    
    datas[index] = ct_to_edit
       
        
    return datas