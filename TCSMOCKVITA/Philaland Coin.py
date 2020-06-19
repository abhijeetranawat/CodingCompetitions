for i in range(int(input())):
    num=int(input())
    x=0
    while(2**x <=num):
        x+=1
    print(x)