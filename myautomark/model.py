from myautomark.automark import db

class Assignment(db.Model):
    name = db.Column(db.String(80), unique = True, nullable = False, primary_key = True)
    desc = db.Column(db.Text)
    deadline = db.Column(db.Date, nullable = False)
    
    
class Journal(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    student = db.Column(db.String(40))
    assignment = db.Column(db.String(80), db.ForeignKey('assignment.name'), nullable=False)
    point = db.Column(db.Integer, default = 0)
    submission_date = db.Column(db.Date, nullable = False)

