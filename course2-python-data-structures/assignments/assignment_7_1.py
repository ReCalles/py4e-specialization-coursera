# 7.1 Write a program that prompts for a file name, then opens that file
# and reads through the file, and print the contents of the file in upper case.
# Use the file words.txt to produce the output below.
# You can download the sample data at http://www.py4e.com/code3/words.txt

# Use words.txt as the file name
fname = input("Enter file name: ")  # This is just to store file name

try:
    fh = open(fname)  # This is the handle we are manipulating
except:
    print('The file', fname, 'cannot be opened')
    quit()

file_read = fh.read()
inp = file_read.rstrip()
print(inp.upper())

