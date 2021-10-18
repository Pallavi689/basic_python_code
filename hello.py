# write a program to find sum of first 5 even  numbers
# i=1
# sum=0
# n=int(input('enter a value of n:'))
# while(i<=n):
#      if(i%2!=0):
#           print(i)
#           sum=sum+i
#      i=i+1
# print('sum of 5 even number : ',sum)



# wap to find sum of digits of a given number like 123=1+2+3=6
# i=int(input('enter a number :'))
# n=0
# while(i>0):
#     n=n+i%10
#     i=i//10            #to remove(.) use //
# print(n)



#123=1^2+2^2+3^2=14
# i=int(input('enter a number :'))
# n=0
# while(i>0):
#     n=n+(i%10)**2
#     i=i//10
# print(n)



# wap to find the area of triangle
# h=int(input('enter height :'))
# b=int(input('enter base :'))
# a=h*b/2
# print('area of triangle : ',a)



#wap to find x
# import math
#
# print('aX^2 + bY +c = 0')
# a=int(input('enter a value of a :'))
# b=int(input('enter a value of b :'))
# c=int(input('enter a value of c :'))
# print('{}X^2 + {}Y + {} = 0'.format(a,b,c))
# d=(b**2)-(4*a*c)
# s1=(-b-math.sqrt(d))/(2*a)
# s2=(-b+math.sqrt(d))/(2*a)
# print('solution is x1= {} and x2 = {}'.format(s1,s2))



#swap two numbers
# a=int(input('enter a value of a :'))
# b=int(input('enter a value of b :'))
#     #a,b=b,a
# a=a+b
# b=a-b
# a=a-b
# print('a = ',a)
# print('b = ',b)


#a random value
# import random
#
# a=random.Random()
# print(a)



#program to convert kilometers to miles
# k=float(input('enter a value(kilometer) to convert miles : '))
# m1=float(input('enter a value(miles) to convert kilometer : '))
# m=k*0.62137
# k1=m1/0.62137
# print('{} kilometer is = {} miles'.format(k,m))
# print('{} miles is = {} kilometer'.format(m1,k1))


#program to convert
# c=float(input('enter a value in celsius :'))
# f=(c*9/5)+32
# print('{} celsius is = {} fahrenheit..'.format(c,f))
# c1=float(input('enter a value in fahrenheit :'))
# f1=(c1-32)*5/9
# print('{} fahrenheit is = {} celsius..'.format(c1,f1))


#display calendar
# import calendar
# yy=int(input('enter year :'))
# mm=int(input('enter month in numbers :'))
# print((calendar.month(yy,mm)))


#check no is +ve -ve or 0
# n=int(input('enter a number :'))
# if(n==0):
#     print('number is ',n)
# elif(n>0):
#     print('+ve :',n)
# else:
#     print('-ve : ',n)


# check number odd or even
# n=int(input('enter a number :'))
# if(n%2==0):
#     print('even number : ',n)
# else:
#     print('odd number : ',n)


#program to check leap year
#n=int(input('enter a year :'))
# if(n%4==0):
#     if(n%100==0):                  #not divide by 100
#         if(n%400==0):
#             print('{} year is leap year '.format(n))
#         else:
#             print('{} year is not leap year '.format(n))
#     else:
#         print('{} year is leap year '.format(n))
# else:
#     print('{} year is not leap year '.format(n))
# if((n%400==0) or (n%100!=0) and (n%4==0)):
#     print('leap year')
# else:
#     print('not leap year')



# check prime number or not
# n=int(input('enter to check number :'))
# if(n>0):
#     for i in range (2,n):
#         if(n%i==0):
#             m=1
#             break
#         else:
#             m=0
#     if(m==1):
#         print('{} is not prime number '.format(n))
#     else:
#         print('{} is prime number '.format(n))


#find factorial  number
# n=int(input('enter a number : '))
# sum=0
# num=0
# for i in range(1,n):
#     sum=(n*i)
#     num=num+sum
# print(num)



#display multiplication table
# n=int(input('enter a number :'))
# sum=0
# #j=1
# #for j in range(1,n+1):
#     for i in range(1,11):
#         sum=j*i
#         print('{} * {} = {}'.format(j,i,sum))


#fibonacci sequence
# n=int(input('enter a number :'))
# n1=0
# n2=1
# count=0
# if(n<=0):
#     print('inter positive int  ')
# elif (n==1):
#     print('up to ',n)
# else:
#     while(count<n):
#         print(n1)
#         n3=n1+n2
#         n1=n2
#         n2=n3
#         count+=1


#check armstrong number or not   153 =1^3+5^3+3^3=153 same
# n=int(input('enter a number :'))
# m=n
# sum=0
# while(m>0):
#     d=m%10
#     sum+=d**3
#     m=m//10
# print(sum)
# if(sum==n):
#     print('given number {} is armstrong number'.format(n))
# else:
#     print('given number {} is not armstrong number '.format(n))




#sum of all natural numbers
# n=int(input('enter a number :'))
# sum=0
# if(n<0):
#     print('print positive number')
# elif(n==0):
#     print('{} is not natural number '.format(n))
# else:
#     while(n>0):
#         sum+=n
#         n-=1
#     print(sum)



#find lcm given number(2)
#basic concept LCM lowest common multiplier example 4 and 6
#4 = 4,8,12,16,20..
#12= 12,24,36,48,...
#common 12,24,36...
#lowest c m =12 ans
# import math
#
# a= math.lcm(4,3)
# b= math.gcd(80,100)
#print(b)


#convert decimal to binary octal and hexadecimal
# def decimal1(a):
#     dec1=bin(a)
#     print('{} in binary {}'.format(a,dec1))
# def decimal2(b):
#     dec2=oct(b)
#     print('{} in octal {}'.format(b, dec2))
# def decimal3(c):
#     dec3=hex(c)
#     print('{} in hexadecimal {}'.format(c,dec3))
# a1=int(input('enter a value to convert decimal to binary octal and hexadecimal :'))
# decimal1(a1)
# decimal2(a1)
# decimal3(a1)

#ascii value find
# val=input('enter a char: ')
# print('ascii value of '+val+' is = ',ord(val))

# print('enter a string : ')
# string = input()
#             #s_l = len(string)        # new string= place od rangr
#             #i = 0
# for i in string:
#     ascii = ord(i)
#     print(i , "\t" , ascii)
#


#to make a simple calculator
# def getvalue(x,y,op):
#     if(op=='+'):
#         add=x+y
#         print(' {} {} {} = {}'.format(x,op,y,add))
#     elif(op=='-'):
#         sub=x-y
#         print(' {} {} {} = {}'.format(x,op,y,sub))
#     elif (op == '*'):
#         mul = x * y
#         print(' {} {} {} = {}'.format(x, op, y, mul))
#     elif (op == '/'):
#         div = x / y
#         print(' {} {} {} = {}'.format(x, op, y, div))
#     elif (op == '%'):
#         mod = x - y
#         print(' {} {} {} = {}'.format(x, op, y, mod))
#     else:
#         print('enter valid operator (+ - * / %)')
# x1=float(input('enter a first number : '))
# y1=float(input('enter a second value : '))
# op1=(input('enter operator : '))
# getvalue(x1,y1,op1)
















