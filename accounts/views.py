from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from django.db import IntegrityError, transaction
from .models import Patient, Doctor
import logging

logger = logging.getLogger(__name__)

# ============================================
# PATIENT REGISTRATION VIEW
# ============================================

@require_http_methods(["GET", "POST"])
@csrf_protect
def patient_register(request):
    """
    Patient registration view.
    Handles GET (display form) and POST (process registration)
    """
    # Ensure CSRF token is available in context
    from django.middleware.csrf import get_token
    get_token(request)
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip().lower()
        phone_number = request.POST.get('phone_number', '').strip()
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        agree_terms = request.POST.get('agree_terms')
        
        # Validation
        errors = {}
        
        # Validate required fields
        if not first_name:
            errors['first_name'] = 'First name is required'
        if not last_name:
            errors['last_name'] = 'Last name is required'
        if not email:
            errors['email'] = 'Email is required'
        if not password1:
            errors['password1'] = 'Password is required'
        if not password2:
            errors['password2'] = 'Password confirmation is required'
        if not agree_terms:
            errors['agree_terms'] = 'You must agree to terms and conditions'
        
        # Validate passwords match
        if password1 and password2 and password1 != password2:
            errors['password2'] = 'Passwords do not match'
        
        # Validate email is not already used
        if email and User.objects.filter(email=email).exists():
            errors['email'] = 'This email is already registered. Please login or use a different email.'
        
        # Validate password strength
        if password1:
            password_errors = []
            if len(password1) < 8:
                password_errors.append('Password must be at least 8 characters')
            if not any(c.isupper() for c in password1):
                password_errors.append('Password must contain uppercase letter')
            if not any(c.islower() for c in password1):
                password_errors.append('Password must contain lowercase letter')
            if not any(c.isdigit() for c in password1):
                password_errors.append('Password must contain number')
            
            if password_errors:
                errors['password1'] = password_errors[0]  # Show only first error
        
        # Validate phone number (optional, but if provided, must be valid format)
        if phone_number:
            import re
            # Remove formatting characters to validate
            phone_clean = phone_number.replace(' ', '').replace('(', '').replace(')', '').replace('-', '')
            phone_pattern = r'^\+?1?\d{9,15}$'
            if not re.match(phone_pattern, phone_clean):
                errors['phone_number'] = 'Enter a valid phone number'
            else:
                # Keep only digits and + for storage (max 15 chars)
                phone_number = phone_clean[:15]  # Ensure it fits in DB field
        
        # If there are errors, re-render form with errors
        if errors:
            context = {
                'errors': errors,
                'form_data': {
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'phone_number': phone_number,
                }
            }
            messages.error(request, 'Please fix the errors below')
            return render(request, 'accounts/register.html', context)
        
        # Create user and patient profile
        try:
            with transaction.atomic():
                # Create user
                user = User.objects.create_user(
                    username=email,  # Use email as username
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=password1
                )
                
                # Create patient profile
                Patient.objects.create(
                    user=user,
                    phone_number=phone_number if phone_number else None
                )
                
                # Log the user in
                login(request, user)
                
                messages.success(request, f'Welcome {first_name}! Your account has been created.')
                return redirect('home')  # Change to your home page
        
        except IntegrityError as e:
            logger.error(f'IntegrityError during registration: {str(e)}')
            messages.error(request, 'An account with this email already exists. Please use a different email.')
            return render(request, 'accounts/register.html', {'form_data': {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'phone_number': phone_number,
            }})
        
        except Exception as e:
            logger.error(f'Unexpected error during registration: {type(e).__name__}: {str(e)}')
            messages.error(request, f'An error occurred during registration: {str(e)}')
            return render(request, 'accounts/register.html', {'form_data': {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'phone_number': phone_number,
            }})
    
    # GET request - display registration form
    return render(request, 'accounts/register.html', {'form_data': {}, 'errors': {}})


# ============================================
# LOGIN VIEW (Both Patient and Doctor)
# ============================================

@require_http_methods(["GET", "POST"])
@csrf_protect
def user_login(request):
    """
    Combined login view for both patients and doctors.
    Patients use email; doctors use Professional ID (from Doctor model).
    """
    professional_id_placeholder = Doctor._meta.get_field('professional_id').help_text
    form_data = {'email': '', 'professional_id': ''}

    if request.method == 'POST':
        role = request.POST.get('role', 'patient')
        password = request.POST.get('password', '')
        remember_me = request.POST.get('remember_me')
        
        errors = {}
        
        # Patient Login
        if role == 'patient':
            email = request.POST.get('email', '').strip().lower()
            form_data['email'] = email
            
            if not email:
                errors['email'] = 'Email is required'
            if not password:
                errors['password'] = 'Password is required'
            
            if not errors:
                # Try to authenticate with email
                try:
                    user = User.objects.get(email=email)
                    user = authenticate(request, username=user.username, password=password)
                    
                    if user is not None:
                        # Check if user has patient profile
                        if hasattr(user, 'patient'):
                            login(request, user)
                            
                            # Set session expiry if not "remember me"
                            if not remember_me:
                                request.session.set_expiry(0)  # Expires when browser closes
                            
                            messages.success(request, f'Welcome back, {user.first_name}!')
                            return redirect('home')  # Change to patient dashboard
                        else:
                            errors['non_field'] = 'This account is not a patient account'
                    else:
                        errors['non_field'] = 'Invalid email or password'
                except User.DoesNotExist:
                    errors['non_field'] = 'Invalid email or password'
        
        # Doctor Login
        elif role == 'doctor':
            professional_id = request.POST.get('professional_id', '').strip()
            form_data['professional_id'] = professional_id
            
            if not professional_id:
                errors['professional_id'] = 'Professional ID is required'
            if not password:
                errors['password'] = 'Password is required'
            
            if not errors:
                try:
                    # Get doctor by professional ID
                    doctor = Doctor.objects.get(professional_id=professional_id)
                    user = doctor.user
                    
                    # Authenticate
                    user = authenticate(request, username=user.username, password=password)
                    
                    if user is not None:
                        # Check if doctor is approved
                        if not user.doctor.is_approved:
                            errors['non_field'] = 'Your account is pending admin approval'
                        elif not user.is_active:
                            errors['non_field'] = 'Your account has been deactivated'
                        else:
                            login(request, user)
                            
                            # Set session expiry if not "remember me"
                            if not remember_me:
                                request.session.set_expiry(0)
                            
                            messages.success(request, f'Welcome back, Dr. {user.first_name}!')
                            return redirect('doctor_dashboard')
                    else:
                        errors['non_field'] = 'Invalid Professional ID or password'
                except Doctor.DoesNotExist:
                    errors['non_field'] = 'Invalid Professional ID or password'
        
        # If there are errors, re-render login form
        if errors:
            context = {
                'errors': errors,
                'role': role,
                'form_data': form_data,
                'professional_id_placeholder': professional_id_placeholder,
            }
            messages.error(request, 'Login failed. Please check your credentials.')
            return render(request, 'accounts/login.html', context)
    
    # GET request - display login form
    return render(request, 'accounts/login.html', {
        'errors': {},
        'form_data': form_data,
        'role': 'patient',
        'professional_id_placeholder': professional_id_placeholder,
    })


# ============================================
# LOGOUT VIEW
# ============================================

@require_http_methods(["GET", "POST"])
def user_logout(request):
    """
    Logout view.
    Logs out the user and redirects to home.
    """
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')  # Change to your login page


# ============================================
# HOME VIEW (Placeholder)
# ============================================

def home(request):
    """
    Home page view.
    Shows different content based on user role.
    """
    if request.user.is_authenticated:
        if hasattr(request.user, 'patient'):
            return render(request, 'home.html', {'user_type': 'patient'})
        elif hasattr(request.user, 'doctor'):
            return render(request, 'home.html', {'user_type': 'doctor'})
    
    return render(request, 'home.html')
