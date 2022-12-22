# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(1,10,2):
    print((i*'H').center(9,' '))
for i in range(1,7):
    print("  HHHHH".ljust(9," "),"HHHHH".rjust(17," "))
for i in range(1,4):
    print(" ",25*"H")
for i in range(1,7):
    print("  HHHHH".ljust(9," "),"HHHHH".rjust(17," "))
for i in range(9,0,-2):
    print(19*" ",(i*'H').center(9,' '))