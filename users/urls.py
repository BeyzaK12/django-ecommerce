from django.urls import path
from .views import SignUpView, redirect_view
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('üyeol/', SignUpView.as_view(), name='signup'),
    path('giriş/', LoginView.as_view(), name='login'),
    path('yönlendirme/', redirect_view, name='redirect'),
]
