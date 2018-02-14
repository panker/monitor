from app import db

class User(db.Model):
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80) , unique=True)
    password = db.Column(db.String(32), unique=True)
    headimg = db.Column(db.String(32), unique=False)

    def __init__(self, id, username, password,headimg):
        self.id = id
        self.username = username
        self.password = password
        self.headimg = headimg

    def __repr__(self):
        return '<User %r>' % self.username