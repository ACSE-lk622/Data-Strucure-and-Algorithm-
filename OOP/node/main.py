from linked_list import LinkedList

my_linked_list = LinkedList()

my_linked_list.insert_node(9)
my_linked_list.insert_node(3)
my_linked_list.insert_node(6)
my_linked_list.insert_node(15)
# 1st :　9
# 2st :  3 -> 9
# 3st :  3 -> 6 -> 9
# 4st :  3 -> 6 -> 9 -> 15 
print(my_linked_list.head.next.next.next.value)
my_linked_list.print_list_items()
my_linked_list.insert_node(0)
print(my_linked_list.count_nodes())
print(my_linked_list.count_nodes_re(my_linked_list.head))
print(my_linked_list.find_node(27))
my_linked_list.print_list_items()
print(my_linked_list.delete_node(0))
my_linked_list.print_list_items()
print(my_linked_list.delete_node(13))
my_linked_list.print_list_items()
my_linked_list.print_reversed(my_linked_list.head)