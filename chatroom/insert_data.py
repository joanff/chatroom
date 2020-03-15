from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from chatroom.models import Room, User, Like, Message


engine = create_engine('mysql://root:1234@db:3306/chatroom2')

Session = sessionmaker(bind=engine)
session = Session()

room = Room('room1')
session.add(room)

room = Room('room2')
session.add(room)

session.commit()

msg = Message('today is rainy', 1)
session.add(msg)

msg = Message('cat is cute', 2)
session.add(msg)

session.commit()

user = User('jack')
session.add(user)

user = User('lola')
session.add(user)

session.commit()

like = Like(1,2)
session.add(like)

like = Like(2,1)
session.add(like)

session.commit()