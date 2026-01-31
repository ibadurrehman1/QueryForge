from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_db
from app.schemas.connection import (
    DatabaseConnectionCreate,
    DatabaseConnectionUpdate,
    DatabaseConnectionResponse,
    DatabaseConnectionTest,
)
from app.models.connection import DatabaseConnection
from datetime import datetime
import secrets

router = APIRouter()


def generate_connection_id() -> str:
    """Generate a unique connection ID"""
    return f"conn_{secrets.token_urlsafe(16)}"


@router.post("/", response_model=DatabaseConnectionResponse, status_code=status.HTTP_201_CREATED)
async def create_connection(
    connection_data: DatabaseConnectionCreate,
    user_id: str,  # Will come from auth middleware
    db: AsyncSession = Depends(get_db)
):
    """
    Create a new database connection.
    """
    # Check if user already has a connection with this name
    result = await db.execute(
        select(DatabaseConnection).where(
            DatabaseConnection.user_id == user_id,
            DatabaseConnection.name == connection_data.name
        )
    )
    existing = result.scalar_one_or_none()
    
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A connection with this name already exists"
        )
    
    # If this is the first connection, make it primary
    result = await db.execute(
        select(DatabaseConnection).where(DatabaseConnection.user_id == user_id)
    )
    is_first_connection = result.first() is None
    
    # Create new connection
    new_connection = DatabaseConnection(
        id=generate_connection_id(),
        user_id=user_id,
        name=connection_data.name,
        dialect=connection_data.dialect,
        host=connection_data.host,
        port=connection_data.port,
        database=connection_data.database,
        username=connection_data.username,
        password=connection_data.password,  # TODO: Encrypt in production
        is_primary=is_first_connection,
    )
    
    db.add(new_connection)
    await db.commit()
    await db.refresh(new_connection)
    
    return new_connection


@router.get("/", response_model=list[DatabaseConnectionResponse])
async def get_connections(
    user_id: str,  # Will come from auth middleware
    db: AsyncSession = Depends(get_db)
):
    """
    Get all database connections for the current user.
    """
    result = await db.execute(
        select(DatabaseConnection)
        .where(DatabaseConnection.user_id == user_id)
        .order_by(DatabaseConnection.is_primary.desc(), DatabaseConnection.created_at.desc())
    )
    connections = result.scalars().all()
    return connections


@router.get("/{connection_id}", response_model=DatabaseConnectionResponse)
async def get_connection(
    connection_id: str,
    user_id: str,  # Will come from auth middleware
    db: AsyncSession = Depends(get_db)
):
    """
    Get a specific database connection.
    """
    result = await db.execute(
        select(DatabaseConnection).where(
            DatabaseConnection.id == connection_id,
            DatabaseConnection.user_id == user_id
        )
    )
    connection = result.scalar_one_or_none()
    
    if not connection:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Connection not found"
        )
    
    return connection


@router.put("/{connection_id}", response_model=DatabaseConnectionResponse)
async def update_connection(
    connection_id: str,
    connection_update: DatabaseConnectionUpdate,
    user_id: str,  # Will come from auth middleware
    db: AsyncSession = Depends(get_db)
):
    """
    Update a database connection.
    """
    result = await db.execute(
        select(DatabaseConnection).where(
            DatabaseConnection.id == connection_id,
            DatabaseConnection.user_id == user_id
        )
    )
    connection = result.scalar_one_or_none()
    
    if not connection:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Connection not found"
        )
    
    # Update connection fields
    update_data = connection_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(connection, field, value)
    
    connection.updated_at = datetime.utcnow()
    
    await db.commit()
    await db.refresh(connection)
    
    return connection


@router.delete("/{connection_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_connection(
    connection_id: str,
    user_id: str,  # Will come from auth middleware
    db: AsyncSession = Depends(get_db)
):
    """
    Delete a database connection.
    """
    result = await db.execute(
        select(DatabaseConnection).where(
            DatabaseConnection.id == connection_id,
            DatabaseConnection.user_id == user_id
        )
    )
    connection = result.scalar_one_or_none()
    
    if not connection:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Connection not found"
        )
    
    await db.delete(connection)
    await db.commit()


@router.post("/test", status_code=status.HTTP_200_OK)
async def test_connection(connection_test: DatabaseConnectionTest):
    """
    Test a database connection without saving it.
    Returns success/failure status.
    """
    # TODO: Implement actual connection testing
    # For now, just return success
    return {
        "success": True,
        "message": "Connection test successful",
        "dialect": connection_test.dialect,
        "host": connection_test.host,
        "database": connection_test.database
    }


@router.put("/{connection_id}/set-primary", response_model=DatabaseConnectionResponse)
async def set_primary_connection(
    connection_id: str,
    user_id: str,  # Will come from auth middleware
    db: AsyncSession = Depends(get_db)
):
    """
    Set a connection as the primary connection for the user.
    """
    # Verify connection exists and belongs to user
    result = await db.execute(
        select(DatabaseConnection).where(
            DatabaseConnection.id == connection_id,
            DatabaseConnection.user_id == user_id
        )
    )
    connection = result.scalar_one_or_none()
    
    if not connection:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Connection not found"
        )
    
    # Unset all other primary connections for this user
    result = await db.execute(
        select(DatabaseConnection).where(
            DatabaseConnection.user_id == user_id,
            DatabaseConnection.is_primary == True
        )
    )
    primary_connections = result.scalars().all()
    
    for conn in primary_connections:
        conn.is_primary = False
    
    # Set this connection as primary
    connection.is_primary = True
    connection.updated_at = datetime.utcnow()
    
    await db.commit()
    await db.refresh(connection)
    
    return connection
