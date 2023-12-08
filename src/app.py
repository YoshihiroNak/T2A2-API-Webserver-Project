from flask import request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta
from os import environ
from models.user import User, UserSchema
from models.journal import Journal, JournalSchema
from setup import app, db, ma, bcrypt, jwt
from blueprints.cli_bp import db_commands
from blueprints.users_bp import users_bp


def authorize(user_id=None):
    jwt_user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id=jwt_user_id)
    user = db.session.scalar(stmt)
    # If it's not the case that the user is an admin ot user_id truthy and matches the token
    # i.e. if user_id isn't passed in, they must be admin
    if not (user.is_admin or (user_id and jwt_user_id == user_id)):
        abort(401)
    
@app.errorhandler(401)
def unauthorized(err):
    return {'error': 'You are not authorized to access this resource'}

app.register_blueprint(db_commands)
app.register_blueprint(users_bp)

	

@app.route('/journals')
@jwt_required()
def all_journals():
    stmt = db.select(Journal) 
    journals = db.session.scalars(stmt).all()
    return JournalSchema(many=True).dump(journals)




@app.route('/')
def hello():
	return 'Hello, world!'
