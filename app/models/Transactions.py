from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey
from app.database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)

    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    vendor_id = Column(Integer, ForeignKey("vendors.id"))

    amount = Column(Numeric(12, 2), nullable=False)
    currency = Column(String(10), default="INR")

    transaction_date = Column(DateTime, nullable=False)

    description = Column(String)

    created_at = Column(DateTime)