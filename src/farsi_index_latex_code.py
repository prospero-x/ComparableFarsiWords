import sys
from verb_indexes import farsi_index

try:
	from comparable_farsi_word import ComparableFarsiWord
except ModuleNotFoundError:
	from .comparable_farsi_word import ComparableFarsiWord


def print_farsi_index_latex_code():
	'''
	I'm using Latex to typeset the index. This function
	prints out the verbs in alphabetical order, with a
	tab buffer between the verb and teh page number.

	Note that Latex doesn't understand that Farsi numbers are
	not reversed. So, we reverse them twice here, so they appear
	in the correct order once Latex renders the document.
	'''

	# Step 1: Sort the verbs
	verbs = [ComparableFarsiWord(verb) for verb in farsi_index.keys()]
	verbs.sort()

	# Step 2: Print out verbs and their corresponding page numbers
	sys.stdout.write("\\\\")
	for v in verbs:
		print("%s" % v, "\\tabto{30mm}", farsi_index[str(v)][::-1], "\\\\\\\\")


if __name__ == '__main__':
	print_farsi_index_latex_code()
