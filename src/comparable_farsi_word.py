try:
	from farsi_character_values import character_values, accent_values
except ModuleNotFoundError:
	from .farsi_character_values import character_values, accent_values


class ComparableFarsiWord(str):
	'''
	ComparableFarsiWord: A subclass of the "str" class which
	overrides comparison operators. When a collection of ComparableFarsiWord
	objects is sorted, these overriding methods are called.

	The COMPARE function makes use of the character values defined in
	farsi_character_values.py.
	'''
	def __new__(cls, word = ''):
		return str.__new__(cls, word)

	def __hash__(self):
		return hash(str(self))

	def remove_accents(self, word):
		'''
		Accents are their own Unicode Character. We ignore them
		when determining the lexicographic value of a word.
		'''
		no_accents = ""
		for character in word:
			if character not in accent_values:
				no_accents += character

		return no_accents

	def compare(self, other):
		'''
		Lexicographically compare this Farsi word to another Farsi word,
		Using the character value map.

		returns:
			0 if the two strings are equal
			-1 if this string is lexicographically less than other
			-1 if this string is lexicographically greater than other
		'''

		if not isinstance(other, ComparableFarsiWord):
			raise TypeError(
				"Cannot compare objects of type 'ComparableFarsiWord'" +
				" and '%s'" % type(other)
			)

		# Corner case: one or both of the strings is empty.
		if len(self) == 0 or len(other) == 0:
			# '' is less than any character
			if len(other) > 0:
				return -1
			elif len(self) > 0:
				return 1
			else:
				return 0

		this_str = self.remove_accents(self)
		other_str = self.remove_accents(other)

		max_self = len(this_str) - 1
		max_other = len(other_str) - 1
		i = 0
		while i <= max_self and i <= max_other:
			if this_str[i] not in character_values:
				raise ValueError(
					"Unrecognized character '%s'." % self[i]
				)

			if other_str[i] not in character_values:
				raise ValueError(
					"Unrecognized character '%s'." % other[i]
				)

			this_val = character_values[this_str[i]]
			other_val = character_values[other_str[i]]

			if this_val == other_val:
				# end of both strings -> they're equal
				if i == max_self and i == max_other:
					return 0

				# end of self -> other is greater
				if i == max_self:
					return -1

				# end of other ->  other is less
				if i == max_other:
					return 1

				# end of neither. Continue.
				i += 1
				continue

			# Found unequal 	.
			return -1 if this_val < other_val else 1

	def __lt__(self, other):
		c = self.compare(other)
		return c < 0

	def __le__(self, other):
		c = self.compare(other)
		return c <= 0

	def __eq__(self, other):
		c = self.compare(other)
		return c == 0

	def __ne__(self, other):
		c = self.compare(other)
		return c != 0

	def __ge__(self, other):
		c = self.compare(other)
		return c >= 0

	def __gt__(self, other):
		c = self.compare(other)
		return c > 0