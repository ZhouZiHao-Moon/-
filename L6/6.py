from flask import *

app = Flask(__name__)


@app.route('/',methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/',methods=['POST'])
def home_button():
    name = request.values.get('name')
    return redirect(url_for('hello',name=name))


@app.route('/hello/<name>',methods=['GET'])
def hello(name):
    return render_template('hello.html',name=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0')