from flask import Flask, render_template

app = Flask(__name__)


# 「/」へアクセスがあった場合に、'Hello World'の文字列を返す
@app.route('/')
def hello():
    return 'Hello World'


#「/index」へアクセスがあった場合に、「index.html」を返す
@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)