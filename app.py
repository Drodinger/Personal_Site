from flask import Flask, render_template, url_for, redirect, session
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired, Email
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from flask_bootstrap import Bootstrap

app = Flask(__name__)

app.config['SECRET_KEY'] = 'a random string'

bootstrap = Bootstrap(app)

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[Email()])
    subject = StringField('Subject')
    message = StringField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/')
def about():
	return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['email'] = form.email.data
        session['subject'] = form.subject.data
        session['message'] = form.message.data
        return redirect(url_for('contact'))
    return render_template('contact.html', form=form, name=session.get('name'), email=session.get('email'), subject=session.get('subject'), message=session.get('message'))

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://flask:password@localhost:5432/personal_site_db"

db.init_app(app)

class Skills(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    backend: Mapped[str] = mapped_column(String, nullable=True)
    frontend: Mapped[str] = mapped_column(String)
    architectures: Mapped[str] = mapped_column(String)
    methodologies: Mapped[str] = mapped_column(String)
    databases: Mapped[str] = mapped_column(String)
    devops: Mapped[str] = mapped_column(String)
    other_technologies: Mapped[str] = mapped_column(String)
    
with app.app_context():
    db.create_all()
