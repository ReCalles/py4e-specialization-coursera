# Calling a JSON API
# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/opengeo.py. 
# The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse 
# that data, and retrieve the first plus_code from the JSON. An Open Location Code is a textual identifier 
# that is another form of address based on the location of the address.

# API End Points
# To complete this assignment, you should use this API endpoint that has a static subset of the Open Street 
# Map Data.
#     http://py4e-data.dr-chuck.net/opengeo?

# This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters,
# you get "No address..." response.
# To call the API, you need to provide the address that you are requesting as the q= parameter that is properly
# URL encoded using the urllib.parse.urlencode() function as shown in http://www.py4e.com/code3/opengeo.py

# Test Data / Sample Execution
# You can test to see if your program is working with a location of "South Federal University" which will 
# have a plus_code of "6FV8QPRJ+VQ".

#     $ python solution.py
#     Enter location: South Federal University
#     Retrieving http://...
#     Retrieved 1290 characters
#     Plus code 6FV8QPRJ+VQ

# Turn In
# Please run your program to find the plus_code for this location:
#     Hanoi University of Science and Technology
# Make sure to enter the name and case exactly as above and enter the plus_code and your Python code below. 
# Hint: The first five characters of the plus_code are "7PH72 ..."
# Make sure to retrieve the data from the URL specified above and not the normal Google API. 
# Your program should work with the Google API - but the plus_code may not match for this assignment.

import urllib.request, urllib.parse
import json, ssl

# Heavily rate limited proxy of https://www.geoapify.com/ api
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# Prompt for location.
address = input('Enter location: ')
if len(address) < 1: 
    address = "Hanoi University of Science and Technology"

address = address.strip()
parms = dict()
parms['q'] = address

url = serviceurl + urllib.parse.urlencode(parms)


# Contact the web service and retrieve JSON.
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)                 # Open the URL provided.
data = uh.read().decode()                                     # Read line of JSON file and decode the Data into string.
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)                                     # Parse and deserialize a JSON string to turn it into a python data structure.
    # Debugging Purposes for the Error Handling.
    # print(json.dumps(js, indent=4))                         # Print the parsed JSON with formatting
    
except json.JSONDecodeError as e:
    print("Failed to parse JSON:", e)
    js = None
        


# Error Handling
if not js or 'features' not in js or 'plus_code' not in js['features'][0]['properties']:
    print('==== plus_code not found ====')
    print(json.dumps(js, indent=4))                         # More informative debugging output
    quit()

# If plus_code exists, extract it
plus_code = js['features'][0]['properties']['plus_code']

# Additional check if the plus_code is empty
if len(plus_code) == 0:
    print('==== Object not found ====')
    print(json.dumps(js, indent=4))                        # More informative debugging output
    quit()

# plus_code = js['features'][0]['properties']['lat']
    
print("Plus code ", plus_code)



