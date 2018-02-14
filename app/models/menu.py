from app import db

class Menu(db.Model):
    __tablename__ = "menu"

    id = db.Column(db.Integer , primary_key=True)
    top_id = db.Column(db.Integer)
    content = db.Column(db.String(128))
    url = db.Column(db.String(255))
    icon = db.Column(db.String(128))

    def __init__(self, id, top_id, content, url, icon):
        self.id = id
        self.top_id = top_id
        self.content = content
        self.url = url
        self.icon = icon

