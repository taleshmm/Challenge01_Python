def delete_contact(datas):
    user_option = int(input("\nWhich contact do you want to delete? -> "))
    index = user_option - 1
    datas.pop(index)
    return datas
   
    