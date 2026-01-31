from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_db
from app.schemas.user import UserResponse, UserUpdate, UserCreate
from app.models.user import User
from datetime import datetime
import secrets

router = APIRouter()


def generate_user_id() -> str:
    """Generate a unique user ID"""
    return f"user_{secrets.token_urlsafe(16)}"


@router.get("/me", response_model=UserResponse)
async def get_current_user(
    clerk_id: str,  # This will come from auth middleware later
    db: AsyncSession = Depends(get_db)
):
    """
    Get current user information.
    For now, we're using clerk_id as a parameter. 
    In production, this will come from JWT token via middleware.
    """
    result = await db.execute(
        select(User).where(User.clerk_id == clerk_id)
    )
    user = result.scalar_one_or_none()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    # Update last login
    user.last_login = datetime.utcnow()
    await db.commit()
    await db.refresh(user)
    
    return user


@router.put("/me", response_model=UserResponse)
async def update_current_user(
    user_update: UserUpdate,
    clerk_id: str,  # This will come from auth middleware later
    db: AsyncSession = Depends(get_db)
):
    """
    Update current user information.
    For now, we're using clerk_id as a parameter.
    In production, this will come from JWT token via middleware.
    """
    result = await db.execute(
        select(User).where(User.clerk_id == clerk_id)
    )
    user = result.scalar_one_or_none()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    # Update user fields
    update_data = user_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(user, field, value)
    
    user.updated_at = datetime.utcnow()
    
    await db.commit()
    await db.refresh(user)
    
    return user


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_create: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    """
    Create a new user.
    This endpoint will typically be called during the signup flow.
    """
    # Check if user already exists
    result = await db.execute(
        select(User).where(User.clerk_id == user_create.clerk_id)
    )
    existing_user = result.scalar_one_or_none()
    
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this Clerk ID already exists"
        )
    
    # Check if email is already registered
    result = await db.execute(
        select(User).where(User.email == user_create.email)
    )
    existing_email = result.scalar_one_or_none()
    
    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists"
        )
    
    # Create new user
    new_user = User(
        id=generate_user_id(),
        clerk_id=user_create.clerk_id,
        email=user_create.email,
        full_name=user_create.full_name,
        avatar_url=user_create.avatar_url,
    )
    
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    
    return new_user


@router.get("/{user_id}", response_model=UserResponse)
async def get_user_by_id(
    user_id: str,
    db: AsyncSession = Depends(get_db)
):
    """
    Get user by ID (admin or self only in production).
    For MVP, this is open but should be protected later.
    """
    result = await db.execute(
        select(User).where(User.id == user_id)
    )
    user = result.scalar_one_or_none()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return user
