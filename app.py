from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

app = Flask(__name__)

@app.route('/')
def about():
	return render_template('about.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')


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