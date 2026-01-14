from flower import db, app

class products(db.Model):
    p_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    p_name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)
    image = db.Column(db.String(300), nullable=False)
    desc = db.Column(db.String(500), nullable=False)

with app.app_context():
    db.create_all()
