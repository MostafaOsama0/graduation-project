# Sage — AI Academic Assistant

Sage is an intelligent academic study companion and planner designed for university students. It combines course material retrieval with page-level citations, adaptive study scheduling, and mastery tracking.

## Architecture

- **Web Frontend (`apps/web`)**: React 19 + TypeScript, Vite, Tailwind CSS, TanStack Query, React Router.
- **Core API (`api`)**: Python 3.11+, FastAPI, SQLAlchemy 2, Alembic, pyodbc.
- **Database (`db`)**: Microsoft SQL Server 2025 with native `VECTOR` embeddings.
- **AI & RAG Engine**: Google Gemini API, local embeddings (`BAAI/bge-small-en-v1.5`), PyMuPDF parsing.
- **Analytics**: Power BI Desktop connecting to SQL Server reporting views (`vw_*`).

---

## Repository Structure

```text
graduation-project/
├── apps/
│   └── web/              # React 19 + TypeScript frontend
├── api/                  # FastAPI backend service
│   ├── app/
│   │   ├── core/         # Settings & configuration
│   │   ├── db/           # Database engine & session
│   │   ├── models/       # SQLAlchemy models
│   │   ├── schemas/      # Pydantic validation schemas
│   │   ├── routers/      # API route handlers
│   │   └── services/     # Ingestion, RAG, mastery & planner logic
│   └── tests/            # Pytest test suite
├── db/
│   └── init/             # SQL Server database bootstrap scripts
├── eval/                 # Evaluation harness and benchmark datasets
├── docker-compose.yml    # Development SQL Server container configuration
└── .env.example          # Environment variable template
```

---

## Quickstart

### 1. Prerequisites
- Python 3.11+
- Node.js 20+
- Docker Desktop or a local Microsoft SQL Server instance
- ODBC Driver 18 (or 17) for SQL Server

### 2. Environment Configuration
Copy `.env.example` to `.env` and fill in your database credentials:
```bash
cp .env.example .env
```

### 3. Backend Setup
```powershell
cd api
python -m venv .venv
.\.venv\Scripts\activate
pip install -e ".[dev]"
pytest
uvicorn app.main:app --reload
```
The API documentation is available at `http://localhost:8000/docs`.

### 4. Frontend Setup
```powershell
cd apps/web
npm.cmd install
npm.cmd run dev
```
The application runs at `http://localhost:5173`.
