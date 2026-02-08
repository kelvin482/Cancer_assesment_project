# "Let's Kill Cancer" - Quick Setup Guide

This guide provides a quick reference for setting up the development environment. For detailed technical documentation, see `TECHNICAL_STACK_DOCUMENTATION.md`.

## Prerequisites

- **Python**: 3.10 or 3.11
- **PostgreSQL**: 14 or 15
- **Node.js & npm**: (if using Tailwind CSS build process)
- **Git**: For version control

## Quick Start Checklist

### 1. Backend Setup
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install Python packages
pip install -r requirements.txt
```

### 2. Database Setup
```bash
# Create PostgreSQL database
createdb letskillcancer

# Or using psql:
psql -U postgres
CREATE DATABASE letskillcancer;
CREATE USER dbuser WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE letskillcancer TO dbuser;
```

### 3. Environment Configuration
1. Copy `.env.example` to `.env` (create manually if needed)
2. Update all environment variables with your local values
3. Generate Django secret key: `python -m django startproject temp && python temp/manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`

### 4. Django Project Initialization
```bash
# Create Django project (if not already created)
django-admin startproject letskillcancer .

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

### 5. Tailwind CSS Setup (Choose One)

**Option A: CDN (Quick Start)**
- Add Tailwind CDN link to `base.html` template
- No build process needed

**Option B: Local Build (Recommended)**
```bash
# Install Tailwind CSS
npm install -D tailwindcss

# Initialize Tailwind
npx tailwindcss init

# Configure tailwind.config.js
# Build CSS
npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --watch
```

## Project Structure Overview

```
letskillcancer/
├── manage.py
├── requirements.txt
├── .env (not in git)
├── .env.example
├── TECHNICAL_STACK_DOCUMENTATION.md
├── SETUP_GUIDE.md
├── letskillcancer/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/                    # Django apps
│   ├── accounts/           # User authentication
│   ├── assessment/         # Risk assessment
│   ├── dashboard/          # Dashboards
│   ├── donations/          # Donation module
│   └── api/                # REST API endpoints
├── templates/              # HTML templates
│   ├── base.html
│   ├── base_dashboard.html
│   └── [app_name]/
├── static/                 # Static files
│   ├── css/
│   ├── js/
│   └── images/
├── media/                  # User uploads
├── models/                 # ML model files
└── tests/                  # Test files
```

## Key Technologies Summary

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Backend Framework | Django 4.2+ | Web framework, ORM, admin |
| API | Django REST Framework | REST API endpoints |
| Database | PostgreSQL 14+ | Data storage |
| Frontend | HTML + Django Templates | Dynamic pages |
| Styling | Tailwind CSS | UI styling |
| Interactivity | Vanilla JavaScript | Client-side logic |
| AI/ML | Scikit-learn, Pandas | Risk assessment |
| Task Queue | Celery + Redis | Async tasks |
| Authentication | Django Allauth | User management |

## Next Steps

1. Review `TECHNICAL_STACK_DOCUMENTATION.md` for detailed explanations
2. Set up your development environment using this guide
3. Create Django apps for each module (accounts, assessment, dashboard, donations)
4. Design database models based on entity list in documentation
5. Create base templates with Tailwind CSS
6. Implement authentication system
7. Build risk assessment questionnaire
8. Integrate AI/ML model
9. Create role-based dashboards
10. Implement donation module

## Important Notes

- **Never commit `.env` file** to version control
- **Set `DEBUG=False`** in production
- **Use strong `SECRET_KEY`** in production
- **Enable HTTPS** in production (SESSION_COOKIE_SECURE=True)
- **Regular database backups** are essential for healthcare data
- **Compliance**: Ensure HIPAA considerations for healthcare data handling

## Support & Documentation

- **Full Technical Documentation**: See `TECHNICAL_STACK_DOCUMENTATION.md`
- **Django Documentation**: https://docs.djangoproject.com/
- **Tailwind CSS Documentation**: https://tailwindcss.com/docs
- **PostgreSQL Documentation**: https://www.postgresql.org/docs/

