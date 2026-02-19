from django import forms
from django.contrib import admin
from django.contrib.auth.password_validation import validate_password
from accounts.models import Doctor

from .models import DoctorInput, Feature, EducationPost


# Unregister Doctor from accounts so we can register with password support
try:
    admin.site.unregister(Doctor)
except admin.sites.NotRegistered:
    pass


class DoctorAdminForm(forms.ModelForm):
    """Form adding password fields for doctor's linked User (no hardcoding)."""
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        required=False,
        help_text='Leave blank to keep current password. Raw password is hashed on save.',
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        required=False,
        help_text='Enter the same password again.',
    )

    class Meta:
        model = Doctor
        fields = '__all__'

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 or password2:
            if password1 != password2:
                raise forms.ValidationError("Passwords don't match.")
            validate_password(password1)
        return password2


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    form = DoctorAdminForm
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
        'specialization',
    ]
    readonly_fields = ['created_at', 'updated_at']
    actions = ['approve_doctors', 'reject_doctors', 'verify_credentials']

    fieldsets = (
        ('User Information', {
            'fields': ('user',),
        }),
        ('Password', {
            'fields': ('password1', 'password2'),
            'description': 'Set or change the doctor login password. Leave blank to keep current.',
        }),
        ('Professional Credentials', {
            'fields': (
                'professional_id',
                'specialization',
                'license_number',
                'institution',
            ),
        }),
        ('Approval Status', {
            'fields': (
                'is_approved',
                'is_verified_credentials',
                'approval_date',
                'approval_notes',
            ),
        }),
        ('Contact Information', {
            'fields': ('phone_number', 'consultation_hours'),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    def doctor_name(self, obj):
        return obj.get_full_name()
    doctor_name.short_description = 'Doctor Name'

    def approval_status(self, obj):
        from django.utils.html import format_html
        if obj.is_approved:
            return format_html('<span style="color: green;">✓ Approved</span>')
        return format_html('<span style="color: red;">✗ Pending</span>')
    approval_status.short_description = 'Approval'

    def credentials_status(self, obj):
        from django.utils.html import format_html
        if obj.is_verified_credentials:
            return format_html('<span style="color: green;">✓ Verified</span>')
        return format_html('<span style="color: orange;">⊘ Not Verified</span>')
    credentials_status.short_description = 'Credentials'

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        password = form.cleaned_data.get('password1')
        if password:
            obj.user.set_password(password)  # Django hashes automatically
            obj.user.save(update_fields=['password'])

    def approve_doctors(self, request, queryset):
        from django.utils import timezone
        updated = queryset.update(
            is_approved=True,
            approval_date=timezone.now(),
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


admin.site.register(DoctorInput)
admin.site.register(Feature)
admin.site.register(EducationPost)
