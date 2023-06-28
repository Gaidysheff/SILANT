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
    #     ----------------------------------------------------------------
    path('directory_model_engines/', DirectoryModelEngineList.as_view(),
         name='directory_model_engines'),
    path('directory_model_engines/<int:modelMachine_pk>/',
         DirectoryModelEngine.as_view(), name='directory_model_engine'),
    #     ----------------------------------------------------------------
    path('directory_model_transmissions/', DirectoryModelTransmissionList.as_view(),
         name='directory_model_transmissions'),
    path('directory_model_transmissions/<int:modelMachine_pk>/',
         DirectoryModelTransmission.as_view(), name='directory_model_transmission'),
    #     ----------------------------------------------------------------
    path('directory_model_drive_axles/', DirectoryModelDriveAxleList.as_view(),
         name='directory_model_drive_axles'),
    path('directory_model_drive_axles/<int:modelMachine_pk>/',
         DirectoryModelDriveAxle.as_view(), name='directory_model_drive_axle'),
    #     ----------------------------------------------------------------
    path('directory_model_steering_axles/', DirectoryModelSteeringAxleList.as_view(),
         name='directory_model_steering_axles'),
    path('directory_model_steering_axles/<int:modelMachine_pk>/',
         DirectoryModelSteeringAxle.as_view(), name='directory_model_steering_axle'),
    #     ----------------------------------------------------------------
    path('directory_maintenance_types/', DirectoryMaintenanceTypeList.as_view(),
         name='directory_maintenance_types'),
    path('directory_maintenance_types/<int:modelMachine_pk>/',
         DirectoryMaintenanceType.as_view(), name='directory_maintenance_type'),
    #     ----------------------------------------------------------------
    path('directory_model_breakdowns/', DirectoryBreakdownList.as_view(),
         name='directory_model_breakdowns'),
    path('directory_model_breakdowns/<int:modelMachine_pk>/',
         DirectoryBreakdown.as_view(), name='directory_model_breakdown'),
    #     ----------------------------------------------------------------
    path('directory_recovery_methods/', DirectoryRecoveryMethodList.as_view(),
         name='directory_recovery_methods'),
    path('directory_recovery_methods/<int:modelMachine_pk>/',
         DirectoryRecoveryMethod.as_view(), name='directory_recovery_method'),
    #     ----------------------------------------------------------------
    path('directory_service_companys/', DirectoryServiceCompanyList.as_view(),
         name='directory_model_engines'),
    path('directory_service_companys/<int:modelMachine_pk>/',
         DirectoryServiceCompany.as_view(), name='directory_service_company'),
]
