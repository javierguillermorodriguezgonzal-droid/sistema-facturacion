from .category import db

class Supplier(db.Model):
    __tablename__ = "supplier"

    id_supplier = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Company_identification = db.Column(db.String(45), nullable=False)
    Company_name = db.Column(db.String(45), nullable=False)
    Directions = db.Column(db.String(45), nullable=False)
    City = db.Column(db.String(45), nullable=True)
    Cell_phones = db.Column(db.String(45), nullable=False)
    Email = db.Column(db.String(45), nullable=False)