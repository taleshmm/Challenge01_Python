def change_bookmar_contact(datas):
    user_option = int(input("\nWhich contact do you want to mark/unmark? -> "))
    index = user_option - 1
    ct_to_edit = datas[index]
    
    ct_to_edit["bookmark"] = not ct_to_edit["bookmark"]
    
    datas[index] = ct_to_edit
    
    return datas
        
    