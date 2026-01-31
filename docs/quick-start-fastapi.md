# QueryForge - Quick Start (FastAPI Backend)

## 🎯 One-Page Setup Guide

---

## Tech Stack Summary

```
Frontend:  Next.js 14 + TypeScript + Tailwind + shadcn/ui
Backend:   FastAPI + Python 3.11+
Database:  PostgreSQL (Neon) - NOT MongoDB
Cache:     Redis (Upstash)
Auth:      Clerk
AI:        Google Gemini Flash (FREE)
Hosting:   Railway (Backend) + Vercel (Frontend)
```

---

## 🚀 Backend Setup (FastAPI)

### 1. Create Project Structure
```bash
mkdir queryforge-backend
cd queryforge-backend

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Create project structure
mkdir -p app/{api/v1,models,schemas,services,utils,middleware}
touch app/__init__.py
touch app/main.py
touch app/config.py
touch app/database.py
touch requirements.txt
touch .env
```

### 2. Install Dependencies
```bash
# Create requirements.txt
cat > requirements.txt << EOF
fastapi==0.109.0
uvicorn[standard]==0.27.0
sqlalchemy[asyncio]==2.0.25
asyncpg==0.29.0
alembic==1.13.1
pydantic==2.5.3
pydantic-settings==2.1.0
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
redis==5.0.1
google-generativeai==0.3.2
resend==0.7.0
httpx==0.26.0
python-dotenv==1.0.0
sentry-sdk[fastapi]==1.40.0
pytest==7.4.4
pytest-asyncio==0.23.3
ruff==0.1.14
black==24.1.1
EOF

# Install
pip install -r requirements.txt
```

### 3. Create Main App (app/main.py)
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="QueryForge API",
    description="Natural Language to SQL",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "QueryForge API", "status": "running"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

# Run: uvicorn app.main:app --reload
```

### 4. Create Config (app/config.py)
```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # App
    APP_NAME: str = "QueryForge"
    DEBUG: bool = True
    
    # Database
    DATABASE_URL: str
    
    # Redis
    REDIS_URL: str
    
    # Auth
    CLERK_SECRET_KEY: str
    
    # AI
    GEMINI_API_KEY: str
    
    # Email
    RESEND_API_KEY: str
    
    class Config:
        env_file = ".env"

settings = Settings()
```

### 5. Create Database (app/database.py)
```python
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

engine = create_async_engine(settings.DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)
Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
```

### 6. Create Environment Variables (.env)
```env
# Database (Neon)
DATABASE_URL=postgresql+asyncpg://user:password@host.neon.tech/dbname

# Redis (Upstash)
REDIS_URL=redis://default:password@host.upstash.io:6379

# Auth (Clerk)
CLERK_SECRET_KEY=sk_test_...

# AI (Gemini)
GEMINI_API_KEY=AIza...

# Email (Resend)
RESEND_API_KEY=re_...
```

### 7. Run Development Server
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# API docs available at:
# http://localhost:8000/docs (Swagger)
# http://localhost:8000/redoc (ReDoc)
```

---

## 🎨 Frontend Setup (Next.js)

### 1. Create Next.js Project
```bash
npx create-next-app@latest queryforge-frontend --typescript --tailwind --app --src-dir --import-alias "@/*"
cd queryforge-frontend
```

### 2. Install Dependencies
```bash
npm install @clerk/nextjs zustand react-hook-form @hookform/resolvers zod recharts lucide-react class-variance-authority clsx tailwind-merge axios
```

### 3. Install shadcn/ui
```bash
npx shadcn-ui@latest init

# Add components
npx shadcn-ui@latest add button input card table dialog toast dropdown-menu tabs badge avatar
```

### 4. Create API Client (lib/api.ts)
```typescript
import axios from 'axios';

const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000',
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add auth token to requests
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('clerk-token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default api;
```

### 5. Environment Variables (.env.local)
```env
# Backend API
NEXT_PUBLIC_API_URL=http://localhost:8000

# Clerk
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_test_...
CLERK_SECRET_KEY=sk_test_...
```

### 6. Run Development Server
```bash
npm run dev
# Frontend: http://localhost:3000
```

---

## 📊 Database Schema (SQLAlchemy Models)

### Create User Model (app/models/user.py)
```python
from sqlalchemy import Column, String, DateTime, Enum
from sqlalchemy.sql import func
from app.database import Base
import enum

class UserRole(str, enum.Enum):
    USER = "user"
    ADMIN = "admin"

class User(Base):
    __tablename__ = "users"
    
    id = Column(String, primary_key=True)
    clerk_id = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    name = Column(String)
    role = Column(Enum(UserRole), default=UserRole.USER)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
```

### Create Query Model (app/models/query.py)
```python
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, ARRAY, Enum
from sqlalchemy.sql import func
from app.database import Base
import enum

class QueryStatus(str, enum.Enum):
    SUCCESS = "success"
    FAILED = "failed"
    WARNING = "warning"

class Query(Base):
    __tablename__ = "queries"
    
    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.id", ondelete="CASCADE"))
    natural_language = Column(String, nullable=False)
    generated_sql = Column(String, nullable=False)
    tables_used = Column(ARRAY(String))
    response_time = Column(Integer)  # milliseconds
    rows_returned = Column(Integer)
    status = Column(Enum(QueryStatus))
    error_message = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
```

### Initialize Database
```bash
# Create migration
alembic init alembic

# Edit alembic.ini and set:
# sqlalchemy.url = postgresql+asyncpg://...

# Create first migration
alembic revision --autogenerate -m "Initial migration"

# Apply migration
alembic upgrade head
```

---

## 🤖 AI Service (Gemini Integration)

### Create AI Service (app/services/ai_service.py)
```python
import google.generativeai as genai
from app.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

class AIService:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-1.5-flash')
    
    async def generate_sql(
        self, 
        natural_language: str, 
        schema: dict
    ) -> str:
        prompt = f"""
        Convert this natural language query to SQL:
        
        Question: {natural_language}
        
        Database Schema:
        {schema}
        
        Return ONLY the SQL query, no explanations.
        """
        
        response = await self.model.generate_content_async(prompt)
        return response.text.strip()

ai_service = AIService()
```

---

## 🔌 API Endpoints (FastAPI Routes)

### Create Query Endpoint (app/api/v1/queries.py)
```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.services.ai_service import ai_service
from app.schemas.query import QueryCreate, QueryResponse
from app.models.query import Query
import time

router = APIRouter()

@router.post("/", response_model=QueryResponse)
async def create_query(
    query: QueryCreate,
    db: AsyncSession = Depends(get_db)
):
    start_time = time.time()
    
    try:
        # Generate SQL using AI
        sql = await ai_service.generate_sql(
            query.natural_language,
            query.schema
        )
        
        # Execute SQL (implement your logic here)
        # result = await execute_sql(sql, query.database_connection)
        
        response_time = int((time.time() - start_time) * 1000)
        
        # Save to database
        db_query = Query(
            user_id=query.user_id,
            natural_language=query.natural_language,
            generated_sql=sql,
            response_time=response_time,
            status="success"
        )
        db.add(db_query)
        await db.commit()
        
        return QueryResponse(
            id=db_query.id,
            sql=sql,
            status="success",
            response_time=response_time
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

---

## 🚀 Deployment

### Deploy Backend to Railway

1. **Create Railway Account**: https://railway.app
2. **Install Railway CLI**:
```bash
npm install -g @railway/cli
```

3. **Login and Deploy**:
```bash
railway login
railway init
railway up
```

4. **Add Environment Variables** in Railway dashboard

5. **Your API is live!** 🎉

### Deploy Frontend to Vercel

1. **Push to GitHub**:
```bash
git init
git add .
git commit -m "Initial commit"
git push origin main
```

2. **Deploy to Vercel**:
```bash
npx vercel
```

3. **Add Environment Variables** in Vercel dashboard:
   - `NEXT_PUBLIC_API_URL=https://your-backend.railway.app`
   - `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_...`
   - `CLERK_SECRET_KEY=sk_...`

4. **Your app is live!** 🎉

---

## 📝 Service Setup Links

| Service | URL | Purpose |
|---------|-----|---------|
| **Neon** | https://neon.tech | PostgreSQL database |
| **Upstash** | https://upstash.com | Redis cache |
| **Clerk** | https://clerk.com | Authentication |
| **Gemini** | https://ai.google.dev | AI (FREE) |
| **Resend** | https://resend.com | Email |
| **Railway** | https://railway.app | Backend hosting |
| **Vercel** | https://vercel.com | Frontend hosting |
| **Sentry** | https://sentry.io | Error tracking |

---

## 🧪 Testing

### Backend Tests (pytest)
```python
# tests/test_api.py
import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "QueryForge API"

@pytest.mark.asyncio
async def test_health():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
```

### Run Tests
```bash
# Backend
pytest

# Frontend
npm run test
```

---

## 📊 Why PostgreSQL NOT MongoDB?

### ❌ MongoDB is WRONG for this project:
1. **Your app generates SQL queries** - MongoDB uses MQL (different language)
2. **Users connect to SQL databases** - PostgreSQL, MySQL, SQL Server
3. **Relational data model** - Users → Queries → Feedback (perfect for SQL)
4. **ACID transactions needed** - For billing, auth, audit logs
5. **Better free tier** - Neon PostgreSQL > MongoDB Atlas

### ✅ PostgreSQL is PERFECT:
1. **Native SQL support** - Your core feature!
2. **Relational model** - Fits your data perfectly
3. **JSONB columns** - Flexible data when needed
4. **Full-text search** - Built-in
5. **Neon free tier** - 0.5 GB, serverless, excellent

---

## 💡 Development Tips

1. **Use FastAPI docs**: http://localhost:8000/docs
2. **Test endpoints** with Swagger UI (built-in)
3. **Use Alembic** for database migrations
4. **Enable hot reload**: `uvicorn app.main:app --reload`
5. **Use pytest** for testing (async support)
6. **Format code**: `black app/` and `ruff check app/`
7. **Monitor logs** in Railway dashboard
8. **Check Sentry** for errors daily

---

## 🎯 Next Steps

1. ✅ Set up all services (30 min)
2. ✅ Create backend structure (1 hour)
3. ✅ Create frontend structure (1 hour)
4. ✅ Implement AI service (30 min)
5. ✅ Deploy to Railway + Vercel (30 min)
6. ✅ Test with sample queries (30 min)

**Total setup time: ~4 hours** ⚡

---

## 📚 Documentation

- **FastAPI**: https://fastapi.tiangolo.com
- **SQLAlchemy**: https://docs.sqlalchemy.org
- **Alembic**: https://alembic.sqlalchemy.org
- **Gemini**: https://ai.google.dev/docs
- **Railway**: https://docs.railway.app
- **Clerk**: https://clerk.com/docs

---

**Ready to build?**

```bash
# Backend
mkdir queryforge-backend && cd queryforge-backend
python -m venv venv && source venv/bin/activate
pip install fastapi uvicorn sqlalchemy asyncpg

# Frontend
npx create-next-app@latest queryforge-frontend

# Let's go! 🚀
```
