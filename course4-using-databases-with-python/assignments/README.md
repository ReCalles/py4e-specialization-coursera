# Course 4: Using Databases with Python - Assignments

This folder contains my solutions to the programming assignments for "Course 4: Using Databases with Python" from the Python for Everybody Specialization. Each assignment is organized into its own dedicated subfolder for clarity and self-containment.

---

## Folder Structure and Content Explanation:

Each subfolder within this `assignments/` directory corresponds to a specific assignment and generally contains the following:

* The main Python script solution (`.py` file).
* Required **input data files** (e.g., `.txt`, `.json`) used by the script.
* **Generated output files** (e.g., `.sqlite`, `.js`, `.html`) that are created as a result of running the Python code.
* Screenshots (`.png`, `.jpg`) demonstrating the program's console output or map visualizations.

---

## Assignment Folders and Their Contents:

Below are the specific assignment folders included in this directory, detailing their purpose and the files you will find within each:

* ### `assignment_15_1_counting_emailsdb/`
    * **Purpose:** This assignment involves reading email data and storing email counts in a SQLite database.
    * `assignment_15_1_counting_emailsdb.py`: The Python script to process email data and populate the database.
    * `mbox.txt`: **Input data file** containing email messages.
    * `counting_emaildb.sqlite`: **Generated SQLite database file** that stores the email counts.

* ### `assignment_15_2_musical_tracks_db/`
    * **Purpose:** This assignment typically involves parsing data (e.g., from XML or JSON, often related to music tracks) and storing it in a SQLite database.
    * `assignment_15_2_musical_tracks_db.py`: The Python script to process track data and populate the database.
    * `trackdb.sqlite`: **Generated SQLite database file** that stores the musical track information.

* ### `assignment_15_8_many_students_in_many_courses/`
    * **Purpose:** This assignment demonstrates how to model a many-to-many relationship (like students in courses) in a relational database.
    * `assignment_15_8_many_students_in_many_courses.py`: The Python script to process roster data and populate the database.
    * `roster_data.json`: **Input data file** containing the roster information (full dataset).
    * `roster_data_small.json`: **Input data file** (a smaller version of the roster data, useful for testing).
    * `rosterdb.sqlite`: **Generated SQLite database file** that stores the student, course, and membership data.

* ### `assignment_16_1_databases_and_visualization/`
    * **Purpose:** This project integrates web data (geocoding), database storage, and visualization on a map (often using OpenStreetMap). It builds upon concepts from previous courses.
    * This folder contains a subfolder named `opengeo/` which holds the core project files:
        * `geoload.py`: Python script to load geocoding data from `where.data` into the database.
        * `geodump.py`: Python script to read geocoded data from the database and prepare it for visualization.
        * `where.data`: **Input data file** containing addresses or locations for geocoding.
        * `opengeo.sqlite` (or `geodata.sqlite`): **Generated SQLite database file** storing the geocoded locations.
        * `where.js`: **Generated JavaScript file** containing the location data in a format suitable for web maps.
        * `where.html`: **Generated HTML file** to display the map with your geocoded locations.
        * `README.md`: A specific README detailing this `assignment_16_1` project.

---

## How to Use These Assignments:

1.  **Navigate to the specific assignment folder** in your terminal or file explorer.
2.  **Inspect the Python script (`.py` file):** Review the code to understand the solution logic and database interactions.
3.  **Ensure input data is present:** Verify any required input files (e.g., `mbox.txt`, `.json` files) are in the correct location.
4.  **Run the Python script:** Execute the Python script from your terminal (e.g., `python assignment_15_1_counting_emailsdb.py`).
5.  **Observe generated files:** After successful execution, new `.sqlite`, `.js`, or `.html` files will appear in the folder as the output of the program.
6.  **Review screenshots:** Compare your program's console output or visual maps with the provided screenshots to confirm correct operation.

---

## Note on Resources:

If you have a top-level `resources/` folder (within your `course4-using-databases-with-python/` directory), it may contain additional resources, cheat sheets, or templates relevant to these assignments.