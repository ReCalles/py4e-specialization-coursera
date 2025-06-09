# In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. 
# The program will use urllib to read the HTML from the data files below, extract the href= values from the anchor tags, 
# scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the 
# process a number of times and report the last name you find.

# We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other 
# is the actual data you need to process for the assignment

#       - Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
#         Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. 
#         The answer is the last name that you retrieve.
#         Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
#         Last name in sequence: Anayah
#       - Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Ceilidh.html
#         Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. 
#         The answer is the last name that you retrieve.
#         Hint: The first character of the name of the last page that you will load is: L

# Strategy
# The web pages tweak the height between the links and hide the page after a few seconds to make it difficult for 
# you to do the assignment without writing a Python program. But frankly with a little effort and patience you can 
# overcome these attempts to make it a little harder to complete the assignment without writing a Python program. 
# But that is not the point. The point is to write a clever Python program to solve the program.

# Sample execution
# Here is a sample execution of a solution:
#       $ python3 solution.py
#       Enter URL: http://py4e-data.dr-chuck.net/known_by_Fikret.html
#       Enter count: 4
#       Enter position: 3
#       Retrieving: http://py4e-data.dr-chuck.net/known_by_Fikret.html
#       Retrieving: http://py4e-data.dr-chuck.net/known_by_Montgomery.html
#       Retrieving: http://py4e-data.dr-chuck.net/known_by_Mhairade.html
#       Retrieving: http://py4e-data.dr-chuck.net/known_by_Butchi.html
#       Retrieving: http://py4e-data.dr-chuck.net/known_by_Anayah.html

# The answer to the assignment for this execution is "Anayah".

import ssl
import re     # Regular expression Library
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Input the URL, count, and position
url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))



# Fetches and returns the HTML content of the given URL.
def get_url_content(url, context):                    
    html = urllib.request.urlopen(url, context=context).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

# Extracts and returns the href values from all anchor tags in the HTML soup.
def extract_href_tags(soup):                         
    hrefs = []
    for tag in soup('a'):
        href = tag.get('href', None)                 # Get the 'href' attribute
        if href is not None:                         # Check if the href attribute exists
            hrefs.append(href)                       # Add the href value to the list
    return hrefs

def extract_and_print_links(url, count, position, ctx):
    for _ in range(count):
        # Get the HTML content
        soup = get_url_content(url, ctx)
        
        # Extract all href values
        href_tags = extract_href_tags(soup)
        

        # # THIS IS JUST FOR DEBUG PURPOSES TO SEE WHICH URL IT FOLLOWS, AND CHECK IF IT WAS CORRECT
        # # Print the URLs up to the specified position
        # print("Links on:", url)
        # for link in href_tags[:position]:  # Slice the list up to the specified position
        #     print(link)
        


        # Get the URL at the specified position (1-based index)
        if position - 1 < len(href_tags):
            current_url = href_tags[position - 1]
            print("Retrieving:", current_url)
            url = current_url  # Update URL for the next iteration
        else:
            print("Position is out of range. No more URLs to follow.")
            break

    
    # After the loop, get the name from the last URL
    final_url = url
    print("\nFinal URL:", final_url)

    # Regular expression to extract the name
    match = re.search(r'known_by_(.*?)\.html', final_url)
    if match:
        name = match.group(1)
        print("Name extracted from the final URL:", name)


# Call the function with the user inputs
extract_and_print_links(url, count, position, ctx)