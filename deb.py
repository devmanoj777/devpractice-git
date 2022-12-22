import collections
# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    u,v=map(int,input().split())
    not_rec=[u,v]
    n=int(input())
    rec=[]
    for j in range(n):
        l,r=map(int,input().split())
        rec=[l,r]
    for j in range(len(rec)):
        p=set(not_rec)
        q=set(rec[j])
        if p==q: 
            print("YES")
        else:
            print("NO")
        
     