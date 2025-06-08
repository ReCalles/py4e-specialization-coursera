# Chapter 9: Dictionaries

* **Dictionaries:** Unordered collections of key-value pairs. Keys must be unique and immutable (e.g., strings, numbers, tuples). Values can be any data type.
* **Creating Dictionaries:**
    * `my_dict = {}` (empty dictionary)
    * `counts = {'apple': 3, 'banana': 2}`
* **Accessing Values:**
    * `counts['apple']` (returns 3)
    * **Error if key not found:** `counts['orange']` would raise a `KeyError`.
* **Adding/Modifying Pairs:**
    * `counts['orange'] = 1` (adds new pair)
    * `counts['apple'] = 5` (updates existing value)
* **`in` Operator:** Checks if a key exists in the dictionary.
    * `'apple' in counts` (True)
* **`get()` Method:** Safely retrieves a value by key; returns a default value if key not found (avoids `KeyError`).
    * `counts.get('apple', 0)` (returns 5)
    * `counts.get('grape', 0)` (returns 0)
* **Looping Through Dictionaries:**
    * `for key in my_dict:`: Iterates through keys.
    * `my_dict.keys()`: Returns a view of all keys.
    * `my_dict.values()`: Returns a view of all values.
    * `my_dict.items()`: Returns a view of key-value pairs as tuples.
        ```python
        for key, value in my_dict.items():
            print(key, value)
        ```
* **Counting Pattern (Histograms):** Common use case for dictionaries to count occurrences of items.
    ```python
    word_counts = {}
    words = ['apple', 'banana', 'apple', 'orange']
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    # word_counts will be {'apple': 2, 'banana': 1, 'orange': 1}
    ```
* **Dictionaries vs. Lists:**
    * Lists are ordered by index, good for sequences.
    * Dictionaries are unordered (in older Pythons, now insertion-ordered), good for lookup by key.