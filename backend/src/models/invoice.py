from .category import db
from sqlalchemy.dialects.mysql import TINYINT

class Invoice(db.Model):
    __tablename__ = "invoice"
    
    id_invoice = db.Column(
        db.BigInterger,
        primary_key=True, 
        autoincrement=True
        )
    Id_person = db.Column(
        db.Interger,
        db.Foreinkey("person.id_person"), 
        nullable=False
        )
    id_Company = db.Column(
        db.Integer,
        db.Foreinkey("company.id_company"),
        nullable=False
    )
    Id_payment_method = db.Column(
        TINYINT,
        db.Foreinkey("payment_method.id_payment_method"),
        nullable=False
    )
    Date = db.Column(db.Date, nullable=False)
    Hour = db.Column(db.Hour, nullable=False)

    Sub_total = db.Column(db.Numeric(10, 2), nullable=False)
    total = db.Column(db.Numeric(10, 2), nullable=False)