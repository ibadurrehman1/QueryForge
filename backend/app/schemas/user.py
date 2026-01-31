from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from app.models.user import UserRole


class UserBase(BaseModel):
    """Base user schema with common attributes"""
    email: EmailStr
    full_name: Optional[str] = None


class UserCreate(UserBase):
    """Schema for creating a new user"""
    clerk_id: str
    email: EmailStr
    full_name: Optional[str] = None
    avatar_url: Optional[str] = None


class UserUpdate(BaseModel):
    """Schema for updating user information"""
    full_name: Optional[str] = None
    avatar_url: Optional[str] = None
    theme_preference: Optional[str] = None  # 'light', 'dark', 'system'


class UserInDB(UserBase):
    """Schema for user as stored in database"""
    id: str
    clerk_id: str
    role: UserRole
    theme_preference: Optional[str] = None
    avatar_url: Optional[str] = None
    last_login: Optional[datetime] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class UserResponse(UserBase):
    """Schema for user responses"""
    id: str
    role: UserRole
    theme_preference: Optional[str] = None
    avatar_url: Optional[str] = None
    last_login: Optional[datetime] = None
    created_at: datetime
    
    class Config:
        from_attributes = True
