from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy

class person(db.model):
    __tablename__ = "person"
    
