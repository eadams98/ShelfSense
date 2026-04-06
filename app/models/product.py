from core.database import Base
from sqlalchemy import Column, Integer, String


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)

    def __init__(self, name: str, description: str = None):
        self.name = name
        self.description = description
