# Chapter 8: Lists

* **Lists:** Ordered, changeable (mutable) sequences of elements. Can hold items of different types.
* **Creating Lists:**
    * `my_list = []` (empty list)
    * `numbers = [10, 20, 30]`
    * `mixed = [1, 'hello', 3.14]`
* **Accessing Elements:**
    * **Indexing:** `my_list[0]` (first item), `my_list[-1]` (last item).
    * **Slicing:** `my_list[1:3]` (from index 1 up to but not including 3).
* **Mutability:** Lists can be changed after creation.
    * `numbers[0] = 5`
* **List Methods:**
    * `list.append(item)`: Adds item to the end.
    * `list.extend(another_list)`: Appends elements from another list.
    * `list.sort()`: Sorts the list in place (modifies the original list).
    * `list.pop(index)`: Removes and returns item at given index (defaults to last).
    * `list.remove(value)`: Removes the first occurrence of a specific value.
    * `list.insert(index, item)`: Inserts item at a specific index.
    * `list.count(item)`: Returns number of occurrences.
    * `list.index(item)`: Returns index of first occurrence.
* **List Concatenation:** `list1 + list2` creates a new combined list.
* **Looping through Lists:**
    * `for item in my_list:` (iterates through values)
    * `for i in range(len(my_list)):` (iterates through indices)
* **Building Lists:**
    * Start with empty list `[]` and `append()` items in a loop.
* **Strings and Lists:**
    * `string.split(delimiter)`: Splits a string into a list of substrings. (Default delimiter is whitespace).
    * `delimiter.join(list_of_strings)`: Joins elements of a list into a single string.
* **List Aliasing:** When one list variable is assigned to another, they both refer to the *same* list object. Be careful with modifications!
    ```python
    a = [1, 2, 3]
    b = a # b now refers to the same list as a
    b[0] = 99
    print(a) # Output: [99, 2, 3]
    ```