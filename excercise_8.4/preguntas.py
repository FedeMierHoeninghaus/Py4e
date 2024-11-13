name = input("Enter file:")
handle = open(name)
emails = dict()
max_emails_sent = None
max_email_address = None
for line in handle:
    line.strip()
    if line.startswith("From "):
        arr = line.split()
        email_address = arr[1]
        emails[email_address] = emails.get(email_address, 0) + 1
    # print(emails)

for email, count in emails.items():
    if max_emails_sent is None or count > max_emails_sent:
        max_email_address = email
        max_emails_sent = count

print(max_email_address, max_emails_sent)

