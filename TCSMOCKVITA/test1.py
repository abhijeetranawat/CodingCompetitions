lst=[31,28,31,30,31,30,31,31,30,31,30,31]
for i in range(1,13):
    num=(6-i)**2
    for j in range(1,lst[i-1]+1):
        num1=abs(j-15)
        print(j,i,(num+num1))