import os
from flask import Flask, render_template, request, url_for, redirect
from flask import SQLAlchemy


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    price = db.Column(db.String(100), nullable=False)
    date_add = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Employee {self.firstname} {self.lastname}>'
