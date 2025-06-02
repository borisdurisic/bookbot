def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = count_words(text)
    print(f"{number_of_words} words found in the document")

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def count_words(book):
    words = book.split()
    counter = 0
    for word in words:
        counter += 1
    return counter

main()