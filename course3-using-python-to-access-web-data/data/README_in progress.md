# Data Files for Web Data Access Assignments

This folder contains local data files (e.g., text, XML, JSON) that are used by various Python assignments throughout the "Using Python to Access Web Data" course. While many assignments in this course involve fetching data directly from web URLs, some exercises may require local files for testing or specific scenarios.

---

## Data File Usage:

Below is a list of common data files (or types of files) used in this course and the assignments/scripts that might utilize them.

### `regex_sum_42.txt` and `regex_sum_38794.txt`

* **Description:** A text file typically containing lines of text with numbers embedded within them.
* **Used for:** `assignment_11_1_regex_sum.py` (Assignments involving extracting and summing numbers using regular expressions).

### `comments_XXXXXXXX.xml` (or similar XML data file)

* **Description:** An XML structured file often containing comment data or similar hierarchical information.
* **Used for:**
    * `assignment_13_1_xml_parsing.py` (Assignments involving parsing XML documents).
    * `scripts/xml_parser_demo.py` (For testing XML parsing logic).

### `comments_XXXXXXXX.json` (or similar JSON data file)

* **Description:** A JSON structured file, often containing comment data, place data, or similar key-value structured information.
* **Used for:**
    * `assignment_13_2_json_parsing.py` (Assignments involving parsing JSON data).
    * `scripts/json_parser_demo.py` (For testing JSON parsing logic).

### `sample_html_page.html` (or `page1.html` etc.)

* **Description:** A simple HTML file that might be used for local testing of basic web page retrieval and parsing without needing a live internet connection.
* **Used for:** `scripts/simple_http_get.py` (For local testing of HTTP requests or basic string parsing of HTML).

---

## How to Use These Files:

For your Python scripts to access these data files correctly, ensure one of the following:

1.  **Place the data file in the same directory as the Python script** that will be reading it.
2.  **Provide the correct relative or absolute path** to the data file when opening it within your Python script (e.g., `open('data/comments_XXXX.xml')` if your script is in a parent directory relative to the `data` folder).
3.  **For web-based assignments**, the script itself will often fetch the data from a provided URL, so these local files are primarily for testing or specific offline scenarios.

It is recommended to keep these data files within this `data/` folder for consistent organization.