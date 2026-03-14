from sqlalchemy import Column, Integer, ForeignKey, String, DateTime

from app.database import Base

class Accounts(Base):

    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    account_name = Column(String)
    account_type = Column(String)
    currency = Column(String)
    created_at = Column(DateTime)

