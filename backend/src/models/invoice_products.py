from ..extensions import db

class Invoice_products(db.Model):
    __tablename__ = "invoice_products"

    id_invoice = db.Column(
        db.BigInteger,
        db.ForeignKey("invoice.id_invoice"),
        primary_key=True
    )
    invoice = db.relationship(
        "Invoice",
        back_populates="invoice_products"
    )
    Id_product = db.Column(
        db.Integer,
        db.ForeignKey("products.Id_product"),
        primary_key=True
    )
    product = db.relationship(
        "Product",
        back_populates="invoice_products"
    )
    Unit_value = db.Column(
        "Unit value",
        db.Numeric(10, 2),
        nullable=False
    )
    Amount = db.Column(
        db.SmallInteger,
        nullable=False
    )