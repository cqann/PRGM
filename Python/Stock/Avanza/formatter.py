file = open("to_format.txt", "r")
result = open("result.txt", "w")

for line in file:
    if line.strip() != "":
        result.write(line.strip())

file.close()
result.close()