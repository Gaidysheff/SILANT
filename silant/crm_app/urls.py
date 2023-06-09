from django.urls import path
from crm_app.views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
]
