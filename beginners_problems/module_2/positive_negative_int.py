'''
Positive and Negative

Write a program to check whether a number given as user input is positive, negative, or zero.
'''
x = input()
x = int(x)
if x>0:
    print("Positive")
elif x<0:
    print("Negative")
elif x==0:
    print("Zero")
else:
    print("Not a number")