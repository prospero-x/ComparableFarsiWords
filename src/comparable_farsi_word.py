try:
	from farsi_character_values import vals
except ModuleNotFoundError:
	from .farsi_character_values import vals


class ComparableFarsiWord(str):
	def __new__(cls, word = ''):
		return str.__new__(cls, word)

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

		max_self = len(self) - 1
		max_other = len(other) - 1
		i = 0
		while i <= max_self and i <= max_other:
			if self[i] not in vals:
				raise ValueError(
					"Unrecognized character '%s'." % self[i]
				)

			if other[i] not in vals:
				raise ValueError(
					"Unrecognized character '%s'." % other[i]
				)

			string1_val = vals[self[i]]
			string2_val = vals[other[i]]

			if string1_val == string2_val:
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

			# Found unequal characters.
			return -1 if string1_val < string2_val else 1

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