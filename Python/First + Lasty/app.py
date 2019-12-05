import random

result_file = open("result_file.txt","w")


for i in range(10000):
    first_names = open("first_names.txt","r")
    last_names = open("last_names.txt","r")
    result_file.write(first_names.readlines()[random.randint(0,34070)].replace("\n"," ")+ (last_names.readlines()[random.randint(0,999)].lower()).capitalize())
    first_names.close()
    last_names.close()

result_file.close()
