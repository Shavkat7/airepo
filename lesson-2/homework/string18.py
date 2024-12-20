# Write a program that checks if a string starts with one word and ends with another.
    # Example:

    # Input: "Python is fun!"
    # Starts with: "Python"
    # Ends with: "fun!"

sent = input("Input: ")
new_sent = sent.strip()
last_word=""

for i in range(len(new_sent)-1, -1, -1):
    if new_sent[i] == " ":
        break
    last_word += new_sent[i]

last_word = last_word[::-1]

first_word=""

for i in range(len(new_sent)):
    if new_sent[i] == " ":
        break
    first_word += new_sent[i]

print("Starts with:", first_word)
print("Ends with:", last_word)
