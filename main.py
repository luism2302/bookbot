def main():
	book = open_book('frankenstein')
	word_count = count_words(book)
	letter_counts = count_letters(book)
	print(f'{word_count} words found in the document')
	for k, v in letter_counts.items():
		print(f'Letter: {k} was found {v} times')
def open_book(book_name: str) -> str:
	path = f'books/{book_name}.txt'
	with open(path, 'r') as file:
			full_book = file.read()
	return full_book
def count_words(text: str) -> int:
	words = text.split()
	return len(words)
def count_letters(text: str) -> dict:
	counts = {}
	for char in text:
		if not char.isalpha(): continue
		clean_char = char.lower()
		counts[clean_char] = counts.get(clean_char, 0) + 1
	ordered_pairs = sorted([(count, letter) for letter, count in counts.items()], reverse = True)
	ordered_counts = dict(ordered_pairs)
	return ordered_counts
main()