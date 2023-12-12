from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from setup import db
from models.journal import Journal, JournalSchema
from auth import authorize
from blueprints.feedbacks_bp import feedbacks_bp

journals_bp = Blueprint('journals', __name__, url_prefix='/journals')

journals_bp.register_blueprint(feedbacks_bp)

# Get all journals
@journals_bp.route('/')
@jwt_required()
def all_journals():
    stmt = db.select(Journal) 
    journals = db.session.scalars(stmt).all()
    return JournalSchema(many=True, exclude=['user.journals']).dump(journals)

# Get one journal
@journals_bp.route('/<int:id>')
@jwt_required()
def one_journal(id):
    stmt = db.select(Journal).filter_by(id=id) 
    journal = db.session.scalar(stmt)
    if journal:
        return JournalSchema().dump(journal)
    else:
        return {'error': 'Journal not found'}, 404

# Post a new journal
@journals_bp.route('/', methods=['POST'])
@jwt_required()
def create_journal():
    journal_info = JournalSchema(exclude=["id", "data_created"]).load(request.json)
    journal = Journal(
        title = journal_info['title'],
        description = journal_info.get('description', ''),
        user_id = get_jwt_identity()
    )
    db.session.add(journal)
    db.session.commit()
    return JournalSchema().dump(journal), 201

# Allows only admin or the user themselves to update a journal from database
@journals_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_journal(id):
    journal_info = JournalSchema(exclude=["id", "data_created"]).load(request.json)
    stmt = db.select(Journal).filter_by(id=id) 
    journal = db.session.scalar(stmt)
    if journal:
        authorize(journal.user_id)
        journal.title = journal_info.get('title', journal.title)
        journal.description = journal_info.get('description', journal.description)
        db.session.commit()
        return JournalSchema().dump(journal)
    else:
        return {'error': 'Journal not found'}, 404
    
# Delete a journal if the user is admin
@journals_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_journal(id):
    authorize()
    stmt = db.select(Journal).filter_by(id=id) 
    journal = db.session.scalar(stmt)
    if journal:
        authorize(journal.user_id)
        db.session.delete(journal)
        db.session.commit()
        return {}, 200
    else:
        return {'error': 'Journal not found'}, 404
    