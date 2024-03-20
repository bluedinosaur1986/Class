def sequential_search(array, target):
    for i in range(len(array)):
        if array[i]==target:
            return i
    return -1
z=1
array=[]
while z<=100:
    array.append(z)
    z=z+1

target=int(input("What number is the target of the search?"))
index=sequential_search(array,target)
if index != -1:
    print("The target value was found at index", index)
else:
    print("The target value was not found in the array")
