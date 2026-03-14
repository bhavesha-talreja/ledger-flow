from sqlalchemy import Column, Integer, String, DateTime

from app.database import Base

class Vendor(Base):
    __tablename__ = "vendors"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    created_at = Column(DateTime)
