def bubbleSort(array): 
    n = len(array) 
    for i in range(n): 

        for j in range(0, n-i-1): 
            if array[j] > array[j+1] : 
                array[j], array[j+1] = array[j+1], array[j] 

list1 = input("Enter the numbers to be sorted")
array = list(map(int, list1.split()))

bubbleSort(array)

print ("Sorted array is:") 
for i in range(len(array)): 
    print ("%d" %array[i]), 