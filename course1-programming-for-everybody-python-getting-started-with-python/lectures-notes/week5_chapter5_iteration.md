# Chapter 5: Iteration (Loops)

* **Loops:** Structures that repeat a set of instructions multiple times.
* **`while` Loop:** Repeats as long as a condition is `True`.
    ```python
    n = 5
    while n > 0:
        print(n)
        n = n - 1 # Crucial to change the condition
    print("Blastoff!")
    ```
* **Infinite Loops:** Occur if the loop condition never becomes `False`.
* **`break` Statement:** Immediately exits the current loop.
    ```python
    while True: # Infinite loop
        line = input('> ')
        if line == 'done':
            break # Exit loop if 'done'
        print(line)
    ```
* **`continue` Statement:** Skips the rest of the current loop iteration and moves to the next.
    ```python
    while True:
        line = input('> ')
        if line[0] == '#':
            continue # Skip lines starting with #
        if line == 'done':
            break
        print(line)
    ```
* **Common Loop Patterns:**
    * **Counting:** Initialize count to 0, increment inside loop.
    * **Summing:** Initialize total to 0, add to total inside loop.
    * **Averaging:** Sum and count, then divide.
    * **Finding Min/Max:** Initialize with a sentinel value or the first item, update inside loop.