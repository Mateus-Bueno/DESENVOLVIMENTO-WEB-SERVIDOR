# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    return render_template('index.html', current_time = datetime.utcnow())

@app.route('/user/<name>/<id>/<institution>')
def name(name, id, institution):
    return render_template('user.html', name = name, id = id, institution = institution)

@app.route('/contextorequisicao/<name>')
def contextorequisicao(name):
    return render_template('contextorequisicao.html', name = name, user_agent = request.headers.get('User-Agent'), user_ip = request.remote_addr, app_host = request.host)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
 return render_template('500.html'), 500