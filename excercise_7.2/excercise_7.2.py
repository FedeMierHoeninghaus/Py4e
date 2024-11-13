# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    quit()
count = 0
total_numbers = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    new_line = line[19:]
    numbers = float(new_line)
    total_numbers += numbers
    count += 1
    average = total_numbers / count
print("Average spam confidence:", average)
