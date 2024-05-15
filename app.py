from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Pantera55285'

db.init_app(app)


def create_tables():
    with app.app_context():
        db.create_all()


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

    if password != confirm_password:
        flash('Пароли не совпадают!', 'error')
        return redirect(url_for('personal_area'))

    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    flash('Регистрация прошла успешно!', 'success')
    return redirect(url_for('personal_area'))


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    user = User.query.filter_by(username=username, password=password).first()
    if user:
        flash('Вход выполнен успешно!', 'success')
        return redirect(url_for('personal_area'))
    else:
        flash('Неверный логин или пароль!', 'error')
        return redirect(url_for('personal_area'))


if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
