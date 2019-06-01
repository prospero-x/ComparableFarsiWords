'''
This purpose of this map is to explicitly establish an ordering of the Farsi
characters, in order to make sorting Farsi words possible. Continue reading
for an explanation.

There is no Farsi Unicode block. When a Farsi keyboard is used on a computer,
the OS binds the keys of the keyboard to the Unicode Block U+0600 - U+06FF
(named "Arabic"), which contains characters for Arabic, Pashto, Persion, and
Urdu.

The Farsi alphabet shares . In the Arabic Unicode Block,
the Arabic alphabet is assigned to the beginning of the code block, in order.
The Farsi characters which are not part of the Arabic alphabet are assigned to
numbers AFTER the Arabic alphabet:

			U+0627: 'ا' ("alif", first letter of the Arabic alphabet, shared by
						Arabic and Farsi)
			...
			(entire Arabic alphabet, in order)
			...
			U+064A: 'ي' ("yaa", the last letter of the Arabic alphabet, does
						not exist in Farsi)
			...
			...
			...
			U+067E: 'پ' ("pe", only in Farsi)
			...
			U+0686: 'چ ("che", only in Farsi)
			...
			U+0698: 'ژ' ("zhe", only in Farsi)
			...
			U+06AF: 'گ' ("gaf", only in Farsi)

If I start an interactive python shell in my terminal, I can type various Farsi
characters in and examine their underlying Unicode value. This was done using
macOS 10.12.6, using the "Persian - Standard" Keyboard.

MacBook-Pro-4:Farsi xerxes$ python --version
Python 3.6.8
MacBook-Pro-4:Farsi xerxes$ python
Python 3.6.8 (v3.6.8:3c6b436a57, Dec 24 2018, 02:04:31)
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> farsi_alphabet = 'ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی'
>>> for character in farsi_alphabet:
...     print("%s\t%d" %(hex(ord(character)), ord(character)))
...
0x627	1575
0x628	1576
0x67e	1662
0x62a	1578
0x62b	1579
0x62c	1580
0x686	1670
0x62d	1581
0x62e	1582
0x62f	1583
0x630	1584
0x631	1585
0x632	1586
0x698	1688
0x633	1587
0x634	1588
0x635	1589
0x636	1590
0x637	1591
0x638	1592
0x639	1593
0x63a	1594
0x641	1601
0x642	1602
0x6a9	1705
0x6af	1711
0x644	1604
0x645	1605
0x646	1606
0x648	1608
0x647	1607
0x6cc	1740
>>>

As you can see, Mac's "Persian Standard" begins the alphabet by using Arabic
values for the shared characters 'ا' and 'ب'. However, when it get's to the
third character, 'پ', it cannot use an Arabic value becuase 'پ' does not exist
in Arabic. Therefore, it needs to use one of the values beyond the Arabic
alphabet (U+067E).

Immediately after, for the fourth letter of the Farsi alphabet, 'ت', a value
from the Arabic range can be used, so the value jumps back down to U+062A.

In addition to these expected jumps, there are unexpected jumps where a
character in fact exists in the Arabic alphabet, but the keyboard does not use
that value. For example, value U+06CC is used for 'ی' when in fact 'ی' exists
in Arabic and has a Unicode value of U+0649.

Therefore, Unicode values of Farsi Characters cannot be relied on to establish
order between the characters. Hence the map.

'''

vals = {
	' ': 0,
	'ا': 1,
	'ب': 2,
	'پ': 3,
	'ت': 4,
	'ث': 5,
	'ج': 6,
	'چ': 7,
	'ح': 8,
	'خ': 9,
	'د': 10,
	'ذ': 11,
	'ر': 12,
	'ز': 13,
	'ژ': 14,
	'س': 15,
	'ش': 16,
	'ص': 17,
	'ض': 18,
	'ط': 19,
	'ظ': 20,
	'ع': 21,
	'غ': 22,
	'ف': 23,
	'ق': 24,
	'ک': 25,
	'گ': 26,
	'ل': 27,
	'م': 28,
	'ن': 29,
	'و': 30,
	'ه': 31,
	'ی': 32
}