/**
 * Authentication JavaScript - Shared functionality for login/register
 * Professional, clean, and maintainable code
 */

// Password visibility toggle functionality
function initPasswordToggles() {
    const passwordToggles = document.querySelectorAll('.password-toggle');
    
    passwordToggles.forEach(toggle => {
        toggle.addEventListener('click', function(e) {
            e.preventDefault();
            
            const inputId = this.getAttribute('data-toggle');
            const input = document.getElementById(inputId);
            const icon = this.querySelector('i');
            
            if (!input) return;
            
            const isPassword = input.type === 'password';
            input.type = isPassword ? 'text' : 'password';
            
            // Toggle icon
            if (isPassword) {
                icon.classList.remove('fa-eye');
                icon.classList.add('fa-eye-slash');
            } else {
                icon.classList.remove('fa-eye-slash');
                icon.classList.add('fa-eye');
            }
        });
    });
}

// Form validation utility
function validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

function validatePasswordStrength(password) {
    // At least 8 characters
    if (password.length < 8) return false;
    // Contains uppercase
    if (!/[A-Z]/.test(password)) return false;
    // Contains lowercase
    if (!/[a-z]/.test(password)) return false;
    // Contains number
    if (!/[0-9]/.test(password)) return false;
    return true;
}

function showFieldError(fieldId, message) {
    const field = document.getElementById(fieldId);
    if (!field) return;
    
    field.classList.add('error');
    field.insertAdjacentHTML('afterend', `<div class="form-error">${message}</div>`);
}

function clearFieldError(fieldId) {
    const field = document.getElementById(fieldId);
    if (!field) return;
    
    field.classList.remove('error');
    const errorMsg = field.nextElementSibling;
    if (errorMsg && errorMsg.classList.contains('form-error')) {
        errorMsg.remove();
    }
}

// Login form specific functions
function initLoginForm() {
    const patientForm = document.getElementById('patientLoginForm');
    const doctorForm = document.getElementById('doctorLoginForm');
    
    if (patientForm) {
        patientForm.addEventListener('submit', function(e) {
            const emailField = this.querySelector('#patient-email');
            
            if (!validateEmail(emailField.value)) {
                e.preventDefault();
                showFieldError('patient-email', 'Please enter a valid email address');
            }
        });
    }
    
    if (doctorForm) {
        doctorForm.addEventListener('submit', function(e) {
            const profIdField = this.querySelector('#doctor-id');
            
            if (!profIdField.value.trim()) {
                e.preventDefault();
                showFieldError('doctor-id', 'Professional ID is required');
            }
        });
    }
}

// Register form specific functions
function initRegisterForm() {
    const registerForm = document.getElementById('registerForm');
    
    if (!registerForm) return;
    
    // Add real-time validation
    const emailField = registerForm.querySelector('#email');
    const password1Field = registerForm.querySelector('#password1');
    const password2Field = registerForm.querySelector('#password2');
    const passwordRequirements = registerForm.querySelector('.password-requirements');
    
    if (emailField) {
        emailField.addEventListener('blur', function() {
            if (this.value && !validateEmail(this.value)) {
                showFieldError('email', 'Please enter a valid email address');
            } else {
                clearFieldError('email');
            }
        });
    }
    
    if (password1Field) {
        // Show requirements on focus
        password1Field.addEventListener('focus', function() {
            if (passwordRequirements) {
                passwordRequirements.classList.add('active');
            }
        });
        
        // Hide requirements on blur if password is valid
        password1Field.addEventListener('blur', function() {
            if (passwordRequirements && validatePasswordStrength(this.value)) {
                passwordRequirements.classList.remove('active');
            }
        });
        
        // Update requirements checklist on input
        password1Field.addEventListener('input', function() {
            const length = this.value.length >= 8;
            const upper = /[A-Z]/.test(this.value);
            const lower = /[a-z]/.test(this.value);
            const digit = /[0-9]/.test(this.value);
            
            // Update visual indicators
            const reqLength = document.getElementById('req-length');
            const reqUpper = document.getElementById('req-upper');
            const reqLower = document.getElementById('req-lower');
            const reqDigit = document.getElementById('req-digit');
            
            if (reqLength) reqLength.classList.toggle('met', length);
            if (reqUpper) reqUpper.classList.toggle('met', upper);
            if (reqLower) reqLower.classList.toggle('met', lower);
            if (reqDigit) reqDigit.classList.toggle('met', digit);
        });
    }
    
    if (password2Field) {
        password2Field.addEventListener('input', function() {
            if (password1Field.value !== this.value) {
                this.classList.add('error');
            } else {
                this.classList.remove('error');
            }
        });
    }
    
    // Form submission validation
    registerForm.addEventListener('submit', function(e) {
        let hasErrors = false;
        
        // Validate first name
        const firstName = this.querySelector('#first-name');
        if (!firstName.value.trim()) {
            showFieldError('first-name', 'First name is required');
            hasErrors = true;
        }
        
        // Validate last name
        const lastName = this.querySelector('#last-name');
        if (!lastName.value.trim()) {
            showFieldError('last-name', 'Last name is required');
            hasErrors = true;
        }
        
        // Validate email
        if (!validateEmail(emailField.value)) {
            showFieldError('email', 'Please enter a valid email address');
            hasErrors = true;
        }
        
        // Validate password strength
        if (!validatePasswordStrength(password1Field.value)) {
            showFieldError('password1', 'Password must be at least 8 characters with uppercase, lowercase, and numbers');
            hasErrors = true;
        }
        
        // Validate password match
        if (password1Field.value !== password2Field.value) {
            showFieldError('password2', 'Passwords do not match');
            hasErrors = true;
        }
        
        // Validate terms agreement
        const termsCheckbox = this.querySelector('#terms');
        if (!termsCheckbox.checked) {
            showFieldError('terms', 'You must agree to the terms and conditions');
            hasErrors = true;
        }
        
        if (hasErrors) {
            e.preventDefault();
        }
    });
}

// Role selector functionality (Login only)
function initRoleSelector() {
    const roleRadios = document.querySelectorAll('input[name="role"]');
    const patientForm = document.getElementById('patientLoginForm');
    const doctorForm = document.getElementById('doctorLoginForm');
    
    if (!roleRadios.length) return;
    
    const dividerPatient = document.getElementById('divider-patient');
    const oauthPatient = document.getElementById('oauth-patient');
    const footerPatient = document.getElementById('footer-patient');
    
    roleRadios.forEach(radio => {
        radio.addEventListener('change', function() {
            if (this.value === 'patient') {
                if (patientForm) patientForm.classList.add('active');
                if (doctorForm) doctorForm.classList.remove('active');
                if (dividerPatient) dividerPatient.style.display = 'flex';
                if (oauthPatient) oauthPatient.style.display = 'flex';
                if (footerPatient) footerPatient.style.display = 'block';
            } else {
                if (patientForm) patientForm.classList.remove('active');
                if (doctorForm) doctorForm.classList.add('active');
                if (dividerPatient) dividerPatient.style.display = 'none';
                if (oauthPatient) oauthPatient.style.display = 'none';
                if (footerPatient) footerPatient.style.display = 'none';
            }
        });
    });
}

// Main initialization function
function initAuth() {
    // Common functionality
    initPasswordToggles();
    
    // Specific to login
    initLoginForm();
    initRoleSelector();
    
    // Specific to register
    initRegisterForm();
}

// Run when DOM is ready
document.addEventListener('DOMContentLoaded', initAuth);

// Utility to add loading state to button
function setButtonLoading(buttonElement, isLoading = true) {
    if (!buttonElement) return;
    
    if (isLoading) {
        buttonElement.classList.add('loading');
        buttonElement.disabled = true;
    } else {
        buttonElement.classList.remove('loading');
        buttonElement.disabled = false;
    }
}

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        validateEmail,
        validatePasswordStrength,
        showFieldError,
        clearFieldError,
        setButtonLoading
    };
}
