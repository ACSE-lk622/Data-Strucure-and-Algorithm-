def mergeLists(lst1,lst2):
    n1 = len(lst1)
    n2 = lent(lst2)
    if n1 == 0 : # list1 is empty
        return list(lst1)
    elif n2 == 0 : #list2 is empty 
        return list(lst2)
    else :
        output_lst = []
        i1 = 0 
        i2 = 0 
        while (i1 < n1 or i2 < n2) : #iteraition position less than list length
            if i1 < n1 and i2 < n2 :
                if lst1[i1] < lst2[i2] :
                    output_lst.append(lst1[i1]) # append smaller one to end of output list )
                    i1 += 1 #advance i1
                else :
                    output_lst.append(lst2[i2])
                    i2 += 1 # advance i2 
            elif : i1 < n1 # lst1 also have element which is not compared 
                output_lst.append(lst1[i1])
                i1 += 1
            else : # lst2 also have element which is not compared 
                output_lst.append(lst2[i2])
                i2 += 1
        return output_lst

def swap(lst, i, j):
    n = len(lst)
    assert(i >= 0 and i < n)
    assert(j >= 0 and j < n)
    lst[i],lst[j] = lst[j],lst[i]
    return 

def copy_back(output_lst, lst, left, right):
    assert(len(output_lst) == right-left + 1 )
    # Ensure the output lenghth has the right lenght for us to copy back
    for i in range(left,right+1)
        lst[i] = output_lst[i - left]
    return 
def mergeHelper(lst, left, mid, right):
    if left > mid or mid > right : # one of the two sublists is empty 
        return 
    i1 =left 
    i2 = mid + 1 
    output_lst = []
    while i1 < mid or i2 < right:
        if i1 < mid and i2 < right:
            if lst[i1] < lst[i2]:
                output_lst.append(lst[i1])
                i1 += 1
            else :
                output_lst.append(lst[i2])
                i2 += 1
        elif i1 < mid :
            output_lst.append(lst[i1])
            i1 += 1
        else :
            output_lst.append(lst[i2])
            i2 += 1
    copy_back(output_lst, lst, left, right)

def mergesortHelper(lst, left, right)
    if left == right :
        return 
    elif left+1 == right: #base case : only two element
        if lst[left] > lst[right]:
            swap(lst, left, right) #　swap it 
    else :
        mid = (right + left ) // 2
        mergesortHelper(lst, left, mid) # sort right half recursively
        mergesortHelper(lst, mid + 1, right) #sort left half recursively
        mergeHelper(lst, left, mid, right) # merge them together
def mergesort(lst):
    if len(lst) <= 1:
        return 
    else :
        mergesortHelper(lst, 0, len(lst)-1)       