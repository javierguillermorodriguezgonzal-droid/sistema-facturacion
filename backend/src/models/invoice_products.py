from .category import db

class Invoice_products(db.Model):
    __tablename__ = "invoice_products"

    id_invoice = db.Column(
        db.BigInteger,
        db.ForeignKey("invoice.id_invoice"),
        primary_key=True
    )
    Id_product = db.Column(
        db.Integer,
        primary_key=True
    )
    Unit_value = db.Column(
        "Unit value"
        db.Numeric(10, 2),
        nullable=False
    )
    Amount = db.Column(
        db.SmallInteger,
        nullable=False
    )