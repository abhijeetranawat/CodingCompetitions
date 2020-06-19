lst1=[]
lst2=[]
lst3=[]

def prime(pnum):
    flag=True
    for g in range(2,pnum//2+1):
        if(pnum%g==0):
            flag=False
            break
    return flag
def fib(totnum):
    for s in range(2,totnum):
        lst3.append(lst3[s-1]+lst3[s-2])
    print(lst3[-1],end="")

def main():
    n,m=map(int,input().split())

    for num in range(n,m+1):
       if num > 1:
           for i in range(2,num):
               if (num % i) == 0:
                   break
           else:
               lst1.append(num)
    for i in range(len(lst1)):
        for j in range(len(lst1)):
            if(j==i):
                continue
            else:
                if(lst1[j]<=9):
                    number=lst1[i]*10+lst1[j]
                else:
                    number = lst1[i] * 100 + lst1[j]
                if(prime(number)):
                    lst2.append(number)
    totnum=len(set(lst2))
    lst3.append(min(lst2))
    lst3.append(max(lst2))
    fib(totnum)
if __name__=="__main__":
    main()