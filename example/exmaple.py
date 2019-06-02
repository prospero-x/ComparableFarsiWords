from src import ComparableFarsiWord

if __name__ == '__main__':
	# 'پ' is the third character of the Farsi Alphabet, but it has a Unicode
	# value of U+067E. 'ق' is the twenty-fourth character of the Farsi
	# alphabet, and it has a unicode value of U+0642.
	#
	# Therefore, Unicode incorrectly places 'پ' AFTER 'ق'.
	#
	# Therefore, relying on Unicode to compare the words 'پارچ', ("parch", the
	# Farsi word for "jar") and'قارچ' ("gharch", the Farsi word for "mushroom")
	# will produce the incorrect result that parch comes after gharch.
	#
	# Only by using this library can a correct result be attained.

	word1 = 'پارچ'  # "parch", the Farsi word for "jar"
	word2 = 'قارچ'  # "gharch", the Farsi word

	try:
		assert word1 < word2
	except AssertionError:
		print(
			"As expected, Unicode incorrectly thinks '%s' is " % word1 +
			"lexicographically greater than '%s'..." % word2
		)

	assert ComparableFarsiWord(word1) < ComparableFarsiWord(word2)
	print(
		"Success! ComparableFarsiWords correctly determined that '%s' " % word1 +
		"is lexicographically less than '%s'." % word2
	)