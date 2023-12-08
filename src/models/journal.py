from setup import db, ma
from datetime import datetime



class Journal(db.Model):
	__tablename__ = 'journals'

	id = db.Column(db.Integer, primary_key=True)

	title = db.Column(db.String(100), nullable=False)
	description = db.Column(db.Text)
	data_created = db.Column(db.Date, default=datetime.now().strftime("%Y-%m-%d"))

class JournalSchema(ma.Schema):
	class Meta:
		fields = ('id', 'title', 'description', 'data_created')

