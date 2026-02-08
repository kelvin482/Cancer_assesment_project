# ✅ STEP 2 - Database Configuration (IN PROGRESS)

## Status: ⏳ PostgreSQL Installation Required

### What Has Been Completed ✅

1. **✅ Settings.py Updated**
   - Configured to use PostgreSQL instead of SQLite
   - Added `django-environ` integration
   - Environment variables loaded from `.env` file
   - Database configuration reads from environment variables

2. **✅ .gitignore Created**
   - Ensures `.env` file is not committed to version control
   - Protects sensitive credentials

3. **✅ .env.example Created**
   - Template file with all required environment variables
   - Can be committed to repository safely

4. **✅ SECRET_KEY Generated**
   - Generated secure Django secret key: `6-)mr1fln_e9ap9qo6joew7b^n1v@%_3&xi%&hvf5vka20l1##`

### What Needs to Be Done ⏳

#### 1. Install PostgreSQL
- **Download:** https://www.postgresql.org/download/windows/
- **Install** PostgreSQL 13+ (latest version recommended)
- **Remember** the `postgres` superuser password during installation
- **Verify:** Run `psql --version` in terminal

#### 2. Create Database and User

**Using psql (Command Line):**
```bash
# Connect to PostgreSQL
psql -U postgres

# Run these SQL commands:
CREATE DATABASE letskillcancer;

CREATE USER lkc_user WITH PASSWORD 'your_secure_password';

ALTER ROLE lkc_user SET client_encoding TO 'utf8';
ALTER ROLE lkc_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE lkc_user SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE letskillcancer TO lkc_user;

\q
```

**⚠️ Replace `your_secure_password` with a strong password of your choice**

#### 3. Create .env File Manually

**IMPORTANT:** The `.env` file cannot be created automatically (security feature). You must create it manually.

**Steps:**
1. Copy `.env.example` to `.env`:
   ```powershell
   Copy-Item .env.example .env
   ```

2. Edit `.env` file and update the password:
   ```
   DEBUG=True
   SECRET_KEY=6-)mr1fln_e9ap9qo6joew7b^n1v@%_3&xi%&hvf5vka20l1##
   ALLOWED_HOSTS=localhost,127.0.0.1

   DATABASE_NAME=letskillcancer
   DATABASE_USER=lkc_user
   DATABASE_PASSWORD=your_secure_password  # ⚠️ CHANGE THIS to match your database password
   DATABASE_HOST=localhost
   DATABASE_PORT=5432
   ```

#### 4. Verify Database Connection

After creating database and .env file:

```bash
# Test connection
python manage.py dbshell
```

If successful, you'll see PostgreSQL prompt. Type `\q` to exit.

#### 5. Run Initial Migrations

```bash
python manage.py migrate
```

This creates all Django default tables in PostgreSQL.

### Current Configuration

**settings.py Changes:**
- ✅ Imports `os` and `environ`
- ✅ Loads environment variables from `.env`
- ✅ Uses PostgreSQL database backend
- ✅ Reads database credentials from environment variables
- ✅ Has fallback defaults for development

**Database Configuration:**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DATABASE_NAME', default='letskillcancer'),
        'USER': env('DATABASE_USER', default='lkc_user'),
        'PASSWORD': env('DATABASE_PASSWORD', default=''),
        'HOST': env('DATABASE_HOST', default='localhost'),
        'PORT': env('DATABASE_PORT', default='5432'),
    }
}
```

### Next Steps After PostgreSQL Setup

Once PostgreSQL is installed and database is created:

1. ✅ Create `.env` file with database credentials
2. ✅ Test database connection: `python manage.py dbshell`
3. ✅ Run migrations: `python manage.py migrate`
4. ✅ Verify: Check that migrations ran successfully

Then proceed to **Step 3: Authentication & User Roles**

---

**See `POSTGRESQL_SETUP.md` for detailed PostgreSQL installation instructions.**



