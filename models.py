import sqlalchemy as _sqlalchemy
from . import database as _database


class Product(_database.Base):
    __tablename__ = "products"
    id = _sqlalchemy.Column(_sqlalchemy.Integer, primary_key=True, index=True)
    name = _sqlalchemy.Column(_sqlalchemy.String)
    description = _sqlalchemy.Column(_sqlalchemy.String)
    price = _sqlalchemy.Column(_sqlalchemy.Integer)
