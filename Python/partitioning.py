#orange partitioning problem

def partition_array(array):
    pivot=array[-1]
    j=0
    for i in range(len(array)-1):
        if array[i]<pivot:
            array[j],array[i]=array[i],array[j]
            j+=1
    array[j],array[-1]=array[-1],array[j]
    
array=[11,18,20,4,6,18,20,26,2,13,13]
print(partition_array(array))
print(array)

