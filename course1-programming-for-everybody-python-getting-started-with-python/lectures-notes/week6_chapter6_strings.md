# Chapter 6: Strings

* **Strings:** Sequences of characters enclosed in single (`' '`) or double (`" "`) quotes.
* **Indexing:** Access individual characters using square brackets `[]` and an integer index (starts at 0).
    * `fruit = 'banana'`
    * `letter = fruit[1]` (`letter` is 'a')
* **`len()` function:** Returns the number of characters in a string.
    * `len(fruit)` is 6.
* **Looping Through Strings:** Use a `for` loop to iterate over each character.
    ```python
    for char in fruit:
        print(char)
    ```
* **String Slicing:** Extract a portion (substring) of a string.
    * `s[start:end]` - `end` is non-inclusive.
    * `s[:end]` - from beginning to `end`.
    * `s[start:]` - from `start` to end.
    * `s[:]` - a copy of the whole string.
    * `fruit[0:5]` is 'banan'.
* **String Concatenation:** Join strings using the `+` operator.
    * `'Hello' + ' ' + 'World'` is `'Hello World'`.
* **`in` Operator:** Check if a substring exists within a string (returns `True`/`False`).
    * `'nan' in fruit` is `True`.
* **String Methods:** Functions that operate on strings.
    * `str.lower()`: Returns a new string in lowercase.
    * `str.upper()`: Returns a new string in uppercase.
    * `str.find(substring)`: Returns the starting index of the first occurrence, or -1 if not found.
    * `str.replace(old, new)`: Returns a new string with replacements.
    * `str.strip()`: Removes whitespace from beginning and end.
    * `str.startswith(prefix)`: Checks if string starts with prefix.
    * `str.endswith(suffix)`: Checks if string ends with suffix.
* **Immutability:** Strings are immutable; string methods return *new* strings, they don't modify the original in place.
* **Parsing Strings:** Extracting specific data from a string (e.g., finding the position of '@' and space in an email address to extract domain).