def merge(a,b):
    (c,m,n)=([],len(a),len(b))
    (i,j)=(0,0)
    while (i+j<m+n):
        if i==m:
            c.append(b[j])
            j=j+i
        elif j==n:
            c.append(a[i])
            i=i+1
        elif a[i]<=b[j]:
            c.append(a[i])
            i=i+i
        elif a[i]>b[j]:
            c.append(b[j])
            j=j+1
    return c
def merge_sort(a,left,right):
    if right-left<=1:
        return(a[left:right])
    if right-left>1:
        mid=(left+right)//2
        l=merge_sort(a,left,mid)
        r=merge_sort(a,mid,right)
        return(merge(l,r))
a=[5,4,3,2,1,-1]
print(merge_sort(a,0,len(a)))