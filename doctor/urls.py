from django.urls import path
from .views import (
    diagnosis_view,
    doctor_dashboard_view,
    diagnosis_report_view,
    doctor_settings_view,
    doctor_education_view,
    patient_records_view,
    doctor_reports_view,
    doctor_ai_insights_view,
)

urlpatterns = [
    path("", doctor_dashboard_view, name="doctor_dashboard"),
    path("diagnosis/", diagnosis_view, name="diagnosis"),
    path("patient-records/", patient_records_view, name="patient_records"),
    path("report/<int:input_id>/", diagnosis_report_view, name="diagnosis_report"),
    path("reports/", doctor_reports_view, name="doctor_reports"),
    path("ai-insights/", doctor_ai_insights_view, name="doctor_ai_insights"),
    path("settings/", doctor_settings_view, name="doctor_settings"),
    path("education/", doctor_education_view, name="doctor_education"),
]
