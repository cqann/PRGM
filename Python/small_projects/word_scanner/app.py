
words_raw = open("svenska.txt", "r")
words = []
for line in words_raw:
    words.append(line[0:-1])


while True:
    print("New query please!")
    query = input()
    length = len(query)
    for word in words:
        if len(word) == length:
            match = True
            for i in range(length):
                if query[i] == "_":
                    continue
                if query[i] != word[i]:
                    match = False
                    break
                
            if match: print(word)
