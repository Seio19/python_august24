def insertion_sort(array):
    for i in range(1,len(array)):
        element=array[i]
        j=i-1
        while j>=0 and element<array[j]:
            array[j+1]=array[j]
            j=j-1
        array[j+1]=element

      
def print_array(array):
    print(array)

if __name__ == "__main__":
   
    arr1 = [12, 11, 13, 5, 6, 22, 18, 20, 4, 11, 1]
    insertion_sort(arr1)
    print("Sorted array 1:", arr1)

   
