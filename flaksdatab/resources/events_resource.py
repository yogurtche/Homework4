from flask_restful import Resource
from flask import jsonify

events_list = [
    {"id": 1, "event": "StartUp"},
    {"id": 2, "event": "HAIR The Musical"},
    {"id": 3, "event": "TEDxAUBG"}
]
class Event_one(Resource):
    
           
    def post(self,event_id,name):  

        id_exist = False
        for i in range(len(events_list)):
            if events_list[i-1]['id'] == event_id:
                id_exist = True
    
        if id_exist == False:
            events_list.append(dict({'id': event_id, 'name': name}))
            return jsonify(events_list)
        else:
            return "ID already exists!"

    def put(self,event_id,name):  

        for a in events_list:
            if a["id"] == event_id:
                a.update({'name': name})
                return jsonify(a)

        events_list.append(dict({'id': event_id, 'name': name}))
        return jsonify(events_list)
    
    

class Event_two(Resource):

    def delete(self, event_id):  
        flag = False
        for i in range(len(events_list)): 
            if events_list[i]['id'] == event_id: 
                del events_list[i]
                flag = True
                return "Event was succesfully deleted!"

        if flag == False:
            return "ID was not found!"
            

    def get(self, event_id):  #get method
        flag = False
        for event in events_list:
            if event["id"] == event_id:
                flag = True
                return jsonify(event)
        if flag == False:    
            return "ID  was not found!"
      

class All_events(Resource):
    def get(self):
        return jsonify(events_list)
