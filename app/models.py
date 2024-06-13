from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    mobile = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, name, mobile, email, password):
        self.name = name
        self.mobile = mobile
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')


class Discussion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    text = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(100))
    hashtags = db.Column(db.String(100))
    created_on = db.Column(db.DateTime, default=db.func.current_timestamp())
    view_count = db.Column(db.Integer, default=0)
