import sqlite3
import json
import codecs

conn = sqlite3.connect('opengeo.sqlite')                         # Opens Database.
cur = conn.cursor()

cur.execute('SELECT * FROM Locations')                           # Reads data file and write the "where.js" file
fhand = codecs.open('where.js', 'w', "utf-8")
fhand.write("myData = [\n")
count = 0


for row in cur :                                                 # Reads every row of the js file and looks for specific
    data = str(row[1].decode())                                  # features or attributes inside the file that are stored in some variables.
    try: js = json.loads(str(data))
    except: continue

    if len(js['features']) == 0: continue

    try:                                                          # Retrieve the lat, lng and place stored in variables.
        lat = js['features'][0]['geometry']['coordinates'][1]
        lng = js['features'][0]['geometry']['coordinates'][0]
        where = js['features'][0]['properties']['display_name']
        where = where.replace("'", "")
    except:
        print('Unexpected format')
        print(js)

    try :
        print(where, lat, lng)                                    # Prints the results.

        count = count + 1
        if count > 1 : fhand.write(",\n")
        output = "["+str(lat)+","+str(lng)+", '"+where+"']"
        fhand.write(output)                                       # Writes the results in where.js file.
    except:
        continue

fhand.write("\n];\n")
cur.close()
fhand.close()
print(count, "records written to where.js")
print("Open where.html to view the data in a browser")

