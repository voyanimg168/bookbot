import sys
from stats import (
    get_num_words, 
    get_chars_dict, 
    chars_dict_to_sorted_list,
) 

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]

    text = get_book_text(path_to_book)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print(f"{num_words} words found in the document")
    print(chars_dict)
    print_report(path_to_book, num_words, chars_sorted_list)

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        return f.read()

def print_report(path_to_book, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print("Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

# call main to execute the program
main()
