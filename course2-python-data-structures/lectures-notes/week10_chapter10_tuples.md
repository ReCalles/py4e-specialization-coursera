# Chapter 10: Tuples

* **Tuples:** Ordered, **unchangeable (immutable)** sequences of elements. Like lists, but cannot be modified after creation.
* **Creating Tuples:**
    * `my_tuple = ()` (empty tuple)
    * `coordinates = (10.0, 20.0)`
    * `single_item_tuple = (5,)` (comma required for single-item tuple to distinguish from an expression in parentheses)
* **Accessing Elements:**
    * **Indexing:** `coordinates[0]`
    * **Slicing:** `coordinates[0:1]`
* **Immutability:**
    * Cannot `append()`, `insert()`, `remove()`, `sort()`, or change elements. Trying to will raise a `TypeError`.
* **Why use Tuples?**
    * **Performance:** Slightly more efficient for iteration than lists.
    * **Safety:** Guarantees that the data won't be accidentally changed.
    * **Function Return Values:** Functions often return multiple values as a tuple.
    * **Dictionary Keys:** Because they are immutable, tuples *can* be used as dictionary keys (unlike lists).
* **Tuple Assignment / Multiple Assignment:** Assign multiple variables at once.
    ```python
    (x, y) = (5, 10) # x is 5, y is 10
    a, b = b, a       # Swaps values of a and b efficiently
    ```
* **Tuples and Dictionaries:**
    * `dict.items()` method returns a list of (key, value) tuples.
    * This is very useful for sorting dictionary content.
* **Sorting Lists of Tuples:**
    * You can sort a list of tuples, and Python will sort by the first element, then the second, and so on.
    ```python
    d = {'a': 10, 'b': 1, 'c': 22}
    t = d.items() # t is now [('a', 10), ('b', 1), ('c', 22)] - order might vary
    sorted_items = sorted(t) # sorted_items will be [('a', 10), ('b', 1), ('c', 22)]
    # To sort by value:
    sorted_by_value = sorted(d.items(), key=lambda item: item[1])
    # sorted_by_value will be [('b', 1), ('a', 10), ('c', 22)]
    ```