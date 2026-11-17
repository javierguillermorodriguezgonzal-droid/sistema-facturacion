from .category import db

class Company(db.Model):
    __tablename__ = "company"

    id_company = db.Column(
        db.Integer,
        primary_key=True,
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