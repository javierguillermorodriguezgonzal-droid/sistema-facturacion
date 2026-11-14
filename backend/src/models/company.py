from .category import db

class Company(db.Model):
    __tablename___ = "company"

    id_company = db.Column(
        db.Integer,
        primay_key=True,
        autoincrement=True
    )
    Nit = db.Column(
        db.String(45),
        nullable=False,
        unique=True
    )
    company_name = db.Column(
        db.String(45),
        nullable=False,
        unique=True
    )