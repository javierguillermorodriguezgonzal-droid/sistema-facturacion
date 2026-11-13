from .category import db

class Person(db.model):
    __tablename__ = "person"

    id_Person = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(45), nullable=True)
    Identification = db.Column(db.String(45), nullable=False, unique=True)
    Name = db.Column(db.String(450), nullable=False)
    address = db.Column(db.String(250), nullable=True)
    city = db.Column(db.String(30), nullable=True)
    potal_code = db.Column(db.String(15), nullable=True)
    phones_number = db.Column(db.String(10), nullable=False, unique= True)
    Email = db.Column(db.String(250), nullable=False, unique=True)


