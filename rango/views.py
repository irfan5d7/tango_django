from django.shortcuts import render
from django.template import RequestContext
from django.urls import reverse

from .models import *
# Create your views here.


from registration.backends.simple.views import RegistrationView
class RangoRegistrationView(RegistrationView):
    def get_success_url(self,user):
        return reverse('rango:register_profile')
