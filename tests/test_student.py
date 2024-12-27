from student import StudentManager
import unittest
import os
import sqlite3
from unittest.mock import patch


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.file_name = "students_test.db"
        self.student_manager = StudentManager(self.file_name)

    def test_create_table(self):
        pass

    def test_write_command():
        pass

    def test_read_command():
        pass

    def test_load_data():
        pass

    def test_create_student_from_sql():
        pass

    def test_add_student(self):
        self.student_manager.add_student("Sanjana", 23, "VG", "maths")
        students = self.student_manager.view_all_students()
        self.assertIn("Sanjana", [student["name"] for student in students.items()])

    def test_view_all_students(self):
        self.student_manager.add_student("Vimal", 23, "VG", "maths")
        students = self.student_manager.view_all_students()
        self.assertIn("Vimal", [student["name"] for student in students.items()])

    def test_view_specifik_student(self):
        self.student_manager.add_student("Shan", 23, "VG", "maths")
        student_id = self.student_manager.get_id_list()
        student = self.student_manager.view_specifik_student(student_id)
        self.assertEqual(student["Name"], "Shan")

    def test_update_student():
        pass

    def test_delete_student():
        pass

    def test_get_student_name():
        pass

    def test_get_id_list():
        pass

    def tearDown():
        pass
