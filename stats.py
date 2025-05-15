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
