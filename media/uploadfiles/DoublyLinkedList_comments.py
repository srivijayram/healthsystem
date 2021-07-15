class DLLNode:#a class to represent each node in the list
    def __init__(self,item):#initializes the data,next and prev nodes
        self.data=item
        self.next=None
        self.prev=None

class DLList:#class of the double linked list
    def __init__(self):#initializes head and tail
        self.head=None
        self.tail=None
        
    def _insert(self,item):#method to insert a node
        node=DLLNode(item)
        if(self.head):#to insert a node if the list is not empty
            self.tail.next=node
            node.prev=self.tail
        else:#inser a node when the list is empty
            self.head=node
        self.tail=node
        print(item,"inserted!")
    
    def _delete(self,item):#method to delete a node
        if(self._search(item)):#checks whether the item is present in the 
            if(self.head.data==item):#if the item is at head
                self.head=self.head.next
                del self.head.prev
                self.head.prev=None
            elif(self.tail.data==item):#if the item is at tail
                self.tail=self.tail.prev
                del self.tail.next
                self.tail.next=None
            else:
                node=self.head
                while(node.next):
                    if(node.data==item):
                        temp1=node.prev
                        temp2=node.next
                        del node
                        temp1.next=temp2#links the adjacent nodes
                        temp2.prev=temp1
                        break
                    node=node.next
            print(item,"deleted")
        else:
            print(item,"not found")
        
    def _search(self,key):#method to search an element
        c=0
        node=self.head
        while(node):
            c+=1
            if(node.data==key):
                break
            node=node.next
        else:#element not found
            c=0
        return c
    
    def _print_list(self):#method to print the list
        node=self.head
        while(node):
            print(node.data,end=' ')
            node=node.next
        print()
        
if __name__ == "__main__":
    llist=DLList()#create an instance of Double Linked List
    n=True
    while(n):#menu driven program to perform operations on the list
        print("\n1.Insert\n2.Delete\n3.Search\n4.Print\n0.Exit\nEnter a number [1/2/3/4/0]:",end=" ")
        n=int(input())
        while(n<0 or n>4):
            n=int(input("Enter a valid number:"))
        if(n==1):
            item=int(input("Enter the number to be inserted:"))
            llist._insert(item)
        elif(n==2):
            item=int(input("Enter the number to be deleted:"))
            llist._delete(item)
        elif(n==3):
            item=int(input("Enter the number to be searched:"))
            res=llist._search(item)
            if(res):
                print(item,"found at node-",res)
            else:
                print(item,"not found")
        elif(n==4):
            print()
            llist._print_list()        