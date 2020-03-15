from flask import Flask
from flask import jsonify, make_response
from chatroom.models import Room, Message, Like
from flask_restful import reqparse, abort, Api, Resource, request
from chatroom.exception import chatroomORMException
from chatroom import logger

app = Flask(__name__)
api = Api(app)

error_message = {
    "errors": [
        {
            "code":400,
            "message":"Bad request data."
        }
    ]
}

class RoomListAPI(Resource):
    def get(self):
        logger.info('{} get method'.format(self.__class__ ))
        rooms = Room.get_rooms()
        response = jsonify({"rooms":rooms})
        return response


class RoomAPI(Resource):
    def post(self):
        logger.info('{} post method'.format(self.__class__ ))
        request_json = request.json
        content = request_json['room']
        room_name = content['name']
        newroom = Room(room_name)
        roomid = newroom.add()
        return roomid, 201

class MsgAPI(Resource):
    def get(self):
        logger.info('{} get method'.format(self.__class__ ))
        request_json = request.json
        room_id = request_json['room_id']
        messages = Message.get_by_roomid(room_id)
        response = jsonify({"messages":messages})
        return response

    def post(self):
        logger.info('{} post method'.format(self.__class__))
        request_json = request.json
        content = request_json['message']
        newmsg = Message(content['content'], content['room_id'])
        msgid = newmsg.add()
        if isinstance(msgid, chatroomORMException):
            return make_response(jsonify(msgid.__str__()), 400)
        return msgid, 201

class LikeAPI(Resource):
    def post(self):
        logger.info('{} post method'.format(self.__class__))
        request_json = request.json
        like = Like(request_json['user_id'], request_json['message_id'])
        likeid = like.add()
        if isinstance(likeid, chatroomORMException):
            return make_response(jsonify(likeid.__str__()), 400)
        return likeid, 201

api.add_resource(RoomListAPI, '/get_rooms')
api.add_resource(RoomAPI, '/get_room', '/create_room')
api.add_resource(MsgAPI, '/add_msg', '/get_msg')
api.add_resource(LikeAPI, '/add_like')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')