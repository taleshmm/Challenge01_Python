def show_contacts_are_bookmark(datas):
    for index, ct in enumerate(datas, start=1):
        if ct["bookmark"]:
            print(f"""{index}. ★ {ct['name']}
Phone: {ct['phone']}
Email: {ct['email']}""")
        print(20*"-")
       
       