from flask import Blueprint, request, jsonify
from app.models import db, User
from flask_jwt_extended import create_access_token

user_bp = Blueprint('user', __name__)

@user_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    new_user = User(
        name=data['name'],
        mobile=data['mobile'],
        email=data['email'],
        password=data['password']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully!"}), 201

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity={'email': user.email})
        return jsonify(access_token=access_token)
    return jsonify({"message": "Invalid credentials"}), 401

@user_bp.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.name for user in users])

@user_bp.route('/search', methods=['GET'])
def search_users():
    name = request.args.get('name')
    users = User.query.filter(User.name.ilike(f'%{name}%')).all()
    return jsonify([user.name for user in users])
