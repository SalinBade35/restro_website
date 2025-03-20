from django.urls import path 
from .views import *
from .views import generate_restaurant_qr_view
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", index, name='index'),
    path("about/", about, name='about'),
    path("contact/", contact, name='contact'),
    path("menu/", menu, name='menu'),
    path("services/", services, name='services'),
    path("support/", support, name='support'),
    path("terms/", terms, name='terms'),
    path("privacy/", privacy, name='privacy'),
    path("policy/", policy, name='policy'),  
    # path('', contact_view, name='contact'),
    # ============================================ auth part ==================================
    path("login/", log_in, name='log_in'),
    path("register/", register, name='register'),
    path("logout/", log_out, name='log_out'),
    path("change_password/", change_password, name='change_password'),
    path('user_profile/',user_profile, name='user_profile'),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="auth/password_reset.html"), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="auth/password_reset_done.html"), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="auth/password_reset_confirm.html"), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="auth/password_reset_complete.html"), name='password_reset_complete'),
    
]