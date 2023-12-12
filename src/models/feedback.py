from setup import db, ma
from marshmallow import fields
from datetime import datetime



class Feedback(db.Model):
    __tablename__ = 'feedbacks'
    id = db.Column(db.Integer, primary_key=True)
    
    message = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='feedbacks')

    journal_id = db.Column(db.Integer, db.ForeignKey('journals.id'), nullable=False)
    journal = db.relationship('Journal', back_populates='feedbacks')


class FeedbackSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['id', 'name'])
    journal = fields.Nested('JournalSchema', only=['id', 'title'])
	
    class Meta:
        fields = ('id', 'message', 'user', 'journal')

