
#Taking the input 
a=int(input())
a=a-1 if a%2==0 else a
for i in range(a):
    print(2*i+1 ,end=" ")