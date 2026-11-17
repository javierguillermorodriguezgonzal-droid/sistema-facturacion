from .category import db
from sqlalchemy.dialects.mysql import TINYINT

class Invoice(db.Model):
    __tablename__ = "invoice"
    
    id_invoice = db.Column(
        db.BigInteger,
        primary_key=True, 
        autoincrement=True
        )
    Id_person = db.Column(
        db.Integer,
        db.Foreinkey("person.id_Person"), 
        nullable=False
        )
    Id_company = db.Column(
        db.Integer,
        db.Foreignkey("company.id_company"),
        nullable=False
    )
    Id_payment_method = db.Column(
        TINYINT,
        db.Foreignkey("payment_method.id_Payment_method"),
        nullable=False
    )
    Date = db.Column(db.Date, nullable=False)
    Hour = db.Column(db.Time, nullable=False)

    Sub_total = db.Column(db.Numeric(10, 2), nullable=False)
    total = db.Column(db.Numeric(10, 2), nullable=False)