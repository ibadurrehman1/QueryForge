import asyncio
import asyncpg
from urllib.parse import urlparse
from app.config import settings

async def create_database_if_not_exists():
    """
    Checks if the database exists and creates it if not.
    Connects to the default 'postgres' database to perform the check/creation.
    """
    db_url = settings.DATABASE_URL
    parsed = urlparse(db_url)
    
    # Extract connection info
    user = parsed.username
    password = parsed.password
    host = parsed.hostname
    port = parsed.port or 5432
    target_db = parsed.path.lstrip('/')
    
    # Connect to default 'postgres' database
    print(f"Checking if database '{target_db}' exists...")
    
    try:
        # Establish connection to 'postgres' database to check/create target db
        sys_conn = await asyncpg.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database='postgres'
        )
        
        # Check if database exists
        exists = await sys_conn.fetchval(
            "SELECT 1 FROM pg_database WHERE datname = $1", 
            target_db
        )
        
        if not exists:
            print(f"Database '{target_db}' does not exist. Creating...")
            # Create database (cannot be done in transaction)
            await sys_conn.execute(f'CREATE DATABASE "{target_db}"')
            print(f"Database '{target_db}' created successfully!")
        else:
            print(f"Database '{target_db}' already exists.")
            
        await sys_conn.close()
        
    except Exception as e:
        print(f"Error checking/creating database: {e}")
        # Build a safe connection string for logging (hide password)
        safe_url = db_url.replace(password, '****') if password else db_url
        print(f"Connection URL used: {safe_url}")
        print("Ensure your PostgreSQL server is running and credentials are correct.")
        raise e

if __name__ == "__main__":
    asyncio.run(create_database_if_not_exists())
