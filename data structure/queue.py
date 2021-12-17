queue = []
def push():
    element = input('enter the element :  ')
    queue.append(element)
    print(queue)
def pop():
    if not queue:
        print('queue is empty ...')
    else:
        e = queue.pop(0)
        print('remove element : ', e)
        print(queue)
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

