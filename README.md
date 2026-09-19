Python Practice Programs

A collection of Python programs covering file handling, data persistence, and a simple AI chatbot — built while learning Python I/O, CSV/binary file handling, MySQL connectivity, and the OpenAI API.

Files

Text file handling
text_file_crud.py — Create, read, search, and append records in a plain .txt file, driven by a menu.
fruits_file_search.py — Writes a list of fruits to a file, then reads it back and copies lines containing a keyword to a second file.

CSV file handling
products_csv_v1.py — Early version of a product-catalog writer using the csv module.
products_csv_v2.py — Revised version: appends product records and reads them back.
products_csv_v3.py — Adds search-by-ID on top of the product CSV writer.
students_csv_v1.py — Student records (ID, name, fees, class) via CSV — create, search, display.
students_csv_v2.py — Slightly revised version of the student CSV manager.
contacts_csv.py — Contacts list via CSV — append, count, and display entries.

Binary file handling (pickle)
employee_records.py — Stores employee ID/name/salary records in a binary file using pickle.
flight_records.py — Flight records (ID, name, passenger count) — create, append, delete, display.
vehicle_records.py — Vehicle records (ID, name, model, colour, price) — append, search, update.

MySQL database programs
student_fees_db.py — Creates a students table (roll no, class, fees) and supports insert/display/delete.
student_roll_db.py — Creates a rolls table (roll no, name, teacher name) and supports insert/display/delete. Setup: these two scripts read your database password from an environment variable rather than hardcoding it:
bash
  export DB_PASSWORD="your_mysql_password_here"

Data structures
stack_operations.py — Basic stack implementation with push/pop via a menu.
roll_number_list.py — Stores roll numbers in a list and looks one up on request.

Notes

Several files are earlier drafts of the same idea (e.g. the three product-CSV scripts, or the two student-CSV scripts) kept to show iteration over time rather than a single "final" version.

Author

Vishal Prasad — Electrical and Computer Engineering, College of Engineering Trivandrum
