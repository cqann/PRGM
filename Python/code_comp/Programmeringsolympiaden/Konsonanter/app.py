
linput = list(inpt)
length = len(inpt)
consonants = "bcdfghjklmnpqrstvwxz"
to_delete_list = []

past = ""
last = ""

for i in range(len(linput)):

    if linput[i] == last and last == past and linput[i] in consonants:
        to_delete_list.append(i)

    past = last 
    last = linput[i]

del_count = len(to_delete_list)

for index in to_delete_list:
    linput[index] = 0

for i in range(del_count):
    linput.remove(0)

print("".join(linput))
    