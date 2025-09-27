"Combining two list to create the tuple and dictionary"

def dictmaker(list1,list2):
    return dict(zip(list1,list2))

def tuplemaker(list1,list2):
    return list(zip(list1,list2)) 
    

list1 = ["apple","ball","cat","dog"]
list2 = [1,2,3,4]

print(dictmaker(list1,list2))
print(tuplemaker(list1,list2)) 
