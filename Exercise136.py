'''
The notion of anagrams can be extended to multiple words. For example, “William
Shakespeare” and “I am a weakish speller” are anagrams when capitalization and
spacing are ignored. Extend your program from Exercise 135 so that it is able 
to check if two phrases are anagrams. Your program should ignore 
capitalization, punctuation marks and spacing when making the determination.
'''

string1 = input('Enter string one: ').lower()
string2 = input('Enter string two: ').lower()

string1Count = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,
'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}

string2Count = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,
'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}

abc = 'abcdefghijklmnopqrstuvwxyz'

for _ in range(len(string1)):
    if string1[_] in string1Count:
        string1Count[string1[_]] += 1

for _ in range(len(string2)):
    if string2[_] in string2Count:
        string2Count[string2[_]] += 1


for _ in range(len(abc)):
    if string1Count[abc[_]] != string2Count[abc[_]]:
        print('Not an anagram.')
        exit()

print('It is an anagram!')