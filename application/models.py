from application import db


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f'<{self.__class__.__name__}>:{self.name} {self.age}'
