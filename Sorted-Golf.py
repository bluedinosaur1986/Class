#Patrick Paul 3/23/24
#1. Sorted Golf Scores
#//Declare and initialize
scoreArray=[]
i=int(0)
score=int(0)
index=int(1)
scan=int(1)
unsorted=int(0)
#//Get user input
while i<=9:
    score=int(input("Input a golf score (integer):"))
    scoreArray.append(score)
    i=i+1
#//Sort scores
while index<len(scoreArray):
    unsorted=int(scoreArray[index])
    scan=index
    while scan>0 and scoreArray[scan-1]>unsorted:
        scoreArray[scan]=scoreArray[scan-1]
        scan=scan-1
    scoreArray[scan]=unsorted
    index=index+1
#//Output
i=int(0)
while i<=9:
    print(scoreArray[i])
    i=i+1
#//Terminate

