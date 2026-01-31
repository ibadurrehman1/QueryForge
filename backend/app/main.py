from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.config import settings
from app.database import engine, Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan events for FastAPI application.
    Handles startup and shutdown events.
    """
    # Startup: Create database tables
    async with engine.begin() as conn:
        # In production, use Alembic migrations instead
        # await conn.run_sync(Base.metadata.create_all)
        pass
    
    yield
    
    # Shutdown: Dispose engine
    await engine.dispose()


# Create FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    description="Transform conversations into insights - Natural Language to SQL API",
    version=settings.VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Root endpoint
@app.get("/")
async def root():
    """Root endpoint - API information"""
    return {
        "message": f"Welcome to {settings.APP_NAME}",
        "version": settings.VERSION,
        "docs": "/docs",
        "redoc": "/redoc",
    }


# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring"""
    return {
        "status": "healthy",
        "environment": settings.ENVIRONMENT,
        "version": settings.VERSION,
    }


# API v1 routes will be added here
# app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
# app.include_router(queries.router, prefix="/api/v1/queries", tags=["queries"])
# app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
# app.include_router(feedback.router, prefix="/api/v1/feedback", tags=["feedback"])
