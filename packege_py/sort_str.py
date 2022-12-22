n = input()
new=""
cap=""
odd=""
even=''
for i in n:
    if i.islower():
         new += "".join(sorted(i))
    elif i.isupper() :
        cap += "".join(sorted(i))
    elif int(i)%2 == 0:
        even +=  i
    else:
        odd += i
       
print(new+cap+odd+even)
        