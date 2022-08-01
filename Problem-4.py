
# Taking input as list
a=list(map(int,input().split()))
# Initializing the values as zero
d={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
for i in range(len(a)):
    if a[i]%2==0:
        d[2]=d.get(2,0)+1
    if a[i]%3==0:
        d[3]=d.get(3,0)+1
    if a[i]%4==0:
        d[4]=d.get(4,0)+1
    if a[i]%5==0:
        d[5]=d.get(5,0)+1
    if a[i]%6==0:
        d[6]=d.get(6,0)+1
    if a[i]%7==0:
        d[7]=d.get(7,0)+1
    if a[i]%8==0:
        d[8]=d.get(8,0)+1
    if a[i]%9==0:
        d[9]=d.get(9,0)+1
# As all are multiples of 1
d[1]=len(a)
print(d)