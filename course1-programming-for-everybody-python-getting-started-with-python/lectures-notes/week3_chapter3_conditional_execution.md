# Chapter 3: Conditional Execution

* **Boolean Expressions:** Expressions that evaluate to `True` or `False`.
* **Comparison Operators:**
    * `==` (equal to)
    * `!=` (not equal to)
    * `<` (less than)
    * `>` (greater than)
    * `<=` (less than or equal to)
    * `>=` (greater than or equal to)
* **Conditional Statements:**
    * **`if` statement:** Executes code block only if a condition is `True`.
        ```python
        if x > 0:
            print("Positive")
        ```
    * **`if/else` statement:** Executes one block if `True`, another if `False`.
        ```python
        if x % 2 == 0:
            print("Even")
        else:
            print("Odd")
        ```
    * **`if/elif/else` (Multi-way):** Checks multiple conditions sequentially.
        ```python
        if x > 0:
            print("Positive")
        elif x < 0:
            print("Negative")
        else:
            print("Zero")
        ```
* **Indentation:** Python uses indentation (spaces/tabs) to define code blocks. This is critical!
* **`try`/`except` for Error Handling:** Gracefully handles errors (like `ValueError` when converting non-numeric input).
    ```python
    try:
        num = int(input("Enter a number: "))
    except:
        print("Invalid input")
    ```