"""  remove_duplicates takes in a list and removes elements of the list that are the same. 
For example: remove_duplicates([1, 1, 2, 2]) should return [1, 2]. 
The list is sorted before removing the duplicates """



def remove_duplicates(inputlist):
    print "lista original:" + str(inputlist)
    if inputlist == []:
        return []    
    # Sort the input list from low to high    
    inputlist = sorted(inputlist)
    # Initialize the output list, and give it the first value of the now-sorted input list
    outputlist = [inputlist[0]]

    # Go through the values of the sorted list and append to the output list
    # ...any values that are greater than the last value of the output list
    for i in inputlist:
        if i > outputlist[-1]:
            outputlist.append(i)
    print "sin duplicados:" + str(outputlist)        
    return outputlist
  
print remove_duplicates([1, 1, 2, 2])
