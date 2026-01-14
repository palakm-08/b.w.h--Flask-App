from flower import app
from flask import render_template
from flower.models import products

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
