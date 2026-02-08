from django.contrib import admin
from django.utils.html import format_html
from .models import Patient, Doctor


# ============================================
# PATIENT ADMIN
# ============================================

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = [
        'patient_name',
        'email',
        'phone_number',
        'is_verified_email',
        'created_at',
    ]
    list_filter = ['is_verified_email', 'created_at', 'gender']
    search_fields = ['user__username', 'user__email', 'user__first_name', 'user__last_name']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('User Information', {
            'fields': ('user',)
        }),
        ('Personal Information', {
            'fields': ('phone_number', 'date_of_birth', 'gender')
        }),
        ('Verification', {
            'fields': ('is_verified_email',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def patient_name(self, obj):
        return obj.get_full_name()
    patient_name.short_description = 'Patient Name'
    
    def email(self, obj):
        return obj.user.email
    email.short_description = 'Email'


# ============================================
# DOCTOR ADMIN
# ============================================

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = [
        'doctor_name',
        'professional_id',
        'specialization',
        'approval_status',
        'credentials_status',
        'created_at',
    ]
    list_filter = ['is_approved', 'is_verified_credentials', 'created_at']
    search_fields = [
        'user__username',
        'user__email',
        'user__first_name',
        'user__last_name',
        'professional_id',
        'specialization'
    ]
    readonly_fields = ['created_at', 'updated_at']
    actions = ['approve_doctors', 'reject_doctors', 'verify_credentials']
    
    fieldsets = (
        ('User Information', {
            'fields': ('user',)
        }),
        ('Professional Credentials', {
            'fields': (
                'professional_id',
                'specialization',
                'license_number',
                'institution',
            )
        }),
        ('Approval Status', {
            'fields': (
                'is_approved',
                'is_verified_credentials',
                'approval_date',
                'approval_notes',
            )
        }),
        ('Contact Information', {
            'fields': ('phone_number', 'consultation_hours')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def doctor_name(self, obj):
        return obj.get_full_name()
    doctor_name.short_description = 'Doctor Name'
    
    def approval_status(self, obj):
        if obj.is_approved:
            color = 'green'
            status = '✓ Approved'
        else:
            color = 'red'
            status = '✗ Pending'
        return format_html(
            '<span style="color: {};">{}</span>',
            color,
            status
        )
    approval_status.short_description = 'Approval'
    
    def credentials_status(self, obj):
        if obj.is_verified_credentials:
            color = 'green'
            status = '✓ Verified'
        else:
            color = 'orange'
            status = '⊘ Not Verified'
        return format_html(
            '<span style="color: {};">{}</span>',
            color,
            status
        )
    credentials_status.short_description = 'Credentials'
    
    def approve_doctors(self, request, queryset):
        from django.utils import timezone
        updated = queryset.update(
            is_approved=True,
            approval_date=timezone.now()
        )
        self.message_user(request, f'{updated} doctor(s) approved successfully.')
    approve_doctors.short_description = 'Approve selected doctors'
    
    def reject_doctors(self, request, queryset):
        updated = queryset.update(is_approved=False)
        self.message_user(request, f'{updated} doctor(s) rejected.')
    reject_doctors.short_description = 'Reject selected doctors'
    
    def verify_credentials(self, request, queryset):
        updated = queryset.update(is_verified_credentials=True)
        self.message_user(request, f'{updated} doctor(s) credentials verified.')
    verify_credentials.short_description = 'Verify credentials'
