# 8.4 Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split() method.
# The program should build a list of words. For each word on each line check to see
# if the word is already in the list and if not append it to the list. When the program completes,
# sort and print the resulting words in python sort() order as shown in the desired output.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt


fname = input("Enter file name: ")  #This is just to store the file name


try:
    fh = open(fname)                 # This is the handle we are manipulating
except:
    print("The file", fname, "cannot be opened")
    quit()

lst = list()                         # list for the desired output
for line in fh:                      # to read every line of file romeo.txt
    #line = print(line.rstrip())
    line = line.rstrip()             # to eliminate the unwanted blanks
    #line = print(line.split())
    line = line.split()              # turn the line into a list of words
    for words in line:               # check every element in the lines
        if words not in lst:         # check if the element not in the list
            lst.append(words)        # append

lst.sort()                         # sort the list (de-indent indicates that you sort when the loop ends)
print(lst)                         # print the list of words splitted