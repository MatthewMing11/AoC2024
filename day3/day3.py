# Python script for day 3
import re
file = open('input.txt','r')
total=0
for line in file:
    ops=re.findall(r'mul\([0-9]+?,[0-9]+?\)',line)
    for op in ops:
        i=op.index(',')
        total+=int(op[4:i])*int(op[i+1:len(op)-1])
print(total)
#part 2 (too high for some reason)
file = open('input.txt','r')
total=0
enable=True
for line in file:
    ops=re.findall(r"mul\([0-9]+?,[0-9]+?\)|do\(\)|don't\(\)",line)
    for op in ops:
        if op == "don't()":
            enable=False
        elif op == "do()":
            enable=True
        else:
            if enable:
                i=op.index(',')
                total+=int(op[4:i])*int(op[i+1:len(op)-1])
print(total)
