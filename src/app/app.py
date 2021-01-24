from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    name = request.args.get('name')
    spot = ['並榎', '問屋', '県スポ', '山形']
    return render_template('index.html', name=name, spot=spot)


if __name__ == '__main__':
    app.run(debug=True)