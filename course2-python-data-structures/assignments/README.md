# Data Files for Assignments

This folder contains the necessary text files and other data inputs used by various Python assignments throughout the "Python Data Structures" course. These files are typically read by your Python scripts to perform operations like parsing, counting, and data analysis.

---

## Data File Usage:

Below is a list of the data files included in this directory and the specific assignments or exercises that utilize them.

### `words.txt`

* Used for: `assignment_7_1.py` (Commonly for reading words, counting etc.)

### `mbox-short.txt`

* Used for the following assignments, often for email parsing and data extraction:
    * `assignment_7_2.py`
    * `assignment_8_5.py`
    * `assignment_9_4.py`
    * `assignment_10_2.py`

### `romeo.txt`

* Used for: `assignment_8_4.py` (Frequently used for word counting with lists or dictionaries.)

---

## How to Use These Files:

For your Python scripts to access these data files correctly, ensure one of the following:

1.  **Place the data file in the same directory as the Python script** that will be reading it.
2.  **Provide the correct relative or absolute path** to the data file when opening it within your Python script (e.g., `open('data/mbox-short.txt')` if your script is in a parent directory relative to the `data` folder).

It is recommended to keep these data files within this `data/` folder for consistent organization.