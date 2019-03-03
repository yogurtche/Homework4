from flask import Blueprint, request, render_template
from flask import jsonify

events_list = [
    {"id": 1, "event": "StartUp"},
    {"id": 2, "event": "HAIR The Musical"},
    {"id": 3, "event": "TEDxAUBG"}
]

event_blue = Blueprint('event_blue', __name__, template_folder='templates')
    

          
@event_blue.route("/<int:event_id>/<name>", methods=['POST', 'PUT'])             #POST AND PUT   
def event_put_post(event_id,name):
    if request.method == 'POST':
        id_exist = False
        for i in range(len(events_list)):
            if events_list[i-1]['id'] == event_id:
                id_exist = True
    
        if id_exist == False:
            events_list.append(dict({'id': event_id, 'name': name}))
            return jsonify(events_list)
        else:
            return "ID already exists!"

    else:
        for a in events_list:
            if a["id"] == event_id:
                a.update({'name': name})
                return jsonify(a)

        events_list.append(dict({'id': event_id, 'name': name}))
        return jsonify(events_list)
    

@event_blue.route("/<int:event_id>", methods=['GET', 'DELETE'])     
def event_delete_get(event_id):
    if request.method == 'GET':
        flag = False
        for event in events_list:
            if event["id"] == event_id:
                flag = True
                return jsonify(event)
        if flag == False:    
            return "ID was not found!"

    else:
        flag = False
        for i in range(len(events_list)): 
            if events_list[i]['id'] == event_id: 
                del events_list[i]
                flag = True
                return "Event was deleted succesfully!"

        if flag == False:
            return "ID was not found!"

@event_blue.route("/all", methods=['GET'])   
def get_all():
    return render_template('event.html', events=events_list)