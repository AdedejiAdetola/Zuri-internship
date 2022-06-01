# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename) as f:
        contents = f.read()
    return contents


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    text_list = text.lower().split()
    word_dict = {}
    char = [".",",","?"]
    for each_word in text_list:
        for i in each_word:
            if i in char:
                each_word = each_word.replace(i,"")

        if each_word not in word_dict:
                word_dict[each_word] = 1

        elif each_word in word_dict:
            word_dict[each_word] = word_dict[each_word] + 1

    return word_dict


print(read_file_content('./story.txt'))
print(count_words())