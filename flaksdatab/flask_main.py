''' Docstring '''

from flask import Flask, jsonify, render_template
from extn import db
from models.models import StudentsModel
from models.models import CoursesModel
from models.models import EventsModel
import json
from flask import request
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'some-secret-string'

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/v3/event/<int:id_number1>/<name1>', methods=["POST", "PUT"])    
def create_event(id_number1, name1):
    if request.method == "POST":
        event = EventsModel(id_number=id_number1, name=name1)
        db.session.add(event)
        db.session.commit()
        return jsonify({'message': 'New event successfully created.'}), 200
    else:
        event = EventsModel.query.get(id_number1)
        event.name = name1
        db.session.commit()
        return jsonify({'message': 'Event was successfully updated.'}), 200

@app.route('/v3/event/<int:id_number1>', methods=["GET", "DELETE"])
def get_event(id_number1):
    if request.method == "GET":
        return render_template('screen.html', item = EventsModel.query.filter_by(id_number=id_number1) )
    else:
        EventsModel.query.filter_by(id_number=id_number1).delete()
        db.session.commit()
        return jsonify({'message': 'Event was successfully deleted.'}), 200

@app.route('/v3/event/all', methods=['GET'])
def get_all_events():
    return render_template('screen_all_components.html', items = EventsModel.query.all() )
    

@app.route('/v1/student/<int:id_number1>/<name1>', methods=["POST", "PUT"]) 
def create_student(id_number1, name1):
    if request.method == "POST":
        student = StudentsModel(id_number=id_number1, name=name1)
        db.session.add(student)
        db.session.commit()
        return jsonify({'message': 'New student was successfully created.'}), 200
    else:
        student = StudentsModel.query.get(id_number1)
        student.name = name1
        db.session.commit()
        return jsonify({'message': 'Student was successfully updated.'}), 200

@app.route('/v1/student/<int:id_number1>', methods=["GET", "DELETE"])
def get_student(id_number1):
    if request.method == "GET":
        return render_template('screen.html', items = StudentsModel.query.filter_by(id_number=id_number1) )
    else:
        StudentsModel.query.filter_by(id_number=id_number1).delete()
        db.session.commit()
        return jsonify({'message': 'Student was successfully deleted.'}), 200

@app.route('/v1/student/all', methods=['GET'])
def get_all_students():
    return render_template('screen_all_components.html', items = StudentsModel.query.all() )

@app.route('/v2/course/<int:id_number1>/<name1>', methods=["POST", "PUT"]) 
def create_course(id_number1, name1):
    if request.method == "POST":
        course = CoursesModel(id_number=id_number1, name=name1)
        db.session.add(course)
        db.session.commit()
        return jsonify({'message': 'New course was successfully created.'}), 200
    else:
        course = CoursesModel.query.get(id_number1)
        course.name = name1
        db.session.commit()
        return jsonify({'message': 'Course was successfully updated.'}), 200

@app.route('/v2/course/<int:id_number1>', methods=["GET", "DELETE"])
def get_course(id_number1):
    if request.method == "GET":
        return render_template('screen.html', items = CoursesModel.query.filter_by(id_number=id_number1) )
    else:
        CoursesModel.query.filter_by(id_number=id_number1).delete()
        db.session.commit()
        return jsonify({'message': 'Student was successfully deleted.'}), 200

@app.route('/v2/course/all', methods=['GET'])
def get_all_courses():
    return render_template('screen_all_components.html', items = CoursesModel.query.all() )