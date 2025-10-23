from stats import count_words, count_chars, sort_chars
from text import get_book_text
import sys

def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	BOOK_PATH = sys.argv[1]
	try: 
		contents = get_book_text(BOOK_PATH)
	except FileNotFoundError:
		print("Couldn't find the book in the path provided")
		sys.exit(1)

	word_count = count_words(contents)	
	char_count = count_chars(contents)
	sorted_count = sort_chars(char_count)
	print('============ BOOKBOT ============')
	print(f'Analyzing book found at {BOOK_PATH}')
	print('----------- Word Count ----------')
	print(f'Found {word_count} total words')
	print('--------- Character Count -------')
	for count in sorted_count:
		print(f'{count['char']}: {count['num']}')
if __name__ == "__main__":
	main()	
	
	