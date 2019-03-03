from flask import Flask, jsonify, render_template
from blueprints.students_blue import student_blue
from blueprints.courses_blue import course_blue
from blueprints.events_blue import event_blue


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

    
app.register_blueprint(student_blue, url_prefix='/v1/student')

app.register_blueprint(event_blue, url_prefix='/v2/event')

app.register_blueprint(course_blue, url_prefix='/v3/course')