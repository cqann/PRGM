
words_raw = open("svenska.txt", "r")
words = []
for line in words_raw:
    words.append(line[0:-1])


for word in words:
    if "v" in word and "m" in word and "i" in word and len(word) < 7:
        print(word)