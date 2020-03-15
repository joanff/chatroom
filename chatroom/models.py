from sqlalchemy import ForeignKey,Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import json
from chatroom.exception import chatroomORMException

engine = create_engine('mysql://root:1234@db:3306/chatroom2')
Base = declarative_base()

class Room(Base):
    __tablename__ = "room"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))

    def __init__(self, username):
        """"""
        self.name = username

    def dict_from_class(self):
        return {'id': self.id, 'name': self.name}

    @staticmethod
    def get_rooms():
        Session = sessionmaker(bind=engine)
        session = Session()

        rooms = session.query(Room).order_by(Room.id).all()
        res_rooms = [r.dict_from_class() for r in rooms]
        return res_rooms

    def dict_from_class(self):
        return {'id': self.id, 'name': self.name}

    def json_repre(self):
        dict = self.dict_from_class()
        return json.dumps(dict)

    def add(self):
        Session = sessionmaker(bind=engine)
        session = Session()

        session.add(self)

        session.commit()
        session.refresh(self)
        return self.id



class Message(Base):
    __tablename__ = "message"

    id = Column(Integer, primary_key=True)
    content = Column(String(200))
    room_id = Column(Integer, ForeignKey('room.id'))
    likes = relationship("Like", uselist=True)
    # likes = relationship("Like", back_populates="messages")

    def __init__(self, content, room_id):
        """"""
        self.content = content
        self.room_id = room_id

    def dict_from_class(self):
        likes_dict = [l.dict_from_class() for l in self.likes]
        return {'id': self.id, 'content': self.content, 'room_id': self.room_id, 'likes':likes_dict}

    def json_repre(self):
        dict = self.dict_from_class()
        return json.dumps(dict)

    @staticmethod
    def get_by_roomid(room_id):
        Session = sessionmaker(bind=engine)
        session = Session()

        messages = session.query(Message).filter(Message.room_id == room_id).all()
        response = [m.dict_from_class() for m in messages]
        return response

    def add(self):
        try:
            Session = sessionmaker(bind=engine)
            session = Session()

            session.add(self)

            session.commit()
            session.refresh(self)
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            return chatroomORMException(error)
        return self.id


class Like(Base):
    __tablename__ = "likes"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    message_id = Column(Integer, ForeignKey('message.id'))
    user = relationship("User", uselist=False)

    def __init__(self, user_id, message_id):
        """"""
        self.user_id = user_id
        self.message_id = message_id

    def dict_from_class(self):
        return {'id': self.id, 'user_id': self.user_id, 'user_name':self.user.name, 'message_id': self.message_id}

    @staticmethod
    def get(id):
        Session = sessionmaker(bind=engine)
        session = Session()

        like = session.query(Like).filter(Like.id == id).first()
        print('like_id', like.id)
        print(like.user)
        return like

    def add(self):
        try:
            Session = sessionmaker(bind=engine)
            session = Session()

            session.add(self)

            session.commit()
            session.refresh(self)

        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            return chatroomORMException(error)
        return self.id



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))

    def __init__(self, name):
        """"""
        self.name = name

    def __str__(self):
        return "{}, {}".format(self.id, self.name)


if __name__ == "__main__":
    engine = create_engine('mysql://root:1234@db')
    engine.execute("CREATE DATABASE chatroom2")
    engine.execute("USE chatroom2")

    # create tables
    Base.metadata.create_all(engine)