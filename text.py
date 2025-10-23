def get_book_text(filepath):	
	with open(filepath) as f:
		contents = f.read()
	return contents