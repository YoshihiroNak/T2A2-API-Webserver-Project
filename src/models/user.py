from setup import db, ma
from marshmallow import fields
from marshmallow.validate import Length



class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String, default='Annonymous')
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    journals = db.relationship('Journal', back_populates='user')
    feedbacks = db.relationship('Feedback', back_populates='user')


class UserSchema(ma.Schema):
    journals = fields.Nested('JournalSchema', exclude=['user'], many=True)
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=Length(min=8, error='Password must be at least 8 characters'))

    class Meta:
        fields = ('id', 'name', 'email', 'password', 'is_admin', 'journals')
