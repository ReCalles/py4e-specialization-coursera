# 10.2 Write a program to read through the mbox-short.txt and figure out the
# distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the
# string a second time using a colon.

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

# Step 1: prompt the file name and open the file.
name = input("Enter file:")

try:
    if len(name) < 1:                             # This condition checks if the user did not enter any file name. If the user did not provide a file name, it sets the name variable to "mbox-short.txt" as a default file name.
        name = "mbox-short.txt"
    handle = open(name)
except:
    print("The file", name, "doesn't exist, try another file name")
    quit()

# Step 2: Extract the hour of the day and create ........... dict with hours as keys and their counts.
hours = dict()
for line in handle:
    if line.startswith("From "):
        words = line.rstrip().split()
        date = words[5]
        hour = date[:2]
        hours[hour] = hours.get(hour,0) + 1       # Here we are creating  the dictionary Keys of the emails in the file and counting them, if the email wasn't present before we store it and create the first instance of the count.

for k, v in sorted(hours.items()):
    print (k,v)