# Chapter 16 (Capstone Focus): Geocoding and Data Preparation for Visualization

*This chapter/section focuses on integrating web data access and databases for visualization, particularly using geocoding.*

## 1. Geocoding

* **Purpose:** The process of converting human-readable addresses or location names (e.g., "1600 Amphitheatre Parkway, Mountain View, CA") into geographical coordinates (latitude and longitude).
* **Reverse Geocoding:** Converting coordinates back into addresses.
* **Web Services/APIs:** Geocoding is typically performed using web-based APIs provided by services like:
    * Google Geocoding API
    * OpenStreetMap's Nominatim
    * Mapbox Geocoding API
    * **Key Concept:** You send a request (often an address) to the API, and it returns a structured response (usually JSON or XML) containing coordinates and other location details.
* **API Keys & Rate Limiting:**
    * Many geocoding APIs require an API key for authentication. **Handle API keys securely!** (e.g., environment variables, `.gitignore`).
    * APIs often have **rate limits** (e.g., "X requests per second/minute/day"). Your code needs to handle these gracefully (e.g., using `time.sleep()`).
* **JSON Processing:** Geocoding API responses are very commonly in JSON format, requiring the use of Python's `json` module to parse and extract `latitude` and `longitude`.

## 2. Database Integration for Geocoded Data

* **Storing Results:** It's inefficient and slow to geocode the same address multiple times. Store geocoded data in a database (e.g., SQLite) to:
    * **Cache results:** Avoid repeated API calls.
    * **Manage data:** Easily query, update, and analyze geocoded locations.
    * **Handle large datasets:** Process and store millions of geocoded entries.
* **Database Schema Design:**
    * Extend existing tables (e.g., `Users` table with `lat` and `lng` columns).
    * Create a new table for locations (e.g., `Locations` table with `address`, `latitude`, `longitude`).
    * Consider `UNIQUE` constraints on address to prevent duplicate entries.
* **Python (`sqlite3`) Workflow:**
    * Connect to the database (`sqlite3.connect()`).
    * Create tables (`CREATE TABLE IF NOT EXISTS ...`).
    * Loop through addresses to geocode.
    * **Check for existing data:** Before geocoding, `SELECT` to see if the address is already in your database.
    * If not found, call geocoding API.
    * **`INSERT` new geocoded data** into your table.
    * `UPDATE` existing data if needed.
    * `conn.commit()` regularly to save changes.

## 3. Data Preparation for Visualization

* **Goal:** Convert your stored geocoded data into a format suitable for mapping or visualization tools.
* **Extracting Data:** Use `SELECT` SQL queries to retrieve `latitude`, `longitude`, and any other relevant data (e.g., user names, counts, attributes) from your database.
* **Output Formats:**
    * **KML (Keyhole Markup Language):** An XML-based language for geographic annotation and visualization. Often used with Google Earth.
        * You can generate KML directly from Python by printing XML tags for Placemarks.
    * **GeoJSON:** A standard format for encoding geographic data structures (like points, lines, polygons) using JSON. Increasingly popular for web maps.
    * **CSV:** Simple Comma Separated Values, can be imported into many GIS or mapping tools.
* **Generating KML Example (Conceptual):**
    ```python
    # Basic KML structure for a point
    # <Placemark>
    #   <name>Location Name</name>
    #   <Point><coordinates>longitude,latitude</coordinates></Point>
    # </Placemark>
    ```
    You would loop through your database results, creating these XML snippets for each location and writing them to a `.kml` file.
* **Mapping Tools:**
    * **Google Earth:** Can open `.kml` files directly for rich 3D visualizations.
    * **Online Mapping Libraries/APIs (e.g., Leaflet.js, Google Maps JavaScript API):** Often consume GeoJSON or custom JSON formats.
    * **Python Libraries (e.g., Folium, Plotly):** Can generate interactive maps directly from Python.