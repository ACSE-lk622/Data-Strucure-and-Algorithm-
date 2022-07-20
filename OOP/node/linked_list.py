from node import Node

class LinkedList:
    
    def __init__(self):
        self.head = None

    def insert_node(self,value):
        new_node = Node(value)

        if self.head is None :
            self.head = new_node 
        elif self.head.value >= value:
            new_node.next = self.head #decend value 
            self.head = new_node  
        else : # this also include insert tail
            previous = self.head 
            runner = self.head.next

            while (runner is not None) and (value > runner.value): #not reach the end of list and value bigger than node value 
                 previous = runner #move to the next node 
                 runner = runner.next
            new_node.next = runner
            previous.next = new_node
    def print_list_items(self):

        if self.head is None :
            print("Empty")
        else :
            runner = self.head
            while runner is not None:
                print(runner.value, end=" ")
                runner = runner.next
            print() 
    def count_nodes(self):
        count = 0 
        runner = self.head 
        while runner is not None:
            count += 1
            runner = runner.next
        return count

    def count_nodes_re(self,node):
        if node is None : 
            return 0 
        else :
            return 1 + self.count_nodes_re(node.next)

    def find_node(self,target_value):
        runner = self.head
        while runner is not None:
            if runner.value == target_value:
                return True 
            runner = runner.next
        
        return False 
    
    def delete_node(self,target_value):
        if self.head is None:
            return False 
        elif self.head.value == target_value: #head
            self.head = self.head.next # assign next node as head node 
            return True 
        else : # middle 
            previous = self.head 
            runner = self.head.next

            while (runner is not None) and (target_value >runner.value): 
                previous = runner 
                runner = runner.next     #move to next node 
            if (runner is not None ) and (runner.value == target_value):
                #previous will now point to the node 
                #that comes after the runner node
                previous.next = runner.next #bridge, if reach tail , runner.next == None
                return True 
            else :
                return False

    def print_reversed(self,node):
        if node is not None:
            self.print_reversed(node.next)
            print(node.value,end=" ")
