from sqlalchemy import Column, Integer, ForeignKey, String, DateTime

from app.database import Base

class Attachment(Base):
    __tablename__ = "attachments"

    id = Column(Integer, primary_key=True)
    file_name = Column(String)
    transaction_id = Column(Integer, ForeignKey("transactions.id"), nullable=False)
    file_path = Column(String)
    uploaded_at = Column(DateTime)


