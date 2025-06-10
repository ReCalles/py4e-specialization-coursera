# Using the OpenStreetMap API with the Database and Data Visualization on OpenStreetMap

In this project, we use the free OpenStreetMap API (Nominatim service) to convert university names entered by users into geographical locations. We then place the processed data on an OpenStreetMap map.

---

## Important Notes & Recommendations:

* After Windows, we recommend that you use the **PowerShell terminal** to avoid problems with displaying UTF-8 characters.

---

## Prerequisites:

To view and modify the database used in this project, the following program must be installed:

* **DB Browser for SQLite:** [https://sqlitebrowser.org/](https://sqlitebrowser.org/)

---

## Project Phases & Workflow:

The Nominatim service is free, but requires adherence to a maximum of one query per second to avoid being blocked from accessing the API. We divide our task into two distinct phases to manage this.

### Phase 1: Geocoding Data and Storing in Database (`geoload.py`)

In this first phase, we take our input from the `where.data` file and read it line by line. For each line, we query the Nominatim geocoding server to retrieve geographical coordinates and then store this processed data in our SQLite database (`opengeo.sqlite` file).

**Key Feature:** Before making an API query, the program checks if data for a particular location already exists in the database. This prevents redundant API calls if the program is restarted or run multiple times.

* **Restarting from Scratch:** You can restart the entire geocoding process from scratch at any time by simply deleting the generated `opengeo.sqlite` file.

* **Running `geoload.py`:**
    This program will read input lines from the file `where.data` and check for each row to see if it's already in the database, and if we do not have data for the location being processed, it will trigger an API query geocoding to retrieve data and store it in SQLite.

    Here is an example of a run after some are already in the database data:

    ```bash
    python3 geoload.py

    Found in database AGH University of Science and Technology

    Found in database Academy of Fine Arts Warsaw Poland

    Found in database American University in Cairo

    Found in database Arizona State University

    Found in database Athens Information Technology

    Retrieving [https://py4e-data.dr-chuck.net/opengeo?q=BITS+Pilani](https://py4e-data.dr-chuck.net/opengeo?q=BITS+Pilani)
    Retrieved 794 characters {"type":"FeatureColl

    Retrieving [https://py4e-data.dr-chuck.net/opengeo?q=Babcock+University](https://py4e-data.dr-chuck.net/opengeo?q=Babcock+University)
    Retrieved 760 characters {"type":"FeatureColl

    Retrieving [https://py4e-data.dr-chuck.net/opengeo?q=Banaras+Hindu+University](https://py4e-data.dr-chuck.net/opengeo?q=Banaras+Hindu+University)
    Retrieved 866 characters {"type":"FeatureColl
    ...
    ```
    As shown in the example, the first five locations are already in the database, and so are they omitted. The program processes data until it finds unsaved locations and starts asking the API for them.

* **Controlling API Calls:** The `geoload.py` file can be stopped at any time, plus the code contains a counter (the variable `'count'`) that can be used to limit the number of connections to the geocoding API in a given program startup.

### Phase 2: Data Visualization (`geodump.py`)

After the geographical data has been loaded into `opengeo.sqlite`, you can visualize it with `geodump.py`. This program reads the database and writes the `where.js` file containing locations, latitudes, and longitudes in a form JavaScript executable. The ZIP file you downloaded already contains `where.js` generated, but you can generate it again to check the operation of the `geodump.py` program.

* **Launching `geodump.py`:**

    ```bash
    python3 geodump.py
    ```

---

## Getting Started / Running the Example:

To perform the full geocoding and visualization exercise, follow these steps:

1.  **Download the code:** Get the project files from [www.py4e.com/code3/opengeo.zip](www.py4e.com/code3/opengeo.zip).
2.  **Unzip the file:** Extract the contents of the `opengeo.zip` file to your desired project location.
3.  **Edit `where.data`:** Open the `where.data` file (found in the unzipped folder) and add an address nearby where you live (but ensure you don't reveal your exact living location for privacy).
4.  **Run `geoload.py`:** Execute this program to look up all entries in `where.data` (including your new address) and populate the database, which will be named `geodata.sqlite` for this exercise.
    ```bash
    python3 geoload.py
    ```
5.  **Run `geodump.py`:** Execute this program to read from the `geodata.sqlite` database and produce the `where.js` file.
    ```bash
    python3 geodump.py
    ```
6.  **Visualize the map:** Open the `where.html` file in your web browser to visualize your geocoded locations on a map.
7.  **Take Screenshots:** You can run the programs and then scroll back in your terminal to take screenshots when the program finishes. Ensure that your added location clearly shows in all three of your screenshots as described below (presumably from `geoload.py` output, `geodump.py` output, and the `where.html` map visualization).