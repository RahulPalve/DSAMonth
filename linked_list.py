class Node:
    data = None
    next = None


print("1. Add to Linked List")
print("2. Remove in linked List")
print("3. Display List")
print("0. Exit")
user = 1
root = Node()
while user !=0:
    user = int(input())
    if user == 1:
        print("Where S, E, M?")
        pos = input()
        print("Value : ")
        data = input()
        node = Node()
        node.data = data
        if pos == "S":
            root, node.next = node, root
        elif pos == "E":
            if not root.data:
                root.data = node.data
                break
            temp = root
            while temp.next:
                temp = temp.next
            temp.next = node
        elif pos == "M":
            print("index?")
            ind = input()

            temp = root
            count = 0
            while temp.next:
                if ind == count:
                    temp.next, node.next = node, temp.next
                    break
                temp = temp.next
                count=count+1
    elif user == 3:
        t =root
        while t:
            print(t.data,"->",end="")
            t = t.next
        
            
            
            




