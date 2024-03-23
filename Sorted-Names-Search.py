#Patrick Paul 3/23/24
#2. Sorted Names
#//Declare and initialize
nameArray=[]
i=int(0)
name=""
index=int(1)
scan=int(1)
unsorted=""
#//Get user input
while i<=19:
    name=input("Input a name (text):")
    nameArray.append(name)
    i=i+1
#//Sort names
while index<len(nameArray):
    unsorted=nameArray[index]
    scan=index
    while scan>0 and nameArray[scan-1]>unsorted:
        nameArray[scan]=nameArray[scan-1]
        scan=scan-1
    nameArray[scan]=unsorted
    index=index+1
#//Output
i=int(0)
while i<=19:
    print(nameArray[i])
    i=i+1
#//Search the array
name=input("Input a name to find (text):")
#//Declare and initialize
first=int(0)
last=len(nameArray)-1
pos=int(-1)
flag=False
middle=int(0)
while flag==False and first<=last:
    middle=int((first+last)/2)
    if nameArray[middle]==name:
        flag=True
        pos=middle
    elif nameArray[middle]>name:
        last=middle-1
    else:
        first=middle+1
if pos==-1:
    print("Name not found!")
else:
    print(nameArray[pos],"found at postion:",pos,"!")
#//Terminate