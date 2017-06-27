## all funciton will take a list of integers as input

def rsum(ints):
    if len(ints) == 1:
        return ints[0]
    else:
        return ints[0] + rsum(ints[1:])


def rmax(list):
    if len(list) == 1:
        return list[0]
    else:
        m = rmax(list[1:])
        return m if m > list[0] else list[0]

def second_smallest(int_list):

    if(len(int_list) == 2):
        if (int_list[0] >= int_list[1]):
            return (int_list[0],int_list[1])
        else:
            return (int_list[1],int_list[0])
    else:
        first_second_smallest,second_second_smallest = second_smallest(int_list[1:])
        current_elem = int_list[0]
        if(second_second_smallest <= current_elem):
            return (second_second_smallest,current_elem)
        else:
            if (current_elem<=first_second_smallest):
               return (current_elem,first_second_smallest)
            else:
               return (first_second_smallest,second_second_smallest)

def sum_max_min(ints):
    pass

list_int = [1, 4, 6, 65, 7, 34, 23, 2]
# print(rsum(list_int))
# print(rmax(list_int))
# print(second_smallest(list_int))