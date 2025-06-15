# Data Files for Course 4: Using Databases with Python

This `data/` folder serves as a centralized repository for both the **input data files** used by assignments in "Course 4: Using Databases with Python" and the **database files generated** as a result of running those assignments. This organization simplifies access to all data-related components for the course.

---

## Files in This Folder:

Below is a list of the data files and generated database files found in this directory, along with their purpose and the assignments they are associated with.

* ### `opengeo/`
    * **Description:** This is a subfolder containing all the input data files (`where.data`) and generated output files (`opengeo.sqlite`, `where.html`, `where.js`) for the `assignment_16_1_databases_and_visualization` project.
    * **Purpose:** Houses the specific files for the geocoding and map visualization assignment.

* ### `counting_emaildb.sqlite`
    * **Description:** This is a **generated SQLite database file**.
    * **Purpose:** It is created and populated by the `assignment_15_1_counting_emailsdb.py` script. It stores the calculated counts of email sender addresses.

* ### `mbox.txt`
    * **Description:** An **input data file** containing a collection of email messages.
    * **Purpose:** Serves as the source data for the `assignment_15_1_counting_emailsdb.py` script.

* ### `roster_data.json`
    * **Description:** An **input data file** in JSON format containing the full roster information for students and courses.
    * **Purpose:** Used by the `assignment_15_8_many_students_in_many_courses.py` script to populate database tables.

* ### `roster_data_small.json`
    * **Description:** An **input data file** in JSON format, representing a smaller dataset of roster information.
    * **Purpose:** Often used by the `assignment_15_8_many_students_in_many_courses.py` script for quick testing and development.

* ### `rosterdb.sqlite`
    * **Description:** This is a **generated SQLite database file**.
    * **Purpose:** It is created and populated by the `assignment_15_8_many_students_in_many_courses.py` script, storing student, course, and membership data.

* ### `trackdb.sqlite`
    * **Description:** This is a **generated SQLite database file**.
    * **Purpose:** It is created and populated by the `assignment_15_2_musical_tracks_db.py` script, typically storing musical track information.

---

## How to Use These Files:

* **Input Data Files:** When running an assignment script (e.g., from the `assignments/` folder), your script will need to reference these input files using a relative path (e.g., `../data/mbox.txt` if your script is in `assignments/assignment_15_1_counting_emailsdb/`).
* **Generated Database Files:** These files will appear in this `data/` folder after you successfully run the corresponding assignment scripts. You can inspect these `.sqlite` files using a database browser like [DB Browser for SQLite](https://sqlitebrowser.org/).
* **`opengeo/` folder:** Navigate into this folder for the specific input (`where.data`) and generated visualization files (`.sqlite`, `.html`, `.js`) related to the geocoding assignment.