def view_contacts(datas):
    for index, ct in enumerate(datas, start=1):
        is_bookmark = "★" if ct["bookmark"] else ""
        print(f"""{index}. {is_bookmark} {ct['name']}
Phone: {ct['phone']}
Email: {ct['email']}""")
        print(20*"-")
        