import sqlalchemy as _sqlalchemy
from .database import Base


class Product(Base):
    __tablename__ = "products"
    id = _sqlalchemy.Column(_sqlalchemy.Integer, primary_key=True, index=True)
    name = _sqlalchemy.Column(_sqlalchemy.String)
    description = _sqlalchemy.Column(_sqlalchemy.String)
    price = _sqlalchemy.Column(_sqlalchemy.Integer)
