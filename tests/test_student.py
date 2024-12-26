from student import StudentManager
import unittest
import os
import sqlite3
from unittest.mock import patch


class TestConfig(unittest.TestCase):
    def setUp(self):
        self.file_name = "students_test.db"
        self.student_manager = StudentManager(self.file_name)

    def test_create_table(self):
        self.assertTrue(self.student_manager.create_table())
        pass

    def test_write_command():
        pass

    def test_read_command():
        pass

    def test_load_data():
        pass

    def test_create_student_from_sql():
        pass

    def test_add_student():
        pass

    def test_view_all_students():
        pass

    def test_view_specifik_student():
        pass

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
