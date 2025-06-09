# Data Files for Web Data Access Assignments

This folder contains local data files (e.g., text, XML, JSON) that are used by various Python assignments throughout the "Using Python to Access Web Data" course. While many assignments in this course involve fetching data directly from web URLs, some exercises may require local files for testing or specific scenarios.

---

## Data File Usage:

Below is a list of common data files (or types of files) used in this course and the assignments/scripts that might utilize them.

### `regex_sum_1865550.txt`

* **Description:** A text file typically containing lines of text.
* **Used for:**
    * `assignment_11_ext_dat_with_reg_exp.py` (Assignments involving extracting and summing numbers).
    * `assignment_12_2_scraping_html_data_with_beautifulsoup.py` (Assignments involving extracting and summing numbers).
    
### `regex_sum_42.txt`

* **Description:** A text file typically containing lines of text.
* **Used for:**
    * `assignment_12_2_scraping_html_data_with_beautifulsoup.py`(Assignments involving extracting and summing numbers).

### `bs4.zip`
* **Description:** A zip file containing beautiful soup code used as reference on the mentioned assignment. This python library Beautiful Soup is a Python library is primarily used for web scraping. It's designed to make it easy to extract data from HTML and XML documents.
* **Used for:**
   * `assignment_12_2_scraping_html_data_with_beautifulsoup.py` (Assignment involving web scraping. It's designed to make it easy to extract data from HTML and XML documents.).


---

## How to Use These Files:

For your Python scripts to access these data files correctly, ensure one of the following:

1.  **Place the data file in the same directory as the Python script** that will be reading it.
2.  **Provide the correct relative or absolute path** to the data file when opening it within your Python script (e.g., `open('data/regex_sum_#####.txt')` if your script is in a parent directory relative to the `data` folder).
3.  **For web-based assignments**, the script itself will often fetch the data from a provided URL, so these local files are primarily for testing or specific offline scenarios.

It is recommended to keep these data files within this `data/` folder for consistent organization.
