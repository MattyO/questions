#0,2 | 1,3  | 1,3 | 1,5 | 1,5 | 1,-1
#1,3 | 2,4  | 3,5 | 4,6 | 5,-1| 6,6
#2,4 | 3,5  | 4,6 | 5,-1| 6,6 |
#3,5 | 4,6  | 5,-1| 6,4
#4,6 | 5,-1 | 6,4 | 
#5,-1| 6,2  | 
#6,0 | 
#
#0,2 | 1,2  | 1,2 | 1,2 | 1,2 | 
#1,2 | 2,4  | 3,5 | 3,5 | 3,-1| 
#2,4 | 3,5  | 4,6 | 5,-1| 6,6 |
#3,5 | 4,6  | 5,-1| 6,6
#4,6 | 5,-1 | 6,4 | 
#5,-1| 6,2  | 
#6,0 | 

def flatten_chains(node_list):
    node_list = node_list.split(',')
    node_list.pop(0)

    node_list = [(str(head), str(int(tail))) for head, tail in enumerate(node_list) ]
    counter = 0
    while counter < len(node_list):
        current_head, current_tail = node_list[counter]
        counter += 1

        found_head, found_tail = next( ((head, tail) for head, tail in node_list if current_tail == head ), (None, None))
        if found_tail  != None and found_head != found_tail:
            node_list.remove((current_head, current_tail))
            node_list.remove((found_head, found_tail))
            node_list.append((current_head, found_tail))
            counter = 0

    return node_list

def number_cycles(reduced_list):
    cycles = 0
    for head, tail in reduced_list:
        if head == tail: 
            cycles += 1
    return cycles


