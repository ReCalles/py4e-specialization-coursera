# Chapter 15: Using Databases with Python

* **Databases vs. Flat Files:**
    * **Flat Files:** Simple text files; good for small, simple data. Difficult to manage large, complex, or related data.
    * **Databases:** Structured storage for large amounts of related data. Provide efficient search, update, deletion, and robust data integrity.

* **Relational Databases:**
    * Data is organized into **tables** (relations).
    * Each table has **rows** (records) and **columns** (fields/attributes).
    * **Primary Key:** A column (or set of columns) that uniquely identifies each row in a table.
    * **Foreign Key:** A column in one table that links to the primary key in another table, establishing relationships.

* **SQL (Structured Query Language):**
    * The standard language for managing and querying relational databases.
    * **DML (Data Manipulation Language):** `SELECT`, `INSERT`, `UPDATE`, `DELETE`.
    * **DDL (Data Definition Language):** `CREATE TABLE`, `DROP TABLE`.

* **Key SQL Commands:**
    * **`CREATE TABLE tablename (column1 type, column2 type, ...)`:** Defines a new table.
    * **`INSERT INTO tablename (col1, col2) VALUES (val1, val2)`:** Adds a new row.
    * **`SELECT columns FROM tablename WHERE condition ORDER BY column DESC/ASC LIMIT num`:** Retrieves data.
    * **`UPDATE tablename SET col = new_val WHERE condition`:** Modifies existing rows.
    * **`DELETE FROM tablename WHERE condition`:** Removes rows.

* **SQLite:**
    * A very popular, lightweight, file-based relational database management system.
    * It doesn't require a separate server process. The database is a single file (`.sqlite` or `.db`).
    * Ideal for small to medium-sized applications or embedded use.

* **Python's `sqlite3` Module:**
    * Python's built-in module for interacting with SQLite databases.
    * **Steps for Database Interaction:**
        1.  `import sqlite3`
        2.  **Connect to Database:** `conn = sqlite3.connect('mydatabase.sqlite')` (Creates file if it doesn't exist).
        3.  **Get a Cursor:** `cur = conn.cursor()` (A cursor allows you to execute SQL commands and fetch results).
        4.  **Execute SQL:** `cur.execute('SQL COMMAND HERE')`
        5.  **Commit Changes:** `conn.commit()` (Saves changes like `INSERT`, `UPDATE`, `DELETE`, `CREATE TABLE` permanently to the disk). Without `commit()`, changes are temporary.
        6.  **Fetch Results (for `SELECT`):**
            * `cur.fetchone()`: Retrieves the next single row.
            * `cur.fetchall()`: Retrieves all remaining rows as a list of tuples.
        7.  **Close Cursor and Connection:** `cur.close()`, `conn.close()` (Good practice to release resources).

* **Database Schema:** The design or structure of your database, defining tables, columns, relationships, etc.

* **Idempotence in `CREATE TABLE`:**
    * Often use `CREATE TABLE IF NOT EXISTS ...` to avoid errors if the table already exists.
    ```python
    cur.execute('CREATE TABLE IF NOT EXISTS Users (name TEXT, email TEXT)')
    ```