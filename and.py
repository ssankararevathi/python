N=int(input())
a=0
mylist=list(map(int,input().split()))
if(N==len(mylist)):
    for i in mylist:
        a=i|a
print(a)
