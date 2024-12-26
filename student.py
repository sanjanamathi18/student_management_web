import sqlite3


def create_table():
    create_table = """CREATE TABLE IF NOT EXISTS Students (
        ID INTEGER PRIMARY KEY, 
        Name text NOT NULL, 
        Age int NOT NULL, 
        Grade text NOT NULL,
        Subjects text NOT NULL
    )"""

    try:
        with sqlite3.connect("students.db") as conn:
            cursor = conn.cursor()
            cursor.execute(create_table)
            conn.commit()
            print("Table created successfully.")
    except sqlite3.OperationalError as e:
        print("Failed to create tables: ", e)


def write_command(command):
    try:
        with sqlite3.connect("students.db") as conn:
            cursor = conn.cursor()
            cursor.execute(command)
            conn.commit()
            print("Command executed successfully.")
    except sqlite3.OperationalError as e:
        print("Failed to execute command: ", e)


def read_command(command):
    try:
        with sqlite3.connect("students.db") as conn:
            cursor = conn.cursor()
            result = cursor.execute(command)
            print("Command executed successfully.")
            return result.fetchall()

    except sqlite3.OperationalError as e:
        print("Failed to execute command: ", e)
        return None


def load_data():
    command = "SELECT * FROM Students"
    data = read_command(command)
    students = {}
    for data in data:
        id = data[0]
        name = data[1]
        age = data[2]
        grade = data[3]
        subjects = data[4]
        students[id] = {"Name": name, "Age": age, "Grade": grade, "Subjects": subjects}

    return students


def add_student(name, age, grade, subjects):
    sql = f"INSERT INTO Students(Name,Age,Grade,Subjects) VALUES('{name}',{age},'{grade}','{subjects}')"
    write_command(sql)


def view_all_students():
    all_students = load_data()
    return all_students


def view_specifik_student(id):
    sql = f"SELECT * FROM Students WHERE ID = {id}"
    result = read_command(sql)
    student = {}
    student["ID"] = result[0][0]
    student["Name"] = result[0][1]
    student["Age"] = result[0][2]
    student["Grade"] = result[0][3]
    student["Subjects"] = result[0][4]
    return student


def update_student(id, name, age, grade, subjects):
    sql = f"UPDATE Students SET Name = '{name}', Age = {age}, Grade = '{grade}', Subjects = '{subjects}' WHERE id = '{id}'"
    write_command(sql)


def delete_student(id):
    sql = f"DELETE FROM Students WHERE ID = {id}"
    write_command(sql)


def get_student_name(id):
    sql = f"SELECT Name FROM Students WHERE ID = {id}"
    result = read_command(sql)
    return result[0][0]


def get_id_list():
    sql = "SELECT DISTINCT ID FROM Students;"
    result = read_command(sql)
    id_list = [ids[0] for ids in result]
    return id_list
