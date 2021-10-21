#print the duplicate elements of the array
arr1=[1,2,3,4,2,3,4,5,6,7,9]
for i in range(0,len(arr1)):
    for j in range(i+1,len(arr1)):
        if(arr1[i]==arr1[j]):
            print(arr1[j])
