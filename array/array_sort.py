a=[32,7,98,4,1,54,6]
max=0
min=0
print('given array : ',a)
print('array elements sorting in ascending order : ')
print('--------------------------------------------')
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if(a[i]>a[j]):
            max=a[i]
            a[i]=a[j]
            a[j]=max
for i in range(0,len(a)):
    print(a[i],end=' | ')
print('\n\narray elements sorting in descending order : ')
print('-------------------------------------------------')
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if(a[i]<a[j]):
            min=a[i]
            a[i]=a[j]
            a[j]=min
for i in range(0,len(a)):
    print(a[i],end=' | ')         

