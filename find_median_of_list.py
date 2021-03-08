"""
The median is the middle number in a sorted sequence of numbers.  
Finding the median of [7, 12, 3, 1, 6] would first consist of sorting the sequence into [1, 3, 6, 7, 12] 
and then locating the middle value, which would be 6.
If you are given a sequence with an even number of elements, you must average the two elements surrounding the middle.
"""

def median (lst):
    sorted_list = sorted(lst)
    print sorted_list
    if len(sorted_list) % 2 != 0:
        #odd number of elements
        index = len(sorted_list)//2 
        return sorted_list[index]
    elif len(sorted_list) % 2 == 0:
        #even no. of elements
        index_1 = len(sorted_list)/2 - 1
        index_2 = len(sorted_list)/2
        mean = (sorted_list[index_1] +     sorted_list[index_2])/2.0
        return mean
   
print median([2, 4, 5, 9])
print median([7, 12, 3, 1, 6])
print median([4, 5, 5, 4])
