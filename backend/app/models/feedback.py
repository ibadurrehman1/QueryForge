from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Feedback(Base):
    __tablename__ = "feedback"
    
    id = Column(String, primary_key=True)  # CUID
    query_id = Column(String, ForeignKey("queries.id", ondelete="CASCADE"), unique=True, nullable=False)
    user_id = Column(String, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    
    rating = Column(Integer, nullable=False)  # 1 for helpful, -1 for not helpful
    comment = Column(Text, nullable=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    query = relationship("Query", back_populates="feedback")
    user = relationship("User", back_populates="feedback")
