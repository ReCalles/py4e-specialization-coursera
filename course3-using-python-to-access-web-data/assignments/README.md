# Course 3: Using Python to Access Web Data - Assignments

This folder contains my solutions to the programming assignments for "Course 3: Using Python to Access Web Data" from the Python for Everybody Specialization. The assignments here focus on network programming, regular expressions, and working with web data formats like XML and JSON, often interacting with web services and APIs.

---

## Assignment Files and Folders Overview:

This directory contains both individual Python script files and dedicated subfolders for more complex or multi-file assignments. Each entry describes its purpose and the typical input/output.

* ### `assignment_11_ext_dat_with_reg_exp/` (Folder)
    * **Purpose:** This subfolder contains the assignment(s) focused on using **Regular Expressions** (`re` module) to search for and extract specific patterns (e.g., numbers) from text, often from a file.
    * **Typical Content:** Likely includes the main Python script (`.py`) for the solution and an input text file (e.g., `regex_sum_XXXXXX.txt`).

* ### `assignment_12_1_understanding_request_response_cycle.py`
    * **Purpose:** This assignment introduces basic network programming, often involving direct socket connections or the `urllib` library to fetch data from a URL and observe the HTTP request/response cycle.
    * **Input/Output:** Typically takes a URL as input (or has it hardcoded) and prints the retrieved web page content or HTTP headers to the console.

* ### `assignment_12_2_scraping_html_data_with_beautifulsoup/` (Folder)
    * **Purpose:** This subfolder contains the assignment(s) that use the **BeautifulSoup** library to parse HTML content retrieved from a web page and extract specific data (e.g., links, numbers from tables, etc.).
    * **Typical Content:** Includes the main Python script (`.py`), and might involve a local HTML file for testing, or rely on fetching data from a given URL.

* ### `assignment_12_3_following_links_in_python.py`
    * **Purpose:** This assignment builds on web data retrieval, typically involving repeatedly fetching web pages and following links (e.g., finding the Nth link on a page, then repeating for M times).
    * **Input/Output:** Takes an initial URL and parameters (like position and count) as input, and prints the URLs or final data found after following the link chain.

* ### `assignment_13_1_extracting_data_from_XML.py`
    * **Purpose:** This assignment focuses on parsing **XML (Extensible Markup Language)** data using Python's `xml.etree.ElementTree` module to navigate the XML tree and extract specific information.
    * **Input/Output:** May read XML data from a URL or a local XML file (e.g., `comments_XXXX.xml`), and prints extracted values (e.g., names, counts).

* ### `assignment_13_2_extracting_data_from_JSON.py`
    * **Purpose:** This assignment focuses on parsing **JSON (JavaScript Object Notation)** data using Python's `json` module, which is a common format for web APIs.
    * **Input/Output:** May read JSON data from a URL or a local JSON file (e.g., `comments_XXXX.json`), and prints extracted values.

* ### `assignment_13_3_calling_a_JSON_API.py`
    * **Purpose:** This assignment demonstrates how to interact with **JSON-based Web APIs**, often involving constructing a URL with parameters, making an HTTP request, and processing the JSON response.
    * **Input/Output:** Takes input (e.g., a location for a geocoding API, or search terms for another API), makes an API call, and prints relevant data extracted from the JSON response.

---

## How to Run These Assignments:

To run any of these Python assignments:

1.  **Open your terminal or command prompt.**
2.  **Navigate to the appropriate directory:**
    * If it's a direct `.py` file: `cd "path/to/course3-using-python-to-access-web-data/assignments"`
    * If it's a subfolder: `cd "path/to/course3-using-python-to-access-web-data/assignments/assignment_XX_X_name"`
3.  **Ensure input data or internet access:**
    * For assignments reading local files, ensure those files are in the correct directory.
    * For assignments accessing web data, ensure you have an active internet connection.
    * If an assignment uses an API, make sure any required API keys are handled securely (e.g., via environment variables, not directly in code for public repos).
4.  **Execute the script:**
    ```bash
    python <assignment_file_name>.py
    # Example: python assignment_12_1_understanding_request_response_cycle.py
    ```
5.  **Follow the prompts:** Scripts will take inputs (e.g., URLs, search terms) and print their output or results directly to the terminal. Some may generate local files (e.g., HTML, JSON) for further inspection.

---

## Note on Resources:

If you have a top-level `resources/` folder (within your `course3-using-python-to-access-web-data/` directory), it may contain additional resources, cheat sheets (e.g., for regex, HTTP status codes), or templates relevant to these assignments.