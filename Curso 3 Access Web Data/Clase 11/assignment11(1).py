import re

filehandle = open("regex_sum_1095703.txt")
x=list()
for line in filehandle:
     y = re.findall('[0-9]+',line)
     x = x+y

sum=0
for z in x:
    sum = sum + int(z)

print(sum)
