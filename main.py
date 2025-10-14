def get_book_text(path_to_file):
    with open(path_to_file) as file:
        text = file.read()
        return text 
    
from stats import word_count
from stats import char_count

text = get_book_text("books/frankenstein.txt")
num_words = word_count(text)
num_chars = char_count(text)
char_dict = char_count(text)

#print(f"Found {num_words} total words")
#print(num_chars)