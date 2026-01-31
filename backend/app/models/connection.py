from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class DatabaseConnection(Base):
    __tablename__ = "database_connections"
    
    id = Column(String, primary_key=True)  # CUID
    user_id = Column(String, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    
    name = Column(String, nullable=False)
    dialect = Column(String, nullable=False)  # postgresql, mysql, mssql
    
    # Connection details (encrypted in real app, keeping simple for now/MVP)
    host = Column(String, nullable=False)
    port = Column(Integer, nullable=False)
    database = Column(String, nullable=False)
    username = Column(String, nullable=False)
    # Password should be encrypted/stored securely. storing as is for MVP but should be addressed
    password = Column(String, nullable=False) 
    
    is_primary = Column(Boolean, default=False)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    user = relationship("User", back_populates="connections")
    queries = relationship("Query", back_populates="connection")
