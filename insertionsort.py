def insertionsort(array) : 
    #loop starts from second element of the index 
    for i in range (1, len(array)):
        
        value = array[i]
        hole = i

        while (hole>0) and (array[hole-1]>value):
           
            array[hole] = array[hole-1]
            
            hole = hole - 1

        
        array[hole] = value
        


arr = [12,11,4,3,1,1,6,7]
insertionsort(arr)


print arr
