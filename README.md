# Caesar-Cipher
README: Text Processing and Caesar Cipher Decoder
Overview
This Python project, titled "Text Processing and Caesar Cipher Decoder," is a comprehensive application designed for text analysis and implementing classical encryption/decryption techniques using the Caesar cipher.

Features
Text Processing:

Letters Function: Processes input text to extract and convert alphabetic characters to lowercase. Non-alphabetic characters are discarded.
Letter Frequency Analysis:

FreqDict Function: Constructs a frequency dictionary for each letter in the alphabet from the processed text. This function plays a crucial role in analyzing the composition of the text.
Caesar Cipher Implementation:

Caesar Class:
Constructor: Initializes with a text and calculates its letter frequency distribution.
Score Method: Compares the frequency distribution of the class's text with another text. This method is useful in deciphering the correct shift used in the Caesar cipher.
Encode Method: Encodes the text using the Caesar cipher. It shifts each letter in the text by a specified number (n).
Decode Method (partially visible): Appears to implement the decoding logic of the Caesar cipher by trying different shift values and using the score method to find the most likely original text.
Usage
To use the Letters function, pass a string to it. It will return a string containing only the alphabetic characters in lowercase.
FreqDict requires a string input and returns a dictionary with the frequency of each letter.
To encode or decode text using the Caesar cipher, instantiate the Caesar class with your text. Use the Encode and Decode methods to perform encryption and decryption, respectively.
