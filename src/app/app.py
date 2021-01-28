from flask import Flask, render_template, request
from models.models import CourtInfo
from models.database import db_session
from datetime import datetime


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    name = request.args.get('name')
    # spot = ['並榎', '問屋', '県スポ', '山形']
    all_info = CourtInfo.query.all()
    print('all_info:', all_info)
    return render_template('index.html', name=name, all_info=all_info)


@app.route('/index', methods=['post'])
def post():
    name = request.form['name']
    all_info = CourtInfo.query.all()
    return render_template('index.html', name=name, all_info=all_info)


@app.route('/add', methods=['post'])
def add():
    name = request.form['name']
    type = request.form['type']
    content = CourtInfo(name, type, datetime.now())
    db_session.add(content)
    db_session.commit()
    return index()


@app.route('/update', methods=['post'])
def update():
    content = CourtInfo.query.filter_by(id=request.form['update']).first()
    content.name = request.form['name']
    content.type = request.form['type']
    db_session.commit()
    return index()


@app.route('/delete', methods=['post'])
def delete():
    id_list = request.form.getlist('delete')
    for id in id_list:
        content = CourtInfo.query.filter_by(id=id).first()
        db_session.delete(content)
    db_session.commit()
    return index()


if __name__ == '__main__':
    app.run(debug=True)