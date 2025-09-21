'''
Write a function reverse_sentence() that takes in a string sentence and returns the sentence with the order of the words reversed. 
The sentence will contain only alphabetic characters and spaces to separate the words. 
If there is only one word in the sentence, the function should return the original string.
'''

def reverse_sentence(sentence):
    if not sentence:
        return None
    lst = sentence.split()
    if len(lst) == 1:
        return lst[0] 
    else:
        lst = lst[::-1]
    return " ".join(lst)
    
print(reverse_sentence("Hello")) 
