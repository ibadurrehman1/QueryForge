# QueryForge - Tech Stack Documentation (FastAPI Backend)
## Optimized for Free Tier (10 Users, Zero Cost, Zero Downtime)

---

## Executive Summary

This tech stack uses **FastAPI** for the backend with a **PostgreSQL** database, carefully selected to support **10 concurrent users** with:
- ✅ **Zero monthly costs**
- ✅ **Zero downtime** (99.9%+ uptime)
- ✅ **Production-ready** performance
- ✅ **Scalable** architecture (easy to upgrade when needed)

---

## Why PostgreSQL Over MongoDB?

### ❌ Why NOT MongoDB for This Project:

1. **The App Generates SQL Queries** 🚨
   - Your core feature is converting natural language to **SQL**
   - MongoDB uses a completely different query language (MQL - MongoDB Query Language)
   - You'd need to convert NL → SQL → MQL (extra complexity and errors)
   - **This defeats the entire purpose of your app!**

2. **Relational Data is Perfect for This Use Case**
   - User → Queries (one-to-many)
   - Query → Feedback (one-to-one)
   - User → DatabaseConnections (one-to-many)
   - These are **textbook relational patterns**

3. **Users Connect to SQL Databases**
   - Your users will connect to PostgreSQL, MySQL, SQL Server, etc.
   - They want to query **their SQL databases**
   - Having your app database also be SQL makes debugging easier
   - You can test queries on your own database structure

4. **ACID Transactions Matter**
   - User authentication, query logging, billing need strong consistency
   - PostgreSQL provides ACID guarantees
   - MongoDB's eventual consistency can cause issues with financial/audit data

5. **Better Free Tier Options**
   - **Neon PostgreSQL**: 0.5 GB free, serverless, excellent
   - **MongoDB Atlas**: 512 MB free, but limited connections (10-100 depending on tier)
   - **Supabase**: 500 MB PostgreSQL free + built-in auth

6. **JSON Support in PostgreSQL**
   - PostgreSQL has JSONB columns (best of both worlds)
   - You can store flexible data when needed
   - No need for MongoDB's schema-less design

7. **Full-Text Search**
   - PostgreSQL has excellent built-in full-text search
   - MongoDB requires separate text indexes
   - PostgreSQL's `tsvector` is powerful and free

### ✅ When MongoDB WOULD Be Better:
- Storing unstructured logs (but we use Axiom for that)
- Real-time analytics with massive write throughput (not needed for 10 users)
- Geospatial queries (not relevant here)
- Document-heavy applications (this is a SQL query tool!)

### 🎯 Verdict: PostgreSQL is the Clear Winner
- Native SQL support
- Relational data model fits perfectly
- Better free tier (Neon)
- ACID compliance
- JSON support when needed
- Easier to debug and maintain

---

## 1. Frontend Stack

### **Framework: Next.js 14+ (App Router)**
- **Cost**: Free (open source)
- **Why**: 
  - Server-side rendering for better SEO
  - React Server Components for performance
  - Strong TypeScript support
  - Easy deployment to Vercel
  - Can call FastAPI backend via API routes or directly

### **Language: TypeScript**
- **Cost**: Free
- **Why**: Type safety, better developer experience

### **Styling: Tailwind CSS**
- **Cost**: Free (open source)
- **Why**: 
  - Utility-first CSS framework
  - Perfect for dark/light mode theming
  - Smaller bundle sizes
  - Highly customizable

### **UI Components: shadcn/ui**
- **Cost**: Free (copy-paste components)
- **Why**:
  - Not a dependency (you own the code)
  - Built on Radix UI (accessible)
  - Fully customizable
  - Dark mode support out of the box

### **Icons: Lucide React**
- **Cost**: Free (open source)
- **Why**: Lightweight, tree-shakeable, modern

### **Charts: Recharts**
- **Cost**: Free (open source)
- **Why**: React-based, responsive, customizable

### **State Management: Zustand**
- **Cost**: Free (open source)
- **Why**: Lightweight (1kb), simple API

### **Form Handling: React Hook Form + Zod**
- **Cost**: Free (open source)
- **Why**: Performant, easy validation

---

## 2. Backend Stack (FastAPI)

### **Framework: FastAPI**
- **Cost**: Free (open source)
- **Why**:
  - ⚡ **Blazing fast** (one of the fastest Python frameworks)
  - 🔒 **Automatic API documentation** (Swagger UI + ReDoc)
  - ✅ **Type hints** with Pydantic (like TypeScript for Python)
  - 🚀 **Async support** (perfect for I/O-heavy operations like database queries)
  - 📝 **Auto-validation** of request/response data
  - 🔌 **WebSocket support** (for future real-time features)
  - 🎯 **Dependency injection** (clean architecture)
  - 📊 **Better for AI/ML integration** (Python ecosystem)

### **Language: Python 3.11+**
- **Cost**: Free
- **Why**:
  - Best ecosystem for AI/ML (Gemini SDK, OpenAI, etc.)
  - Excellent for data processing
  - Great for SQL query parsing and validation
  - Mature libraries for database connections

### **ORM: SQLAlchemy 2.0**
- **Cost**: Free (open source)
- **Why**:
  - Industry-standard Python ORM
  - Async support (SQLAlchemy 2.0+)
  - Works with PostgreSQL, MySQL, SQL Server
  - Type-safe with Pydantic
  - Migration support via Alembic

### **Database Driver: asyncpg**
- **Cost**: Free (open source)
- **Why**:
  - Fastest PostgreSQL driver for Python
  - Async/await support
  - Better performance than psycopg2

### **Validation: Pydantic V2**
- **Cost**: Free (open source)
- **Why**:
  - Built into FastAPI
  - Type validation
  - JSON schema generation
  - Data serialization

### **API Documentation: Automatic (FastAPI)**
- **Cost**: Free (built-in)
- **Why**:
  - Swagger UI at `/docs`
  - ReDoc at `/redoc`
  - OpenAPI schema auto-generated

---

## 3. Database Stack

### **Primary Database: Neon (PostgreSQL)**
- **Cost**: **FREE TIER**
  - 0.5 GB storage
  - Unlimited compute hours
  - Serverless PostgreSQL
  - Auto-scaling
- **Why**:
  - True PostgreSQL (not limited)
  - Serverless (scales to zero)
  - Built-in connection pooling
  - 99.95% uptime SLA
  - Branching for dev/staging
  - **Perfect for SQL-based app**
- **Alternative**: **Supabase** (500MB free + built-in auth)

### **Caching: Upstash Redis**
- **Cost**: **FREE TIER**
  - 10,000 commands/day
  - 256 MB storage
  - Serverless Redis
- **Why**:
  - Query result caching
  - Session storage
  - Rate limiting
  - No idle costs

### **File Storage: Cloudflare R2**
- **Cost**: **FREE TIER**
  - 10 GB storage
  - 1M requests/month
- **Why**: S3-compatible, generous free tier
- **Alternative**: Vercel Blob (1 GB free)

---

## 4. Authentication & Authorization

### **Auth Provider: Clerk**
- **Cost**: **FREE TIER**
  - Up to 10,000 monthly active users
  - Email/password + OAuth
  - Session management
  - User management UI
  - 2FA included
- **Why**:
  - Drop-in authentication
  - Beautiful pre-built UI
  - Dark mode support
  - RBAC (Role-Based Access Control)
  - Works seamlessly with FastAPI (JWT tokens)

### **JWT Handling: python-jose**
- **Cost**: Free (open source)
- **Why**: Verify Clerk JWT tokens in FastAPI

### **Authorization: Custom RBAC**
- **Cost**: Free (implement yourself)
- **Why**: Simple admin/user roles, easy to implement in FastAPI

---

## 5. AI/LLM Integration

### **Primary LLM: Google Gemini 1.5 Flash**
- **Cost**: **FREE TIER**
  - 15 requests per minute
  - 1 million tokens per minute
  - 1,500 requests per day
  - **Completely free for 10 users!**
- **Why**:
  - Excellent SQL generation
  - Fast inference
  - 1M token context window
  - Python SDK available
  - No cost for MVP

### **Alternative: OpenAI GPT-4o-mini**
- **Cost**: **PAY-AS-YOU-GO**
  - $0.150 per 1M input tokens
  - $0.600 per 1M output tokens
  - ~$5-15/month for 10 users
- **Why**: Better accuracy if needed

### **LLM Library: google-generativeai**
- **Cost**: Free (official SDK)
- **Why**: Official Python SDK for Gemini

### **Prompt Management: Jinja2 Templates**
- **Cost**: Free (open source)
- **Why**: Template-based prompts, easy to version control

---

## 6. Deployment & Hosting

### **Backend Hosting: Railway.app**
- **Cost**: **FREE TIER**
  - $5 free credits/month (enough for 10 users)
  - 500 hours/month execution time
  - 100 GB bandwidth
  - Automatic HTTPS
  - GitHub integration
  - Zero-config deployment
- **Why**:
  - Perfect for FastAPI
  - PostgreSQL included (can use Neon instead)
  - Auto-scaling
  - Built-in monitoring
  - Easier than Docker + VPS

### **Alternative Backend Hosting: Render.com**
- **Cost**: **FREE TIER**
  - 750 hours/month
  - Automatic HTTPS
  - Auto-deploy from Git
- **Why**: Also excellent for FastAPI

### **Frontend Hosting: Vercel**
- **Cost**: **FREE TIER**
  - Unlimited deployments
  - 100 GB bandwidth/month
  - Automatic HTTPS
  - Global CDN
  - 99.99% uptime SLA
- **Why**:
  - Built for Next.js
  - Zero-config deployment
  - Edge functions

### **Alternative: Cloudflare Pages**
- **Cost**: **FREE TIER**
  - Unlimited requests
  - Unlimited bandwidth
- **Why**: Even more generous

---

## 7. Monitoring & Analytics

### **Error Tracking: Sentry**
- **Cost**: **FREE TIER**
  - 5,000 errors/month
  - Python + JavaScript support
- **Why**: Catch bugs in both frontend and backend

### **API Monitoring: Better Stack (Uptime)**
- **Cost**: **FREE TIER**
  - 10 monitors
  - 3-minute checks
- **Why**: Monitor FastAPI endpoints
- **Alternative**: UptimeRobot (50 monitors, 5-min checks)

### **Logging: Axiom**
- **Cost**: **FREE TIER**
  - 500 MB/month
  - 30-day retention
- **Why**: Centralized logging for FastAPI

### **Analytics: Vercel Analytics**
- **Cost**: **FREE** (included)
- **Why**: Frontend analytics, privacy-friendly

---

## 8. Email Service

### **Transactional Emails: Resend**
- **Cost**: **FREE TIER**
  - 3,000 emails/month
  - 1 custom domain
- **Why**:
  - Modern API
  - Python SDK available
  - Great deliverability

---

## 9. Development Tools

### **Version Control: GitHub**
- **Cost**: Free
- **Why**: Industry standard

### **CI/CD: GitHub Actions**
- **Cost**: **FREE TIER**
  - 2,000 minutes/month
- **Why**: Automated testing, deployment

### **Code Quality:**
- **Backend**: Ruff (fast Python linter), Black (formatter)
- **Frontend**: ESLint + Prettier
- **Cost**: Free (open source)

### **Testing:**
- **Backend**: pytest + httpx (async testing)
- **Frontend**: Vitest + React Testing Library
- **Cost**: Free (open source)

### **API Testing: HTTPie or Postman**
- **Cost**: Free
- **Why**: Test FastAPI endpoints

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    USER (Browser)                            │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│              Vercel (Next.js Frontend)                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   React UI   │  │  API Client  │  │    Clerk     │      │
│  │  (TypeScript)│  │   (Fetch)    │  │   (Auth)     │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────┬───────────────────────────────────────┘
                      │ HTTPS/REST
                      ▼
┌─────────────────────────────────────────────────────────────┐
│           Railway.app (FastAPI Backend)                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   FastAPI    │  │  SQLAlchemy  │  │  JWT Auth    │      │
│  │   Routes     │  │     ORM      │  │  Middleware  │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────┬───────────────────────────────────────┘
                      │
        ┌─────────────┼─────────────┬─────────────┐
        │             │             │             │
        ▼             ▼             ▼             ▼
┌──────────────┐ ┌─────────┐ ┌──────────┐ ┌─────────────┐
│    Clerk     │ │  Neon   │ │ Upstash  │ │   Gemini    │
│  (Auth JWT)  │ │  (DB)   │ │ (Redis)  │ │  Flash AI   │
└──────────────┘ └─────────┘ └──────────┘ └─────────────┘
```

---

## Cost Breakdown (Monthly)

| Service | Free Tier Limit | Estimated Usage (10 Users) | Cost |
|---------|----------------|---------------------------|------|
| Railway (Backend) | $5 credits/month | ~$3-4 usage | **$0** |
| Vercel (Frontend) | 100 GB bandwidth | ~10-20 GB | **$0** |
| Neon (PostgreSQL) | 0.5 GB storage | ~100-200 MB | **$0** |
| Upstash Redis | 10K commands/day | ~1-2K/day | **$0** |
| Clerk Auth | 10K MAUs | 10 users | **$0** |
| Gemini Flash | 1,500 req/day | ~50-100/day | **$0** |
| Sentry | 5K errors/month | ~100-500/month | **$0** |
| Resend | 3K emails/month | ~100-300/month | **$0** |
| Better Stack | 10 monitors | 2 monitors | **$0** |
| Domain (optional) | N/A | 1 domain | **$1.25/month** |
| **TOTAL** | | | **$0-1.25/month** |

---

## FastAPI Project Structure

```
queryforge-backend/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI app entry point
│   ├── config.py               # Settings (env vars)
│   ├── database.py             # Database connection
│   ├── models/                 # SQLAlchemy models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── query.py
│   │   └── feedback.py
│   ├── schemas/                # Pydantic schemas
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── query.py
│   │   └── feedback.py
│   ├── api/                    # API routes
│   │   ├── __init__.py
│   │   ├── deps.py            # Dependencies (auth, db)
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── auth.py
│   │       ├── queries.py
│   │       ├── users.py
│   │       └── feedback.py
│   ├── services/               # Business logic
│   │   ├── __init__.py
│   │   ├── ai_service.py      # Gemini integration
│   │   ├── query_service.py   # Query execution
│   │   └── email_service.py   # Resend integration
│   ├── utils/                  # Utilities
│   │   ├── __init__.py
│   │   ├── auth.py            # JWT verification
│   │   ├── cache.py           # Redis caching
│   │   └── db_connector.py    # Connect to user databases
│   └── middleware/             # Custom middleware
│       ├── __init__.py
│       └── cors.py
├── alembic/                    # Database migrations
│   ├── versions/
│   └── env.py
├── tests/                      # Tests
│   ├── __init__.py
│   ├── test_api.py
│   └── test_services.py
├── .env                        # Environment variables
├── .env.example
├── requirements.txt            # Python dependencies
├── pyproject.toml             # Poetry config (optional)
├── alembic.ini                # Alembic config
└── README.md
```

---

## Backend Dependencies (requirements.txt)

```txt
# FastAPI
fastapi==0.109.0
uvicorn[standard]==0.27.0
python-multipart==0.0.6

# Database
sqlalchemy[asyncio]==2.0.25
asyncpg==0.29.0
alembic==1.13.1

# Validation
pydantic==2.5.3
pydantic-settings==2.1.0
email-validator==2.1.0

# Authentication
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6

# Redis
redis==5.0.1
upstash-redis==0.15.0

# AI/LLM
google-generativeai==0.3.2

# Email
resend==0.7.0

# HTTP Client (for calling user databases)
httpx==0.26.0

# Utilities
python-dotenv==1.0.0
jinja2==3.1.3

# Monitoring
sentry-sdk[fastapi]==1.40.0

# Testing
pytest==7.4.4
pytest-asyncio==0.23.3
httpx==0.26.0

# Code Quality
ruff==0.1.14
black==24.1.1
```

---

## FastAPI Main App (app/main.py)

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import sentry_sdk

from app.config import settings
from app.database import engine, Base
from app.api.v1 import auth, queries, users, feedback

# Initialize Sentry
sentry_sdk.init(
    dsn=settings.SENTRY_DSN,
    traces_sample_rate=1.0,
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Shutdown
    await engine.dispose()

app = FastAPI(
    title="QueryForge API",
    description="Natural Language to SQL API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(queries.router, prefix="/api/v1/queries", tags=["queries"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(feedback.router, prefix="/api/v1/feedback", tags=["feedback"])

@app.get("/")
async def root():
    return {"message": "QueryForge API", "version": "1.0.0"}

@app.get("/health")
async def health():
    return {"status": "healthy"}
```

---

## Environment Variables (.env)

```env
# App
APP_NAME=QueryForge
ENVIRONMENT=development
DEBUG=True
ALLOWED_ORIGINS=http://localhost:3000,https://yourdomain.com

# Database (Neon)
DATABASE_URL=postgresql+asyncpg://user:password@host.neon.tech/dbname

# Redis (Upstash)
REDIS_URL=redis://default:password@host.upstash.io:6379

# Auth (Clerk)
CLERK_SECRET_KEY=sk_test_...
CLERK_PUBLISHABLE_KEY=pk_test_...

# AI (Gemini)
GEMINI_API_KEY=AIza...

# Email (Resend)
RESEND_API_KEY=re_...

# Sentry
SENTRY_DSN=https://...@sentry.io/...

# JWT
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## Deployment Commands

### **Deploy Backend to Railway:**
```bash
# 1. Install Railway CLI
npm install -g @railway/cli

# 2. Login
railway login

# 3. Initialize project
railway init

# 4. Add environment variables in Railway dashboard

# 5. Deploy
railway up

# Done! Your FastAPI backend is live
```

### **Deploy Frontend to Vercel:**
```bash
# 1. Push to GitHub
git push origin main

# 2. Connect to Vercel
vercel

# 3. Add environment variables (backend URL)
# NEXT_PUBLIC_API_URL=https://your-backend.railway.app

# Done! Your Next.js frontend is live
```

---

## Why FastAPI > Next.js API Routes?

### ✅ Advantages of FastAPI:
1. **Better for Python AI/ML ecosystem** (Gemini, OpenAI, data processing)
2. **Automatic API documentation** (Swagger UI, ReDoc)
3. **Async/await** for better performance with I/O operations
4. **Type safety** with Pydantic (like TypeScript)
5. **Easier to test** (pytest is excellent)
6. **Better for complex SQL operations** (Python has better DB libraries)
7. **Separation of concerns** (frontend and backend can scale independently)
8. **WebSocket support** (for future real-time features)

### ❌ Disadvantages:
1. **Two deployments** instead of one (but both are free!)
2. **CORS configuration** needed
3. **Slightly more complex** architecture

### 🎯 Verdict: FastAPI is Better for This Project
- Your app is **data-heavy** (SQL queries, AI processing)
- Python is **better for AI/ML** integration
- FastAPI is **faster** for async operations
- **Automatic API docs** save development time
- **Easier to scale** backend independently

---

## Getting Started Checklist

- [ ] Set up GitHub repository
- [ ] Create Neon PostgreSQL database
- [ ] Create Upstash Redis instance
- [ ] Create Clerk account
- [ ] Get Gemini API key
- [ ] Create Resend account
- [ ] Create Railway account
- [ ] Create Vercel account
- [ ] Deploy FastAPI backend to Railway
- [ ] Deploy Next.js frontend to Vercel
- [ ] Configure environment variables
- [ ] Test with 2-3 users

---

## Conclusion

This **FastAPI + PostgreSQL** stack provides:
- ✅ **Production-ready** backend with automatic API docs
- ✅ **Zero-cost** hosting for 10 users
- ✅ **Better AI/ML integration** (Python ecosystem)
- ✅ **Relational database** (perfect for SQL-based app)
- ✅ **Fast async performance**
- ✅ **Easy to scale** when you grow

**Total cost: $0-1.25/month** (domain optional)

**Estimated Development Time**: 4-6 weeks for MVP with 1-2 developers.
