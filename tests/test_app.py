import unittest
from app import create_app
from bs4 import BeautifulSoup
import os


class StudentManagementTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("test.db")
        self.app.testing = True
        self.client = self.app.test_client()

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"WELCOME TO STUDENT MANAGEMENT", response.data)
        self.assertIn(b"Add Student", response.data)
        self.assertIn(b"View All Students", response.data)
        self.assertIn(b"View Specific Student", response.data)

    def test_add_student_get(self):
        response = self.client.get("/add")
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.data, "html.parser")
        form = soup.find("form")
        self.assertIsNotNone(form)
        name_input = form.find("input", {"id": "name"})
        self.assertIsNotNone(name_input)

        age_input = form.find("input", {"id": "age"})
        self.assertIsNotNone(age_input)

        grade_select = form.find("select", {"id": "grade"})
        self.assertIsNotNone(grade_select)

        subjects_input = form.find("input", {"id": "subjects"})
        self.assertIsNotNone(subjects_input)

        submit_button = form.find("button", {"type": "submit"})
        self.assertIsNotNone(submit_button)

    def test_add_student_post(self):
        response = self.client.post(
            "/add",
            data=dict(name="John Doe", age="20", grade="A", subjects="Math, Science"),
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data)

    def test_view_all_students(self):
        # Add a student to the database
        self.client.post(
            "/add",
            data=dict(name="John Doe", age="20", grade="A", subjects="Math, Science"),
            follow_redirects=True,
        )

        # Get the view all students page
        response = self.client.get("/view_all_students")
        self.assertEqual(response.status_code, 200)

        # Parse the HTML
        soup = BeautifulSoup(response.data, "html.parser")

        # Check the table headers
        headers = [th.text for th in soup.find_all("th")]
        self.assertEqual(headers, ["ID", "Name", "Age", "Grade", "Subjects", "Actions"])

        # Check the student data
        rows = soup.find_all("tr")
        self.assertGreater(len(rows), 1)  # There should be at least one student row

        # Check the first student row
        columns = [td.text for td in rows[1].find_all("td")]
        self.assertEqual(columns[1], "John Doe")  # The name should be "John Doe"
        self.assertEqual(columns[2], "20")  # The age should be "20"
        self.assertEqual(columns[3], "A")  # The grade should be "A"
        self.assertEqual(columns[4], "Math, Science")  # The subjects should be "Math, Science"

        # Check the update and delete buttons
        update_button = rows[1].find("button", string="Update")
        self.assertIsNotNone(update_button)
        delete_button = rows[1].find("button", string="Delete")
        self.assertIsNotNone(delete_button)

    def tearDown(self):
        if os.path.exists("test.db"):
            os.remove("test.db")


if __name__ == "__main__":
    unittest.main()
