k = 4 - 1
count = 0
for i in range(0,4):
    for j in range(0,k):
        print(end=' ')
    k -=1
    for j in range(0,i+1):
        print("*",end=" ")
        count +=1
    print()
l = 4 - 1
for i in range(0, 4):
    for j in range(0,i+1):
        print(end=" ")
    for j in range(0,l):
        print("*",end=' ')
    l = l - 1
    print()

