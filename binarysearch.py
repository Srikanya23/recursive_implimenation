def Binary_search(arr,tar,l,r):
    if r>l:
        mid = (l+r)//2
    
        if arr[mid] == tar:
            return mid
        elif tar > arr[mid]:
            return Binary_search(arr,tar,mid,r)
        else :
            return Binary_search(arr,tar,l,mid) 
    else :
        return -1
