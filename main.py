from stats import count_words, count_chars

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = count_words(text)
    number_of_chars = count_chars(text)
    print(f"{number_of_words} words found in the document")
    print(number_of_chars)

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

main()