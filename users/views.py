from .forms import CustomUserCreationForm
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import redirect


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:redirect')
    template_name = 'registration/signup.html'


def redirect_view(request):
    response = redirect('core:home')
    return response
