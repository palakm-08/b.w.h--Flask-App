from werkzeug.security import generate_password_hash, check_password_hash
from flower import db, app

class User(db.Model):
    __tablename__ = 'users'
    u_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    u_name = db.Column(db.String(100), nullable=False)
    u_age = db.Column(db.Integer(), nullable=False)
    u_email = db.Column(db.String(120), nullable=False, unique=True, index=True)
    u_items = db.relationship('products', backref='owned_user', lazy=True)
    password_hash = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class products(db.Model):
    p_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    p_name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)
    image = db.Column(db.String(300), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey('users.u_id'))
    
with app.app_context():
    db.create_all()
