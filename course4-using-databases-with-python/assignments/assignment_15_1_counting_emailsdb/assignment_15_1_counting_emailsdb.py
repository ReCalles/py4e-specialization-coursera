# This application will read the mailbox data (mbox.txt) and count the number of email messages per 
# organization (i.e. domain name of the email address) using a database with the following schema to maintain the counts.

#     CREATE TABLE Counts (org TEXT, count INTEGER)

# When you have run the program on mbox.txt upload the resulting database file above for grading.
# If you run the program multiple times in testing or with different files, make sure to empty out the data before each run.

# You can use this code as a starting point for your application: http://www.py4e.com/code3/emaildb.py.

# The data file for this application is the same as in previous assignments: http://www.py4e.com/code3/mbox.txt.
# Because the sample code is using an UPDATE statement and committing the results to the database as each record is read in 
# the loop, it might take as long as a few minutes to process all the data. The commit insists on completely writing all the 
# data to disk every time it is called.

# The program can be speeded up greatly by moving the commit operation outside of the loop. In any database program, there is 
# a balance between the number of operations you execute between commits and the importance of not losing the results of 
# operations that have not yet been committed.

import sqlite3

conn = sqlite3.connect('counting_emaildb.sqlite')              # Makes a connection to DB, if not we will create the file.
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')                     # This is checking if there is a table to prevent blowup.

#cur.execute('DELETE FROM Counts')                             # Delete every row inside the table for every time we run the code.

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')     


# Open the File
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)

# Process the File
for line in fh:
    if not line.startswith('From: '): continue                   # Looks only for "From" line start.

    # Extract the domain name from the email address.
    pieces = line.split()
    email = pieces[1]
    org = email.split('@')[1]

    # Check if the domain is already in the database.
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()

    # Insert or update the domain count.
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
# Retrieve and display the top 10 domains
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()