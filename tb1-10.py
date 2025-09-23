# print("Hello World")
#1
# to print vowles and consonents
#Take an input character from the user and check whether the given input is a vowel or consonant

t = input("Enter the alphabet: ").lower()
vowel = ['a', 'e', 'i', 'o', 'u']
if t.isalpha():
    for i in vowel:
        if t == i:
            print("Vowel")
            break
    else:
        print("Consonant")
else:
    print("Invalid Input")

#2
#check weather it is an aplabet or not
if('a'<t<'z' or t=='a' or t=='z'):
    print("Alphabet")
else:
    print("Not an alphabet")

#3
# get the ascii number of the input character
a = input()
