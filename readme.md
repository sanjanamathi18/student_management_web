
# Student Management System

An interactive **Student Management System** that enables users to perform CRUD (Create, Read, Update, Delete) operations on student data through a **web interface** powered by Flask. The system supports data persistence using SQLite3 and includes unit testing for Python, Flask endpoints, and HTML.

## Description

The purpose of this project is to create a robust and user-friendly system for managing student information. It incorporates modern web technologies and Python programming concepts to ensure scalability, maintainability, and reliability.

### Key Features:

1. **Web-based Interface**: Users can manage student data through an intuitive web interface.

2. **CRUD Operations**: Supports creating, reading, updating, and deleting student records.

3. **Data Persistence**: Stores records securely in an SQLite3 database.

4. **Unit Testing**: Includes unit tests for Python, Flask endpoints, and HTML pages using BeautifulSoup.

5. **Scalable and Extendable**: Easily integrates with other systems or scales for larger implementations.

This system is ideal for learning purposes, small-scale implementations in schools or tuition centers, or as a foundational component for larger projects.

---

## Getting Started

### Dependencies

To run this system, ensure the following dependencies are installed:

- **Python 3.8 or higher**

- **Flask** (for the web application)

- **SQLite3** (for database management)

- **Unittest** (for testing Python and Flask)

- **BeautifulSoup4** (for HTML testing)

- Other required packages are listed in `requirements.txt`.

### Installation and Setup

1. Clone or download the repository:
   ```
   git clone 
   
   https://github.com/sanjanamathi18/student_management_system_web.git
   ```

2. Set up a virtual environment and install dependencies:
   ```
   python3 -m venv .venv

   source .venv/bin/activate

   pip install -r requirements.txt
   ```


3. Start the Flask server:
   ```
   python3 app.py 

   Or click RUN button
   ```

4. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

---

## System Design

### Workflow

1. **Start the Application**

2. **Main Menu**: Interact with the web interface to:
    - **Add Student**: Submit student details through a form.
    - **View All Students**: See a list of all students.
    - **Update Student**: Modify student details by selecting a record.
    - **Delete Student**: Remove a student record by ID.

3. **Save and Exit**: Ensure all changes are saved to the database.

### Data Flow

- User inputs are validated through the web interface.
- Valid data is sent to the Flask server, which interacts with the SQLite3 database for storage and retrieval.
- Outputs are rendered dynamically in the browser.

---

## Testing

This project includes robust testing mechanisms:

### Unit Tests

- **Python Code**: Validates core logic and data manipulation.

- **Flask Endpoints**: Ensures API endpoints work as expected.

- **HTML Testing**: Uses BeautifulSoup to verify the structure and content of rendered HTML pages.

Run all tests:

```
python3 -m unittest  tests/test_student.py

python3 -m unittest  tests/test_app.py
```

---

## Version History

### 2.0

- Added Flask-based web server and SQLite3 database integration.
- Included BeautifulSoup for HTML testing.
- Enhanced UI with HTML and CSS.

### 1.1

- Introduced unit tests for Python and Flask endpoints.
- Added better error handling and input validation.

### 1.0

- Initial release with command-line interface supporting basic CRUD operations.

---

## Help

### Common Issues

1. **Package Installation Problems**:
   - Use a virtual environment to avoid dependency conflicts.
     ```
     python3 -m venv .venv

     source .venv/bin/activate

     pip install -r requirements.txt
     ```

2. **Database Issues**:
   - Ensure database connection has been executed to set up the SQLite3 database.

3. **Server Errors**:
   - Verify all required ports are open and available.
   - Check Flask debug logs for detailed error messages.

---

## Authors

- **Sanjana Mathiyalagan**

  - GitHub: [@Sanjana Mathi](https://github.com/sanjanamathi18)



