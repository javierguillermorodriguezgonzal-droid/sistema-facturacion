from .extensions import db
from sqlalchemy.dialects.mysql import TINYINT
class Payment_method (db.Model):
    __tablename__ = "payment_method"
    id_Payment_method = db.Column(
        TINYINT,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(db.String(45), nullable=False)
    Description = db.Column(db.String(45), nullable=True)