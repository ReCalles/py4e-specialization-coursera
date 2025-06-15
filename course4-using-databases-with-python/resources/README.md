# Resource Files for Using Databases with Python Assignments

This `resources/` folder contains local resource files, helper scripts, and sample data that are auxiliary to various Python assignments throughout the "Using Databases with Python" course. These files serve as references, templates, or specific input data for certain activities, helping to set up or understand the assignments.

---

## Resource File Usage Overview:

The resources are organized into specific subfolders, each grouping files related to a particular assignment or topic.

### `email_counting_db_resources/` 

* **Description:** Contains resources specifically for the email counting database assignment (`assignment_15_1_counting_emailsdb.py`).
* **Contents:**
    * `emaildb.py`: A Python code file, likely serving as a template or reference for setting up the email database.
    * `mbox.txt`: A text file containing email data. This file is directly used as input by the assignment's Python script.

### `musical_tracks_db_resources/` 

* **Description:** Contains resources for the musical tracks database assignment (`assignment_15_2_musical_tracks_db.py`).
* **Contents:**
    * `tracks.csv`: A CSV file containing musical track data. This file is typically used as input for the assignment's Python script to populate the database.
    * `tracks.py`: A Python code file, likely a template or reference script for processing track data.
    * `README.txt`: A plain text README specific to this resource set.
    * `old/`: An additional subfolder, likely containing older versions or related files.

### `student_roster_db_resources/` 

* **Description:** Contains resources for the student roster database assignment (`assignment_15_8_many_students_in_many_courses.py`), which typically models many-to-many relationships.
* **Contents:**
    * `roster.py`: A Python code file, likely a template or reference script for managing student rosters.
    * `roster_data_sample.json`: A JSON file containing sample roster data.
    * `roster_data_small.json`: A smaller JSON file of roster data, often used for quick testing.

---

## How to Use These Files:

* **Referencing Resources:** When working on an assignment, refer to the specific subfolder within `resources/` for any accompanying data, templates, or helper scripts.
* **File Paths:** Ensure your Python scripts (located in `assignments/`) correctly reference these resource files using appropriate relative paths (e.g., `../resources/email_counting_db_resources/mbox.txt`).
* **Templates/References:** Python files like `emaildb.py`, `tracks.py`, or `roster.py` found here are typically provided by the course as starting points or examples, not necessarily the final assignment solutions (which would be in your `assignments/` folder).
