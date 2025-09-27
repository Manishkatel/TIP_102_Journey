"Counting the total number of occurences of item in a list"

def frequency_map(list1):
    frequency = {}
    for item in list1:
        frequency[item] = frequency.get(item, 0) + 1 
        
    return frequency
        
        
my_list = [1, 2, 3, 1, 2, 1, 4]
print(frequency_map(my_list))
