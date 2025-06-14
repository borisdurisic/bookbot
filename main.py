import sys
from stats import (
    count_words,
    count_chars,
    sorted_list
)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        number_of_words = count_words(text)
        number_of_chars = count_chars(text)
        chars_sorted_list = sorted_list(number_of_chars)
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {number_of_words} total words")
        print("--------- Character Count -------")
        for i in chars_sorted_list:
            if not i["char"].isalpha():
                continue
            print(f"{i['char']}: {i['num']}")
        print("============= END ===============")

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

main()