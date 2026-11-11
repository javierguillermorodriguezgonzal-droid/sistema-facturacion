from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class category(db.Model):
    __tablename__ = "category"

    id_Category = db.column(db.integer,primary_key=True)
    name = db.column(db.string(150, nullable=False))
    