# Chapter 7: Files

* **File Handle:** An object that allows you to read from or write to a file.
* **Newline Character (`\n`):** Represents the end of a line in a text file. `print()` adds one by default.
* **Opening Files:**
    * `open(filename, mode)`: Returns a file handle.
    * `mode='r'` (read - default), `'w'` (write - truncates/creates), `'a'` (append - adds to end).
* **Reading Files:**
    * `handle = open('filename.txt', 'r')`
    * `handle.read()`: Reads entire file into a single string.
    * `for line in handle:`: Iterates through file line by line (common pattern).
    * `line.rstrip()`: Removes whitespace (including newline) from the right end of a string.
* **Searching in Files:**
    * Use `if` statements with string methods (`startswith()`, `find()`, `in`) within a file loop.
* **Writing Files:**
    * `handle = open('output.txt', 'w')`
    * `handle.write(string)`: Writes the string to the file. Remember to add `\n` for new lines.
* **Closing Files:**
    * `handle.close()`: Important to save changes and release file resources. Often handled automatically by `with open(...) as handle:`.
* **Handling File Not Found Errors:**
    * Use `try` and `except` blocks for robustness.
    ```python
    fname = input('Enter the file name: ')
    try:
        fhand = open(fname)
    except:
        print('File cannot be opened:', fname)
        quit()
    ```