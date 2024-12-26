import sqlite3


class StudentManager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.create_table()

    def write_command(self, command):
        try:
            with sqlite3.connect(self.file_name) as conn:
                cursor = conn.cursor()
                cursor.execute(command)
                conn.commit()
                print("Command executed successfully.")
        except sqlite3.OperationalError as e:
            raise RuntimeError("Failed to execute command: ", e)

    def create_table(self):
        create_table = """CREATE TABLE IF NOT EXISTS Students (
            ID INTEGER PRIMARY KEY, 
            Name text NOT NULL, 
            Age int NOT NULL, 
            Grade text NOT NULL,
            Subjects text NOT NULL
        )"""
        self.write_command(create_table)

    def read_command(self, command):
        try:
            with sqlite3.connect(self.file_name) as conn:
                cursor = conn.cursor()
                result = cursor.execute(command)
                print("Command executed successfully.")
                return result.fetchall()

        except sqlite3.OperationalError as e:
            raise RuntimeError("Failed to execute command: ", e)

    def create_student_from_sql(self, data):
        id = data[0]
        name = data[1]
        age = data[2]
        grade = data[3]
        subjects = data[4]
        return {"ID": id, "Name": name, "Age": age, "Grade": grade, "Subjects": subjects}

    def load_data(self):
        command = "SELECT * FROM Students"
        data = self.read_command(command)
        students = {}
        for data in data:
            students[id] = self.create_student_from_sql(data)
        return students

    def add_student(self, name, age, grade, subjects):
        sql = f"INSERT INTO Students(Name,Age,Grade,Subjects) VALUES('{name}',{age},'{grade}','{subjects}')"
        self.write_command(sql)

    def view_all_students(self):
        all_students = self.load_data()
        return all_students

    def view_specifik_student(self, id):
        sql = f"SELECT * FROM Students WHERE ID = {id}"
        result = self.read_command(sql)
        return self.create_student_from_sql(result[0])

    def update_student(self, id, name, age, grade, subjects):
        sql = f"UPDATE Students SET Name = '{name}', Age = {age}, Grade = '{grade}', Subjects = '{subjects}' WHERE id = '{id}'"
        self.write_command(sql)

    def delete_student(self, id):
        sql = f"DELETE FROM Students WHERE ID = {id}"
        self.write_command(sql)

    def get_student_name(self, id):
        sql = f"SELECT Name FROM Students WHERE ID = {id}"
        result = self.read_command(sql)
        return result[0][0]

    def get_id_list(self):
        sql = "SELECT DISTINCT ID FROM Students;"
        result = self.read_command(sql)
        id_list = [ids[0] for ids in result]
        return id_list
