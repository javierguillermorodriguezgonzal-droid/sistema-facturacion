from .extensions import db

class Supplier_has_products(db.Model):
    __tablename__ = "supplier_has_products"

    Supplier_id_supplier = db.Column(
        db.Integer,
        db.ForeignKey("supplier.id_supplier"),
        nullable=False
    )
    Products_Id_producto = db.Column(
        db.Integer,
        db.ForeignKey("products.Id_product"),
        nullable=False
    )
    __table_args__ = (
        db.PrimaryKeyConstraint(
            "Supplier_id_supplier",
            "Products_Id_producto"
        ),
    )