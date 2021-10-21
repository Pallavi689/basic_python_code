#print the element of an array in reverse
arr1=[2,3,4,5,6,7]
print('before reverse : ')
for i in range(0,len(arr1)):
   print('a[{}] = {}'.format(i,arr1[i]))
print('\n\nafter reverse : ')
for i in range(len(arr1)-1,-1,-1):
   print('a[{}] = {}'.format(i,arr1[i]))
