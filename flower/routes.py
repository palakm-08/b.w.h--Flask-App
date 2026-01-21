from flower import app
from flask import render_template
from flower.models import products
from flower.forms import RegisterForm

@app.route('/')
@app.route('/home')
def home_pg():
    return render_template('home.html')

@app.route('/profile/register')
def create_account():
    form = RegisterForm()
    return render_template('regForm.html', form=form)

@app.route('/shop')
def shop_products():
    all_products= products.query.all()
    return render_template('shop.html', items=all_products)
