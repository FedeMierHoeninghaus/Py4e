import re

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "regex_sum_2107779.txt"
try:
    fh = open(fname)
except:
    quit()
total = 0
for line in fh:
    line.rsplit()
    # print(line)
    numbers = re.findall('[0-9]+', line)
    # print(numbers)
    for number in numbers:
        total += int(number)
print(total)
