from setup import db, ma
from marshmallow import fields
from datetime import datetime
from marshmallow.validate import Regexp, Length, And


class Journal(db.Model):
    __tablename__ = 'journals'
    
    id = db.Column(db.Integer, primary_key=True)
    
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    data_created = db.Column(db.Date, default=datetime.now().strftime("%Y-%m-%d"))
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='journals')
    feedbacks = db.relationship('Feedback', back_populates='journal')



class JournalSchema(ma.Schema):
    user = fields.Nested('UserSchema', exclude=['password'])
    feedbacks = fields.Nested('FeedbackSchema', many=True, exclude=['journal'])

    title = fields.String(required=True, validate=And(
        Regexp('^[0-9a-zA-Z ]+$', error='Title must contain only letters, numbers and spances'),
        Length(min=3, error='Title must be at least 3 characters long')
    ))
	
    class Meta:
        fields = ('id', 'title', 'description', 'data_created', 'user', 'feedbacks')

