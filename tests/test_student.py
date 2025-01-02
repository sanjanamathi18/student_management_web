from student import StudentManager
import unittest
import os


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.file_name = "students_test.db"
        self.student_manager = StudentManager(self.file_name)

    def test_add_student(self):
        self.student_manager.add_student("Sanjana", 23, "VG", "Maths")
        students = self.student_manager.view_all_students()
        self.assertEqual("Sanjana", students[0]["Name"])

    def test_view_all_students(self):
        self.student_manager.add_student("Vimal", 23, "VG", "Maths")
        students = self.student_manager.view_all_students()
        self.assertEqual("Vimal", students[0]["Name"])

    def test_view_specifik_student(self):
        self.student_manager.add_student("Shan", 23, "VG", "Maths")
        student_id = self.student_manager.get_id_list()
        student = self.student_manager.view_specifik_student(student_id[0])
        self.assertEqual(student["Name"], "Shan")
        self.assertEqual(student["Age"], 23)
        self.assertEqual(student["Grade"], "VG")
        self.assertEqual(student["Subjects"], "Maths")

    def test_update_student(self):
        self.student_manager.add_student("Shan", 23, "VG", "Maths")
        student_id = self.student_manager.get_id_list()
        id = student_id[0]
        self.assertEqual(id, 1)
        self.student_manager.update_student(id, "San", 26, "Pass", "English")
        students = self.student_manager.view_all_students()
        self.assertEqual("San", students[0]["Name"])
        self.assertEqual(26, students[0]["Age"])
        self.assertEqual("Pass", students[0]["Grade"])
        self.assertEqual("English", students[0]["Subjects"])

    def test_delete_student(self):
        self.student_manager.add_student("David", 23, "VG", "Maths")
        student_id = self.student_manager.get_id_list()
        id = student_id[0]
        self.assertEqual(id, 1)
        self.student_manager.delete_student(id)
        student_id = self.student_manager.get_id_list()
        self.assertFalse(student_id)

    def test_get_student_name(self):
        self.student_manager.add_student("David", 23, "VG", "Maths")
        student_id = self.student_manager.get_id_list()
        id = student_id[0]
        self.assertEqual(id, 1)
        name = self.student_manager.get_student_name(id)
        self.assertEqual(name, "David")

    def test_get_id_list(self):
        self.student_manager.add_student("Sanju", 23, "VG", "Maths")
        self.student_manager.add_student("Vim", 25, "Pass", "English")
        id = self.student_manager.get_id_list()
        length = len(id)
        self.assertEqual(2, length)

    def tearDown(self):
        if os.path.exists(self.file_name):
            os.remove(self.file_name)
