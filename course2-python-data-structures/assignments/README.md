# Course 2: Python Data Structures - Assignments

This folder contains my solutions to the programming assignments for "Course 2: Python Data Structures" from the Python for Everybody Specialization. Each Python script (`.py` file) here demonstrates concepts related to files, lists, dictionaries, and tuples.

---

## Assignment Files Overview:

These Python files cover core concepts from chapters focusing on Python's built-in data structures and file handling. Assignments typically involve reading data from files, processing it using lists and dictionaries, and displaying results.

* ### `assignment_6_5.py`
    * **Purpose:** This assignment typically involves string manipulation, likely extracting a specific number from a line of text (e.g., finding and converting a floating-point number from a string, often from a line in a file).
    * **Input/Output:** May take a file as input (or a string from the user) and prints a processed numeric result.

* ### `assignment_7_1.py`
    * **Purpose:** Commonly focuses on reading and processing text files, such as converting text to uppercase or counting lines.
    * **Input/Output:** Takes a text file (e.g., `words.txt` or `mbox.txt`) as input and prints processed output to the console.

* ### `assignment_7_2.py`
    * **Purpose:** Frequently involves reading through a file and extracting specific numerical data, like finding numbers in lines and performing calculations (e.g., summing `X-DSPAM-Confidence:` values from `mbox.txt`).
    * **Input/Output:** Reads data from a text file (e.g., `mbox.txt`) and prints calculated statistics (e.g., average).

* ### `assignment_8_4.py`
    * **Purpose:** Often involves reading a text file, splitting lines into words, and building a unique sorted list of words.
    * **Input/Output:** Takes a text file (e.g., `romeo.txt`) as input and prints a sorted list of unique words.

* ### `assignment_8_5.py`
    * **Purpose:** Typically focuses on processing lines from a file using lists, often involving filtering lines and extracting specific data elements (e.g., extracting "From" lines from `mbox.txt` and printing the second word).
    * **Input/Output:** Reads from a text file (e.g., `mbox.txt`) and prints specific extracted words or phrases.

* ### `assignment_9_4.py`
    * **Purpose:** Commonly uses dictionaries to count the frequency of items, such as counting email sender addresses from a file.
    * **Input/Output:** Reads from a text file (e.g., `mbox.txt`), uses a dictionary to store counts, and prints the most common email sender.

* ### `assignment_10_2.py`
    * **Purpose:** Often involves more advanced dictionary and tuple usage, such as counting messages by hour of the day or building a sorted list of common words and their counts.
    * **Input/Output:** Reads from a text file (e.g., `mbox.txt`), uses dictionaries for counting, and often involves sorting results using lists of tuples before printing.

---

## How to Run These Assignments:

To run any of these Python assignments:

1.  **Open your terminal or command prompt.**
2.  **Navigate to this `assignments/` folder:**
    ```bash
    cd "path/to/your/course2-python-data-structures/assignments"
    ```
    (Replace with your actual path).
3.  **Ensure input data files are present:** For assignments that read from files (e.g., `mbox.txt`, `romeo.txt`), make sure these files are either in this `assignments/` directory or in your `data/` folder in the course root, and the script's `open()` call uses the correct path.
4.  **Execute the desired script:**
    ```bash
    python <assignment_file_name>.py
    # Example: python assignment_7_2.py
    ```
5.  **Follow the prompts:** Scripts will take file names as input or simply print their output directly to the terminal.