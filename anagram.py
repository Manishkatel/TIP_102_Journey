# Checking if two words are anagrams or not

def is_anagram(a,b):
    if len(a) !=len(b):
        return False
    return sorted(a) == sorted(b) 

print(is_anagram("cat","act"))

