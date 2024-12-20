# Write a program that asks the user for a sentence and prints the number of words in it.

sent = input("Enter a sentence: ")
print("There are", sent.strip().count(" ") + 1, "words")