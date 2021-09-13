from datetime import datetime
from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from model import Assignment
from model import Journal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data_structure.db'
db = SQLAlchemy(app)


@app.route("/submit", methods = ['POST'])
def submit():
    student, assign_name, point = request.form['name'], request.form['hwname'], int(request.form['point'])
    now = datetime.now()
    assignment = Assignment.query.filter_by(name = assign_name).first()
    if assignment == None:
        return '{"success": 0}'
    
    if now.date() > assignemnt.deadline:
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
