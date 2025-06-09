# 9.4 Write a program to read through the mbox-short.txt and
# figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person
# who sent the mail. The program creates a Python dictionary that maps the sender's mail address
# to a count of the number of times they appear in the file. After the dictionary is produced,
# the program reads through the dictionary using a maximum loop to find the most prolific committer.


# Step 1: prompt the file name and open the file
name = input("Enter file:")

try:
    if len(name) < 1:                             # This condition checks if the user did not enter any file name. If the user did not provide a file name, it sets the name variable to "mbox-short.txt" as a default file name.
        name = "mbox-short.txt"
    handle = open(name)
except:
    print("The file", name, "doesn't exist, try another file name")
    quit()

# Step 2: Extract email addresses and create a list
emails = dict()
for line in handle:
    if line.startswith("From "):
        words = line.rstrip().split()
        email = words[1]
        emails[email] = emails.get(email, 0) + 1  # Here we are creating a dictionary  with its key, of the emails in the file and counting them, if the email wasn't present before we store it and create the first instance of the count.

# Step 3: Find the mail address with most instances
max_email = None
max_count = None
for email, count in emails.items():               # The items function return a list of Keys and their values
    if max_count is None or count > max_count:
        max_count = count
        max_email = email

print (max_email, max_count )