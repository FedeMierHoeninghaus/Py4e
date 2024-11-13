name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
arr = []
hours = dict()
sorted_hours = list()
for line in handle:
    if line.startswith('From '):
        arr = line.split()
        times = arr[5]
        hour = times.split(":")[0]
        hours[hour] = hours.get(hour, 0) + 1
for k, v in hours.items():
    sorted_hours.append((k, v))
sorted_hours.sort()

for hour, count in sorted_hours:
    print(hour, count)
