# Let's Kill Cancer (CancerProject2026)

A Django-based clinical awareness and risk-assessment platform with role-based workflows for patients and doctors.

> Important: This system is AI-assisted and non-diagnostic. It supports clinical review and awareness, and does not replace professional medical judgment.

## Current Status

Implemented and working in this repository:

- Patient registration and login
- Doctor login using professional ID
- Doctor dashboard with AI-support analytics UI
- Dynamic diagnosis form driven by active `Feature` rows in DB
- ML-backed risk prediction integration
- Patient-linked diagnosis records
- Professional report view with print + PDF download flow
- Doctor settings page (profile image, contact, and professional details)

## Project Structure

- `letskillcancer/` - project config (`settings.py`, `urls.py`, etc.)
- `accounts/` - auth, patient/doctor profiles
- `doctor/` - doctor dashboard, diagnosis, report, settings
- `ml_engine/` - model/scaler loading and prediction mapping
- `templates/`, `static/` - shared frontend assets
- `docs/` - setup and planning documentation

## Tech Stack

- Backend: Django
- Database: PostgreSQL (configured in `settings.py` via `.env`)
- AI/ML: scikit-learn, pandas, numpy
- Report PDF: WeasyPrint

## Quick Start (Windows / PowerShell)

Prerequisites:

- Python 3.11+ (3.13 is currently being used in this project)
- PostgreSQL

```bash
# 1) Create and activate virtual environment
python -m venv venv
venv\Scripts\Activate.ps1

# 2) Install dependencies
pip install -r requirements.txt

# 3) Apply migrations
python manage.py migrate

# 4) Run server
python manage.py runserver
```

Open: `http://127.0.0.1:8000/`

## Environment Variables

Create a `.env` file in project root. Typical values:

- `SECRET_KEY`
- `DEBUG`
- `ALLOWED_HOSTS`
- `DATABASE_NAME`
- `DATABASE_USER`
- `DATABASE_PASSWORD`
- `DATABASE_HOST`
- `DATABASE_PORT`

## Doctor Workflow (Implemented)

1. Doctor signs in.
2. Doctor opens dashboard (`/doctor/`).
3. Doctor starts a new diagnosis (`/doctor/diagnosis/`) and optionally selects a registered patient.
4. Prediction result is saved as a `DoctorInput` record linked to doctor and (optionally) patient.
5. Doctor opens report page (`/doctor/report/<id>/`) to print or download PDF.

## PDF Notes

PDF generation uses WeasyPrint.

If PDF download fails in your local Windows environment, install required WeasyPrint system dependencies in addition to Python packages.

## Safety Notes

- Treat all health-related data as sensitive.
- Keep `DEBUG=False` in production.
- Enforce secure secret management and HTTPS in deployment.

## License / Usage

This repository is for educational and project development use unless otherwise specified by the maintainer.
