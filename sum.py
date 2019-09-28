n=int(input())
s=0
ld=n%10
while n>=10:
    n//=10
fd=n
sum=fd+ld
print(sum)
