
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
  name = StringField('What is your name?', validators= [DataRequired()])
  submit = SubmitField('Submit')


app = Flask(__name__)

@app.route('/')
def index():

    return '''
    <h1>Avaliação contínua: Aula 030</h1>
    <ul>
        <li>
            <a href=/>Home</a>
        </li>
        <li>
            <a href=/user/Mateus%20Bueno/PT3025322/IFSP>Identificação</a>
        </li>
        <li>
            <a href=/contextorequisicao>Contexto da requisição</a>
        </li>
    </ul>


    '''

@app.route('/user/<name>/<id>/<institution>')
def user(name, id, institution):
    return '''
    <h1>Avaliação contínua: Aula 030</h1>
    <h2>Aluno: {}</h2>
    <h2>Prontuário: {}</h2>
    <h2>Instituição: {}</h2>
    <a href=/><p>Voltar</p></a>
    '''.format(name, id, institution)

@app.route('/contextorequisicao')
def contextorequisicao():
    user_agent = request.headers.get('User-Agent')
    user_ip = request.remote_addr
    app_host = request.host

    return '''
    <h1>Avaliação contínua: Aula 030</h1>
    <h2>Seu navegador é: {}</h2>
    <h2>O IP do computador remoto é: {}</h2>
    <h2>O host da aplicação é: {}</h2>
    <a href=/><p>Voltar</p></a>
    '''.format(user_agent, user_ip, app_host)