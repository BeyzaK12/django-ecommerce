from django.urls import path
from .views import SignUpView, redirect_view


urlpatterns = [
    path('üyeol/', SignUpView.as_view(), name='signup'),
    path('yönlendirme/', redirect_view, name='redirect'),
]
