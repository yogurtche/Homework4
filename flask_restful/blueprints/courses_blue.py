from flask import Blueprint, request, render_template
from flask import jsonify

courses_list = [
    {"id": 1, "name": "COS250"},
    {"id": 2, "name": "COS350"},
    {"id": 3, "name": "COS450"}
]

course_blue = Blueprint('course_blue', __name__, template_folder='templates')
    

          
@course_blue.route("/<int:course_id>/<name>", methods=['POST', 'PUT'])             #POST AND PUT   
def course_put_post(course_id,name):
    if request.method == 'POST':
        id_exist = False
        for i in range(len(courses_list)):
            if courses_list[i-1]['id'] == course_id:
                id_exist = True
    
        if id_exist == False:
            courses_list.append(dict({'id': course_id, 'name': name}))
            return jsonify(courses_list)
        else:
            return "The ID already exists!"

    else:
        for a in courses_list:
            if a["id"] == course_id:
                a.update({'name': name})
                return jsonify(a)

        courses_list.append(dict({'id': course_id, 'name': name}))
        return jsonify(courses_list)
    


@course_blue.route("/<int:course_id>", methods=['GET', 'DELETE'])     
def course_delete_get(course_id):
    if request.method == 'GET':
        flag = False
        for course in courses_list:
            if course["id"] == course_id:
                flag = True
                return jsonify(course)
        if flag == False:    
            return "ID was not found!"

    else:
        flag = False
        for i in range(len(courses_list)): 
            if courses_list[i]['id'] == course_id: 
                del courses_list[i]
                flag = True
                return "Course deleted succesfully!"

        if flag == False:
            return "ID was not found!"


@course_blue.route("/all", methods=['GET'])   
def get_all():
    return render_template('course.html', courses=courses_list)
