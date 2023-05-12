from application import db
from marshmallow import Schema, fields, validate


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f'<{self.__class__.__name__}>:{self.name} {self.age}'


class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    age = fields.Integer(required=True)
    email = fields.String(required=True)

user_schema = UserSchema()
