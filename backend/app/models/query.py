from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Enum, Text, ARRAY
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
import enum

class QueryStatus(str, enum.Enum):
    SUCCESS = "success"
    FAILED = "failed"
    WARNING = "warning"

class Query(Base):
    __tablename__ = "queries"
    
    id = Column(String, primary_key=True)  # CUID
    user_id = Column(String, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    connection_id = Column(String, ForeignKey("database_connections.id", ondelete="SET NULL"), nullable=True)
    
    natural_language = Column(Text, nullable=False)
    generated_sql = Column(Text, nullable=False)
    
    # Analysis results
    tables_used = Column(ARRAY(String))
    query_type = Column(String)  # SELECT, UPDATE, etc.
    
    # Execution stats
    response_time = Column(Integer)  # milliseconds
    rows_returned = Column(Integer)
    
    status = Column(Enum(QueryStatus), default=QueryStatus.SUCCESS)
    error_message = Column(Text, nullable=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    user = relationship("User", back_populates="queries")
    connection = relationship("DatabaseConnection", back_populates="queries")
    feedback = relationship("Feedback", back_populates="query", uselist=False, cascade="all, delete-orphan")
