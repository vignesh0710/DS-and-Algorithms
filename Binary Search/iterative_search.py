#iterative binary search
def iterative_bin_search(arr,size_arr,numb):
    
    start = 0;end = size_arr-1
    while (start<=end):
   
        mid = int((start+end)/2)
        
        
        if arr[mid] == numb:
            return ("Number found", mid)
        elif numb<arr[mid]:
            end = mid -1 
            
        elif numb>arr[mid]:
            start= mid+1
    return ("Number not found",-1)
        
arr = [2,6,13,21,36,47,63,81,97]
iterative_bin_search(arr,len(arr),811)
