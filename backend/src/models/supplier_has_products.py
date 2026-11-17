from .category import db

class Supplier_has_products(db.Model):
    __tablename__ = "supplier_has_products"

    Supplier_id_supplier = db.Column(
        db.Integer,
        db.ForeignKey("supplier.id_supplier"),
        nullable=False
    )
    Products_Id_producto = db.Column(
        db.Integer,
        db.Foreignkey("Products.Id_product"),
        nullable=False
    )
    __table_args__ = (
        db.PrimarykeyConstraint(
            "Supplier_id_supplier",
            "Products_Id_producto"
        ),
    )