from flask import Flask, render_template, request, redirect
import hackbright_app

app = Flask(__name__)

@app.route("/")
def get_github():
    hackbright_app.connect_to_db()
    return render_template("get_github.html")

@app.route("/student")
def get_student():
    hackbright_app.connect_to_db()
    student_github = request.args.get("student")
    name = hackbright_app.get_student_by_github(student_github)
    # first_name=name[0]
    # last_name=name[1]
    # github=name[2]
    grades = hackbright_app.student_grades(name[0], name[1])
    html = render_template("student_info.html", first_name = name[0],
                                                last_name = name[1],
                                                github = name[2],
                                                grades = grades)
    return html

@app.route("/project")
def get_project():
    hackbright_app.connect_to_db()
    project = request.args.get("project")
    project_details = hackbright_app.get_project_grades(project)
    description = hackbright_app.get_projects_by_title(project)

    html = render_template("project_info.html", project_title = description[0],
                                                description = description[1],
                                                max_grade = description[2],
                                                students = project_details)

    return html

@app.route("/add_new_student")
def add_new_student():
    hackbright_app.connect_to_db()
    return render_template("insert_new_student.html")


@app.route("/new_student", methods = ["POST"])
def new_student():
    hackbright_app.connect_to_db()

    new_student_firstname = request.form.get("firstname")
    new_student_lastname = request.form.get("lastname")
    new_student_github = request.form.get("github")
    #if new_student_firstname != None:
    #if 
    hackbright_app.make_new_student(new_student_firstname, 
                                    new_student_lastname, 
                                    new_student_github)

    return redirect("/student?student=%s" % new_student_github)
    #else:
    #    error = "error message"

        #new student is either already in the system or was entered incorrectly
        #try again


@app.route("/add_new_project")
def add_new_project():
    hackbright_app.connect_to_db()
    return render_template("insert_new_project.html")


@app.route("/new_project", methods = ["POST"])
def new_project():
    hackbright_app.connect_to_db()

    new_project_title = request.form.get("title")
    new_project_description = request.form.get("description")
    new_project_max_grade = request.form.get("max_grade")
    hackbright_app.make_new_project(new_project_title, new_project_description, new_project_max_grade)

    return redirect("/project?project=%s" % new_project_title)

    # returns an empty list! Need to fix this

if __name__=="__main__":
    app.run(debug=True)

