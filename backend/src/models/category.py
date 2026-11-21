from ..extensions import db

class Category(db.Model):
    __tablename__ = "category"

    Id_Category = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
        )
    name = db.Column(db.String(150), nullable=False)
    products = db.relationship(
        "Product",
        back_populates="category"
    )
    