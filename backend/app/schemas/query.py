from pydantic import BaseModel
from typing import Optional, Any
from datetime import datetime
from app.models.query import QueryStatus


class QueryBase(BaseModel):
    """Base schema for queries"""
    natural_language_query: str


class QueryCreate(QueryBase):
    """Schema for creating a query"""
    connection_id: str


class QueryResponse(QueryBase):
    """Schema for query responses"""
    id: str
    user_id: str
    connection_id: str
    generated_sql: Optional[str] = None
    result_data: Optional[Any] = None
    status: QueryStatus
    error_message: Optional[str] = None
    execution_time_ms: Optional[int] = None
    rows_returned: Optional[int] = None
    created_at: datetime
    
    class Config:
        from_attributes = True


class QueryExecuteRequest(BaseModel):
    """Schema for executing a query"""
    natural_language_query: str
    connection_id: str


class QueryExecuteResponse(BaseModel):
    """Schema for query execution response"""
    query_id: str
    generated_sql: str
    result_data: Optional[Any] = None
    status: QueryStatus
    error_message: Optional[str] = None
    execution_time_ms: int
    rows_returned: int
