from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:palak_1008@localhost:5432/flower'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class products(db.Model):
    p_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    p_name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)
    image = db.Column(db.String(300), nullable=False)
    desc = db.Column(db.String(500), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
@app.route('/home')
def home_pg():
    return render_template('home.html')

@app.route('/about/<username>')
def about_pg(username):
    return f'<h1>About {username}</h1>'

@app.route('/shop')
def shop_products():
    all_products= products.query.all()
    return render_template('shop.html', items=all_products)




if __name__ == "__main__":
    app.run(debug=True)
