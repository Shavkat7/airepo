content = ""

try:
    with open("lesson-6/homework/sample.txt") as file:
        content_l = file.readlines()
        for i in content_l:
            content = content + i + ", "
        print(file.read())
except FileNotFoundError as e:
    content_l = input("Type a paragraph: ")
    content = content_l
    with open("lesson-6/homework/sample.txt", "w") as file:
        file.writelines(content)

without_punc = ""
total_words = 1
content = content.strip()

for char in content:
    if char == " ":
        total_words +=1
        without_punc += " "
    if char.isalpha():
        without_punc += char.lower() 


without_punc = without_punc.lower()
words_list = without_punc.split(" ")
unique_words = []

word_with_count = {}


for word in words_list:
    if word not in unique_words:
        unique_words.append(word)
total_words = len(words_list)


for word in unique_words:
    word_with_count[word] = words_list.count(word)

sorted_dic = dict(sorted(word_with_count.items(), key=lambda item: item[1], reverse=True))




with open("lesson-6/homework/word_count_report.txt", "w") as output:
    # BONUS     BONUS   BONUS   BONUS   BONUS   BONUS   BONUS j = input()
    j=int(input("Enter number of top most common words to be displayed: "))

    print(f"Total words: {total_words}")
    print(f"Top {j} most common words:")

    output.write(f"Word Count Report\nTotal words: {total_words}\nTop {j} words:\n")
    
    i=0
    for word in sorted_dic:
        print(f"{word} - {word_with_count[word]} times")
        output.write(f"{word} - {word_with_count[word]} times\n")
        i += 1
        if i == j:
            break
    