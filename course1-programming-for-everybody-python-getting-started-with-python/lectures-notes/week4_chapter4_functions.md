# Chapter 4: Functions

* **What are Functions?** Reusable blocks of code that perform a specific task. They promote code organization and reduce redundancy.
* **Built-in Functions:** Functions provided by Python (e.g., `print()`, `input()`, `len()`, `type()`, `max()`, `min()`).
* **Defining New Functions:** Use the `def` keyword.
    ```python
    def greet():
        print("Hello!")
    ```
* **Calling Functions:** Execute the function by its name followed by parentheses: `greet()`.
* **Parameters & Arguments:**
    * **Parameters:** Variables listed inside the parentheses in the function definition (e.g., `name` in `def greet(name):`).
    * **Arguments:** Actual values passed to the function when it's called (e.g., `"Chuck"` in `greet("Chuck")`).
* **Return Values:** Functions can send a result back using the `return` statement.
    ```python
    def add(a, b):
        return a + b
    result = add(5, 3) # result will be 8
    ```
* **Void Functions:** Functions that do not explicitly `return` a value (they implicitly return `None`).
* **Function Reuse:** Once defined, a function can be called multiple times.