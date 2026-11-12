from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Category(db.Model):
    __tablename__ = "category"

    Id_Category = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    