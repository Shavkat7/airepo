# Write a program that asks the user for a string and a character, 
# then removes all occurrences of that character from the string.

sent = input("Enter a string: ")
char = input("Enter character: ")

new_sent = sent.replace(char, "")
print(new_sent)