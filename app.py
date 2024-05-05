from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main/search.html')

@app.route('/personal_area')
def personal_area():
    return render_template('main/personal_area.html')

if __name__ == '__main__':
    app.run(debug=True)
