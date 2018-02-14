from app import db

class Game(db.Model):
    __tablename__ = 'game'

    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(128))
    code = db.Column(db.String(128))
    log_server = db.Column(db.String(128))

    def __init__(self , id , name , code , log_server):
        self.id = id
        self.name = name
        self.code = code
        self.log_server = log_server



