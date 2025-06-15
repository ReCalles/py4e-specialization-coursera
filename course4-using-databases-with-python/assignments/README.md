# Course 4: Using Databases with Python - Assignments

This folder contains my solutions to the programming assignments for "Course 4: Using Databases with Python" from the Python for Everybody Specialization. Each assignment is organized into its own dedicated subfolder to ensure clarity and self-containment of all related files.

---

## Assignment Contents Overview:

Below is a detailed list of each assignment folder, outlining the Python scripts, any required input data files, and the output files that are generated when you run the code. Screenshots demonstrating the program's execution or results are also included where applicable.

### `assignment_15_1_counting_emailsdb/`

* **Purpose:** This assignment focuses on reading email data from a text file, parsing it, and storing email sender counts in a SQLite database.
* `assignment_15_1_counting_emailsdb.py`: The Python script that implements the solution.
* `mbox.txt`: **Input data file** containing the email messages to be processed.
* `counting_emaildb.sqlite`: **Generated SQLite database file** that stores the calculated email sender counts.

### `assignment_15_2_musical_tracks_db/`

* **Purpose:** This assignment typically involves parsing musical track data (often from an XML source, though not explicitly shown here) and populating a SQLite database with track information.
* `assignment_15_2_musical_tracks_db.py`: The Python script for processing track data and building the database.
* `trackdb.sqlite`: **Generated SQLite database file** that stores the parsed musical track details.

### `assignment_15_8_many_students_in_many_courses/`

* **Purpose:** This assignment models a many-to-many relationship in a relational database, specifically for students enrolled in multiple courses, using JSON input data.
* `assignment_15_8_many_students_in_many_courses.py`: The Python script to process the roster JSON data and create the database tables with relationships.
* `roster_data.json`: **Input data file** containing the full roster information.
* `roster_data_small.json`: **Input data file** with a smaller dataset for easier testing.
* `rosterdb.sqlite`: **Generated SQLite database file** containing the student, course, and membership tables.

### `assignment_16_1_databases_and_visualization/`

* **Purpose:** This project integrates concepts from web data access (geocoding), database storage, and prepares data for visualization on a map (e.g., OpenStreetMap).
* This folder contains a subfolder named `opengeo/` which holds the core project files:
    * `geoload.py`: Python script responsible for reading addresses from `where.data`, geocoding them via an API, and storing results in the database.
    * `geodump.py`: Python script that reads geocoded data from the database and generates files for map visualization.
    * `where.data`: **Input data file** containing addresses or locations to be geocoded.
    * `opengeo.sqlite` (or `geodata.sqlite`): **Generated SQLite database file** that stores the geocoded latitude and longitude coordinates.
    * `where.js`: **Generated JavaScript file** containing the location data, ready for web-based mapping.
    * `where.html`: **Generated HTML file** that loads `where.js` to display the interactive map.
    * `README.md`: A specific README detailing this `assignment_16_1` project's setup and execution.

---

## How to Use These Assignments:

To run and understand these assignments, follow these general steps:

1.  **Navigate to the specific assignment's subfolder** in your terminal or file explorer.
2.  **Inspect the Python script (`.py` file):** Open and read the Python code to understand the logic, database interactions, and purpose of the assignment.
3.  **Ensure Input Data is Present:** Verify that any required input files (e.g., `mbox.txt`, `roster_data.json`, `where.data`) are located within the same assignment folder.
4.  **Run the Python Script:** Execute the main Python script from your terminal (e.g., `python assignment_15_1_counting_emailsdb.py`).
5.  **Observe Generated Files:** After successful execution, new files (e.g., `.sqlite` database files, `.js` JavaScript files, `.html` visualization files) will appear in the assignment folder as a direct result of the program's operation.
6.  **Review Screenshots:** Included screenshots illustrate typical console output or map visualizations, helping to verify the correct functioning of the programs.

---

## Note on Resources:

There is a `resources/` folder (typically located in the parent `course4-using-databases-with-python/` directory) that contains supplementary materials. These resources might include SQL command cheat sheets, database design principles, or other references that are helpful for working on these assignments.