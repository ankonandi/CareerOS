# CareerOS

CareerOS is a production-grade AI-powered Career Copilot designed to help professionals navigate and optimize their career journeys. It acts as an intelligent assistant that parses resumes, analyzes job descriptions, identifies skill gaps, creates personalized learning pathways, and provides simulated voice/text interview coaching with automated AI evaluation.

---

## Project Vision

The long-term roadmap for CareerOS includes the following capability layers, which will be introduced incrementally:

*   **Secure Core:** Secure authentication and profile management.
*   **Resume Intelligence:** Resume parsing and structured content extraction.
*   **Market Analysis:** Job description parsing and matching algorithms.
*   **Skill Optimization:** Gap analysis and personalized learning plans.
*   **Interview Coaching:** Interactive text and voice-based mock interviews with automated AI feedback.
*   **Advanced AI Workflows:** Retrieval-Augmented Generation (RAG) and collaborative multi-agent setups.
*   **Analytics & Reporting:** Rich metrics for users and an administrative dashboard.

---

## Tech Stack

### Backend Service
*   **Language:** Python 3.13+
*   **API Framework:** FastAPI
*   **Database:** PostgreSQL
*   **ORM:** SQLAlchemy 2.0
*   **Database Migrations:** Alembic
*   **Configuration Management:** Pydantic Settings
*   **Package Manager:** uv
*   **Code Quality:** Ruff (linting/formatting), pytest (testing)
*   **Containerization:** Docker

### GenAI & Infrastructure (Planned)
*   **Local LLM Execution:** Ollama
*   **Agentic Workflows:** LangGraph
*   **Caching & Session Management:** Redis
*   **Vector Search:** Qdrant
*   **Observability:** Prometheus & Grafana

---

## Directory Structure

```text
CareerOS/
├── .github/                  # GitHub configurations and templates
│   ├── workflows/            # CI/CD pipeline definitions
│   └── ISSUE_TEMPLATE/       # Automated issue templates
├── backend/                  # Python backend application
│   ├── alembic/              # Database migration scripts
│   ├── app/                  # Main application source code
│   │   ├── api/              # API endpoints and routers
│   │   ├── common/           # Shared helpers and utility code
│   │   ├── config/           # Pydantic settings and configuration
│   │   ├── core/             # Core server logic (security, server lifecycle)
│   │   ├── database/         # Database connection and session management
│   │   └── main.py           # Application entrypoint
│   ├── tests/                # Test suite (unit and integration tests)
│   └── pyproject.toml        # Backend dependencies and tool configurations
├── docker/                   # Custom Dockerfiles and local service setups
├── docs/                     # Project documentation
│   ├── adr/                  # Architectural Decision Records (ADRs)
│   ├── architecture/         # System design diagrams and specs
│   ├── api/                  # API contracts and specifications
│   ├── development/          # Setup guides and code standards
│   └── deployment/           # Production deployment plans
├── scripts/                  # Utility and orchestration scripts
├── .env.example              # Example environment variables
├── .gitignore                # Git untracked patterns
├── docker-compose.yml        # Development infrastructure setup
├── LICENSE                   # Software license (MIT)
└── README.md                 # Project README
```

---

## Development Roadmap

```mermaid
gantt
    title CareerOS Release Plan
    dateFormat  YYYY-MM
    section Core Infrastructure
    Sprint 0 - Engineering Foundation   :active, 2026-07, 2026-08
    Sprint 1 - Auth & Resume Parse      : 2026-08, 2026-09
    section Matching & Skills
    Sprint 2 - JD Matching & Analysis   : 2026-09, 2026-10
    Sprint 3 - Skill Gap & Learning     : 2026-10, 2026-11
    section AI Interviews
    Sprint 4 - Interview Gen & Voice    : 2026-11, 2026-12
    Sprint 5 - Evaluation & Tracking    : 2026-12, 2027-01
    section Advanced & Ops
    Sprint 6 - RAG & Multi-Agent        : 2027-01, 2027-02
    Sprint 7 - Analytics & Dashboards   : 2027-02, 2027-03
    Sprint 8 - Production Deployment    : 2027-03, 2027-04
```

---

## Development Setup

Follow these steps to set up a local development environment for CareerOS:

### 1. Prerequisites
Ensure you have Python 3.13+ installed on your host system.

### 2. Install `uv`
`uv` is the package and environment manager utilized in this project.
*   **macOS / Linux:**
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
*   **Windows (PowerShell):**
    ```powershell
    powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```
*   **Via pip:**
    ```bash
    pip install uv
    ```

### 3. Initialize Virtual Environment & Install Dependencies
Navigate to the `backend/` directory, set up the virtual environment, and synchronize all packages and development tools:
```bash
cd backend
uv venv
uv sync
```
This generates a local `.venv` environment and installs all dependencies specified in the `pyproject.toml` configuration.

### 4. Activate the Virtual Environment
*   **macOS / Linux:**
    ```bash
    source .venv/bin/activate
    ```
*   **Windows (PowerShell):**
    ```powershell
    .venv\Scripts\Activate.ps1
    ```

### 5. Local Configurations (.env)
Copy the example environment settings to `.env` in the repository root directory:
```bash
cp .env.example .env
```
Update database names, credentials, or custom settings in your local `.env` file.

### 6. Development Quality Tools
We use Ruff for code formatting and linting. Run these checks inside the `backend/` directory:
*   **Run Linter:**
    ```bash
    uv run ruff check .
    ```
*   **Run Linter (with Auto-fixes):**
    ```bash
    uv run ruff check --fix .
    ```
*   **Run Formatter Check:**
    ```bash
    uv run ruff format --check .
    ```
*   **Run Formatter:**
    ```bash
    uv run ruff format .
    ```

### 7. Run the Skeleton Application
Verify that the configuration is parsed correctly by running the application entrypoint:
```bash
uv run python -m app.main
```

### 8. Git Pre-Commit Hooks
Pre-commit checks are configured to block commits containing format or lint violations.
Install the hooks in your local Git folder (run this from the `backend/` directory or root):
```bash
uv run pre-commit install
```
To run the hooks manually on all repository files:
```bash
uv run pre-commit run --all-files
```

---

## Sprint Status

### Sprint 0: Engineering Foundation (Current)
*   **Goal:** Establish clean repository layout, configure local database services, set up documentation templates, and define initial dependency management systems.
*   **Status:** In Progress (Repository Structure Setup)
