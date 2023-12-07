from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://journal_dev:1234@127.0.0.1:5432/journal"

db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)


class Journal(db.Model):
	__tablename__ = 'journals'

	id = db.Column(db.Integer, primary_key=True)

	title = db.Column(db.String(100), nullable=False)
	description = db.Column(db.Text)
	data_created = db.Column(db.Date, default=datetime.now().strftime("%Y-%m-%d"))

class JournalSchema(ma.Schema):
	class Meta:
		fields = ('id', 'title', 'description', 'data_created')

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String, default='Annonymous')
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)


class UserSchema(ma.Schema):
	class Meta:
		fields = ('id', 'name', 'email', 'password', 'is_admin')


@app.cli.command('db_create')
def db_create():
	db.drop_all()
	db.create_all()
	print('Created tables')

@app.cli.command('db_seed')
def db_seed():
	users = [
		User(
			email='admin@spam.com',
			password=bcrypt.generate_password_hash('admin123').decode('utf8'),
			is_admin=True
		),
		User(
			name='Ben',
			email='ben@spam.com',
			password=bcrypt.generate_password_hash('ben12345').decode('utf8'),
		)
	]


	journals = [
		Journal(
			title = 'On boarding',
			description = 'Learning history of the company',
			data_created = date.today()
		),
		Journal(
			title = 'Presentation',
			description = 'Give a speech in front of everyone',
			data_created = date.today()
		),
		Journal(
			title = 'Role play',
			description = 'Train to know how to sale',
			data_created = date.today()
		)
	]

	db.session.add_all(users)
	db.session.commit()
	db.session.add_all(journals)
	db.session.commit()
	print('Database seeded')


@app.route('/users/register', methods=['POST'])
def register():
	user_info = UserSchema().load(request.json)
	user = User(
		email=user_info['email'],
		password=bcrypt.generate_password_hash(user_info['password']).decode('utf8'),
		name=user_info.get('name', '')
	)

	db.session.add(user)
	db.session.commit()

	return UserSchema(exclude=['password']).dump(user), 201

@app.route('/journals')
def all_journals():
    stmt = db.select(Journal) 
    journals = db.session.scalars(stmt).all()
    return JournalSchema(many=True).dump(journals)




@app.route('/')
def hello():
	return 'Hello, world!'
