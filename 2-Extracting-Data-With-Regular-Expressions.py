import re
fh = open('py4e-data.dr-chuck.netregex_sum_1858583.txt')
sum=0
for line in fh: 
    line =line.rstrip()
    y = re.findall('[0-9]+',line)
    for astring in y:
        x = int(astring)
        sum = sum + x
print(sum)