#print the element of an array present in even  or odd position
a=[1,9,6,9,7,4,7,3,10]
print('given array :')
print(a)
print('element in even position :')
for i in range(1,len(a),2):
    print(a[i]) 
print('element in odd position :')
for i in range(0,len(a),2):
    print(a[i]) 
