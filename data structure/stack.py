# def stack2():
#     stack = []
#     print('(1)  push element in a stack : ')
#     print('(2)  pop element in a stack : ')
#     print('(3)  show element in a stack : ')
#     print('(4)  last element in a stack : ')
#     print('(5)  first element in a stack : ')
#     a = int(input('enter your choice : '))
#     if a == 1:
#         stack1 = int(input('enter element : '))
#         stack.append(stack1)
#     elif a == 2:
#         if not stack:
#             print('stack is empty ..')
#         else:
#             stack.pop()
#     elif a == 3:
#         if not stack:
#             print('stack is empty ..')
#         else:
#             print(stack)
#     elif a == 4:
#         if not stack:
#             print('stack is empty ..')
#         else:
#             print(stack[-1])
#     elif a == 5:
#         if not stack:
#             print('stack is empty ..')
#         else:
#             print(stack[0])
#     else:
#         print('enter valid choice ...')
# stack2()
# while (True):
#     b = input("if continue y/n :")
#     if b == 'y':
#         stack2()
#     else:
#         exit()
stack = []
def push():
    element = input('enter the element :  ')
    stack.append(element)
    print(stack)
def pop():
    if not stack:
        print('stack is empty ...')
    else:
        e = stack.pop()
        print('remove element : ', e)
        print(stack)
while True:
    print('select the option is \n 1) push \n 2) pop \n 3) exit ')
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        break
    else:
        print('enter valid choice ......')




