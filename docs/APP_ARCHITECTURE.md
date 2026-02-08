# App Architecture - "Let's Kill Cancer"

## Simple 3-App Structure

**Goal:** Keep code organized, simple, and conflict-free with clear separation of concerns.

---

## 📱 App Structure Overview

### 1. **accounts** - User Management (Patients & Authentication)
**Purpose:** Handle all user authentication and patient-related features

**Responsibilities:**
- User registration and login
- Patient profiles
- Password management
- User authentication

**Models:**
- PatientProfile (extends User)

**Views:**
- Login, Register, Logout
- Patient dashboard
- Patient profile management

---

### 2. **doctors** - Doctor Management
**Purpose:** Handle all doctor-related features

**Responsibilities:**
- Doctor profiles
- Doctor verification
- Doctor dashboard
- Viewing patient assessments
- Providing advice

**Models:**
- DoctorProfile (extends User)
- Consultation
- DoctorPatientAssignment

**Views:**
- Doctor dashboard
- Patient assessment review
- Advice submission
- Doctor profile management

---

### 3. **admin** - Super Admin Management
**Purpose:** Handle all admin/system management features

**Responsibilities:**
- Admin dashboard
- User management
- Doctor approval/rejection
- Content management
- System settings
- Reports and statistics

**Models:**
- (Uses models from other apps)
- SystemSettings (optional)

**Views:**
- Admin dashboard
- User management
- Doctor approval interface
- Content management
- System settings

---

## 🔗 Shared Apps (Supporting)

### **assessment** - Risk Assessment
**Purpose:** AI risk assessment questionnaire and results

**Used by:**
- accounts (patients take assessment)
- doctors (doctors view assessments)

**Models:**
- Questionnaire
- QuestionnaireResponse
- RiskAssessment

---

### **content** - Awareness Content
**Purpose:** Articles and health tips

**Used by:**
- All apps (display content)
- admin (manage content)

**Models:**
- Article
- HealthTip

---

### **donations** - Donations Module
**Purpose:** Handle donations

**Used by:**
- All apps (donation links)
- admin (donation management)

**Models:**
- Donation
- DonationReceipt

---

## 📋 App Dependencies

```
accounts (base)
    ↓
doctors (depends on accounts)
    ↓
admin (depends on accounts, doctors, assessment, content, donations)
```

**Key Rule:** 
- `accounts` is independent (base)
- `doctors` can use `accounts` models
- `admin` can use all apps
- Shared apps (`assessment`, `content`, `donations`) are used by all

---

## 🎯 User Flow by App

### Patient Flow (accounts app)
1. Register → `accounts`
2. Login → `accounts`
3. Take assessment → `assessment` (but accessed via `accounts`)
4. View results → `assessment` (but accessed via `accounts`)
5. View doctor advice → `doctors` (but accessed via `accounts`)
6. View content → `content` (but accessed via `accounts`)

### Doctor Flow (doctors app)
1. Register → `accounts` (but doctor profile in `doctors`)
2. Wait for admin approval → `admin`
3. Login → `accounts`
4. View dashboard → `doctors`
5. View patient assessments → `assessment` (accessed via `doctors`)
6. Provide advice → `doctors`

### Admin Flow (admin app)
1. Login → `accounts`
2. View dashboard → `admin`
3. Manage users → `admin` (uses `accounts` models)
4. Approve doctors → `admin` (uses `doctors` models)
5. Manage content → `admin` (uses `content` models)
6. View reports → `admin` (uses all apps)

---

## 🔐 Access Control Strategy

### Decorators Location
Create `accounts/decorators.py` with:
- `patient_required` - for accounts app
- `doctor_required` - for doctors app
- `admin_required` - for admin app

**Usage:**
- Each app uses its own decorator
- Decorators check user groups and profiles
- No conflicts because each app has clear boundaries

---

## 📁 File Structure

```
letskillcancer/
├── accounts/              # Patient & Authentication
│   ├── models.py         # PatientProfile
│   ├── views.py          # Login, Register, Patient Dashboard
│   ├── urls.py
│   ├── decorators.py     # patient_required
│   └── templates/accounts/
│
├── doctors/              # Doctor Management
│   ├── models.py         # DoctorProfile, Consultation
│   ├── views.py          # Doctor Dashboard, Advice
│   ├── urls.py
│   └── templates/doctors/
│
├── admin/                # Super Admin
│   ├── views.py          # Admin Dashboard, Management
│   ├── urls.py
│   └── templates/admin/
│
├── assessment/           # Risk Assessment (Shared)
│   ├── models.py         # Questionnaire, RiskAssessment
│   ├── views.py
│   └── templates/assessment/
│
├── content/              # Content (Shared)
│   ├── models.py         # Article, HealthTip
│   └── views.py
│
└── donations/            # Donations (Shared)
    ├── models.py         # Donation
    └── views.py
```

---

## ✅ Benefits of This Structure

1. **Clear Separation:** Each role has its own app
2. **No Conflicts:** Apps don't interfere with each other
3. **Easy to Find:** Know exactly where to look for code
4. **Simple:** Easy to understand and maintain
5. **Scalable:** Easy to add features to specific apps

---

## 🚫 Rules to Avoid Conflicts

1. **Don't import models across apps unnecessarily**
   - Use foreign keys to reference other apps' models
   - Example: `doctor = ForeignKey(User)` not `doctor = ForeignKey(DoctorProfile)`

2. **Keep URLs separate**
   - `/accounts/` - for patient features
   - `/doctors/` - for doctor features
   - `/admin/` - for admin features
   - `/assessment/` - for assessment features

3. **Templates in app folders**
   - `accounts/templates/accounts/` - patient templates
   - `doctors/templates/doctors/` - doctor templates
   - `admin/templates/admin/` - admin templates

4. **One User model**
   - All apps use Django's built-in User model
   - Extend with profiles in respective apps
   - No custom user model conflicts

---

## 📝 Updated Roadmap with App Structure

### Phase 3: Create accounts app
- Create app
- Add authentication
- Add PatientProfile

### Phase 4: Create doctors app
- Create app
- Add DoctorProfile
- Add doctor features

### Phase 5: Create admin app
- Create app
- Add admin features
- Add management interfaces

### Phase 6+: Create shared apps
- assessment app
- content app
- donations app

---

**This structure keeps everything simple, organized, and conflict-free!**



