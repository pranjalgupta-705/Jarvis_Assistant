n,m=map(int,input().split())
a=0
b=0
c=0
p=int('1'*len(bin(n).replace('0b','')),2)+1
q=int('1'*(len(bin(m).replace('0b',''))-1),2)+1
if((p>=n and p<m) and (q>n and q<=m)):
    for i in range(n,p):
        k=bin(i).replace('0b','')
        if(k.count('0')==1):
            c+=1
    for j in range(q+1,m+1):
        k=bin(j).replace('0b','')
        if(k.count('0')==1):
            c+=1
    #c+=sum(list(range(d[p]-1,d[p]+(d[q]-d[p]))))
    print(d[p]-1,d[p]+(d[q]-d[p]),bin(2))
else:
    print(0)