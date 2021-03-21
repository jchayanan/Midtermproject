from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class Student(db.Model):
    __tablename__ = "student"
 
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer(),unique = True)
    name = db.Column(db.String())
    img = db.Column(db.String())
 
    def __repr__(self):
        return f"{self.name}:{self.student_id}:{self.img}"