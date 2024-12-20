# Ask the user to input a sentence and a word to replace. 
# Replace that word with another word provided by the user.
    # Example:

    # Input sentence: "I love apples."
    # Replace: "apples"
    # With: "oranges"
    # Output: "I love oranges."

sent = input("Input sentence: ")
to_replace = input("Replace: ")
with_word = input("With: ")

output = sent.replace(to_replace, with_word)
print(f"Output: {output}")