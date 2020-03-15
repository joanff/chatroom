

class chatroomORMException(Exception):
    def __init__(self, message):
       self.message = message

    def __str__(self):
        repre_str = {'Error Class':self.__class__.__name__, 'message':self.message}
        return repre_str
