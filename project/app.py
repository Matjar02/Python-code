from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from models import db, User

app = Flask(__name__)
app.secret_key = 'jdsjsdjdsjsddsj'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)
bcrypt = Bcrypt(app)

with app.app_context():
    db.create_all()
#users = {
#    "admin": "password123",
#    "user": "test123"
#}

@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        
        if user and bcrypt.check_password_hash(user.password, request.form['password']):
            session['username'] = user.username
            flash('Logged in successfully!', category='success')
            return redirect(url_for('home'))
        else:
            flash("Incorrect login or password", category='error')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        if User.query.filter_by(username=username).first():
            flash('User already exists', category='error')
        else:
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash('The account has been created', category='success')
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logout', category='success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
