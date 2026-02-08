from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# ============================================
# Patient Model
# ============================================

class Patient(models.Model):
    """
    Patient profile model extending Django User.
    Stores patient-specific information.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient')
    
    # Additional patient info
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message='Enter a valid phone number',
                code='invalid_phone'
            )
        ]
    )
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(
        max_length=10,
        choices=[
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other'),
            ('N', 'Prefer not to say'),
        ],
        blank=True,
        null=True
    )
    
    # Profile status
    is_verified_email = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Patient: {self.user.get_full_name() or self.user.username}"
    
    def get_full_name(self):
        """Get patient's full name"""
        if self.user.first_name and self.user.last_name:
            return f"{self.user.first_name} {self.user.last_name}"
        return self.user.username


# ============================================
# Doctor Model
# ============================================

class Doctor(models.Model):
    """
    Doctor profile model extending Django User.
    Stores doctor-specific information and credentials.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor')
    
    # Professional credentials
    professional_id = models.CharField(
        max_length=50,
        unique=True,
        help_text="Medical license or professional ID number"
    )
    specialization = models.CharField(
        max_length=100,
        blank=True,
        help_text="Medical specialization (e.g., Oncology, General Practice)"
    )
    license_number = models.CharField(
        max_length=100,
        blank=True,
        help_text="Medical license number"
    )
    institution = models.CharField(
        max_length=255,
        blank=True,
        help_text="Medical institution or hospital"
    )
    
    # Approval status
    is_approved = models.BooleanField(
        default=False,
        help_text="Admin approval status"
    )
    is_verified_credentials = models.BooleanField(
        default=False,
        help_text="Credentials verification status"
    )
    approval_date = models.DateTimeField(blank=True, null=True)
    approval_notes = models.TextField(
        blank=True,
        help_text="Admin notes for approval/rejection"
    )
    
    # Contact and availability
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message='Enter a valid phone number',
                code='invalid_phone'
            )
        ]
    )
    consultation_hours = models.CharField(
        max_length=255,
        blank=True,
        help_text="Available consultation hours"
    )
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Dr. {self.user.get_full_name() or self.user.username}"
    
    def get_full_name(self):
        """Get doctor's full name"""
        if self.user.first_name and self.user.last_name:
            return f"Dr. {self.user.first_name} {self.user.last_name}"
        return f"Dr. {self.user.username}"
    
    def can_consult(self):
        """Check if doctor is approved and can consult patients"""
        return self.is_approved and self.user.is_active
