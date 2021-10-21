a=[54,3,2,12,43,24,57,54,32,50]
max=a[0]
min=a[0]
for i in range(0,len(a)):
   if(a[i]>max):
       max=a[i]
   elif (a[i]<min):
       min=a[i]
print('maximum element in array : ',max)
print('minimum element in array : ',min)
