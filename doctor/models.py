# doctor/models.py
from django.db import models
from django.contrib.auth.models import User  # assuming doctors are users
from accounts.models import Patient

class DoctorInput(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="inputs")
    patient = models.ForeignKey(
        Patient,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="diagnoses",
    )
    # Store the answers as JSON to allow dynamic number of inputs
    answers = models.JSONField()
    prediction = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.doctor.username} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"



class Feature(models.Model):
    name = models.CharField(max_length=100, unique=True)
    display_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    min_value = models.FloatField(default=1)
    max_value = models.FloatField(default=5)

    def __str__(self):
        return self.display_name


class EducationPost(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="education_posts")
    title = models.CharField(max_length=160)
    summary = models.CharField(max_length=300)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} ({self.doctor.username})"
