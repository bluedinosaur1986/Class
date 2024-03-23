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
#//Terminate