import numpy as np
from ch11utilities import print_pass
from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import sys
# from ch11soundutilities import play_sound


def update(frame_data):
    """Display bars representing the current state."""    
    # unpack info for graph update
    data, colors, swaps, comparisons = frame_data
    plt.cla()  # clear old contents of current Figure

    # create barplot and set its xlabel
    bar_positions = np.arange(len(data))
    axes = sns.barplot(bar_positions, data, palette=colors)  # new bars
    axes.set(xlabel=f'Comparisons: {comparisons}; Swaps: {swaps}',
             xticklabels=data)  

def flash_bars(index1, index2, data, colors, swaps, comparisons):
    """Flash the bars about to be swapped and play their notes."""
    for x in range(0, 2):
        colors[index1], colors[index2] = 'white', 'white'
        yield (data, colors, swaps, comparisons) 
        colors[index1], colors[index2] = 'purple', 'purple'
        yield (data, colors, swaps, comparisons) 
        # play_sound(data[index1], seconds=0.05)
        # play_sound(data[index2], seconds=0.05)

def selection_sort(data):
    """Sort data using the selection sort algorithm and
    yields values that update uses to visualize the algorithm."""
    swaps = 0  
    comparisons = 0
    colors = ['lightgray'] * len(data)  # list of bar colors
    
    # display initial bars representing shuffled values
    yield (data, colors, swaps, comparisons)    
    
    # loop over len(data) - 1 elements    
    for index1 in range(0, len(data) - 1):
        smallest = index1
        
        # loop to find index of smallest element's index   
        for index2 in range(index1 + 1, len(data)):
            comparisons += 1
            colors[smallest] = 'purple'
            colors[index2] = 'red'            
            yield (data, colors, swaps, comparisons) 
            # play_sound(data[index2], seconds=0.05)

            # compare elements at positions index and smallest
            if data[index2] < data[smallest]:
                colors[smallest] = 'lightgray'
                smallest = index2
                colors[smallest] = 'purple'
                yield (data, colors, swaps, comparisons) 
            else: 
                colors[index2] = 'lightgray'
                yield (data, colors, swaps, comparisons) 
            
        # ensure that last bar is not purple
        colors[-1] = 'lightgray'
        
        # flash the bars about to be swapped
        yield from flash_bars(index1, smallest, data, colors, 
                              swaps, comparisons)

        # swap the elements at positions index1 and smallest
        swaps += 1
        data[smallest], data[index1] = data[index1], data[smallest]  
        
        # flash the bars that were just swapped
        yield from flash_bars(index1, smallest, data, colors, 
                              swaps, comparisons)
        
        # indicate that bar index1 is now in its final spot
        colors[index1] = 'lightgreen'
        yield (data, colors, swaps, comparisons)    

    # indicate that last bar is now in its final spot
    colors[-1] = 'lightgreen'
    yield (data, colors, swaps, comparisons)    
    # play_sound(data[-1], seconds=0.05)

    # play each bar's note once and color it darker green
    for index in range(len(data)):
        colors[index] = 'green'
        yield (data, colors, swaps, comparisons)
        # play_sound(data[index], seconds=0.05)

def main():
    number_of_values = int(sys.argv[1]) if len(sys.argv) == 2 else 10 

    figure = plt.figure('Selection Sort')  # Figure to display barplot
    numbers = np.arange(1, number_of_values + 1)  # create array 
    np.random.shuffle(numbers)  # shuffle the array

    # start the animation
    anim = animation.FuncAnimation(figure, update, repeat=False,
        frames=selection_sort(numbers), interval=50)

    plt.show()  # display the Figure

# call main if this file is executed as a script
if __name__ == '__main__':
    main()







# def square_generator(values):
#     for value in values:
#         yield value ** 2

# squares = square_generator([1,2,3,4])

# print(squares)
# # <generator object square_generator at 0x7f7aeaed0270>


# for number in squares:
#     print(number, end=' ')
# # 1 4 9 16

# print()

# squares = square_generator([4,3,2,1])

# print( next(squares) )
# # 16
# print( next(squares) )
# # 9
# print( next(squares) )
# # 4
# print( next(squares) )
# # 1

# # print( next(squares) ) #Error StopIteration



# ----------------------------------------------------
# Merge Sort
# ----------------------------------------------------

# # calls recursive sort_array method to begin merge sorting
# def merge_sort(data):
#     sort_array(data, 0, len(data) - 1) 

# def sort_array(data, low, high):
#     """Split data, sort subarrays and merge them into sorted array."""
#     # test base case size of array equals 1     
#     if (high - low) >= 1:  # if not base case
#         middle1 = (low + high) // 2  # calculate middle of array
#         middle2 = middle1 + 1  # calculate next element over     

#         # output split step
#         print(f'split:   {subarray_string(data, low, high)}') 
#         print(f'         {subarray_string(data, low, middle1)}') 
#         print(f'         {subarray_string(data, middle2, high)}\n') 

#         # split array in half then sort each half (recursive calls)
#         sort_array(data, low, middle1)  # first half of array       
#         sort_array(data, middle2, high)  # second half of array     

#         # merge two sorted arrays after split calls return
#         merge(data, low, middle1, middle2, high)              

# # merge two sorted subarrays into one sorted subarray             
# def merge(data, left, middle1, middle2, right):
#     left_index = left  # index into left subarray              
#     right_index = middle2  # index into right subarray         
#     combined_index = left  # index into temporary working array
#     merged = [0] * len(data)  # working array        
  
#     # output two subarrays before merging
#     print(f'merge:   {subarray_string(data, left, middle1)}') 
#     print(f'         {subarray_string(data, middle2, right)}') 

#     # merge arrays until reaching end of either         
#     while left_index <= middle1 and right_index <= right:
#         # place smaller of two current elements into result  
#         # and move to next space in arrays                   
#         if data[left_index] <= data[right_index]:       
#             merged[combined_index] = data[left_index]
#             combined_index += 1
#             left_index += 1
#         else:                                                 
#             merged[combined_index] = data[right_index] 
#             combined_index += 1
#             right_index += 1

#     # if left array is empty                                
#     if left_index == middle2:  # if True, copy in rest of right array
#         merged[combined_index:right + 1] = data[right_index:right + 1]
#     else: # right array is empty, copy in rest of left array                              
#         merged[combined_index:right + 1] = data[left_index:middle1 + 1]

#     data[left:right + 1] = merged[left:right + 1]  # copy back to data

#     # output merged array
#     print(f'         {subarray_string(data, left, right)}\n') 

# # method to output certain values in array
# def subarray_string(data, low, high):
#     temp = '   ' * low  # spaces for alignment
#     temp += ' '.join(str(item) for item in data[low:high + 1])
#     return temp

# def main():
#     data = np.array([35, 73, 90, 65, 23, 86, 43, 81, 34, 58])
#     print(f'Unsorted array: {data}\n')
#     merge_sort(data) 
#     print(f'\nSorted array: {data}\n')

# # call main if this file is executed as a script
# if __name__ == '__main__':
#     main()

    
# ----------------------------------------------------
# Insertion Sort
# ----------------------------------------------------

# def insertion_sort(data):
#     """Sort an array using insertion sort."""
#     # loop over len(data) - 1 elements      
#     for next in range(1, len(data)):
#         insert = data[next]  # value to insert 
#         move_item = next  # location to place element

#         # search for place to put current element         
#         while move_item > 0 and data[move_item - 1] > insert:  
#             # shift element right one slot
#             data[move_item] = data[move_item - 1]         
#             move_item -= 1                                      
                                              
#         data[move_item] = insert  # place inserted element 
#         print_pass(data, next, move_item)  # output pass of algorithm

# def main(): 
#     data = np.array([35, 73, 90, 65, 23, 86, 43, 81, 34, 58])
#     print(f'Unsorted array: {data}\n')
#     insertion_sort(data) 
#     print(f'\nSorted array: {data}\n')

# # call main if this file is executed as a script
# if __name__ == '__main__':
#     main()

# ----------------------------------------------------
# Selection Sort
# ----------------------------------------------------

# """Sorting an array with selection sort."""
# import numpy as np

# def selection_sort(data):
#     """Sort array using selection sort."""
#     # loop over len(data) - 1 elements      
#     for index1 in range(len(data) - 1):
#         smallest = index1  # first index of remaining array

#         # loop to find index of smallest element                      
#         for index2 in range(index1 + 1, len(data)): 
#             if data[index2] < data[smallest]:
#                 smallest = index2
                                              
#         # swap smallest element into position
#         data[smallest], data[index1] = data[index1], data[smallest]  
#         print_pass(data, index1 + 1, smallest)  

# def main(): 
#     data = np.array([35, 73, 90, 65, 23, 86, 43, 81, 34, 58])
#     print(f'Unsorted array: {data}\n')
#     selection_sort(data) 
#     print(f'\nSorted array: {data}\n')

# # call main if this file is executed as a script
# if __name__ == '__main__':
#     main()


# ----------------------------------------------------
# Binary Search
# ----------------------------------------------------

# def binary_search(data, key):
#     """Perform binary search of data looking for key."""
#     low = 0   # low end of search area
#     high = len(data) - 1  # high end of search area
#     middle = (low + high + 1) // 2  # middle element index
#     location = -1  # return value -1 if not found
    
#     # loop to search for element
#     while low <= high and location == -1:
#         # print remaining elements of array
#         print(remaining_elements(data, low, high))

#         print('   ' * middle, end='')  # output spaces for alignment
#         print(' * ')  # indicate current middle

#         # if the element is found at the middle                    
#         if key == data[middle]:                                   
#             location = middle  # location is the current middle     
#         elif key < data[middle]:  # middle element is too high
#             high = middle - 1  # eliminate the higher half          
#         else:  # middle element is too low                         
#             low = middle + 1  # eliminate the lower half            
                                                                        
#         middle = (low + high + 1) // 2  # recalculate the middle

#     return location  # return location of search key
                            
# def remaining_elements(data, low, high):
#     """Display remaining elements of the binary search."""
#     return '   ' * low + ' '.join(str(s) for s in data[low:high + 1])

# def main():
#     # create and display array of random values
#     data = np.random.randint(10, 91, 15)
#     data.sort()
#     print(data, '\n')

#     search_key = int(input('Enter an integer value (-1 to quit): ')) 

#     # repeatedly input an integer; -1 terminates the program
#     while search_key != -1:
#         location = binary_search(data, search_key)  # perform search

#         if location == -1:  # not found
#             print(f'{search_key} was not found\n') 
#         else:
#             print(f'{search_key} found in position {location}\n')

#         search_key = int(input('Enter an integer value (-1 to quit): '))

# # call main if this file is executed as a script
# if __name__ == '__main__':
#     main()


# ----------------------------------------------------
# Linear Search
# ----------------------------------------------------

# def linear_search(data, search_key):
#     for index, value in enumerate(data):
#         if value == search_key:
#             return index
#     return -1


# np.random.seed(11)

# values = np.random.randint(10, 91, 10)

# print(values)
# # [35 73 90 65 23 86 43 81 34 58]

# print( linear_search(values, 23) )
# # 4

# print( linear_search(values, 61) )
# # -1

# print( linear_search(values, 34) )
# # 8


# ----------------------------------------------------
# Recursive Fibonacci Series
# ----------------------------------------------------

# # Function fibonacci 
# def fibonacci(n):
#     if n in (0, 1):  # base cases
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
    
# # Testing Function fibonacci
# for n in range(41):
#     print(f'Fibonacci({n}) = {fibonacci(n)}')

# # Self Check Exercise 3
# def iterative_fibonacci(n):
#     result = 0
#     temp = 1
#     for j in range(0, n):
#         temp, result = result, result + temp
#     return result

# # %timeit fibonacci(30)
# # 807 ms ± 787 µs per loop (mean ± std. dev. of 7 runs, 1 loop each)

# # %timeit iterative_fibonacci(30)
# # 5.11 µs ± 36 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)


# ----------------------------------------------------
# Recursive Factorial
# ----------------------------------------------------

# def factorial(number):
#     """Return factorial of number."""
#     if number <= 1:
#         return 1
#     return number * factorial(number - 1)  # recursive call
    
# for i in range(11):
#     print(f'{i}! = {factorial(i)}')


# print(factorial(50))

# ----------------------------------------------------
# Factorial
# ----------------------------------------------------

# factorial = 1

# for number in range(5,0,-1):
#     factorial *= number

# # 5!
# print(factorial)
# # 120