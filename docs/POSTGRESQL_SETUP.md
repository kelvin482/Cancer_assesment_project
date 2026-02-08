# PostgreSQL Setup Guide - Step 2

## Status: ⏳ PostgreSQL Installation Required

### Step 1: Install PostgreSQL

**Windows:**
1. Download PostgreSQL from: https://www.postgresql.org/download/windows/
2. Run the installer
3. During installation:
   - Remember the password you set for the `postgres` superuser
   - Default port: 5432 (keep this)
   - Install pgAdmin (optional but recommended for GUI management)
4. Complete the installation

**Verify Installation:**
```bash
psql --version
```

**Start PostgreSQL Service:**
- Windows: Open Services app → Find "postgresql" → Start service
- Or: PostgreSQL will start automatically after installation

### Step 2: Create Database and User

**Option A: Using psql Command Line**

1. Open Command Prompt or PowerShell
2. Connect to PostgreSQL:
```bash
psql -U postgres
```
(Enter the password you set during installation)

3. Run these SQL commands:
```sql
CREATE DATABASE letskillcancer;

CREATE USER lkc_user WITH PASSWORD 'your_secure_password';

ALTER ROLE lkc_user SET client_encoding TO 'utf8';
ALTER ROLE lkc_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE lkc_user SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE letskillcancer TO lkc_user;

\q
```

**Option B: Using pgAdmin (GUI)**

1. Open pgAdmin
2. Connect to PostgreSQL server (use postgres user password)
3. Right-click "Databases" → Create → Database
   - Name: `letskillcancer`
   - Click Save
4. Right-click "Login/Group Roles" → Create → Login/Group Role
   - General tab: Name: `lkc_user`
   - Definition tab: Password: `your_secure_password`
   - Privileges tab: Check "Can login?"
   - Click Save
5. Right-click `letskillcancer` database → Properties → Security
   - Add `lkc_user` with ALL privileges

### Step 3: Create .env File

**IMPORTANT:** Create `.env` file manually in project root (copy from `.env.example`)

1. Copy `.env.example` to `.env`:
```bash
# Windows PowerShell
Copy-Item .env.example .env
```

2. Edit `.env` file and update these values:
```
DEBUG=True
SECRET_KEY=6-)mr1fln_e9ap9qo6joew7b^n1v@%_3&xi%&hvf5vka20l1##
ALLOWED_HOSTS=localhost,127.0.0.1

DATABASE_NAME=letskillcancer
DATABASE_USER=lkc_user
DATABASE_PASSWORD=your_secure_password  # CHANGE THIS to your actual password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

**⚠️ Replace `your_secure_password` with the actual password you set for `lkc_user`**

### Step 4: Verify Database Connection

After creating the database and .env file:

```bash
# Test database connection
python manage.py dbshell
```

If successful, you'll see the PostgreSQL prompt. Type `\q` to exit.

### Step 5: Run Initial Migrations

```bash
python manage.py migrate
```

This will create all Django default tables in PostgreSQL.

**Expected Output:**
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  ...
```

### Troubleshooting

**Error: "psql: command not found"**
- PostgreSQL not installed or not in PATH
- Add PostgreSQL bin directory to system PATH
- Or use full path: `C:\Program Files\PostgreSQL\15\bin\psql.exe`

**Error: "password authentication failed"**
- Check password in .env file matches database user password
- Verify user exists: `psql -U postgres -c "\du"`

**Error: "database does not exist"**
- Create database: `CREATE DATABASE letskillcancer;`
- Verify: `psql -U postgres -l`

**Error: "connection refused"**
- PostgreSQL service not running
- Start PostgreSQL service in Windows Services

**Error: "permission denied"**
- User doesn't have privileges
- Grant privileges: `GRANT ALL PRIVILEGES ON DATABASE letskillcancer TO lkc_user;`

---

**Next Steps:** After database is configured, proceed to Step 3: Authentication & User Roles



