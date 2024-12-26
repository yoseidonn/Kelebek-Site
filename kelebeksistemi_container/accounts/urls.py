##################### ACCOUNTS URLS #####################
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from accounts.views import (user_login,
                            user_register, 
                            user_profile, 
                            user_edit_profile,
                            user_verify_email,
                            user_logout,
                            )


urlpatterns = [
    path('login/', user_login, name="login"),
    path('register/', user_register, name="register"),
    path('profile/', user_profile, name="profile"),
    path('edit-profile/', user_edit_profile, name="edit_profile"),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"), 
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"), 
    path('verify-email/<str:uid>/<str:token>', user_verify_email, name="verify_email"), 
    path('logout/', user_logout, name="logout"),
]