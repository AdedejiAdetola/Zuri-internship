# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagrams(word, anagram):
    # [assignment] Add your code here
    str_word = str(word)
    str_anagram = str(anagram)

    if len(str_word) == len(str_anagram):
        for i in str_word:
            if i not in str_anagram:
                return False
    return True


#print(find_anagrams("hello", "check"))

#print(find_anagrams("below", "elbow"))
