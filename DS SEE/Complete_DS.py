                                #Searching
        #Linear Search

'''
def linear_search(arr,target):
    for i in range(len(arr)):
        if (arr[i] == target):
            return i
    return -1

arr = [12 , 54 , 87 ,90 , 64 , 21 ]
target = int(input("Enter the number you want to search : "))
res = linear_search(arr , target)
if(res == -1):
    print(f"The target element : {target} is not found in the given list .")
else:
    print(f"The target element {target} is found at the index {res}")
'''


        #Binary Search 

'''
def binary_search(arr,target):
    left , right = 0 , len(arr)-1
    while(left<=right):
        mid = (left+right)//2
        if(arr[mid] == target):
            return mid
        elif (arr[mid] > target):
            right = mid - 1
        else:
            left = mid + 1
    return -1

arr = [12 , 54 , 87 ,90 , 64 , 21 ]
arr.sort()
print(arr)
target = int(input("Enter the number you want to search : "))
res = binary_search(arr , target)
if(res == -1):
    print(f"The target element : {target} is not found in the given list .")
else:
    print(f"The target element {target} is found at the index {res}")


'''

'''
def binary_search(arr,target,left,right):
    if(right >= left):
        mid = (left+right)//2
        if(arr[mid] == target):
            return mid
        elif (arr[mid] > target):
            return binary_search(arr,target,left,mid-1)
        elif (arr[mid] < target):
            return binary_search(arr,target,mid+1,right)
    return -1

arr = [12 , 54 , 87 ,90 , 64 , 21 ]
arr.sort()
print(arr)
target = int(input("Enter the number you want to search : "))
res = binary_search(arr , target , 0 , len(arr)-1)
if(res == -1):
    print(f"The target element : {target} is not found in the given list .")
else:
    print(f"The target element {target} is found at the index {res}")
'''



                                #Sorting

        #Bubble Sort

'''
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]

arr = [12 , 54 , 87 ,90 , 64 , 21 ]
print("Original array : " , *arr)
bubble_sort(arr)
print("Sorted array : " , *arr)
'''

        #Selection Sort

'''
def selection_sort(arr):
    for i in range(len(arr)):
        min_ind = i
        for j in range(i,len(arr)):
            if (arr[min_ind]>arr[j]):
                min_ind = j
        arr[min_ind] , arr[i] = arr[i] , arr[min_ind]

arr = [12 , 54 , 87 ,90 , 64 , 21 ]
print("Original array : " , *arr)
selection_sort(arr)
print("Sorted array : " , *arr)
'''


        #Insertion Sort

'''
def insertion_sort(arr):
    for i in range(len(arr)):
        k= arr[i]
        j= i-1
        while(j>=0 and arr[j]>k):
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] =k

arr = [12 , 54 , 87 ,90 , 64 , 21 ]
print("Original array : " , *arr)
insertion_sort(arr)
print("Sorted array : " , *arr)
'''



        #Quick Sort


'''
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x<pivot]
    middle = [x for x in arr if x==pivot]
    right = [x for x in arr if x>pivot]
    return quick_sort(left) + middle + quick_sort(right)


arr = [12 , 54 , 87 ,90 , 64 , 21 ]
print("Original array : " , *arr)
new_list = quick_sort(arr)
print("Sorted array : " , *new_list)
'''




                    #Merge Sort

'''
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    left_half = merge_sort(left_half)  
    right_half = merge_sort(right_half)  

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result

arr = [12 , 54 , 87 ,90 , 64 , 21 ]
print("Original array : " , *arr)
sorted_list = merge_sort(arr)  
print("Sorted array : ", *sorted_list)
'''



                                #Linear Data Structure

            #Stack

'''
class Stack:
    
    def __init__(self):
        self.top = -1
        self.s=[]

    def Push(self , data ):
        self.s.append(data)
        self.top += 1
    
    def Pop(self):
        if(self.top == -1):
            print("Stack is empty cannot pop ")
        else:
            self.top -= 1
            return self.s.pop()
    
    def peek(self):
        if(self.top == -1):
            print("Stack is empty cannot display any items")
        else:
            return self.s[self.top]

    def isEmpty(self):
        if(self.top == -1):
            return 1
        return 0

stack =Stack()
if(stack.isEmpty()):
    print("Stack is empty.")
l=[12 , 21 , 32 , 45 , 87 , 1]
for i in l:
    stack.Push(i)
print("The top element in the stack is: " , stack.peek())
print("Popped element is : ", stack.Pop())
print("The top element in the stack is: " , stack.peek())
'''


            #Queue

'''
class Queue:

    def __init__(self):
        self.queue = []
    
    def enqueue(self , data):
        self.queue.append(data)

    def dequeue(self):
        if(len(self.queue)<1):
            return 1
        return self.queue.pop(0)

    def display(self):
        print(*self.queue)
    
    def size(self):
        return len(self.queue)

q=Queue()
l=[12 , 21 , 32 , 45 , 87 , 1]
for i in l:
    q.enqueue(i)
q.display()
q.dequeue()
print("After removing an element")
q.display()
'''


            #Linked List

'''
class Node:

    def __init__(self , data):
        self.data = data
        self.next = None
    
class LinkedList:

    def __init__(self):
        self.head = None
    
    def addatBeg(self , data) :
        curr = Node(data)
        curr.next = self.head
        self.head = curr

    def addatEnd(self , data) :
        curr= Node(data)
        temp = self.head
        while(temp.next!=None):
            temp = temp.next
        temp.next = curr
    
    def deleteatBeg(self):
        self.head = self.head.next
    
    def deleteatEnd(self):
        temp = self.head
        while(temp.next.next!=None):
            temp=temp.next
        temp.next = None
    
    def printing(self):
        temp = self.head
        while(temp!=None):
            print(temp.data , end=" --> ")
            temp = temp.next
        print("None")

ll = LinkedList()
l1=[12 , 21 , 32 ]
l2=[45 , 87 , 1]
for i in l1:
    ll.addatBeg(i)
ll.printing()
for i in l2:
    ll.addatBeg(i)
ll.printing()
ll.deleteatBeg()
ll.printing()
ll.deleteatEnd()
ll.printing()
'''


                                #Non Linear Data Structure

            #Trees


'''
class Node:
    def __init__(self , data):
        self.left = None
        self.data = data
        self.right = None
    
class Tree:
    def createNode(self , data):
        return Node(data)

    def insert(self , node , data):
        if(node is None):
            return self.createNode(data)
        if node.data < data:
            node.left = self.insert(node.left , data)
        else:
            node.right = self.insert(node.right , data)
        return node
    
    def inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)

    def preorder(self,root):
        if root is not None:
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self,root):
        if root is not None:
            self.inorder(root.left)
            self.inorder(root.right)
            print(root.data,end=" ")


t=Tree()
l=[12 , 21 , 32 , 45 , 87 , 1]
root=Node(5)
for i in l:
    t.insert(root,i)
t.inorder(root)
'''