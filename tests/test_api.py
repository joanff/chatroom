from requests import get, post


# Retrieving a list of rooms
res = get('http://localhost:5000/get_rooms').json()
print(res)


# Retrieving messages from a room
res = get('http://localhost:5000/get_msg', json={'room_id':10}).json()
print(res)


# Creating rooms
# add a room named: testroom2
res = post('http://localhost:5000/create_room', json={'room':{'name':'testroom5'}}).json()
print(res)
#
#
# Adding messages to rooms
# add a message content='test content two', room_id=2
res = post('http://localhost:5000/add_msg', json={'message':{'content':'test content kaka', 'room_id':3}}).json()
print(res)

# "liking" a message
# add a like user_id=1, room_id=1
res = post('http://localhost:5000/add_like', json={'user_id':2, 'message_id':3}).json()
print(res)

