#program to find the frequency of each element in the array 
arr1=[1,2,3,5,2,3,2,1,2,1,6,7,7]
arr2=[None]*len(arr1)
visit=-1            #check same value
for i in range(0,len(arr1)):
    count=1
    for j in range(i+1,len(arr1)):
        if(arr1[i]==arr1[j]):
            count+=1
            arr2[j]=visit
    if(arr2[i]!=visit):
        arr2[i]=count          #count frequency
print('------------------------------')        
print('element | frequency')
print('------------------------------')
for i in range(0,len(arr2)):
    if(arr2[i]!=visit):
        print("  "+str(arr1[i])+"     |    "+str(arr2[i]))


