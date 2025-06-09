# Chapter 13: Web Services and XML

* **Web Services / APIs (Application Programming Interfaces):**
    * Programs that provide data or functionality over the web.
    * Allow applications to interact with each other programmatically, without human intervention.
    * Instead of humans reading web pages, programs request and receive structured data.
* **Data Serialization Formats:** Ways to represent complex data structures (like lists, dictionaries) as strings, so they can be easily transmitted over a network or stored in files.
    * **XML (Extensible Markup Language):** One of the oldest and widely used data serialization formats.
        * **Structure:** Uses tags (`<tag>`), elements (content between tags), and attributes (key-value pairs within a tag).
        * Hierarchical (tree-like) structure.
        * Self-describing (tags describe the data).
    * **JSON (JavaScript Object Notation):** A lighter-weight and more commonly used format today (often covered immediately after XML or in parallel).
* **Parsing XML in Python (`xml.etree.ElementTree` module):**
    * Allows you to read XML data and navigate its tree structure.
    * `ET.fromstring(xml_string)`: Parses an XML string into an ElementTree object.
    * `Element.find('tag_name')`: Finds the first sub-element with the given tag.
    * `Element.findall('tag_name')`: Finds all sub-elements with the given tag (returns a list).
    * `Element.get('attribute_name')`: Gets the value of an attribute.
    * `Element.text`: Gets the text content of an element.
    * **Tree Traversal:** Navigating up/down/across the XML tree to find specific data.
    ```python
    import xml.etree.ElementTree as ET

    data = '''<person>
        <name>Chuck</name>
        <phone type="intl">
            +1 734 303 4456
        </phone>
        <email hide="yes"/>
    </person>'''

    tree = ET.fromstring(data)
    name = tree.find('name').text
    phone = tree.find('phone').text
    phone_type = tree.find('phone').get('type')

    print(f'Name: {name}')      # Output: Name: Chuck
    print(f'Phone: {phone}')     # Output: Phone: +1 734 303 4456
    print(f'Phone Type: {phone_type}') # Output: Phone Type: intl
    ```
* **Understanding APIs:** Web services provide data through an API, which is a set of rules and specifications for how applications should communicate. Often, APIs return data in XML or JSON format.