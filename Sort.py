import time
import random
def bubbleSort(arr1,n) :
    
    for i in range(n) :
        for j in range (0,n-i-1) :
            if arr1[j] > arr1[j+1] :
                arr1[j] , arr1[j+1] = arr1[j+1], arr1[j]

    #print(arr1)

def selectionSort(arr2,n) :
    
    for i in range(n) :
        sorted_index = i
        for j in range(i+1,n) :
            if arr2[j] < arr2[sorted_index] :
                sorted_index = j
        arr2[i], arr2[sorted_index] = arr2[sorted_index],arr2[i]

    #print(arr2)

def insertionSort(arr3,n) :
    
    for i in range(1,n) :
        previous = i - 1
        current = arr3[i]
        
        while (previous >= 0 and arr3[previous] > current) :
            arr3[previous + 1] = arr3[previous]
            previous -= 1
        
        arr3[previous + 1] = current 
    
    #print(arr3)

def mysorting(arr4,n) :
    
    for i in range(n) :
        for j in range(i,n) :
            if arr4[i] > arr4[j] :
                arr4[i] , arr4[j] = arr4[j], arr4[i]

    #print(arr4)

def measure_time(sorting_function,arr) :
    n = 1000
    start_time = time.time()
    sorting_function(arr,n)
    end_time = time.time()
    return (end_time-start_time)

def main() :
    n = 1000  # Change this value to test larger datasets
    arr1 = [random.randint(0, 10000) for i in range(n)]
    arr2 = arr1.copy()
    arr3 = arr1.copy()
    arr4 = arr1.copy()
    bubble_time = measure_time(bubbleSort,arr1)
    selection_time = measure_time(selectionSort,arr2)
    insertion_time = measure_time(insertionSort,arr3)
    mysort_time = measure_time(mysorting,arr4)
    print(f"Bubble Sort time {bubble_time:.8f} seconds")
    print(f"Selection Sort time {selection_time:.8f} seconds")
    print(f"Insertion Sort time {insertion_time:.8f} seconds")
    print(f"My Algorithm Sort time {mysort_time:.8f} seconds")


main()