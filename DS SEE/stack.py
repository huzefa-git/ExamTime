def create():
    stack = []
    return
def isEmpty(stack):
    return len(stack)==0
def push(stack,item):
    if(len(stack)==size):
        print("Stack overflow")
    else:
        stack.append(item)
def pop(stack):
    if(isEmpty(stack)):
        print("Stack underflow")
    else:
        stack.pop()
def peek(stack):
    if(isEmpty(stack)):
        print("Stack is empty")
    else:
        n = len(stack)
        print("peek element is:",stack[n-1])
def display(stack):
    print(stack)

stack = create()
size = int(input("Enter the size of the stack"))
print("Menu\n 1.push(p)\n 2.pop(o)\n 3.peek(e)")
choice =1
while choice!='q':
    print("Enter your choice")
    ch = input()
    choice = ch.lower()
    if(choice == 'p'):
        push(stack,int(input("Enter a value:")))
        display(stack)
    elif(choice == 'o'):
        pop(stack)
        display(stack)
    elif(choice == 'e'):
        peek(stack)
    else:
        print("Enter proper choice or q for quit")