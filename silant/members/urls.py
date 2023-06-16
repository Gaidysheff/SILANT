from django.urls import path
from members.views import *


urlpatterns = [
    path('login_user', login_user, name='login'),
]
