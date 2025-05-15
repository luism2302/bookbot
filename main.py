from stats import count_words, count_letters 
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = open_book(sys.argv[1])
    word_count = count_words(book)
    letter_counts = count_letters(book)
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {sys.argv[1]}...') 
    print("------------ Word Count ------------")
    print(f'Found {word_count} total words')
    print("------------ Character Count ------------")
    for k, v in letter_counts.items():
        print(f'{v}: {k}')
def open_book(book_path: str) -> str:
	with open(book_path, 'r') as file:
			full_book = file.read()
	return full_book
main()
