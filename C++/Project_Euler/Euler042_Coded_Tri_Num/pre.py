
inpt = open("words.txt","r")
write_to = open("formatted.txt","w")
arr = []
for line in inpt:
    arr.append(line)

text = arr[0]
words = text.split("\",\"")
words[0] = words[0][1:]
words[-1] = words[-1][:-1]

for word in words:
    write_to.write(word + "\n")

inpt.close()
write_to.close()