import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

# https://py4e-data.dr-chuck.net/opengeo?q=Ann+Arbor%2C+MI
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Additional detail for urllib
# http.client.HTTPConnection.debuglevel = 1

# Create or Open an existing Database
conn = sqlite3.connect('opengeo.sqlite')
cur = conn.cursor()


# Create a simple table
cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# Open and read data and retrieve.
fh = open("where.data")
count = 0
nofound = 0

# Loop to each entry
for line in fh:
    if count > 100 :
        print('Retrieved 100 locations, restart to retrieve more')      # Stops retrieving after 100 addresses are retrieved.
        break

    address = line.strip()                                              # Strip end of line.
    print('')
    cur.execute("SELECT geodata FROM Locations WHERE address= ?",       # Checks if the address has already been retrieved.
        (memoryview(address.encode()), ))

    try:
        data = cur.fetchone()[0]                                         # Retrieve records that are already in database.
        print("Found in database", address)
        continue
    except:
        pass
                                                                         # If record is not in database, we create URL
    parms = dict()
    parms['q'] = address

    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)                                            # After creating URL we retrieve the info and read it.
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    count = count + 1

    try:
        js = json.loads(data)                                            # Parse and convert the data from json into python dictionary.
    except:
        print(data)  # We print in case unicode causes an error
        continue

    if not js or 'features' not in js:                                   # This is a sanity check, to see if we are getting real data.
        print('==== Download error ===')
        print(data)
        break

    if len(js['features']) == 0:
        print('==== Object not found ====')
        nofound = nofound + 1
                                                                        # Insert into Database.
    cur.execute('''INSERT INTO Locations (address, geodata)              
        VALUES ( ?, ? )''',
        (memoryview(address.encode()), memoryview(data.encode()) ) )

    conn.commit()                                                       # Commit    

    if count % 10 == 0 :                                                # Retrieve every 5 locations and then pause for 5 seconds.
        print('Pausing for a bit...')
        #time.sleep(5)

if nofound > 0:
    print('Number of features for which the location could not be found:', nofound)

print("Run geodump.py to read the data from the database so you can vizualize it on a map.")

