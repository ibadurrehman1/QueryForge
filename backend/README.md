# QueryForge Backend

FastAPI backend for QueryForge - Natural Language to SQL SaaS application.

## Setup

1. **Create virtual environment:**
```bash
python -m venv venv
```

2. **Activate virtual environment:**
```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables:**
```bash
cp .env.example .env
# Edit .env and add your API keys
```

5. **Run development server:**
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI application
│   ├── config.py         # Settings & environment variables
│   ├── database.py       # Database connection
│   ├── models/           # SQLAlchemy models
│   ├── schemas/          # Pydantic schemas
│   ├── api/              # API routes
│   │   └── v1/           # API version 1
│   ├── services/         # Business logic
│   ├── utils/            # Utilities
│   └── middleware/       # Custom middleware
├── alembic/              # Database migrations
├── tests/                # Tests
├── requirements.txt      # Python dependencies
└── .env.example          # Environment variables template
```

## Testing

```bash
pytest
```

## Code Quality

```bash
# Format code
black app/

# Lint code
ruff check app/
```

## Database Migrations

```bash
# Create migration
alembic revision --autogenerate -m "Description"

# Apply migrations
alembic upgrade head

# Rollback
alembic downgrade -1
```

## Deployment

See main project documentation for deployment instructions.
