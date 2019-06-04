from verb_indexes import english_index


def print_english_index_latex_code():
	verbs = sorted(english_index.keys())
	for verb in verbs:
		pages = english_index[verb]
		pages.sort()
		print(verb, ", ".join([str(page) for page in pages]), "\\\\")


if __name__ == '__main__':
	print_english_index_latex_code()
