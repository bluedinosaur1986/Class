password=input("create a password? ")
def view():
    with open('passwords.txt','r') as f:
        for i in f:
                print(i)
def add():
    name=input('Account Name:')
    pwd=input('Password: ')
    #with allows our code to auto close
    with open('passwords.txt','a') as f:
        f.write(name+"|"+pwd+"\n")

while True:
    mode=input("Would you like to add a new password or view existing ones (view, add), press q to quit ").lower()
    if mode=='q':
        break
    elif mode=='view':
        view()
    elif mode=='add':
        add()
    else:
        print("Invalid mode.")
        continue