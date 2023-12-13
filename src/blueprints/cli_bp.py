
from flask import Blueprint
from setup import db, bcrypt
from models.journal import Journal
from models.user import User
from models.feedback import Feedback
from datetime import date

db_commands = Blueprint('db' , __name__) 

# db_create drops all tables and then creates all tables.
@db_commands.cli.command('create')
def db_create():
	db.drop_all()
	db.create_all()
	print('Created tables')

# db_seed is the function that adds data to the database table columns.
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

	db.session.add_all(users)
	db.session.commit()

	journals = [
		Journal(
			title = 'On boarding',
			description = 'Learning history of the company',
			data_created = date.today(),
            user_id = users[0].id
		),
		Journal(
			title = 'Presentation',
			description = 'Give a speech in front of everyone',
			data_created = date.today(),
            user_id = users[1].id
		),
		Journal(
			title = 'Role play',
			description = 'Perform to sale in front of everyone',
			data_created = date.today(),
            user_id = users[0].id
		),
	]


	db.session.add_all(journals)
	db.session.commit()

	feedbacks = [
        Feedback(
            message = "Feedback 1",
            user_id = users[0].id,
            journal_id = journals[1].id
        ),
        Feedback(
            message = "Feedback 2",
            user_id = users[1].id,
            journal_id = journals[1].id
        ),
        Feedback(
            message = "Feedback 3",
            user_id = users[2].id,
            journal_id = journals[0].id
        )
    ]
	
	db.session.add_all(feedbacks)
	db.session.commit()
	print('Database seeded')
