
## binary search use loop
def binary search (lst,elt)
    left = 0 
    right = len(lst)-1
    if lst[left] > elt or lst[right] > elt :
        return none 
    
    while left < = right :
        mid = (left+right) // 2
        if lst[mid] == elt :
            return mid 
        elif lst[mid] < elt :
            left = mid + 1 
        else : 
            right = mid - 1
    return none 



def binaryS (a,target):
    left = 0 
    right = len(a)-1
    if a[left] > target or a[right]< target :
        return none 
    else :
        return binarySearch(a,left,right,target)


def binarySearch(a, left, right, target):
    if right < left: 
        return False
    mid = (left + right)//2
    if a[mid] == target: 
        return True 
    if a[mid] > target: 
        return binarySearch(a, left, mid-1, target)
    else: 
        # a[mid] < target
        return binarySearch(a, mid+1, right, target)
    #This line is never reached