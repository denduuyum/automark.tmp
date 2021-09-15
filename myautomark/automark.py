from datetime import datetime
from datetime import date
from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data_structure.db'
db = SQLAlchemy(app)

from myautomark.model import Assignment
from myautomark.model import Journal


@app.route("/create_assignment", methods = ['POST'])
def create_assignment():
    assign_name, desc, deadline = request.form['name'], request.form['desc'], request.form['deadline']
    assignment = Assignment(name = assign_name, deadline = date.fromisoformat(deadline), desc = desc)
    db.session.add(assignment)
    db.session.commit()
    return 'success'

@app.route("/submit", methods = ['POST'])
def submit():
    student, assign_name, point = request.form['name'], request.form['hwname'], int(request.form['point'])
    now = datetime.now()
    assignment = Assignment.query.filter_by(name = assign_name).first()
    if assignment == None:
        return '{"success": 0}'
    
    if now.date() > assignment.deadline:
        point /= 2

    submission = Journal.query.filter_by(student = student, assignment = assign_name).first()

    if submission != None:
        if submission.point < point:
            submission.point = point
            db.session.commit()
    else:
        submission = Journal(student = student, assignment = assign_name, point = point, submission_date = now)
        db.session.add(submission)
        db.session.commit()
    return '{"success": 1}'

#     return app
