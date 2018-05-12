
###implementing a binary search without knowing the number of elements that exist inthe array####
array = [-1,1,2,3,4,5,6,7,8,9,11,57,99] 
#adding a buffer -1 value since we want array to start from 1

key = 99
#to check if key is present in the array

pos = 1

def binsearch(arr, key, low, high):
    
    while low < high:
        mid = (low + high )/2
        
        if arr[mid] == key:
            return mid
        
        elif arr[mid]< key : 
            low = mid
        
        else:
            high = mid
    return 0 
            
while pos<=len(array):
    
    if key == array[pos] :
        print "found at " +  str(pos)
        break
    
    elif key < array[pos]:
        upperlmt = pos
        pos= binsearch(array,key,(pos/2),pos)
    
    else: 
        if (pos*2 < len(array)):
            pos = pos * 2 
        else:
            pos = len(array)-1


        

