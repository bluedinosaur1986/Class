names=[]
phone_number=[]
emails=[]
num=0
cont="Y"
while cont!="N":
    name=input("Enter Name:")
    phone_num=input("Enter Phone Number:")
    names.append(name)
    phone_number.append(phone_num)
    email=input("Input Email:")
    emails.append(email)
    num=num+1
    cont=input("Continue? Y or N:")
print(f"\tNAME\t\t\tPHONE NUMBER\t\t\tEMAIL")
for i in range(num):
    print(f"\t{names[i]}\t\t\t{phone_number[i]}\t\t\t{emails[i]}")
s=input("Enter the Name to search:")
if s in names:
    index=names.index(s)
    names=names[index]
    phone_number=phone_number[index]
    print(f"Name: {names}, Phone: {phone_number}")
else:
    print("Name not found!")
