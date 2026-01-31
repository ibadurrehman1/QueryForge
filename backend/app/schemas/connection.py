from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class DatabaseConnectionBase(BaseModel):
    """Base schema for database connections"""
    name: str
    dialect: str  # postgresql, mysql, mssql
    host: str
    port: int
    database: str
    username: str


class DatabaseConnectionCreate(DatabaseConnectionBase):
    """Schema for creating a database connection"""
    password: str


class DatabaseConnectionUpdate(BaseModel):
    """Schema for updating a database connection"""
    name: Optional[str] = None
    host: Optional[str] = None
    port: Optional[int] = None
    database: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    is_primary: Optional[bool] = None


class DatabaseConnectionResponse(DatabaseConnectionBase):
    """Schema for database connection responses (without password)"""
    id: str
    user_id: str
    is_primary: bool
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class DatabaseConnectionTest(BaseModel):
    """Schema for testing a database connection"""
    dialect: str
    host: str
    port: int
    database: str
    username: str
    password: str
