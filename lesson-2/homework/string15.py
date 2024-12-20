# Ask the user for a sentence and create an acronym from the first letters of each word.
# Example:

# Input: "World Health Organization"
# Output: "WHO"

sent = input("Input: ")
output=sent.strip()[0]
for i in range(len(sent.strip())):
    if sent.strip()[i-1] == " ":
        output += sent.strip()[i]
print("Output:", output)