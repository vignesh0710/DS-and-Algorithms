def recur_bin_search(arr,start,end,numb):
    
    if start> end:
        return -1
    else:
        mid = int((start+end)/2)
        if numb == arr[mid]:
            return ("Number found", mid)
        elif numb < arr[mid]:
            return recur_bin_search(arr, start,mid-1,numb)
        else:
            return recur_bin_search(arr, mid+1,end,numb)
    
    
arr = [2,6,13,21,36,47,63,81,97] 
print(arr)
recur_bin_search(arr,0,len(arr)-1,13)
