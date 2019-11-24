#first occurence
def iterative_bin_search_first(arr,size_arr,numb):
    
    start = 0;end = size_arr-1; result = -1
    while (not start> end):
   
        mid = int((start+end)/2)
        if arr[mid] == numb:
            
            ##imp for finding the first occurence
            result = mid
            end  = mid - 1
        elif numb<arr[mid]:
            end = mid -1 
            
        elif numb>arr[mid]:
            start= mid+1
    return result
    
arr = [2,13,13,13,21,36,47,63,81,97]
print (iterative_bin_search_first(arr,len(arr),13))
