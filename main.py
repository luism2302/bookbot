def get_book_text(filepath):	
	with open(filepath) as f:
		contents = f.read()
	return contents

def count_words(text):
	separated = text.split()
	return len(separated)

def main():
	FRANKENSTEIN_PATH = "books/frankenstein.txt"
	try: 
		contents = get_book_text(FRANKENSTEIN_PATH)
	except FileNotFoundError:
		print("Couldn't find the book provided")
	word_count = count_words(contents)	
	print(f'Found {word_count} total words')
main()
	
	
	