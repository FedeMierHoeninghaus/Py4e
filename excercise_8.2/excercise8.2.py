fname = input("Enter file name: ")

lst = list()
try:
    fh = open(fname)
except:
    quit()
for line in fh:
    words_list = line.rstrip().split()
    for word in words_list:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)
