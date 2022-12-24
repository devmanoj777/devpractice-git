def generate_mat(n, m):
    # Top
    a=0
    for i in range(1,int(n),2):
        print("-"*((m-3)//2-a) + ".|." *i+ "-"*((m-3)//2-a))
        a+=3
    
    # Center
    print("-"*((m-7)//2) + "WELCOME" + "-"*((m-7)//2))
    
    # Bottom
    b=int(n)
    for i in range(int(n)-2,0,-2):
        print("-"*((m-3)//2+b-12) + ".|."*i + "-"*((m-3)//2+b-12))
        b +=3
        

n, m = map(int, input().split())
generate_mat(n, m)
