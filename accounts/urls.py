from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # Authentication URLs
    path('register/', views.patient_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
    # Google OAuth URLs (will add later)
    # path('google-register/', views.google_register, name='google-register'),
    # path('google-login/', views.google_login, name='google-login'),
    # path('google-callback/', views.google_callback, name='google-callback'),
]
