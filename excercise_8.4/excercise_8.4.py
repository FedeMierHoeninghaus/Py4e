fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
count = 0
for lines in fh:
    line = lines.rstrip()
    if line.startswith("From "):
        new_line = line.split()
        print(new_line[1])
        count += 1

print("There were", count, "lines in the file with From as the first word")
