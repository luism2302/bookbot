def count_words(text):
	separated = text.split()
	return len(separated)
def count_chars(text):
	counts = {}
	for char in text:
		if not char.isalpha():
			continue
		counts[char.lower()] = counts.get(char.lower(), 0) + 1
	return counts

def helper_sort(char_count):
	return char_count['num']

def sort_chars(char_count):
	list_of_dicts = []
	for k, v in char_count.items():
		curr_char = {'char': k, 'num': v}
		list_of_dicts.append(curr_char)
	list_of_dicts.sort(reverse = True, key = helper_sort)
	return list_of_dicts