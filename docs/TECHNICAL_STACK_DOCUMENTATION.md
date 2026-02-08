# "Let's Kill Cancer" - Technical Stack Documentation

## Project Overview

"Let's Kill Cancer" is a simple, beginner-friendly web-based cancer awareness and early risk assessment platform. The platform is designed to be ethical, non-diagnostic, and hackathon-ready.

### Project Goals
- **Educate** people about cancer through awareness content
- **Help users understand** possible early risk signs through AI-assisted screening
- **Connect patients** with doctors for professional advice
- **Allow admins** to manage the system securely

### Important: Non-Diagnostic Platform
⚠️ **This platform does NOT diagnose cancer.** It is an awareness and guidance tool only.

### Target Users & Roles

1. **Patient**
   - Registers and logs in
   - Reads cancer awareness content
   - Completes AI-assisted risk screening form
   - Views risk results (Low / Medium / High)
   - Receives advice from doctors

2. **Doctor**
   - Registers but cannot act until approved by admin
   - Views patient risk results
   - Provides professional advice
   - Works only after admin verification

3. **Admin**
   - Has full system control
   - Adds and manages users
   - Approves or rejects doctors
   - Manages awareness content and donations

### System Design Approach
- **Single User System**: One user model with role-based access control
- **Role-Based Access**: Control access using roles (Patient, Doctor, Admin)
- **Profile Extension**: Extend users using profile models
- **Doctor Approval**: Doctors must be approved by admin before accessing doctor features
- **Simple & Secure**: Keep the system simple, secure, and beginner-friendly

---

## Step 1: Backend (Python)

### Python Version
- **Recommended Version**: Python 3.10 or 3.11
- **Minimum Version**: Python 3.9
- **Why**: Django 4.x+ requires Python 3.9+, and Python 3.10+ provides better performance and type hinting support

### Virtual Environment Setup
- **Tool**: `venv` (built-in) or `virtualenv`
- **Purpose**: Isolates project dependencies from system Python packages
- **Setup Process**:
  1. Create virtual environment: `python -m venv venv`
  2. Activate (Windows): `venv\Scripts\activate`
  3. Activate (Linux/Mac): `source venv/bin/activate`
- **Why Important**: Prevents dependency conflicts and ensures reproducible deployments

### Required Python Packages

#### Core Django Packages
1. **Django** (v4.2+)
   - **Purpose**: Main web framework providing MVC architecture, ORM, admin panel, and URL routing
   - **Usage**: Foundation for the entire backend application

2. **djangorestframework** (v3.14+)
   - **Purpose**: Adds REST API capabilities to Django
   - **Usage**: Enables API endpoints for frontend-backend communication, mobile app support, and third-party integrations

3. **django-cors-headers** (v4.0+)
   - **Purpose**: Handles Cross-Origin Resource Sharing (CORS) headers
   - **Usage**: Allows frontend to make API requests from different origins (essential for development and production)

#### Database Packages
4. **psycopg2-binary** (v2.9+)
   - **Purpose**: PostgreSQL database adapter for Python
   - **Usage**: Enables Django ORM to communicate with PostgreSQL database
   - **Note**: Binary version is easier to install (no compilation required)

5. **django-environ** (v0.11+)
   - **Purpose**: Manages environment variables and settings
   - **Usage**: Securely loads database credentials, API keys, and configuration from `.env` files

#### Security Packages
6. **django-allauth** (v0.54+)
   - **Purpose**: Comprehensive authentication solution
   - **Usage**: Handles user registration, login, password reset, email verification, and social authentication

7. **django-crispy-forms** (v2.0+)
   - **Purpose**: Better form rendering and styling
   - **Usage**: Creates clean, accessible forms for user registration and data entry

8. **django-guardian** (v2.4+)
   - **Purpose**: Object-level permissions for Django
   - **Usage**: Implements fine-grained access control (e.g., patients can only see their own records, doctors see assigned patients)

9. **cryptography** (v41+)
   - **Purpose**: Cryptographic recipes and primitives
   - **Usage**: Encrypts sensitive healthcare data, secure password hashing, and data protection

#### Utility Packages
10. **python-decouple** (v3.8+)
    - **Purpose**: Separates settings from code
    - **Usage**: Alternative to django-environ for managing environment variables

11. **Pillow** (v10+)
    - **Purpose**: Python Imaging Library
    - **Usage**: Handles image uploads (user avatars, medical documents, profile pictures)

12. **django-filter** (v23+)
    - **Purpose**: Advanced filtering for Django REST Framework
    - **Usage**: Enables complex search and filter operations on patient records and dashboards

13. **django-extensions** (v3.2+)
    - **Purpose**: Collection of custom extensions for Django
    - **Usage**: Provides useful management commands and development tools

#### Testing Packages
16. **pytest** (v7.4+)
    - **Purpose**: Testing framework
    - **Usage**: Unit and integration testing for backend logic

17. **pytest-django** (v4.7+)
    - **Purpose**: Pytest plugin for Django
    - **Usage**: Enables pytest to work seamlessly with Django test cases

18. **coverage** (v7.3+)
    - **Purpose**: Code coverage measurement
    - **Usage**: Tracks how much of the codebase is covered by tests

---

## Step 2: AI / Machine Learning (Python)

### AI Risk Assessment Rules (Important)

⚠️ **Ethical Guidelines**:
- Uses **non-medical data only** (age, lifestyle factors, family history, general symptoms)
- Outputs **risk level only** (Low / Medium / High)
- **No diagnosis** or medical claims
- Used strictly for **awareness and guidance** purposes
- Always includes disclaimers that this is not a medical diagnosis

### Required AI/ML Libraries

1. **scikit-learn** (v1.3+)
   - **Purpose**: Core machine learning library for risk classification
   - **Usage**: 
     - Simple classification model (Random Forest or Logistic Regression recommended)
     - Risk level prediction (Low/Medium/High)
     - Feature preprocessing and scaling
     - Model evaluation metrics

2. **pandas** (v2.1+)
   - **Purpose**: Data manipulation and analysis
   - **Usage**: 
     - Loading questionnaire responses
     - Converting form data to feature vectors
     - Simple data cleaning and transformation

3. **numpy** (v1.24+)
   - **Purpose**: Numerical computing library
   - **Usage**: 
     - Mathematical operations for ML algorithms
     - Array operations for feature vectors
     - Required dependency for scikit-learn

4. **joblib** (v1.3+)
   - **Purpose**: Model persistence (saving and loading)
   - **Usage**: 
     - Saving trained ML model to disk (`model.pkl`)
     - Loading pre-trained model for predictions
     - Simple and efficient for small to medium models

### AI Model Integration with Django Backend

**Simple Architecture Flow**:
1. **Data Collection**: Patient fills out risk assessment questionnaire via Django form
2. **Data Processing**: Django view collects form data and converts to feature array using pandas/numpy
3. **Model Prediction**: Pre-trained scikit-learn model (loaded via joblib) processes features
4. **Result**: Model outputs risk level (Low/Medium/High) with confidence score
5. **Storage**: Risk assessment result stored in database via Django ORM
6. **Display**: Results shown to user with clear disclaimers (non-diagnostic notice)

**Integration Points**:
- **Django Views**: Handle form submission and coordinate AI processing
- **Django Models**: Store questionnaire responses and risk assessment results
- **Custom Service Class**: Simple Python class to handle model loading and prediction
- **Template Display**: Show results with appropriate warnings and disclaimers

**Model Storage**:
- Trained model stored as `models/risk_assessment_model.pkl` in project directory
- Model can be trained separately and loaded at runtime
- Simple approach: Load model once at Django startup or on-demand per request

**Questionnaire Data (Non-Medical)**:
- Age range
- Family history (yes/no questions)
- Lifestyle factors (smoking, exercise, diet)
- General symptoms (non-specific, awareness-focused)
- No medical test results or diagnostic data

---

## Step 3: Frontend (HTML + Django Templates)

### Django Template System Overview

Django uses a template engine that combines HTML with Django Template Language (DTL) to create dynamic web pages. Templates allow:
- **Template Inheritance**: Base templates with blocks for reusable layouts
- **Variable Rendering**: Display data from Django views using `{{ variable }}`
- **Template Tags**: Control flow (`{% if %}`, `{% for %}`) and template logic
- **Template Filters**: Transform data (`{{ value|filter }}`)

### Key Template Components Required

#### Base Templates
1. **base.html**
   - **Purpose**: Master template with common structure
   - **Contains**: HTML head, navigation bar, footer, Tailwind CSS links
   - **Blocks**: `{% block content %}`, `{% block scripts %}`, `{% block styles %}`

2. **base_dashboard.html**
   - **Purpose**: Base template for all dashboard pages
   - **Contains**: Sidebar navigation, user profile section, dashboard-specific layout
   - **Extends**: `base.html`

#### Authentication Templates
3. **registration/login.html**
   - **Purpose**: User login form
   - **Components**: Email/username field, password field, "Remember me" checkbox, forgot password link

4. **registration/signup.html**
   - **Purpose**: User registration form
   - **Components**: Email, password, confirm password, terms acceptance checkbox, role selection (patient/doctor)
   - **Note**: Doctors register but cannot access doctor features until admin approval

5. **registration/password_reset.html**
   - **Purpose**: Password reset request form
   - **Components**: Email input field, submit button

#### Dashboard Templates
6. **dashboard/patient_dashboard.html**
   - **Purpose**: Patient's main dashboard
   - **Components**: 
     - Risk assessment card/button
     - Previous assessment results summary
     - Upcoming appointments section
     - Health tips/articles section
     - Profile quick view

7. **dashboard/doctor_dashboard.html**
   - **Purpose**: Doctor's main dashboard
   - **Components**:
     - Patient list/queue
     - Assessment review section
     - Patient search/filter
     - Statistics cards (total patients, assessments today)
     - Quick actions panel

8. **dashboard/admin_dashboard.html**
   - **Purpose**: Admin's main dashboard
   - **Components**:
     - System statistics (users, assessments, donations)
     - User management interface
     - Content management section
     - System health monitoring

#### Assessment Templates
9. **assessment/questionnaire.html**
   - **Purpose**: Risk assessment questionnaire form
   - **Components**: 
     - Multi-step form (age, family history, lifestyle factors, symptoms)
     - Progress indicator
     - Previous/Next buttons
     - Save draft functionality

10. **assessment/results.html**
    - **Purpose**: Display risk assessment results
    - **Components**:
      - Risk level indicator (visual)
      - Risk factors summary
      - Recommendations section
      - Disclaimer (non-diagnostic notice)
      - "Consult a doctor" CTA button

#### Donation Templates
11. **donations/donate.html**
    - **Purpose**: Donation form
    - **Components**: Amount input, payment method selection, donor information form

12. **donations/success.html**
    - **Purpose**: Donation confirmation page
    - **Components**: Thank you message, transaction details, receipt download

#### Profile Templates
13. **profile/view.html**
    - **Purpose**: User profile view
    - **Components**: Personal information display, assessment history, account settings link

14. **profile/edit.html**
    - **Purpose**: Profile editing form
    - **Components**: Editable fields (name, email, phone, address), avatar upload, save button

#### Shared Components (Included Templates)
15. **components/navbar.html**
    - **Purpose**: Reusable navigation bar
    - **Components**: Logo, menu items, user dropdown, notification icon

16. **components/footer.html**
    - **Purpose**: Site footer
    - **Components**: Links, copyright, social media icons

17. **components/messages.html**
    - **Purpose**: Display Django messages (success, error, info)
    - **Components**: Alert boxes with Tailwind styling

---

## Step 4: Styling (Tailwind CSS)

### Tailwind CSS Setup Options

#### Option 1: CDN (Quick Start - Development)
- **Method**: Include Tailwind via CDN link in HTML `<head>`
- **Pros**: Fast setup, no build process, good for prototyping
- **Cons**: Larger file size, limited customization, not recommended for production
- **Use Case**: Initial development and hackathon quick setup

#### Option 2: Local Build (Recommended - Production)
- **Method**: Install via npm and configure with `tailwind.config.js`
- **Process**:
  1. Install: `npm install -D tailwindcss`
  2. Initialize: `npx tailwindcss init`
  3. Configure: Set content paths in `tailwind.config.js`
  4. Build: Compile CSS with `npx tailwindcss -i ./input.css -o ./output.css`
- **Pros**: Smaller file size, full customization, production-ready
- **Cons**: Requires Node.js/npm, build step needed
- **Use Case**: Production deployment and optimized performance

#### Option 3: Django-Tailwind (Django Integration)
- **Method**: Use `django-tailwind` package
- **Pros**: Seamless Django integration, automatic build process
- **Cons**: Additional dependency, requires npm anyway
- **Use Case**: Django-specific projects wanting Tailwind integration

### Required UI Components

#### Layout Components
1. **Navigation Bar**
   - Responsive hamburger menu for mobile
   - Logo and branding
   - User authentication buttons (login/signup) or user dropdown
   - Role-based menu items

2. **Sidebar** (Dashboard)
   - Collapsible sidebar for dashboard navigation
   - Menu items based on user role
   - Active state indicators
   - User profile section at bottom

3. **Footer**
   - Multi-column layout
   - Links (About, Contact, Privacy Policy, Terms)
   - Social media icons
   - Copyright information

#### Form Components
4. **Input Fields**
   - Text inputs with labels
   - Error states and validation messages
   - Focus states and transitions
   - Required field indicators

5. **Buttons**
   - Primary buttons (CTAs)
   - Secondary buttons
   - Danger buttons (delete actions)
   - Loading states (spinner)
   - Disabled states

6. **Cards**
   - Assessment result cards
   - Dashboard stat cards
   - Patient info cards
   - Article/blog cards

#### Feedback Components
7. **Alerts/Notifications**
   - Success messages (green)
   - Error messages (red)
   - Warning messages (yellow)
   - Info messages (blue)
   - Dismissible alerts

8. **Modals**
   - Confirmation dialogs
   - Form modals
   - Information modals
   - Backdrop overlay

9. **Loading Spinners**
   - Page loading indicators
   - Button loading states
   - Data fetching indicators

#### Data Display Components
10. **Tables**
    - Patient lists
    - Assessment history
    - Transaction history
    - Sortable columns
    - Pagination

11. **Progress Bars**
    - Questionnaire progress indicator
    - Risk level visualization
    - Donation goal progress

12. **Badges/Tags**
    - Risk level badges (Low, Medium, High)
    - Status indicators (Active, Pending, Completed)
    - Role badges (Patient, Doctor, Admin)

#### Interactive Components
13. **Dropdowns**
    - User menu dropdown
    - Filter dropdowns
    - Action menus

14. **Tabs**
    - Dashboard tab navigation
    - Profile section tabs
    - Assessment step indicators

15. **Tooltips**
    - Help text on form fields
    - Information icons
    - Feature explanations

---

## Step 5: Interactivity (JavaScript)

### Where JavaScript is Required

#### Form Handling
1. **Form Validation**
   - **Location**: All form templates (registration, login, questionnaire, donation)
   - **Purpose**: Client-side validation before submission
   - **Functionality**: 
     - Real-time field validation
     - Password strength checking
     - Email format validation
     - Required field checking
     - Custom validation messages

2. **Multi-Step Forms**
   - **Location**: `assessment/questionnaire.html`
   - **Purpose**: Break long questionnaire into manageable steps
   - **Functionality**:
     - Show/hide form sections
     - Progress tracking
     - Data persistence between steps
     - Previous/Next navigation
     - Step validation before proceeding

#### UI Feedback and Interactions
3. **Dynamic Content Loading**
   - **Location**: Dashboard pages
   - **Purpose**: Load data without full page refresh
   - **Functionality**:
     - Fetch assessment results via AJAX
     - Update dashboard stats dynamically
     - Load patient lists asynchronously

4. **Real-Time Updates**
   - **Location**: Doctor dashboard
   - **Purpose**: Show new patient assessments as they arrive
   - **Functionality**:
     - WebSocket or polling for new data
     - Notification badges
     - Auto-refresh patient queue

5. **Interactive Charts/Visualizations**
   - **Location**: Dashboard statistics
   - **Purpose**: Display risk trends, statistics
   - **Functionality**:
     - Chart.js or similar library integration
     - Risk level visualization
     - Progress bars animation

#### User Experience Enhancements
6. **Modal Management**
   - **Location**: Throughout application
   - **Purpose**: Display confirmations, forms, information
   - **Functionality**:
     - Open/close modals
     - Form submission within modals
     - Backdrop click handling
     - Escape key to close

7. **Toast Notifications**
   - **Location**: All pages
   - **Purpose**: Show success/error messages
   - **Functionality**:
     - Display Django messages as toast notifications
     - Auto-dismiss after timeout
     - Manual dismiss button
     - Stack multiple notifications

8. **Search and Filter**
   - **Location**: Doctor dashboard, admin dashboard
   - **Purpose**: Filter patient lists, assessments
   - **Functionality**:
     - Real-time search filtering
     - Multi-criteria filtering
     - URL parameter updates
     - Filter state persistence

9. **Infinite Scroll / Pagination**
   - **Location**: Patient lists, assessment history
   - **Purpose**: Load more data as user scrolls
   - **Functionality**:
     - Load next page on scroll
     - Pagination controls
     - Loading indicators

#### Data Manipulation
10. **CSV Export**
    - **Location**: Admin dashboard, doctor dashboard
    - **Purpose**: Export patient data, assessment reports
    - **Functionality**:
      - Generate CSV from table data
      - Download file trigger
      - Format data appropriately

11. **Print Functionality**
    - **Location**: Assessment results page
    - **Purpose**: Print assessment reports
    - **Functionality**:
      - Print-friendly CSS
      - Print button handler
      - Hide unnecessary elements when printing

#### Security and Performance
12. **CSRF Token Handling**
    - **Location**: All forms with POST requests
    - **Purpose**: Include CSRF token in AJAX requests
    - **Functionality**:
      - Extract CSRF token from cookies
      - Include in request headers
      - Handle CSRF errors gracefully

13. **Debouncing**
    - **Location**: Search inputs, form fields
    - **Purpose**: Reduce API calls and improve performance
    - **Functionality**:
      - Delay function execution
      - Cancel previous calls
      - Optimize search queries

### Typical JavaScript Functionalities Needed

1. **Event Listeners**: Click, submit, change, scroll, keypress handlers
2. **DOM Manipulation**: Show/hide elements, update content, add/remove classes
3. **AJAX/Fetch API**: Make HTTP requests to Django REST endpoints
4. **Local Storage**: Save form drafts, user preferences
5. **Form Serialization**: Convert form data to JSON for API submission
6. **Error Handling**: Try-catch blocks, error message display
7. **Loading States**: Show/hide spinners, disable buttons during requests
8. **URL Manipulation**: Update query parameters, handle browser history
9. **Date Formatting**: Display dates in user-friendly format
10. **Input Masking**: Format phone numbers, dates, amounts

---

## Step 6: Database (PostgreSQL + SQL)

### PostgreSQL Requirements

#### Version
- **Recommended**: PostgreSQL 14 or 15
- **Minimum**: PostgreSQL 12
- **Why**: Better performance, JSON support, improved indexing

#### Configuration Requirements
- **Encoding**: UTF-8 (essential for international characters)
- **Timezone**: UTC (store all timestamps in UTC, convert in application)
- **Connection Pooling**: Configured for Django (handled by psycopg2)
- **Backup Strategy**: Regular backups (daily recommended for healthcare data)

#### Database Setup
- Create dedicated database: `CREATE DATABASE letskillcancer;`
- Create database user with appropriate permissions
- Grant privileges: `GRANT ALL PRIVILEGES ON DATABASE letskillcancer TO dbuser;`

### Django ORM Interaction with SQL

**How Django ORM Works**:
- Django ORM (Object-Relational Mapping) translates Python code to SQL queries
- Developers write Python code, Django generates SQL automatically
- ORM provides abstraction layer, making database operations database-agnostic

**Example Flow**:
```python
# Python/Django ORM Code
Patient.objects.filter(age__gte=18).order_by('created_at')

# Django generates SQL:
# SELECT * FROM patients WHERE age >= 18 ORDER BY created_at;
```

**Key ORM Concepts**:
- **Models**: Python classes representing database tables
- **Querysets**: Lazy-evaluated collections of database objects
- **Migrations**: Version control for database schema changes
- **Relationships**: Foreign keys, many-to-many, one-to-one relationships

**When to Use Raw SQL**:
- Complex queries that ORM struggles with
- Performance-critical operations
- Database-specific features (PostgreSQL JSON queries, full-text search)

### Core Database Entities (Tables)

#### Authentication & User Management
1. **users** (extends Django's User model)
   - Fields: id, email, password_hash, first_name, last_name, role (patient/doctor/admin), is_active, created_at, updated_at
   - Purpose: Store all user accounts

2. **user_profiles**
   - Fields: id, user_id (FK), phone, date_of_birth, gender, address, avatar_url, created_at
   - Purpose: Extended user information

#### Assessment & Risk Screening
3. **questionnaires**
   - Fields: id, user_id (FK), submitted_at, status (draft/completed), version
   - Purpose: Track questionnaire submissions

4. **questionnaire_responses**
   - Fields: id, questionnaire_id (FK), question_id, answer_value, answer_text, created_at
   - Purpose: Store individual question responses

5. **risk_assessments**
   - Fields: id, questionnaire_id (FK), user_id (FK), risk_level (low/medium/high), risk_score, model_version, factors_summary (JSON), recommendations (JSON), created_at
   - Purpose: Store AI-generated risk assessment results

6. **assessment_history**
   - Fields: id, user_id (FK), assessment_id (FK), viewed_at, notes
   - Purpose: Track when users view their assessment results

#### Doctor-Patient Relationships
7. **doctor_patient_assignments**
   - Fields: id, doctor_id (FK), patient_id (FK), assigned_at, status (active/inactive), notes
   - Purpose: Link doctors to their assigned patients

8. **consultations**
   - Fields: id, doctor_id (FK), patient_id (FK), assessment_id (FK), consultation_date, notes, status (scheduled/completed/cancelled), created_at
   - Purpose: Track doctor consultations with patients

#### Donations
9. **donations**
   - Fields: id, donor_id (FK, nullable), amount, currency, payment_method, transaction_id, status (pending/completed/failed), donor_name, donor_email, created_at
   - Purpose: Store donation transactions

10. **donation_receipts**
    - Fields: id, donation_id (FK), receipt_number, issued_at, pdf_path
    - Purpose: Generate and store donation receipts

#### Content Management
11. **articles**
    - Fields: id, title, content, author_id (FK), category, published_at, status (draft/published), views_count, created_at
    - Purpose: Store health awareness articles and blog posts

12. **health_tips**
    - Fields: id, title, content, category, priority, display_order, is_active, created_at
    - Purpose: Store health tips displayed on dashboards

#### System & Administration
13. **audit_logs**
    - Fields: id, user_id (FK), action_type, resource_type, resource_id, details (JSON), ip_address, created_at
    - Purpose: Track user actions for security and compliance

14. **system_settings**
    - Fields: id, key, value, data_type, description, updated_at
    - Purpose: Store system configuration (donation goals, feature flags, etc.)

15. **notifications**
    - Fields: id, user_id (FK), title, message, type, is_read, created_at
    - Purpose: Store user notifications

#### AI Model Management
16. **ml_models**
    - Fields: id, model_name, version, file_path, accuracy_score, training_date, is_active, parameters (JSON), created_at
    - Purpose: Track ML model versions and metadata

17. **model_predictions**
    - Fields: id, model_id (FK), assessment_id (FK), prediction_result, confidence_score, features_used (JSON), created_at
    - Purpose: Log all AI predictions for model improvement and auditing

### Database Relationships Summary
- **One-to-Many**: User → Questionnaires, User → Donations, Doctor → Consultations
- **Many-to-Many**: Doctors ↔ Patients (through doctor_patient_assignments)
- **One-to-One**: User → UserProfile
- **Foreign Keys**: Most tables reference users, questionnaires, or assessments

---

## Step 7: Environment Configuration

### Required Environment Variables

#### Database Configuration
1. **DATABASE_NAME**
   - **Value**: `letskillcancer` (or production database name)
   - **Purpose**: PostgreSQL database name
   - **Security**: Not sensitive, but should be environment-specific

2. **DATABASE_USER**
   - **Value**: Database username
   - **Purpose**: PostgreSQL connection username
   - **Security**: Sensitive - should never be committed to version control

3. **DATABASE_PASSWORD**
   - **Value**: Database password
   - **Purpose**: PostgreSQL connection password
   - **Security**: Highly sensitive - must be kept secret

4. **DATABASE_HOST**
   - **Value**: `localhost` (development) or production DB host
   - **Purpose**: PostgreSQL server hostname/IP
   - **Security**: Not sensitive, but environment-specific

5. **DATABASE_PORT**
   - **Value**: `5432` (default PostgreSQL port)
   - **Purpose**: PostgreSQL server port
   - **Security**: Not sensitive

#### Django Configuration
6. **SECRET_KEY**
   - **Value**: Long random string (generated by Django)
   - **Purpose**: Used for cryptographic signing, CSRF protection, session security
   - **Security**: Extremely sensitive - must be unique per environment and never exposed

7. **DEBUG**
   - **Value**: `True` (development) or `False` (production)
   - **Purpose**: Enables/disables Django debug mode
   - **Security**: Must be False in production to prevent information leakage

8. **ALLOWED_HOSTS**
   - **Value**: Comma-separated list of domain names (e.g., `localhost,127.0.0.1,letskillcancer.com`)
   - **Purpose**: Security feature - restricts which hosts can serve the Django app
   - **Security**: Important for preventing host header attacks

#### Email Configuration
9. **EMAIL_HOST**
   - **Value**: SMTP server hostname (e.g., `smtp.gmail.com`)
   - **Purpose**: Email server for sending notifications, password resets
   - **Security**: Not sensitive

10. **EMAIL_PORT**
    - **Value**: SMTP port (e.g., `587` for TLS)
    - **Purpose**: SMTP server port
    - **Security**: Not sensitive

11. **EMAIL_HOST_USER**
    - **Value**: Email account username
    - **Purpose**: SMTP authentication username
    - **Security**: Sensitive - should be kept private

12. **EMAIL_HOST_PASSWORD**
    - **Value**: Email account password or app password
    - **Purpose**: SMTP authentication password
    - **Security**: Highly sensitive

13. **EMAIL_USE_TLS**
    - **Value**: `True` or `False`
    - **Purpose**: Enable TLS encryption for email
    - **Security**: Should be True for security

#### Third-Party Services
14. **PAYMENT_GATEWAY_API_KEY**
    - **Value**: Payment provider API key (Stripe, PayPal, etc.)
    - **Purpose**: Process donation payments
    - **Security**: Extremely sensitive - must be kept secret

15. **PAYMENT_GATEWAY_SECRET_KEY**
    - **Value**: Payment provider secret key
    - **Purpose**: Secure payment processing
    - **Security**: Extremely sensitive

#### AI/ML Configuration
16. **ML_MODEL_PATH**
    - **Value**: Path to trained model files (e.g., `/app/models/risk_model_v1.pkl`)
    - **Purpose**: Location of pre-trained ML models
    - **Security**: Not sensitive, but environment-specific

17. **ML_MODEL_VERSION**
    - **Value**: Model version identifier (e.g., `v1.2`)
    - **Purpose**: Track which model version is in use
    - **Security**: Not sensitive

#### Redis/Celery Configuration
18. **REDIS_URL**
    - **Value**: Redis connection URL (e.g., `redis://localhost:6379/0`)
    - **Purpose**: Celery message broker and caching
    - **Security**: May contain password - should be protected

19. **CELERY_BROKER_URL**
    - **Value**: Same as REDIS_URL typically
    - **Purpose**: Celery task queue broker
    - **Security**: May contain credentials

#### Security & Compliance
20. **SESSION_COOKIE_SECURE**
    - **Value**: `True` (production) or `False` (development)
    - **Purpose**: Only send session cookies over HTTPS
    - **Security**: Important for production security

21. **CSRF_COOKIE_SECURE**
    - **Value**: `True` (production) or `False` (development)
    - **Purpose**: Only send CSRF cookies over HTTPS
    - **Security**: Important for production security

22. **CORS_ALLOWED_ORIGINS**
    - **Value**: Comma-separated list of allowed frontend origins
    - **Purpose**: Control which domains can make API requests
    - **Security**: Important for preventing unauthorized API access

### Why Environment Variables are Important

#### Security Benefits
1. **Secret Protection**: Prevents sensitive data (passwords, API keys) from being committed to version control
2. **Access Control**: Limits who can see sensitive configuration (only those with server access)
3. **Compliance**: Essential for healthcare data compliance (HIPAA considerations)
4. **Key Rotation**: Easy to update secrets without code changes

#### Operational Benefits
5. **Environment Separation**: Different values for development, staging, and production
6. **Configuration Management**: Centralized configuration management
7. **Deployment Flexibility**: Same codebase works across different environments
8. **Team Collaboration**: Developers can have different local configurations

#### Best Practices
- **Never commit `.env` files** to version control
- **Use `.env.example`** file with dummy values as template
- **Validate required variables** at application startup
- **Use different values** for each environment (dev, staging, prod)
- **Rotate secrets regularly** especially for production
- **Use secret management tools** (AWS Secrets Manager, HashiCorp Vault) in production
- **Document all variables** in project documentation

### Environment File Structure

**`.env.example`** (committed to repo):
```
# Database
DATABASE_NAME=letskillcancer
DATABASE_USER=dbuser
DATABASE_PASSWORD=your_password_here
DATABASE_HOST=localhost
DATABASE_PORT=5432

# Django
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Email
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
EMAIL_USE_TLS=True

# Add other variables...
```

**`.env`** (NOT committed, created locally):
- Contains actual values for local development
- Each developer creates their own copy

---

## Summary

This technical stack documentation provides a comprehensive overview of all technologies, packages, and configurations required for the "Let's Kill Cancer" platform. The stack is designed to be:

- **Secure**: Multiple security layers (authentication, encryption, CORS, CSRF protection)
- **Scalable**: Django + PostgreSQL + Celery architecture supports growth
- **Maintainable**: Clear separation of concerns, well-documented components
- **Compliant**: Healthcare data considerations built into architecture
- **Hackathon-Ready**: Can be set up quickly with provided configurations

Before development begins, ensure:
1. ✅ Python 3.10+ installed
2. ✅ PostgreSQL 14+ installed and running
3. ✅ Virtual environment created
4. ✅ All Python packages installed from requirements.txt
5. ✅ Environment variables configured
6. ✅ Database created and migrations run
7. ✅ Tailwind CSS configured (CDN or build process)
8. ✅ Node.js/npm installed (if using Tailwind build process)

---

**Document Version**: 1.0  
**Last Updated**: 2026  
**Status**: Pre-Development Technical Specification

