# Write a program that counts the number of vowels and consonants in a given string.

inp = input("enter a word: ")

vowels=0
consonants=0

for i in inp:
    if i == 'a' or i == 'i' or i == 'o' or i == 'u' or i == 'e':
        vowels += 1
    else:
        consonants += 1

print(f"In the word {inp}, the number of vowels is {vowels}, and the number of consonants is {consonants}")