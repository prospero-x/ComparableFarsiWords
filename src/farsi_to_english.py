from verb_indexes import english_index, farsi_index

try:
	from farsi_character_values import number_values
	from comparable_farsi_word import ComparableFarsiWord
except ModuleNotFoundError:
	from .farsi_character_values import number_values
	from .comparable_farsi_word import ComparableFarsiWord


def farsi_verbs_by_page_value():
	index = {}
	for verb, page_string in farsi_index.items():
		first_char = page_string[0]
		page_num = number_values[first_char]
		for farsi_number in page_string[1:]:
			page_num = page_num * 10 + number_values[farsi_number]

		index[page_num] = ComparableFarsiWord(verb)
	return index


def english_verbs_by_page_value():
	'''
	index: a dictionary in which keys are verbs and values
	are lists of page numbers.

	Return a dictionary in which keys are page numbers and
	values are lists of verbs.
	'''
	reverse_index = {}
	for verb, pages in english_index.items():
		for page in pages:
			if page not in reverse_index:
				reverse_index[page] = []
			reverse_index[page].append(verb)
	return reverse_index


def farsi_to_english():
	farsi_verbs = farsi_verbs_by_page_value()
	english_verbs = english_verbs_by_page_value()

	assert sorted(farsi_verbs.keys()) == sorted(english_verbs.keys())

	verb_matches = {}
	for page_num, verbs in english_verbs.items():
		verb_matches[farsi_verbs[page_num]] = verbs

	return verb_matches


if __name__ == '__main__':
	verb_matches = farsi_to_english()

	for farsi_verb in sorted(verb_matches.keys()):
		print(", ".join(verb_matches[farsi_verb]), farsi_verb)
