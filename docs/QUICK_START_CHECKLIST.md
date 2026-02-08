# Quick Start Checklist - "Let's Kill Cancer"

## 🚀 Ready to Code? Follow These Steps!

### ✅ STEP 1: Project Planning
- [x] **COMPLETED** - User roles defined, system boundaries set

### 🔄 STEP 2: Environment Setup (START HERE)
```bash
# 1. Check Python version
python --version  # Should be 3.10 or 3.11

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 4. Install Django
pip install Django>=4.2

# 5. Create Django project
django-admin startproject letskillcancer .

# 6. Install required packages
pip install -r requirements.txt

# 7. Run server
python manage.py runserver

# 8. Verify: Open http://127.0.0.1:8000/ - Should see Django welcome page
```
**✅ Success when:** Django welcome page loads in browser

---

### ⏳ STEP 3: Database & Core Configuration
```bash
# 1. Install PostgreSQL (if not installed)
# Windows: Download from postgresql.org
# Mac: brew install postgresql@14
# Linux: sudo apt-get install postgresql-14

# 2. Create database
psql -U postgres
CREATE DATABASE letskillcancer;
CREATE USER dbuser WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE letskillcancer TO dbuser;
\q

# 3. Create .env file (copy from .env.example)
# Fill in database credentials

# 4. Update settings.py to use environment variables
# (See IMPLEMENTATION_GUIDE.md for code)

# 5. Run migrations
python manage.py migrate

# 6. Test database connection
python manage.py dbshell
```
**✅ Success when:** Migrations run successfully, database connection works

---

### ⏳ STEP 4: Authentication & User Roles
```bash
# 1. Create accounts app
python manage.py startapp accounts

# 2. Add 'accounts' to INSTALLED_APPS in settings.py

# 3. Create user groups
python manage.py create_groups

# 4. Create login, register, logout views
# (See IMPLEMENTATION_GUIDE.md for code)

# 5. Create templates (login.html, register.html)

# 6. Test: Create test users and login
```
**✅ Success when:** Can register as patient/doctor, login works, users assigned to groups

---

### ⏳ STEP 5: Profile Models
```bash
# 1. Create PatientProfile and DoctorProfile models
# (See IMPLEMENTATION_GUIDE.md for code)

# 2. Create migrations
python manage.py makemigrations accounts

# 3. Apply migrations
python manage.py migrate

# 4. Create signals to auto-create profiles
# (See IMPLEMENTATION_GUIDE.md for code)

# 5. Register models in admin.py
```
**✅ Success when:** User registration auto-creates profile, profiles visible in admin

---

### ⏳ STEP 6: Role-Based Access Control
```bash
# 1. Create decorators (patient_required, doctor_required, admin_required)
# (See IMPLEMENTATION_GUIDE.md for code)

# 2. Test access control:
# - Patient cannot access doctor views
# - Unverified doctor cannot access doctor views
# - Verified doctor can access doctor views
# - Admin can access admin views
```
**✅ Success when:** Access control works correctly, unverified doctors blocked

---

### ⏳ STEP 7: Basic Dashboards
```bash
# 1. Create dashboard app
python manage.py startapp dashboard

# 2. Add 'dashboard' to INSTALLED_APPS

# 3. Create dashboard views (patient, doctor, admin)

# 4. Create basic dashboard templates

# 5. Update login to redirect to correct dashboard
```
**✅ Success when:** Each role sees their dashboard, login redirects correctly

---

### ⏳ STEP 8: Core Features
```bash
# Now build features:
# - AI risk assessment
# - Doctor advice system
# - Awareness content
# - Donations module
```
**✅ Success when:** All features work correctly with proper access control

---

## 📋 Current Status Tracker

**Current Step:** _______________

**Completed Steps:**
- [x] Step 1: Project Planning
- [ ] Step 2: Environment Setup
- [ ] Step 3: Database & Configuration
- [ ] Step 4: Authentication & User Roles
- [ ] Step 5: Profile Models
- [ ] Step 6: Role-Based Access Control
- [ ] Step 7: Basic Dashboards
- [ ] Step 8: Core Features

---

## 🆘 Troubleshooting

### Python version wrong?
- Download correct version from python.org
- Use `py -3.11` on Windows if multiple versions installed

### Virtual environment not activating?
- Windows: Use `venv\Scripts\activate.bat` or `venv\Scripts\Activate.ps1`
- Mac/Linux: Ensure you're in project directory

### Django server won't start?
- Check if port 8000 is already in use
- Use `python manage.py runserver 8001` to use different port

### Database connection fails?
- Verify PostgreSQL is running
- Check .env file has correct credentials
- Test connection: `psql -U dbuser -d letskillcancer`

### Migrations fail?
- Check database exists
- Verify user has permissions
- Check settings.py database configuration

---

## 📚 Reference Documents

- **Full Implementation Guide**: `IMPLEMENTATION_GUIDE.md`
- **Technical Stack**: `TECHNICAL_STACK_DOCUMENTATION.md`
- **Setup Guide**: `SETUP_GUIDE.md`

---

**Remember:** Complete each step fully before moving to the next!

