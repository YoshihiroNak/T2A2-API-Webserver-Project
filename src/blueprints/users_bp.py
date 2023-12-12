from flask import Blueprint, request
from models.user import User, UserSchema
from setup import bcrypt, db
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, jwt_required
from datetime import timedelta
from auth import authorize


users_bp = Blueprint('users', __name__, url_prefix='/users')


@users_bp.route('/register', methods=['POST'])
@jwt_required()
def register():
    authorize()
    try:
        user_info = UserSchema(exclude=['id', 'is_admin']).load(request.json)
        user = User(
			email=user_info['email'],
			password=bcrypt.generate_password_hash(user_info['password']).decode('utf8'),
			name=user_info.get('name', '')
		)
        db.session.add(user)
        db.session.commit()
        
        return UserSchema(exclude=['password']).dump(user), 201
    except IntegrityError:
        return {'error': 'Email address already in use'}, 409

# Allows admin to get all users
@users_bp.route('/')
@jwt_required()
def all_users():
    authorize() # Admin only

    stmt = db.select(User)
    users = db.session.scalars(stmt).all()
    return UserSchema(many=True, exclude=['password']).dump(users)


@users_bp.route('/login', methods=['POST'])
def login():
    # Parse incoming POST body through the schema
    user_info = UserSchema(exclude=['id', 'name', 'is_admin']).load(request.json)

    # Select user with email that matches the one in the POST body
    # Check password hask
    stmt = db.select(User).where(User.email==user_info['email'])
    user = db.session.scalar(stmt)
    if user and bcrypt.check_password_hash(user.password, user_info['password']):

        # Create a JWT token
        token = create_access_token(identity=user.id, expires_delta=timedelta(hours=3))

        # Rerurn the token
        return {'token': token, 'user': UserSchema(exclude=['password','journals']).dump(user)}
    else:
        return {'error': 'Invalid email or password'}, 401

# Allows only admin or the user themselves to delete the user from database
@users_bp.route('/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    try:
        stmt = db.select(User).filter_by(id=user_id) 
        user = db.session.scalar(stmt)
        if user:
            authorize(user_id)
            db.session.delete(user)
            db.session.commit()
            return {}, 200
        else:
            return {'error': 'User not found'}, 404
    except AttributeError:
        return {'error': 'You are not authorized to delete the user'}, 401 