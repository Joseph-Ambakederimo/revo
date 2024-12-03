# urls.py
from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('service/', service, name='service'),
    path('employment/', employment, name='employment'),
    path('success/', success, name='success'),
    # path('success/', TemplateView.as_view(template_name='success.html'), name='success'),  # Optional success page
]

