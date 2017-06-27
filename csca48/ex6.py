def rsum(abc):
    result = 0
    l = len(abc)
    if l > 1:
        l = l // 2
        lsum = rsum(abc[:l])
        risum = rsum(abc[l:])
        result = lsum + risum
    else:
        if isinstance(abc[0], list):
            if len(abc[0]) == 0:
                result += 0
            else:
                result += rsum(abc[0])
        else:
            result += abc[0]
    return result

def rmax(abc):
    l = len(abc)
    if l > 1:
        l = l // 2
        left = rmax(abc[:l])
        right = rmax(abc[l:])
        if left > right:
            result = left
        else:
            result = right
    else:
        if isinstance(abc[0], list):
            if len(abc[0]) < 1:
                result = -99999
            else:
                result = rmax(abc[0])
        else:
            result = abc[0]
    return result


def second_smallest(asd):
    return find(asd)[0]


def sum_max_min(abc):
    a = findmm(abc)
    return a[0] + a[1]


def find(abc):
    print(abc)
    if len(abc) == 2:
        if isinstance(abc[0], list) and isinstance(abc[1], list):
            re = find(abc[0] + abc[1])
        elif isinstance(abc[1], list):
            re = find(abc[:1] + abc[1])
        elif isinstance(abc[0], list):
            fe = find(abc[0] + abc[1:])
        else:
            if abc[0] > abc[1]:
                re = (abc[0], abc[1])
            else:
                re = (abc[1], abc[0])
    elif len(abc) == 0:
        re = (99999,99909)
    else:
        if isinstance(abc[0], list):
            re = find(abc[0] + abc[1:])
        else:
            current = abc[0]
            second, first = find(abc[1:])
            if (second < current):
                re = (second, first)
            elif (current > first) and (second >= current):
                re = (current, first)
            else:
                re = (first, current)            
    return re

def findmm(abc):
    print(abc)
    # base case
    if len(abc) == 2:
        if isinstance(abc[0], list) and isinstance(abc[1], list):
            re = findmm(abc[0] + abc[1])
        elif isinstance(abc[1], list):
            re = findmm(abc[:1] + abc[1])
        elif isinstance(abc[0], list):
            fe = findmm(abc[0] + abc[1:])
        else:
            if abc[0] > abc[1]:
                re = (abc[0], abc[1])
            else:
                re = (abc[1], abc[0])  
    else:
        # long list first element is list
        if len(abc)> 2 and isinstance(abc[0], list):
            re = findmm(abc[0] + abc[1:])
        # list has one element and its a list
        elif len(abc) ==1 and isinstance(abc[0], list):
            re = findmm(abc[0])
        # list has one element
        elif len(abc) == 1:
            re = (abc[0],abc[0])
        elif len(abc) == 0:
            
        else:
            # recursive step 
            current = abc[0]
            maxi, mini = findmm(abc[1:])
            if (current >= maxi):
                re = (current, mini)
            elif (mini <= current):
                re = (maxi, mini)
            else:
                re = (maxi, current)
    return re
