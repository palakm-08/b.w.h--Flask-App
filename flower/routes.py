from flower import app
from flask import render_template, redirect, url_for, flash
from flower.models import products, User
from flower.forms import RegisterForm
from flower import db

@app.route('/')
@app.route('/home')
def home_pg():
    return render_template('home.html')

@app.route('/profile/register', methods=['GET', 'POST'])
@app.route('/register', methods=['GET', 'POST'])
def create_account():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(
            u_name = form.username.data,
            u_email = form.user_email.data,
            password_hash = form.pass1.data
            )
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('shop_products'))
    
    if form.errors != {}:
        for error_msg in form.errors.values():
            flash(f"There was an error with creating a user : {error_msg}", category='danger')
    return render_template('regForm.html', form=form)

@app.route('/shop')
def shop_products():
    all_products= products.query.all()
    return render_template('shop.html', items=all_products)
