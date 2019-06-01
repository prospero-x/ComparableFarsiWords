from src import ComparableFarsiWord
import unittest2


class TestComparableFarsiWord(unittest2.TestCase):

	def test_first_string_empty(self):
		word1 = ComparableFarsiWord("")
		word2 = ComparableFarsiWord("بودن")

		self.assertLess(word1, word2)

	def test_second_string_empty(self):
		word1 = ComparableFarsiWord("بودن")
		word2 = ComparableFarsiWord("")

		self.assertGreater(word1, word2)

	def test_both_strings_empty(self):
		word1 = ComparableFarsiWord("")
		word2 = ComparableFarsiWord("")

		self.assertEqual(word1, word2)

	def test_same_length_last_char_different_1(self):
		word1 = ComparableFarsiWord("سنجیده بودید")
		word2 = ComparableFarsiWord("سنجیده بودیم")

		self.assertLess(word1, word2)

	def test_same_length_last_char_different_2(self):
		word1 = ComparableFarsiWord("سنجیده بودیم")
		word2 = ComparableFarsiWord("سنجیده بودید")

		self.assertGreater(word1, word2)

	def test_same_length_first_char_different_1(self):
		word1 = ComparableFarsiWord("مرسی")
		word2 = ComparableFarsiWord("ارسی")

		self.assertGreater(word1, word2)

	def test_same_length_first_char_different_2(self):
		word1 = ComparableFarsiWord("ارسی")
		word2 = ComparableFarsiWord("مرسی")

		self.assertLess(word1, word2)

	def test_different_length_words(self):
		word1 = ComparableFarsiWord("تخلف کرد")
		word2 = ComparableFarsiWord("تخلف کردیم")

		self.assertLess(word1, word2)

	def test_equal_words(self):
		word1 = ComparableFarsiWord("سنجیده بودید")
		word2 = ComparableFarsiWord("سنجیده بودید")

		self.assertEqual(word1, word2)
