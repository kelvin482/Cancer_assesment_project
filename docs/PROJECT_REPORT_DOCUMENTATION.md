# Project Report: Let's Kill Cancer (CancerProject2026)

## 1. Project Overview
**Project Name:** Let's Kill Cancer (CancerProject2026)  
**Project Type:** AI-assisted web platform for cancer risk pattern screening support  
**Framework:** Django (Python)

This project is designed to support early awareness and structured clinical screening workflows by combining role-based access (patients and doctors) with an ML-backed risk pattern predictor.

Important note: The system is **supportive and non-diagnostic**. Final clinical decisions remain with qualified medical professionals.

## 2. Main Objectives
1. Build a secure role-based health platform for patients and doctors.
2. Provide a structured digital workflow for symptom/feature-based risk screening.
3. Integrate a machine learning model to assist doctors with quick risk pattern indication.
4. Store diagnosis history and link records to registered patients.
5. Generate professional reports that can be printed or exported as PDF.
6. Prepare a scalable foundation for future modules (education, analytics, and broader patient support).

## 3. System Objects / Core Modules
### 3.1 `accounts` app
- Patient registration and login.
- Doctor login via professional ID.
- Profile-linked user model extensions:
  - `Patient`
  - `Doctor`

### 3.2 `doctor` app
- Doctor dashboard.
- Dynamic diagnosis form driven by active DB features.
- Patient-linked diagnosis saving (`DoctorInput`).
- Report view and PDF download flow.
- Doctor settings update page.
- Doctor education content posting (`EducationPost`).

### 3.3 `ml_engine` module
- Loads trained model + scaler artifacts.
- Maps submitted feature values into model input vector.
- Produces risk category output:
  - `Higher Pattern Concern`
  - `Lower Pattern Concern`

## 4. How the Project Works (End-to-End Workflow)
1. **Authentication**
- Patient registers with personal credentials.
- Doctor logs in with professional ID + password (with approval checks).

2. **Doctor Clinical Workflow**
- Doctor opens dashboard.
- Doctor starts a diagnosis session.
- System loads active screening features from database.
- Doctor enters feature values and optionally links the record to a patient.

3. **AI-Assisted Prediction**
- Input values are transformed into model feature order.
- Scaler normalization is applied.
- Trained model predicts the screening category.

4. **Record and Reporting**
- Diagnosis result and input values are stored in database.
- Doctor can open a full report page for each diagnosis.
- Report can be printed or downloaded as PDF (WeasyPrint flow).

## 5. Achievements So Far (Implemented)
1. Django project setup with modular app structure.
2. PostgreSQL-ready configuration via environment variables.
3. Patient registration with validation (email uniqueness, password rules, phone checks).
4. Unified login supporting both patient and doctor roles.
5. Doctor approval-aware authentication logic.
6. Dynamic diagnosis form generated from database `Feature` records.
7. ML prediction integration (`ml_engine/predict.py`) connected to diagnosis workflow.
8. Persistent diagnosis history (`DoctorInput`) linked to doctor and optional patient.
9. Doctor dashboard with recent activity.
10. Professional report page with print + downloadable PDF option.
11. Doctor profile/settings management including image upload.
12. Education post feature for doctor-authored patient guidance.

## 6. Current Technical Stack
- **Backend:** Django
- **Database:** PostgreSQL
- **ML/Data:** scikit-learn, pandas, numpy
- **Media:** Pillow
- **PDF:** WeasyPrint
- **Config:** django-environ + `.env`

## 7. Key Challenges Encountered
1. **Documentation drift vs implementation**
- Some roadmap/progress documents are older than current code state, creating mismatch in status communication.

2. **Environment dependencies**
- PostgreSQL setup and local environment consistency are required for smooth onboarding.
- PDF generation may require additional system libraries depending on OS setup.

3. **Security and medical-data sensitivity**
- Strong handling is needed for sensitive patient data (credentials, profile and diagnosis info).
- Production hardening (DEBUG off, secure secrets, HTTPS, access control audits) is mandatory.

4. **ML governance**
- Model outputs must be presented as support signals, not diagnoses.
- Ongoing model validation and dataset quality checks are needed as usage grows.

5. **Testing depth**
- Core workflows are implemented, but broader automated test coverage is still needed for reliability and regression safety.

## 8. Lessons Learned
1. Dynamic, database-driven forms improve maintainability and reduce hardcoded logic.
2. Separating domain modules (`accounts`, `doctor`, `ml_engine`) improves scalability.
3. AI integration is most effective when embedded into clear user workflows and explicit safety boundaries.

## 9. Next Steps
1. Expand automated testing (unit + integration for auth, diagnosis, and reporting).
2. Strengthen role-based authorization checks and audit trails.
3. Improve error handling and user feedback in edge cases.
4. Add monitoring and logging for prediction/report workflows.
5. Align all project documentation with actual implementation status.
6. Prepare deployment pipeline with production security configuration.

## 10. Conclusion
The project has progressed from planning to a functioning AI-assisted clinical support prototype. Core workflows for registration, doctor-led assessment, ML-backed risk indication, and professional report generation are operational. The current stage is suitable for academic demonstration and can be further strengthened through testing, security hardening, and deployment readiness.

## 11. Doctor App UI Premium Standard (Non-Breaking)
This section defines how to make the doctor-facing UI look premium and professional **without changing page structure or workflow behavior**.

### 11.1 Non-Breaking Rule (Mandatory)
1. Keep existing template layout and route flow unchanged.
2. Do not rename/remove core HTML classes used by JS logic.
3. Apply improvements through shared design tokens and scoped CSS refinements.
4. Preserve current doctor workflow order: Dashboard -> Diagnosis -> Result -> Report -> Settings -> Education.

### 11.2 Uniform Color System (Doctor App)
Use one consistent palette across all doctor pages:

- Primary Brand: `#E91E63`
- Primary Hover/Dark: `#D81B60`
- Primary Light Surface: `#F8BBD0`
- Accent/Info: `#2196F3`
- Success: `#4CAF50`
- Error/High Risk: `#F44336`
- Warning: `#FF9800`
- Text Primary: `#212121`
- Text Secondary: `#757575`
- Surface White: `#FFFFFF`
- Surface Light: `#FAFAFA`
- Border: `#CCCCCC`

Color usage target (60/30/10):
1. `60%` neutral surfaces (`#FFFFFF`, `#FAFAFA`, soft borders).
2. `30%` structural/support tones (light blue or soft surface contrasts).
3. `10%` primary emphasis (`#E91E63` family) for key CTA and active state only.

### 11.3 Premium UI Principles
1. Reduce visual noise: fewer heavy gradients, glows, and competing accents.
2. Strengthen hierarchy: clear title > subtitle > body > metadata rhythm.
3. Increase consistency: same button logic, same card structure, same spacing scale.
4. Improve clarity: semantic colors only for meaning (risk, success, warning).
5. Keep interactions subtle: soft hover/focus, no exaggerated motion.

### 11.4 Typography and Spacing Rules
1. Use one heading family and one body family consistently across doctor pages.
2. Standardize text scale and weights across cards, tables, labels, and buttons.
3. Apply an 8px spacing system (`4, 8, 12, 16, 24, 32`).
4. Keep card radii and shadows consistent to avoid mixed visual styles.

### 11.5 Component Consistency Rules
1. Buttons:
- Primary only for most important action on each screen.
- Secondary/ghost for all non-critical actions.
2. Cards:
- Same border, radius, and padding system on dashboard, diagnosis, settings, education.
3. Tables/lists:
- Uniform row height, typography, badge style, and hover behavior.
4. Status colors:
- Red only for high-risk/error.
- Green only for benign/success.
- Amber only for pending/warning.

### 11.6 Implementation Order (Safe Rollout)
1. Define/confirm tokens in `static/css/variables.css`.
2. Normalize shared doctor shell styles in `doctor/static/doctor/css/doctor_theme.css`.
3. Apply dashboard visual cleanup in `doctor/static/doctor/pages/dashboard/dashboard.css`.
4. Apply diagnosis consistency in `doctor/static/doctor/css/diagnosis.css`.
5. Apply settings/education consistency in:
- `doctor/static/doctor/pages/settings/settings.css`
- `doctor/static/doctor/pages/education/education.css`
6. Validate templates still render correctly:
- `doctor/templates/doctor/dashboard.html`
- `doctor/templates/doctor/diagnosis.html`
- `doctor/templates/doctor/pages/settings/settings.html`
- `doctor/templates/doctor/pages/education/education.html`

### 11.7 Quality Checklist Before Finalizing
1. No layout/route breakage in doctor pages.
2. Colors are consistent across all doctor views.
3. One clear primary CTA per section.
4. Readability and contrast pass visual review.
5. No hidden content due to JS-only visibility logic.
6. Mobile and desktop both remain usable.

### 11.8 Step 1 Delivery (Token Cleanup + Conflict Reduction)
This is the first safe implementation step for premium dashboard polish.

1. Define doctor-specific 60/30/10 tokens in `static/css/variables.css` and reference them from dashboard theme rules.
2. Keep one active premium token block for `.doctor-dashboard-premium`; remove deprecated duplicate theme blocks with competing palettes.
3. Keep navbar brand/action colors inherited from shared global tokens instead of redefining multiple variants in page-level CSS.
4. Do not change dashboard HTML structure while performing token cleanup.
5. Validate after each CSS edit with visual checks on:
- Dashboard overview
- Diagnosis page buttons
- Education nav badge
