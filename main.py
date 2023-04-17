# Glen Correia
# 1001980331

from tkinter import *
import random
import time

root = Tk()
# set window size of User Interface
root.geometry("700x400")
# Title
root.title("SortAlgo")

# Creating  labels
courseLabel = Label(root, text="DAA")
myLabel2 = Label(root, text="Enter list size: ")
myLabel3 = Label(root, text="Enter highest number: ")
myLabel4 = Label(root, text="Select SortAlgo: ")
validVal = Label(root, text="")

# Input for list size and highest element in list along with Algorithm selection option from drop down
list_size = Entry(root, borderwidth=1, width=20)
list_size.insert(0, 10)
highest_list = Entry(root, borderwidth=1, width=20)
highest_list.insert(0, 10)
sorting_algo_selected1 = StringVar(root)
sorting_algo_selected1.set("select a sorting algorithm")  # default value
option1 = OptionMenu(root, sorting_algo_selected1, "Bubblesort", "Insertionsort", "Selection", "Heapsort", "Mergesort",
                     "Quicksort", "QuickSort3median")
sorting_algo_selected2 = StringVar(root)
sorting_algo_selected2.set("select a sorting algorithm")  # default value
option2 = OptionMenu(root, sorting_algo_selected2, "Bubblesort", "Insertionsort", "Selection", "Heapsort", "Mergesort",
                     "Quicksort", "QuickSort3median")


# Performs sorting and provides the run time of algorithms

def myClick():
    list_size_label = "Size of list: " + list_size.get();
    myLabel = Label(root, text=list_size_label)
    highest_val = Label(root, text="Highest number in list: " + highest_list.get())
    # Generates the list of random values
    unsorted_list = random_gen()
    sortingAlgo_label = Label(root, text="")
    sortingAlgo_label1 = Label(root, text="")
    list_size_val = int(list_size.get())
    if sorting_algo_selected1.get() == "Bubblesort":
        bubblesort_time = bubble_sort(unsorted_list)
        sortingAlgo_label = Label(root, text="BubbleSort time: " + str(bubblesort_time))
    elif sorting_algo_selected1.get() == "Insertionsort":
        insertionsort_time = insertion_sort(unsorted_list)
        sortingAlgo_label = Label(root, text="InsertionSort time: " + str(insertionsort_time))
    elif sorting_algo_selected1.get() == "Selection":
        selectionsort_time = selection_sort(unsorted_list)
        sortingAlgo_label = Label(root, text="SelectionSort time: " + str(selectionsort_time))
    elif sorting_algo_selected1.get() == "Heapsort":
        heapsort_time = heap_sort(unsorted_list)
        sortingAlgo_label = Label(root, text="HeapSort time: " + str(heapsort_time))
    elif sorting_algo_selected1.get() == "Mergesort":
        start_time = time.time()
        merge_sort(unsorted_list)
        mergesort_endtime = time.time()
        mergesort_time = mergesort_endtime - start_time
        sortingAlgo_label = Label(root, text="MergeSort time: " + str(mergesort_time))
    elif sorting_algo_selected1.get() == "Quicksort":
        start_time = time.time()
        quicksort(unsorted_list, 0, list_size_val - 1)
        quicksort_endtime = time.time()
        quicksort_time = quicksort_endtime - start_time
        sortingAlgo_label = Label(root, text="QuickSort time: " + str(quicksort_time))
    elif sorting_algo_selected1.get() == "QuickSort3median":
        start_time = time.time()
        quicksort3median(unsorted_list, 0, list_size_val)
        quicksort3median_endtime = time.time()
        quicksort3median_time = quicksort3median_endtime - start_time
        sortingAlgo_label = Label(root, text="QuickSor3median time: " + str(quicksort3median_time))
    if sorting_algo_selected2.get() == "Bubblesort":
        bubblesort_time1 = bubble_sort(unsorted_list)
        sortingAlgo_label1 = Label(root, text="BubbleSort time: " + str(bubblesort_time1))
    elif sorting_algo_selected2.get() == "Insertionsort":
        insertionsort_time1 = insertion_sort(unsorted_list)
        sortingAlgo_label1 = Label(root, text="InsertionSort time: " + str(insertionsort_time1))
    elif sorting_algo_selected2.get() == "Selection":
        selectionsort_time1 = selection_sort(unsorted_list)
        sortingAlgo_label1 = Label(root, text="SelectionSort time: " + str(selectionsort_time1))
    elif sorting_algo_selected2.get() == "Heapsort":
        heapsort_time1 = heap_sort(unsorted_list)
        sortingAlgo_label1 = Label(root, text="HeapSort time: " + str(heapsort_time1))
    elif sorting_algo_selected2.get() == "Mergesort":
        start_time = time.time()
        merge_sort(unsorted_list)
        mergesort_endtime = time.time()
        mergesort_time1 = mergesort_endtime - start_time
        sortingAlgo_label1 = Label(root, text="MergeSort time: " + str(mergesort_time1))
    elif sorting_algo_selected2.get() == "Quicksort":
        start_time = time.time()
        quicksort(unsorted_list, 0, list_size_val - 1)
        quicksort_endtime = time.time()
        quicksort_time1 = quicksort_endtime - start_time
        sortingAlgo_label1 = Label(root, text="QuickSort time: " + str(quicksort_time1))
    elif sorting_algo_selected2.get() == "QuickSort3median":
        start_time = time.time()
        quicksort3median(unsorted_list, 0, list_size_val)
        quicksort3median_endtime = time.time()
        quicksort3median_time1 = quicksort3median_endtime - start_time
        sortingAlgo_label1 = Label(root, text="QuickSort3median time: " + str(quicksort3median_time1))
    # Add value to the grid view of the interface on click of button "Sort!! And Get run time"
    myLabel.grid(row=2, column=1)
    sortingAlgo_label.grid(row=7, column=1)
    sortingAlgo_label1.grid(row=7, column=2)
    highest_val.grid(row=4, column=1)


# Button creation and fuction call myclick on click of the button
myButton = Button(root, text="SORT & FIND", command=myClick, fg="yellow", bg="blue")

#https://www.geeksforgeeks.org/bubble-sort/

def bubble_sort(array):
    """
    Bubble sort is simple algorithm which performs swap with adjacent element in the list
    till the entire list is sorted.
    Having worst case of O(n^2) comparison and swaps
    :param array: Unsorted list
    :return: sorted list
    """
    b_s_start = time.time()
    array_len = len(array)
    if array_len > 1:
        for i in range(0, array_len):
            for j in range(0, array_len - 1):
                if array[j] > array[j + 1]:
                    # Swapping adjacent element in the list
                    array[j] = array[j] ^ array[j + 1]
                    array[j + 1] = array[j] ^ array[j + 1]
                    array[j] = array[j] ^ array[j + 1]
        b_s_end = time.time()
        # print("Run time of Bubblesort: ", b_s_end - b_s_start)
        return b_s_end - b_s_start
    else:
        return "List is Empty"

#https://www.geeksforgeeks.org/selection-sort/

def selection_sort(array):
    """
    Selection sort is an inplace sorting algorithm with worst case time complexity of O(n^2)
    efficient for small datasets and when memory space is costly
    Algorithm divides the input list into two parts: a sorted sublist of items (which is initially empty)
    from left to right and a sublist of the remaining unsorted items that occupy the rest of the list
    :param array: Unsorted list
    :return: Sorted list
    """
    start = time.time()
    array_len = len(array)
    for i in range(0, array_len):
        min_index = i
        for j in range(i + 1, array_len):
            if array[j] < array[min_index]:
                min_index = j
        # Swap the element from unsorted sublist to sorted sublist
        temp = array[i]
        array[i] = array[min_index]
        array[min_index] = temp
    end = time.time()
    # print("Running time", end - start)
    return end - start

#https://www.geeksforgeeks.org/insertion-sort/

def insertion_sort(array):
    """
    Insertion sort is an inplace sorting algorithm with worst case time complexity of O(n^2)
    efficient for small datasets and when memory space is costly
    It removes an element and place in its position in sorted array.
    :param array:Unsorted list
    :return: Sorted list
    """
    start = time.time()
    array_len = len(array)
    for i in range(0, array_len):
        value = array[i]
        j = i - 1
        while j >= 0 and array[j] > value:
            array[j + 1] = array[j]
            array[j] = value
            j -= 1
    end = time.time()
    # Printing the running time of algorithm
    # print("Running time", end - start)
    return end - start

 #https://www.geeksforgeeks.org/merge-sort/   

def merge_sort(array):
    """
    Merge sort is a recursive algorithm with worst case of O(nlog n)
    uses divide and conquer technique
    :param array: Unsorted list
    """
    array_len = len(array)
    if array_len > 1:
        middle = array_len // 2
        arr1 = array[:middle]
        arr2 = array[middle:]
        merge_sort(arr1)
        merge_sort(arr2)
        n1 = len(arr1)
        n2 = len(arr2)
        i = 0
        j = 0
        k = 0
        # Merge sublist
        while i < n1 and j < n2:
            if arr1[i] <= arr2[j]:
                array[k] = arr1[i]
                i += 1
                k += 1
            else:
                array[k] = arr2[j]
                j += 1
                k += 1
        while i < n1:
            array[k] = arr1[i]
            i += 1
            k += 1
        while j < n2:
            array[k] = arr2[j]
            j += 1
            k += 1

#https://www.geeksforgeeks.org/heap-sort/

def heapify(array, array_len, index):
    """
    Heapify function helps in balancing the binary tree recursively
    :param array: list
    :param array_len:size of list
    :param index: element at this index needs to be placed in heap order
    """
    root = index
    left_tree = 2 * index + 1
    right_tree = 2 * index + 2
    if (left_tree < array_len) and (array[index] < array[left_tree]):
        root = left_tree
    if (right_tree < array_len) and (array[root] < array[right_tree]):
        root = right_tree
    if root != index:
        # Swap the elements using bitwise xor
        array[root] = array[index] ^ array[root]
        array[index] = array[index] ^ array[root]
        array[root] = array[index] ^ array[root]
        heapify(array, array_len, root)


def heap_sort(array):
    """
    Heap sort function returns sorted list in O(nlog n)time
    :param array: Unsorted list
    :return:run time of heapsort
    """
    start = time.time()
    array_len = len(array)
    for i in range(array_len, -1, -1):
        heapify(array, array_len, i)

    for i in range(array_len - 1, 0, -1):
        temp = array[i]
        array[i] = array[0]
        array[0] = temp
        heapify(array, i, 0)
    end = time.time()
    # Printing the running time of algorithm
    # print("Running time", end - start)
    return end - start

#https://wangyy395.medium.com/sortings-algorithms-implementation-analyze-bd91f38eaa02 

def partition(array, low, high):
    """
    Divides the list into sublist based on pivot element value
    Reorder its elements, while determining a point of division based on pivot value
    :param array: unsorted list
    :param low: first index of list
    :param high: last index of list
    :return: final position
    """
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            # increment the smaller value
            i += 1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
    temp = array[i + 1]
    array[i + 1] = array[high]
    array[high] = temp
    return i + 1

#https://www.geeksforgeeks.org/quick-sort/

def quicksort(array, low, high):
    """
    Quicksort is inplace & recursive sorting algorithm which follows divide and conquer approach
    worst case of O(n^2) and Average case of O(nlog n)
    :param array: Unsorted list
    :param low: first index of the list
    :param high: last index of the list
    :return: sorted list
    """
    array_len = len(array)
    if array_len == 1:
        return array
    if low < high:
        position = partition(array, low, high)
        quicksort(array, low, position - 1)
        quicksort(array, position + 1, high)
    # return array


def swap(array, x, y):
    """
    :param array:Array which requires swap
    :param x:value of array at index x to be swapped with value of array at index y
    :param y:value of array at index y to be swapped with value of array at index x
    """
    array[x], array[y] = array[y], array[x]


def partition3median(array, low, high):
    """
    Divides the list into sublist based on 3 pivot elements value
    first sublist has elements in between min to median
    second sublist has elements in between median to high-1
    Reorder its elements, while determining a point of division based on median value
    :param array: list for partition
    :param low: first index of list
    :param high: last index of list
    :return: final index
    """
    # find median value
    median = low + int(((high - 1 - low) / 2))
    i = low + 1
    # This will return array[median] if the value obtained from multiplication is positive
    if (array[median] - array[high - 1]) * (array[low] - array[median]) >= 0:
        swap(array, low, median)
    # This will return array[high-1] if the value obtained from multiplication is positive
    elif (array[high - 1] - array[median]) * (array[low] - array[high - 1]) >= 0:
        swap(array, low, high - 1)
    # array[low] is returned if above two condition are not satisfied
    pivot = array[low]
    for j in range(low, high):
        if pivot > array[j]:
            swap(array, i, j)
            i += 1
    swap(array, low, i - 1)
    return i - 1


def quicksort3median(array, low, high):
    """
    3median Quick sort is an improved version of quicksort having worst case of O(nlog n)
    :param array: unsorted list
    :param low: first index of the list
    :param high: last index of the list
    :return: sorted list
    """
    array_len = len(array)
    if array_len == 1:
        return array
    if low < high:
        partition_position = partition3median(array, low, high)
        quicksort3median(array, low, partition_position)
        quicksort3median(array, partition_position + 1, high)
    # return array

 #https://www.geeksforgeeks.org/generating-random-number-list-in-python/

def random_gen():
    """
    Random_gen function creates list of random element of user specific size and the range of element
    is from 1 to ceiling value provided by user
    :return: list of random element of size specified by user
    """
    # Random number generator
    size_of_array = int(list_size.get())
    highest_number = int(highest_list.get())
    random_list = []
    for i in range(0, size_of_array):
        number = random.randint(1, highest_number)
        random_list.append(number)
    return random_list


# Adding Labels to the grid view
myButton.grid(row=6, column=0)
validVal.grid(row=1, column=3)
courseLabel.grid(row=0, column=0, columnspan=2)
myLabel2.grid(row=1, column=0)
myLabel3.grid(row=3, column=0)
myLabel4.grid(row=5, column=0)
option1.grid(row=5, column=1)
option2.grid(row=5, column=2)
list_size.grid(row=1, column=1)
highest_list.grid(row=3, column=1)
root.mainloop()


#References:
#https://blog.51cto.com/u_15349661/3704183
#https://zhuanlan.zhihu.com/p/347852171
#https://www.freecodecamp.org/news/sorting-algorithms-explained-with-examples-in-python-java-and-c/