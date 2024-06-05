'''
The Twelve Days of Christmas is a repetitive song that describes an increasingly
long list of gifts sent to one’s true love on each of 12 days. A single gift is sent on
the first day. A new gift is added to the collection on each additional day, and then
the complete collection is sent. The first three verses of the song are shown below.
The complete lyrics are available on the internet.
On the first day of Christmas
my true love sent to me:
A partridge in a pear tree.
On the second day of Christmas
my true love sent to me:
Two turtle doves,
And a partridge in a pear tree.
On the third day of Christmas
my true love sent to me:
Three French hens,
Two turtle doves,
And a partridge in a pear tree.
Your task is to write a program that displays the complete lyrics for The Twelve
Days of Christmas. Write a function that takes the verse number as its only parameter
and displays the specified verse of the song. Then call that function 12 times with
integers that increase from 1 to 12.
Each item that is sent to the recipient in the song should only appear once in your
program, with the possible exception of the partridge. It may appear twice if that
helps you handle the difference between “A partridge in a pear tree” in the first verse
and “And a partridge in a pear tree” in the subsequent verses. Import your solution
to Exercise 85 to help you complete this exercise.
'''

def displayVerse(day):
    ordinal_numbers = [
        "first", "second", "third", "fourth", "fifth", "sixth", 
        "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
    ]
    
    gifts = [
        "Twelve drummers drumming",
        "Eleven pipers piping",
        "Ten lords a-leaping",
        "Nine ladies dancing",
        "Eight maids a-milking",
        "Seven swans a-swimming",
        "Six geese a-laying",
        "Five golden rings",
        "Four calling birds",
        "Three French hens",
        "Two turtle doves",
        "A partridge in a pear tree"
    ]
    
    print(f"On the {ordinal_numbers[day - 1]} day of Christmas")
    print("my true love sent to me:")
    
    for i in range(day, 0, -1):
        if i == 1 and day > 1:
            print("And a partridge in a pear tree.")
        else:
            print(gifts[12 - i])


for day in range(1, 12 + 1):
    displayVerse(day)
    print()

