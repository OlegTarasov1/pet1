from django.urls import path
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, LogoutView, PasswordResetCompleteView, PasswordChangeDoneView, PasswordResetDoneView, PasswordChangeView
from . import views

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name = 'login'),
    path('register/', views.RegisterUser.as_view(), name = 'register'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('profile/', views.MyProfile.as_view(), name = 'profile'),
    path('password-change/', views.UserPasswordChange.as_view(), name = 'password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name = 'users/password_change_done.html'), name = 'password_change_done'),
    path('password-reset/', PasswordResetView.as_view(template_name = 'users/password_reset_form.html'), name = 'password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name = 'users/password_reset_done.html'), name = 'password_reset_done'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name = 'users/password_reset_confirm.html'), name = 'password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(template_name = 'users/password_reset_complete.html'), name = 'password_reset_complete')
]