# Ask the user for a string and replace all the vowels with a symbol (e.g., *).

sent = input("Enter a sting: ")
vowels = ["e", "u", "i", "o", "a"]
new_sent=""
for i in range(len(sent)):
    if sent[i] in vowels:
        new_sent +="*"
    else:
        new_sent += sent[i]
print(new_sent)

