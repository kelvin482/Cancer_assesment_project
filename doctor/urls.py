from django.urls import path
from .views import diagnosis_view, doctor_dashboard_view, diagnosis_report_view, doctor_settings_view

urlpatterns = [
    path("", doctor_dashboard_view, name="doctor_dashboard"),
    path("diagnosis/", diagnosis_view, name="diagnosis"),
    path("report/<int:input_id>/", diagnosis_report_view, name="diagnosis_report"),
    path("settings/", doctor_settings_view, name="doctor_settings"),
]
