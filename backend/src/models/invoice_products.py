from .category import db

class Invoice_products(db.Model):
    __tablename__ = "invoice_products"

    Invoice_id_invoice = db.Column(
        db.BigInterger,
        db.ForeignKey("Invoice.id_invoice"),
        nullable=False
    )
    Products_Id_producto = db.Column(
        db.Integer,
        db.Foreignkey("Products.Id_product"),
        nullable=False
    )
    __table_args__ = (
        db.PrimarykeyConstraint(
            "Invoice.id_invoice",
            "Products_Id_producto"
        ),
    )