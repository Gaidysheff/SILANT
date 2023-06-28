from django.urls import path
from crm_app.views import *

urlpatterns = [
    # path('', index, name='index'),
    path('', MachinesHomePage.as_view(), name='index'),
    path('machine/<int:machine_id>/', show_machine, name='machine'),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('search_machine/', search_machine, name='search_machine'),
    path('you_db/', page_after_authorization, name='page_after_authorization'),
    path('directory_model_machines/', DirectoryModelMachineList.as_view(),
         name='directory_model_machines'),
    path('directory_model_machines/<int:modelMachine_pk>/',
         DirectoryModelMachine.as_view(), name='directory_model_machine'),
]
