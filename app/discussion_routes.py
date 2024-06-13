from flask import Blueprint, request, jsonify
from app.models import db, Discussion

discussion_bp = Blueprint('discussion', __name__)

@discussion_bp.route('/', methods=['POST'])
def create_discussion():
    data = request.get_json()
    new_discussion = Discussion(
        user_id=data['user_id'],
        text=data['text'],
        image=data.get('image'),
        hashtags=data.get('hashtags')
    )
    db.session.add(new_discussion)
    db.session.commit()
    return jsonify({"message": "Discussion created successfully!"}), 201

@discussion_bp.route('/', methods=['GET'])
def get_discussions():
    discussions = Discussion.query.all()
    return jsonify([discussion.text for discussion in discussions])

@discussion_bp.route('/search/tags', methods=['GET'])
def search_discussions_by_tags():
    tags = request.args.get('tags')
    discussions = Discussion.query.filter(Discussion.hashtags.ilike(f'%{tags}%')).all()
    return jsonify([discussion.text for discussion in discussions])

@discussion_bp.route('/search/text', methods=['GET'])
def search_discussions_by_text():
    text = request.args.get('text')
    discussions = Discussion.query.filter(Discussion.text.ilike(f'%{text}%')).all()
    return jsonify([discussion.text for discussion in discussions])
