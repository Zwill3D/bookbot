def word_count(text):    
    num_words = text.split()
    return len(num_words)

def char_count(text):
    lowercase_text = text.lower()
    char_dict = {}
    for char in lowercase_text:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def sort_on(item):
    

def sort_it (char_dict):
    sorted_dict = []
    for char in char_dict:
        if char.isalpha = true:
            char_entry = {"char": char, "num": (char_dict[char])}
            sorted_dict.append(char_entry)
        else:
            pass
    
    
    
    return sorted_dict
