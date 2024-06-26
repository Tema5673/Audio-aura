from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Pantera55285'

db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Initialize Flask-Migrate

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    tags = db.Column(db.String(150), nullable=True)

@app.route('/')
def index():
    return render_template('main/search.html')

@app.route('/personal_area', methods=['GET', 'POST'])
def personal_area():
    return render_template('main/personal_area.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm-password']

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        flash('Пользователь с таким логином уже существует!', 'error')
        return jsonify({'status': 'error'}), 409

    if password != confirm_password:
        flash('Пароли не совпадают!', 'error')
        return jsonify({'status': 'error'}), 400

    new_user = User(username=username, password=password, tags='Registered User')
    db.session.add(new_user)
    db.session.commit()
    flash('Регистрация прошла успешно!', 'success')
    return jsonify({'status': 'success'}), 200

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    user = User.query.filter_by(username=username).first()
    if user:
        if user.password == password:
            flash('Вход выполнен успешно!', 'success')
            return jsonify({'status': 'success'}), 200
        else:
            flash('Неверный пароль!', 'error')
            return jsonify({'status': 'wrong_password'}), 401
    else:
        flash('Такого пользователя не существует!', 'error')
        return jsonify({'status': 'user_not_found'}), 404

@app.route('/logout')
def logout():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
