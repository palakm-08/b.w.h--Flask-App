from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:palak_1008@localhost:5432/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class products(db.Model):
    p_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    p_name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)
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
    items = [
        {'p_id' : 1, 'p_name' : 'Lily', 'price' : 30, 'image' : 'lily.jpg', 'desc' : 'Elegant white bloom'},
        {'p_id' : 2, 'p_name' : 'Sunflower', 'price' : 100, 'image' : 'sunflower.jpg', 'desc' : 'Bright summer delight'},
        {'p_id' : 3, 'p_name' : 'Rose', 'price' : 20, 'image' : 'rose.jpg', 'desc' : 'Classic romantic flower'},
        {'p_id' : 4, 'p_name' : 'Daisy', 'price' : 50, 'image' : 'daisy.jpg', 'desc' : 'Simple cheerful bloom'}
        # {'p_id' : 5, 'p_name' : 'Tullip', 'price' : 100},
        # {'p_id' : 6, 'p_name' : 'Iris', 'price' : 50},
        # {'p_id' : 7, 'p_name' : 'Freesia', 'price' : 80},
        # {'p_id' : 8, 'p_name' : 'Peony', 'price' : 200},
        # {'p_id' : 9, 'p_name' : 'Gerbera', 'price' : 75},
        # {'p_id' : 10, 'p_name' : 'Orchid', 'price' : 100},
        # {'p_id' : 11, 'p_name' : 'Carnation', 'price' : 200},
        # {'p_id' : 12, 'p_name' : 'Lavender', 'price' : 40},
        # {'p_id' : 13, 'p_name' : 'Chrysanthemum', 'price' : 100},
        # {'p_id' : 14, 'p_name' : 'Plumeria', 'price' : 50},
        # {'p_id' : 15, 'p_name' : 'Hibiscus', 'price' : 508},
    ]
    return render_template('shop.html', items=items)




if __name__ == "__main__":
    app.run(debug=True)
