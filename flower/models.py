from werkzeug.security import generate_password_hash, check_password_hash
from flower import db, app

class User(db.Model):
    u_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    u_name = db.Column(db.String(100), nullable=False)
    u_age = db.Column(db.Integer(), nullable=False)
    u_email = db.Column(db.String(120), nullable=False, unique=True)
    u_items = db.relationship('products', backref='owned_user', lazy=True)


class products(db.Model):
    p_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    p_name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)
    image = db.Column(db.String(300), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey('u_id'))
    
with app.app_context():
    db.create_all()
