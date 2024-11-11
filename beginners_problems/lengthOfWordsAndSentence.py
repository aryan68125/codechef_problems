'''
Print the length

Write a program to print the length of each word of the sentence given below as well as the length of the whole sentence.
"Coding on CodeChef"

Note: Please print the outputs in the same format as given below.
Output Format

Coding - 6
on - 2
CodeChef - 8
Coding on CodeChef - 18

'''

sentence = "Coding on CodeChef"
count=0
count_s = 0
char=''
for i,ch in enumerate(sentence):
    if ch == " ":
        print(f"{char} - {count}")
        char=''
        count=0
    else:
        char=char+ch
        count+=1
    count_s+=1
print(f"{char} - {count}")
print(f"{sentence} - {count_s}")
