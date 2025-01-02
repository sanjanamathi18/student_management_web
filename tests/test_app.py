import unittest
from app import create_app
from bs4 import BeautifulSoup
import os


class StudentManagementTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("test.db")
        self.app.testing = True
        self.client = self.app.test_client()

    def home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"WELCOME TO STUDENT MANAGEMENT", response.data)
        self.assertIn(b"Add Student", response.data)
        self.assertIn(b"View All Students", response.data)
        self.assertIn(b"View Specific Student", response.data)

    def table_exists(self):
        response = self.client.get("/view_all_students")
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.data, "html.parser")

        headers = [th.text for th in soup.find_all("th")]
        self.assertEqual(headers, ["ID", "Name", "Age", "Grade", "Subjects", "Actions"])

        rows = soup.find_all("tr")
        self.assertGreater(len(rows), 1)

    def form_exists(self):
        response = self.client.get("/add")
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.data, "html.parser")

        form = soup.find("form")
        self.assertIsNotNone(form)
        name_input = form.find("input", {"id": "name"})
        self.assertIsNotNone(name_input)

        age_input = form.find("input", {"id": "age"}, {"type": "number"})
        self.assertIsNotNone(age_input)

        grade_select = form.find("select", {"id": "grade"})
        self.assertIsNotNone(grade_select)

        subjects_input = form.find("input", {"id": "subjects"})
        self.assertIsNotNone(subjects_input)

        submit_button = form.find("button", {"type": "submit"})
        self.assertIsNotNone(submit_button)

    def add_student(
        self, name="Sanjana Mathiyalagan", age="20", grade="VG", subjects="Math, Science"
    ):
        response = self.client.post(
            "/add",
            data=dict(name=name, age=age, grade=grade, subjects=subjects),
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data)

    def test_home_page(self):
        self.home_page()

    def test_add_student_get(self):
        self.form_exists()

    def test_add_student_post(self):
        response = self.client.post(
            "/add",
            data=dict(name="Sanjana Mathiyalagan", age="20", grade="VG", subjects="Math, Science"),
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data)

    def test_view_all_students(self):
        self.table_exists()
        self.add_student(age=25)
        response = self.client.get("/view_all_students")
        soup = BeautifulSoup(response.data, "html.parser")

        rows = soup.find_all("tr")
        columns = [td.text for td in rows[1].find_all("td")]
        self.assertEqual(columns[1], "Sanjana Mathiyalagan")
        self.assertEqual(columns[2], "25")
        self.assertEqual(columns[3], "VG")
        self.assertEqual(columns[4], "Math, Science")

        update_button = rows[1].find("button", string="Update")
        self.assertIsNotNone(update_button)
        delete_button = rows[1].find("button", string="Delete")
        self.assertIsNotNone(delete_button)

    def test_view_specific_student(self):
        self.home_page()
        self.form_exists()
        self.table_exists()
        self.add_student()
        self.add_student("Vimal")
        response = self.client.post(
            "/view_specific_student",
            data=dict(ID=1),
            follow_redirects=True,
        )
        soup = BeautifulSoup(response.data, "html.parser")
        paragraphs = [p.get_text() for p in soup.find_all("p")]
        self.assertIn("ID: 1", paragraphs)
        self.assertIn("Name: Sanjana Mathiyalagan", paragraphs)
        self.assertIn("Age: 20", paragraphs)
        self.assertIn("Grade: VG", paragraphs)
        self.assertIn("Subjects: Math, Science", paragraphs)

    def test_update_student(self):
        self.form_exists()
        self.table_exists()
        self.add_student()
        response = self.client.get("/update_student/1")
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            "/update_student/1",
            data=dict(name="Vimal", age="20", grade="VG", subjects="Math, Science"),
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data)
        soup = BeautifulSoup(response.data, "html.parser")
        rows = soup.find_all("tr")
        columns = [td.text for td in rows[1].find_all("td")]
        self.assertEqual(columns[1], "Vimal")
        self.assertEqual(columns[2], "20")
        self.assertEqual(columns[3], "VG")
        self.assertEqual(columns[4], "Math, Science")

    def test_delete_student(self):
        self.form_exists()
        self.table_exists()
        self.add_student(name="Shan")
        response = self.client.get("/delete_student/1")
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            "/delete_student/1",
            data=dict(argument="true"),
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data)
        self.assertIn(b"No students found.", response.data)

    def tearDown(self):
        if os.path.exists("test.db"):
            os.remove("test.db")


if __name__ == "__main__":
    unittest.main()
