from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.contrib import messages
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import DoctorInput, Feature
from .forms import DiagnosisForm  # dynamic form
from ml_engine.predict import predict_risk
from accounts.models import Patient

try:
    from weasyprint import HTML
    WEASYPRINT_AVAILABLE = True
except Exception:
    WEASYPRINT_AVAILABLE = False


@login_required
@ensure_csrf_cookie
def doctor_dashboard_view(request):
    """Landing page for doctors after login - avoids CSRF issues from missing redirect target."""
    recent_inputs = (
        DoctorInput.objects.select_related("patient", "patient__user")
        .order_by("-created_at")[:10]
    )
    return render(request, "doctor/dashboard.html", {
        "recent_inputs": recent_inputs,
    })


@login_required
@ensure_csrf_cookie
def doctor_settings_view(request):
    doctor_profile = getattr(request.user, "doctor", None)
    if doctor_profile is None:
        messages.error(request, "Doctor profile not found for this account.")
        return render(request, "doctor/pages/settings/settings.html", {"doctor_profile": None})

    if request.method == "POST":
        request.user.first_name = request.POST.get("first_name", "").strip()
        request.user.last_name = request.POST.get("last_name", "").strip()

        email = request.POST.get("email", "").strip()
        if email:
            request.user.email = email

        doctor_profile.phone_number = request.POST.get("phone_number", "").strip() or None
        doctor_profile.specialization = request.POST.get("specialization", "").strip()
        doctor_profile.institution = request.POST.get("institution", "").strip()
        doctor_profile.license_number = request.POST.get("license_number", "").strip()
        doctor_profile.consultation_hours = request.POST.get("consultation_hours", "").strip()

        if request.FILES.get("profile_image"):
            doctor_profile.profile_image = request.FILES["profile_image"]

        request.user.save(update_fields=["first_name", "last_name", "email"])
        doctor_profile.save()
        messages.success(request, "Settings updated successfully.")

    return render(request, "doctor/pages/settings/settings.html", {
        "doctor_profile": doctor_profile,
    })


@login_required
@ensure_csrf_cookie
def diagnosis_view(request):
    """
    Handles displaying the dynamic form, processing doctor input,
    running ML prediction, saving results, and rendering the outcome.
    """
    patients = Patient.objects.select_related("user").order_by("user__first_name", "user__last_name")

    if request.method == "POST":
        form = DiagnosisForm(request.POST)
        if form.is_valid():
            patient = None
            patient_id = request.POST.get("patient_id")
            if patient_id:
                patient = Patient.objects.filter(id=patient_id).first()

            # Build a dictionary of feature answers dynamically
            feature_values = {
                feature.name: form.cleaned_data[feature.name]
                #You need to ensure the view only looks for data corresponding to the active features,
                for feature in Feature.objects.filter(is_active=True)
            }

            # Run ML prediction
            prediction = predict_risk(feature_values)

            # Create and save DoctorInput (DiagnosisForm is Form, not ModelForm - no .save())
            record = DoctorInput.objects.create(
                doctor=request.user,
                patient=patient,
                answers=feature_values,
                prediction=prediction,
            )

            # Render the results page
            return render(request, "doctor/result.html", {
                "prediction": prediction,
                "feature_values": feature_values,
                "patient": patient,
                "record_id": record.id,
            })
    else:
        # GET request -> show empty form
        form = DiagnosisForm()

    return render(request, "doctor/diagnosis.html", {"form": form, "patients": patients})


@login_required
def diagnosis_report_view(request, input_id):
    record = get_object_or_404(DoctorInput, id=input_id, doctor=request.user)
    context = {
        "record": record,
        "patient": record.patient,
        "feature_values": record.answers,
    }

    if request.GET.get("download") == "1":
        if not WEASYPRINT_AVAILABLE:
            return HttpResponse(
                "PDF generation requires WeasyPrint. Install it and try again.",
                status=501,
            )
        html = render_to_string("doctor/pages/report/report.html", context, request=request)
        pdf = HTML(string=html, base_url=request.build_absolute_uri("/")).write_pdf()
        response = HttpResponse(pdf, content_type="application/pdf")
        response["Content-Disposition"] = f'attachment; filename="diagnosis-report-{record.id}.pdf"'
        return response

    return render(request, "doctor/pages/report/report.html", context)
