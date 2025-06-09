# Using Databases with Python

This subfolder contains all materials related to **"Using Databases with Python"**, the fourth course in the "Python for Everybody Specialization" offered by the University of Michigan on Coursera. This course introduces you to the fundamental concepts of databases, SQL, and how to interact with relational databases using Python, particularly SQLite. It also touches upon Object-Oriented Programming (OOP) as a way to structure your code when dealing with complex data. This course covers chapters 14-16 of the Charles R. Severance 'Python for Everybody: Exploring Data in Python 3' book.

## 1. Course Overview and Learning Objectives

This course bridges your Python programming skills with the power of databases. You will learn how to store, manage, and retrieve data efficiently using structured queries and database systems. Understanding databases is crucial for developing robust, data-driven applications.

### Key Learning Objectives:

Upon successful completion of this course, you should be able to:

* **Understand Database Concepts:** Grasp the basics of relational databases, tables, rows, columns, and primary/foreign keys.
* **Write SQL Queries:** Construct fundamental SQL commands for `CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE`, and `DELETE` data.
* **Use SQLite:** Work with SQLite, a lightweight, embedded relational database system.
* **Connect Python to Databases:** Utilize Python's `sqlite3` module to connect to SQLite databases.
* **Execute SQL from Python:** Run SQL queries directly from your Python scripts and process the results.
* **Manage Database Transactions:** Understand and implement `commit()` and `rollback()` for data integrity.
* **Apply Object-Oriented Programming (OOP) Concepts:** Understand basic OOP principles (classes, objects, methods, constructors) and how they can be used to model real-world entities in your Python code, often relevant when interacting with database records.
* **Build Data-Driven Applications:** Develop Python applications that can store and retrieve data from a database.

## 2. Folder Structure and Content Explanation

This subfolder is organized to reflect the course's focus on database interaction and potentially Object-Oriented Programming.

* ### `lectures/` or `notes/`
    Your personal notes, summaries of video lectures, or Markdown files outlining key concepts related to relational databases, SQL syntax, Python's `sqlite3` module, and Object-Oriented Programming.
    * *Example Files:* `week14_chapter14_oop.md`, `week15_chapter15_databases_sqlite.md`, `sql_commands_cheatsheet.md`.

* ### `assignments/` or `exercises/`
    Your solutions to programming assignments and practical exercises, specifically those involving database creation, data insertion, querying, and potentially using OOP principles.
    * *Example Files:* `emaildb.py` (often a common assignment for processing email data into a database), `tracks.py`, `assignment_15_1.py`.
    * **Sub-folders within `assignments/` (Optional):** Consider `assignments/week_14/`, `assignments/week_15/` for further organization.

* ### `data/` 
    This folder can store sample data files (e.g., `.txt`, `.csv`) that are used as input for your assignments or scripts, especially for file handling exercises.
    * *Example Files:* `mbox-short.txt`, `words.txt`, `sample_data.csv`.

* ### `databases/`
    (Highly recommended for this course!) This folder can store your SQLite database files (`.sqlite`, `.db`) that you create or interact with during assignments.
    * *Example Files:* `emaildb.sqlite`, `tracks.sqlite`, `roster.sqlite`.

* ### `resources/` or `cheatsheets/`
    Supplementary materials found helpful, such as SQL command cheat sheets, database design principles, or links to `sqlite3` module documentation.
    * *Example Files:* `sql_commands.md`, `sqlite3_tips.txt`, `database_design_basics.md`.

## 3. How to Use This Content

This repository is a valuable resource for reviewing and reinforcing your understanding of databases with Python and OOP.

* **Review Concepts:** Use `lectures/` or `notes/` to refresh your memory on database fundamentals, SQL, and OOP.
* **Examine Solutions:** Explore `assignments/` to see how specific problems involving databases were solved.
* **Access Databases:** Open `.sqlite` or `.db` files in the `databases/` folder using database browsers (like DB Browser for SQLite) to inspect your data.
* **Reference Materials:** Utilize `resources/` for quick lookups of SQL syntax or database concepts.

## 4. Getting Started (For New Learners)

If you're new to this course or databases with Python, here are some steps to get started:

1.  **Ensure Python is Installed:** Verify Python 3 is installed on your system ([python.org](https://www.python.org/)).
2.  **Use an IDE:** A robust IDE like PyCharm or VS Code is highly recommended.
3.  **Install Database Browser:** Consider installing a tool like **DB Browser for SQLite** ([sqlitebrowser.org](https://sqlitebrowser.org/)) to easily view and manage your `.sqlite` database files outside of Python.
4.  **Review Course Lectures:** Supplement these files by going through the actual Coursera course lectures or equivalent tutorials on databases with Python for full context.

## 5. Contributing and Feedback

This repository serves as a personal record of my learning journey. However, if you find any errors in the notes or solutions, have suggestions for improvement, or would like to discuss any of the concepts or code, please feel free to open an issue or pull request (if this is a shared repository). Constructive feedback is always welcome.
