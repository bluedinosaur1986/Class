while True:
    q=input("Add(a) or Search(s) or Quit(q)")
    if q=='a':
        with open('contact.txt','a') as f:
            name=input("Name:")
            phone=input("Phone:")
            email=input("Email:")
            f.writelines(('Name: ',name, '\n', 'Phone: ',phone, '\n', 'Email: ',email,'\n\n'))
    elif q=='s':
        with open('contact.txt','r') as f:
            search=input("Search:")
            for i in f:
                if search in i:
                    print(i)
    else:
        break