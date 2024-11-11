'''
word[:1] takes the substring from the beginning of word to the character at index 1 (excluding the character at index 1), which is "C".

'P' is the character we want to insert into the string.

word[2:] takes the substring starting from the character at index 2 to the end of the string, which is "+".

These parts are concatenated together: "C" + "P" + "+" results in "CP+".
'''

word = "C++"
word = word[:1] + 'P' + word[2:]
print(word)

'''
How do you change the character at index 3 of the string variable "Cable" to 'r'?
'''
Cable = "Cable"
print(Cable[:3] + 'r' + Cable[4:])