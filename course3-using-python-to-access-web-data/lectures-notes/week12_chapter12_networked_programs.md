# Chapter 12: Networked Programs

* **Network Protocols:** Rules that computers use to communicate (e.g., HTTP for web, TCP for reliable data transfer, IP for addressing).
* **Sockets:** Software endpoints that allow applications to send and receive data across a network. It's like a phone connection for programs.
    * Python's `socket` module allows low-level network programming.
    * Typically involves creating a socket, connecting, sending data (e.g., HTTP GET request), receiving data, and closing.
* **HTTP (HyperText Transfer Protocol):** The protocol for fetching resources from the web.
    * **GET Request:** Most common HTTP method to retrieve a web page or resource.
    * Includes request lines (e.g., `GET /page.html HTTP/1.0`), headers.
    * Response includes status codes (e.g., `200 OK`, `404 Not Found`).
* **`urllib` Library:** Python's standard library for working with URLs. Simplifies web data retrieval compared to raw sockets.
    * `urllib.request.urlopen(url)`: Opens a URL like a file. Returns a file-like object.
    * You can then read from this object (`read()`, iterate line by line).
* **Retrieving Web Pages:**
    ```python
    import urllib.request

    try:
        fhand = urllib.request.urlopen('[http://www.py4e.com/code3/romeo.txt](http://www.py4e.com/code3/romeo.txt)')
        for line in fhand:
            print(line.decode().strip()) # Decode bytes to string
    except urllib.error.URLError as e:
        print(f"Error accessing URL: {e.reason}")
    ```
* **Decoding Data:**
    * Data received over a network is typically in bytes.
    * You must `decode()` bytes into a string, specifying the character encoding (e.g., `UTF-8`).
* **Parsing HTML (Basic):**
    * Once you have the HTML content as a string, you can use string methods (like `find()`, `split()`) or regular expressions to extract data.
    * For complex HTML parsing, libraries like `BeautifulSoup` are often used (introduced in later courses/topics, not core py4e Chapter 12).
* **Web Crawlers/Spiders (Concept):** Programs that automatically navigate the web by following links and collecting information.
* **Binary Data:** HTTP can transmit any type of file (images, audio). You read them as bytes.