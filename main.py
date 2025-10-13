def get_book_text(path_to_file):
    with open(path_to_file) as file:
        text = file.read()
    print(text)

get_book_text("books/frankenstein.txt")