# Comparable Farsi Words
Use this code to compute the lexicographic order of a list of Farsi words.

## Runnning the Tests
To run the tests, execute `$ pytest` from the project root.

## Developer
You should regularly execute `flake8` from the root of this project. Specific flake rules to ignore are specified in `setup.cfg`

## Explanation

### The Problem
If I start an interactive python shell in my terminal, I can print out the Unicode value for every character in the Farsi alphabet. Note: this was done using macOS 10.12.6, using the "Persian - Standard" Keyboard, and Python 3.6.
```
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
```
As you can see, using Mac's "Persian Standard" Keyboard, when I iterate over Farsi alphabet in order, I get out-of-order Unicode values. So, what's going on?

### Background
The Farsi alphabet has 32 characters, 26 of which are shared with the Arabic alphabet. Due to this overlap, there is no Unicode Block dedicated to Farsi characters. Instead, when a Farsi keyboard is used on a computer, the OS binds the keys of the keyboard to the Arabic Unicode Block `U+0600 - U+06FF`, which contains characters used in Arabic, Pashto, Farsi, and Urdu.

For more information:
-  Unicode Overview: https://en.wikipedia.org/wiki/Unicode
-  Arabic Unicode Block: https://www.unicode.org/charts/PDF/U0600.pdf

### The Arabic Unicode Block

In the Arabic Unicode Block, the Arabic alphabet is assigned, in order, to values at the beginning of the block. Farsi characters which are not part of the Arabic alphabet are assigned to numbers AFTER the Arabic alphabet. The chart looks something like this:

| Unicode Value | Character | Description |
|:-:|:-:|:-:|
| U+0627 |ا | "alif", first letter of the Arabic alphabet, used in both Arabic and Farsi |
|...|...|...|
|...|...|(entire Arabic alphabet, in order)|
|...|...|...|
| U+064A |ي | "yaa", the final letter of the Arabic alphabet, used only in Arabic |
|...|...|...|
| U+067E |پ| "pe", used only in Farsi |
| U+0686 |چ| "che", used only in Farsi |
| U+0698 |ژ| "zhe", used only in Farsi |
| U+06AF |گ| "gaf", used only in Farsi |

This explains the sporadic assignments of Unicode Values to Farsi characters. When a Farsi character is **shared by Arabic**, it can be represented using an Arabic character, which has a value at the lower-end of the Arabic Unicode Block. On the other hand, when a Farsi character is **not used in Arabic**, a Unicode value from the upper-end of the Arabic Unicode Block must be used.

Therefore, Unicode values of Farsi Characters cannot be relied on to establish
order between the characters. Hence why I made this project.