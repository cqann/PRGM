import re

file = open("Day14.txt","r")
rec_list = [line[:-1] for line in file]
rec = {}
vals = {}
for r in rec_list:
    cur = r.split(" => ")
    rec[re.findall(r"[A-Z]+\Z",cur[1])[0]] = re.findall(r"\A\d+",cur[1]) + cur[0].split(", ")
    for comp in cur[0].split(", "):
        k = re.findall(r"[A-Z]+\Z",comp)[0]
        if k not in vals:
            vals[k] = 0
print(rec)
print(vals["ORE"])

def calc(key):
    pass






