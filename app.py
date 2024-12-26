from flask import Flask, render_template, request, redirect, url_for
import student

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("home_page.html")


@app.route("/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        grade = request.form["grade"]
        subject = request.form["subjects"]
        student.add_student(name, age, grade, subject)
        return redirect(url_for("view_all_students"))
    return render_template("add_student.html")


@app.route("/view_all_students", methods=["GET", "POST"])
def view_all_students():
    students = student.view_all_students()
    return render_template("view_all_students.html", students=students)


@app.route("/view_specific_student", methods=["GET", "POST"])
def view_specific_student():
    id_list = student.get_id_list()
    specific_student = None
    id = None
    if request.method == "POST":
        id = request.form.get("ID")
        if id:
            specific_student = student.view_specifik_student(id)
    return render_template(
        "view_specific_student.html",
        specific_student=specific_student,
        id_list=id_list,
        id=id,
    )


@app.route("/update_student/<int:id>", methods=["GET", "POST"])
def update_student(id):
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        grade = request.form["grade"]
        subjects = request.form["subjects"]
        student.update_student(id, name, age, grade, subjects)
        return redirect(url_for("view_all_students"))
    return render_template("update_student.html")


@app.route("/delete_student/<int:id>", methods=["GET", "POST"])
def delete_student(id):
    name = student.get_student_name(id)
    if request.method == "POST":
        condition = request.form.get("argument")
        if condition == "true":
            student.delete_student(id)
        return redirect(url_for("view_all_students"))
    return render_template("delete_student.html", name=name, id=id)


if __name__ == "__main__":
    app.run(debug=True)
    student.create_table()
