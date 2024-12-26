"""
input: hello
output: hel_lo
input: assalom
output: ass_alom
input: abcabcdabcdeabcdefabcdefg
output: abc_abcd_abcdeab_cdef_abcdefg
"""

txt = input("Enter string: ")
result = ""
vowels = ['e', 'u', 'i', 'o', 'a']
letters_after_underscore = []
count = 0

for ind, char in enumerate(txt):
    result += char
    count += 1

    if count == 3 and ind != len(txt) - 1:
        if char not in vowels and char not in letters_after_underscore:
            result += "_"
            letters_after_underscore.append(char)
        count = 0  

        
print(result)
