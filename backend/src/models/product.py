from .category import db

class Product(db.Model):
    __tablename__ = "products"
    Id_product = db.Column(db.Integer,primary_key=True)
    Id_Categoria = db.Column(
        db.Integer,
        db.ForeignKey("category.Id_Category"),
        nullable=False
    )
    Product_code = db.Column(db.String(50), nullable=False, unique=True)
    name = db.Column(db.String(45), nullable=False)
    Description = db.Column(db.String(250), nullable=False)
    Purchase_price = db.Column(db.Numeric(10, 2), nullable=False)
    Selling_price = db.Column(db.Numeric(10, 2), nullable=False)
    Stock = db.Column(db.Integer, nullable=False)