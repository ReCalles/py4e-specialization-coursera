# Extracting Data from JSON

# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. 
# The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract 
# the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing 
# and the other is the actual data you need to process for the assignment.

#       Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
#       Actual data: http://py4e-data.dr-chuck.net/comments_1865555.json (Sum ends with 90)
# You do not need to save these files to your folder since your program will read the data directly from 
# the URL. Note: Each student will have a distinct data url for the assignment - so only use your own 
# data url for analysis.

# Data Format
# The data consists of a number of names and comment counts in JSON as follows:
# {
#   comments: [
#     {
#       name: "Matthias"
#       count: 97
#     },
#     {
#       name: "Geomer"
#       count: 97
#     }
#     ...
#   ]

# The closest sample code that shows how to parse JSON and extract a list is json2.py. You might also want 
# to look at xml3.py to see how to prompt for a URL and retrieve data from a URL.

# Sample Execution
#   $ python3 solution.py
#   Enter location: http://py4e-data.dr-chuck.net/comments_42.json
#   Retrieving http://py4e-data.dr-chuck.net/comments_42.json
#   Retrieved 2733 characters
#   Count: 50
#   Sum: 2...


# Input the URL
import urllib.request, urllib.parse, urllib.error
import json, ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

location = input("Enter location: ")
if len(location) < 1:                             # This condition checks if the user did not enter any URL name. If the user did not provide a URL name, it sets the url_name variable to "http://py4e-data.dr-chuck.net/comments_1865555.json" as a default URL name.
        location= "http://py4e-data.dr-chuck.net/comments_1865555.json"


# Function to read the URL data, parse, and extract data.
def read_url(location):
    print ("Retrieving ", location)
    uh = urllib.request.urlopen(location, context=ctx)         # Open the URL provided.
    data = uh.read().decode()                                  # Read line of JSON file and decode the Data into string.
    print("Retrieved ", len(data), "characters")    

    try: 
        js = json.loads(data)                                  # Parse and deserialize a JSON string to turn it into a python data structure.

    except:
        js = None 

    # Error handling
    if not js or "comments" not in js:
        print("====== Download Error ======")
        print(data)
        quit()
    if len(js["comments"]) == 0:
        print("====== Object Not Found =======")
        print(data)
        quit()
    

    # Extracting comments count and calculate the sum.
    comments = js["comments"]                                # Accessing the "Comment" Dictionary variable.
    sum_of_counts = 0
    count_comments = len(comments)                           # Doing the sum of all the comment dictionaries.

    for comment in comments:                                 # Iterating through comments list and sum the "count" values.
         sum_of_counts += comment["count"]

    print("Count: ", count_comments)
    print("Sum: ", sum_of_counts)
   

read_url(location)
