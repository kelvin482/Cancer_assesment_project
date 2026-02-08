# Let's Kill Cancer (CancerProject2026)

A beginner-friendly web-based **cancer awareness + early risk screening** platform built with **Django + PostgreSQL**.

> **Important (Non‑Diagnostic):** This project **does not diagnose cancer**. It is an awareness and guidance tool that outputs a risk level (Low/Medium/High) and encourages professional medical consultation.

## What this app is

- **Patients**: register/login, read awareness content, complete an AI-assisted risk questionnaire, view results, receive doctor advice
- **Doctors**: register, wait for admin approval, review patient assessments, provide advice
- **Admins**: approve doctors, manage users/content/donations, view system stats

## Repository structure (current)

- `letskillcancer/`: Django project configuration (`settings.py`, `urls.py`, `asgi.py`, `wsgi.py`)
- `manage.py`: Django entrypoint
- `docs/`: All project documentation (see below)

## Architecture (planned apps)

Per `docs/APP_ARCHITECTURE.md`, the codebase is intended to use a clear multi-app layout:

- **Core role apps**
  - `accounts`: authentication + patient features
  - `doctors`: doctor features (depends on `accounts`)
  - `admin`: super admin features (can use all apps)
- **Shared feature apps**
  - `assessment`: questionnaire + risk assessment results
  - `content`: articles + health tips
  - `donations`: donations module

## Tech stack

High level:

- **Backend**: Django (4.2+), Django REST Framework
- **Database**: PostgreSQL (14/15 recommended)
- **Styling**: Tailwind CSS (CDN quick start or local build)
- **AI/ML**: scikit-learn + pandas + numpy + joblib (risk level classification)

Dependencies live in `requirements.txt`.

## Quick start (Windows / PowerShell)

Prereqs: **Python 3.10/3.11**, **PostgreSQL 14/15**.

```bash
# 1) Create + activate venv
python -m venv venv
venv\Scripts\Activate.ps1

# 2) Install dependencies
pip install -r requirements.txt

# 3) Run migrations
python manage.py migrate

# 4) Start server
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## Database setup (PostgreSQL)

Create a database and user, then configure your environment variables (.env).

See:
- `docs/POSTGRESQL_SETUP.md`
- `docs/SETUP_GUIDE.md`

## Environment variables

This project is designed to load secrets from a local `.env` file (do not commit it).

See `docs/TECHNICAL_STACK_DOCUMENTATION.md` for the expected variables (e.g. `DATABASE_*`, `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`).

## Documentation map

- **Setup / install**: `docs/SETUP_GUIDE.md`, `docs/QUICK_START_CHECKLIST.md`
- **Architecture**: `docs/APP_ARCHITECTURE.md`
- **Implementation details**: `docs/IMPLEMENTATION_GUIDE.md`
- **Stack / design notes**: `docs/TECHNICAL_STACK_DOCUMENTATION.md`
- **Progress / roadmap**: `docs/CURRENT_STATUS.md`, `docs/PROGRESS_TRACKER.md`, `docs/PROJECT_ROADMAP.md`, `docs/SIMPLE_ROADMAP.md`

## Safety & ethics

- The app must clearly communicate that results are **awareness-only** and **non-diagnostic**
- Store and handle user data responsibly (health-adjacent data; treat as sensitive)
- For production: run with `DEBUG=False`, configure HTTPS cookies, and use strong secret management

## Contributing

If you’re working on this project:

1. Follow `docs/SETUP_GUIDE.md` to get a working environment.
2. Stick to the app boundaries in `docs/APP_ARCHITECTURE.md` to avoid cross-app conflicts.
3. Keep changes small and documented; update `docs/CURRENT_STATUS.md` / roadmap docs as you implement.

