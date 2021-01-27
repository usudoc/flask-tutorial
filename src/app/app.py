from flask import Flask, render_template, request
from models.models import CourtInfo

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    name = request.args.get('name')
    # spot = ['並榎', '問屋', '県スポ', '山形']
    all_spot = CourtInfo.query.all()
    print(all_spot)
    return render_template('index.html', name=name, all_spot=all_spot)


@app.route('/index', methods=['post'])
def post():
    name = request.form['name']
    all_spot = CourtInfo.query.all()
    return render_template('index.html', name=name, all_spot=all_spot)


if __name__ == '__main__':
    app.run(debug=True)