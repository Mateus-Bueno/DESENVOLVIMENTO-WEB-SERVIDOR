import os
from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class CourseName(db.Model):
    __tablename__ = 'courseNames'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    courseDescription = db.relationship('CourseDescription', backref='desc', lazy='dynamic')

    def __repr__(self):
        return '<CourseName %r>' % self.name


class CourseDescription(db.Model):
    __tablename__ = 'courseDescriptions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courseNames.id'))

    def __repr__(self):
        return '<CourseDescription %r>' % self.description


class CourseForm(FlaskForm):
    CourseName = StringField('Qual é o nome do curso?', validators=[DataRequired()])
    CourseDescription = TextAreaField('Descrição (250 caracteres)', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, CourseName=CourseName, CourseDescription=CourseDescription)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/professores')
def professores():
    return render_template('professores.html')

@app.route('/disciplinas')
def disciplinas():
    return render_template('disciplinas.html')

@app.route('/alunos')
def alunos():
    return render_template('alunos.html')

@app.route('/cursos', methods=['GET', 'POST'])
def cursos():
    form = CourseForm()
    if form.validate_on_submit():
        course = CourseName.query.filter_by(name=form.CourseName.data).first()
        if course is None:
            course = CourseName(name=form.CourseName.data)
            db.session.add(course)

        desc = CourseDescription.query.filter_by(name=form.CourseDescription.data).first()
        if desc is None:
            desc = CourseDescription(name=form.CourseDescription.data)
            db.session.add(desc)
            db.session.commit()
    return render_template('cursos.html', form=form)

@app.route('/ocorrencias')
def ocorrencias():
    return render_template('ocorrencias.html')