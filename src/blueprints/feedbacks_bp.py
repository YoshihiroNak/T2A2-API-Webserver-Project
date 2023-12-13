from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from setup import db
from models.feedback import Feedback, FeedbackSchema
from auth import authorize

feedbacks_bp = Blueprint('feedbacks', __name__, url_prefix='/<int:journal_id>/feedbacks')


# @feedbacks_bp.route('/')
# @jwt_required()
# def all_feedbacks():
#     stmt = db.select(Feedback) 
#     feedbacks = db.session.scalars(stmt).all()
#     return FeedbackSchema(many=True, exclude=['user.feedbacks']).dump(feedbacks)

# @feedbacks_bp.route('/<int:id>')
# @jwt_required()
# def one_feedback(id):
#     stmt = db.select(Feedback).filter_by(id=id) 
#     feedback = db.session.scalar(stmt)
#     if feedback:
#         return FeedbackSchema().dump(feedback)
#     else:
#         return {'error': 'Feedback not found'}, 404

# Post a new feedback
@feedbacks_bp.route('/', methods=['POST'])
@jwt_required()
def create_feedback(journal_id):
    feedback_info = FeedbackSchema(only=['message']).load(request.json)
    feedback = Feedback(
        message = feedback_info['message'],
        user_id = get_jwt_identity(),
        journal_id = journal_id
    )
    db.session.add(feedback)
    db.session.commit()
    return FeedbackSchema().dump(feedback), 201

# Allows only admin or the user themselves to update a feedback from database
@feedbacks_bp.route('/<int:feedback_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_feedback(journal_id, feedback_id):
    feedback_info = FeedbackSchema(only=['message']).load(request.json)
    stmt = db.select(Feedback).filter_by(id=feedback_id) 
    feedback = db.session.scalar(stmt)
    if feedback:
        authorize(feedback.user_id)
        feedback.message = feedback_info.get('message', feedback.message)
        db.session.commit()
        return FeedbackSchema().dump(feedback)
    else:
        return {'error': 'Feedback not found'}, 404
    
# Allows only admin or the user themselves to delete a feedback from database
@feedbacks_bp.route('/<int:feedback_id>', methods=['DELETE'])
@jwt_required()
def delete_feedback(journal_id, feedback_id):
    stmt = db.select(Feedback).filter_by(id=feedback_id) 
    feedback = db.session.scalar(stmt)
    if feedback:
        authorize(feedback.user_id)
        db.session.delete(feedback)
        db.session.commit()
        return {}, 200
    else:
        return {'error': 'Feedback not found'}, 404
    
    