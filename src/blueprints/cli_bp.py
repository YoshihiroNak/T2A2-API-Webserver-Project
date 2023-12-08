
from flask import Blueprint
from setup import db, bcrypt
from models.journal import Journal
from models.user import User
from datetime import date

db_commands = Blueprint('db' , __name__) 

@db_commands.cli.command('create')
def db_create():
	db.drop_all()
	db.create_all()
	print('Created tables')

@db_commands.cli.command('seed')
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
