from django.urls import path
from crm_app.views import *

urlpatterns = [
    path('', MachinesHomePage.as_view(), name='index'),
    #     ----------------------------------------------------------------
    path('search_machine/', search_machine, name='search_machine'),
    path('you_db/', page_after_authorization, name='page_after_authorization'),
    path('full_db_list/', full_db_list, name='full_db_list'),
    #     ---------------------- CRUD -------------------------------
    path('machine/<int:machine_id>/', show_machine, name='machine'),
    path('maintenance/<int:maintenance_id>/',
         show_maintenance, name='maintenance'),
    path('claim/<int:claim_id>/', show_claim, name='claim'),
    #     ----------------------
    path('add_machine/', AddMachine.as_view(), name='add_machine'),
    path('add_maintenance/', AddMaintenance.as_view(), name='add_maintenance'),
    path('add_claim/', AddClaim.as_view(), name='add_claim'),
    #     ----------------------
    path('machine/<int:pk>/update/',
         UpdateMachine.as_view(), name='update_machine'),
    path('maintenance/<int:pk>/maintenance_update/', UpdateMaintenance.as_view(),
         name='update_maintenance'),
    path('claim/<int:pk>/claim_update/',
         UpdateClaim.as_view(), name='update_claim'),
    #     ----------------------
    path('machine/<int:pk>/delete_machine/',
         DeleteMachine.as_view(), name='delete_machine'),
    path('maintenance/<int:pk>/delete_maintenance/',
         DeleteMaintenance.as_view(), name='delete_maintenance'),
    path('claim/<int:pk>/delete_claim/',
         DeleteClaim.as_view(), name='delete_claim'),
    #     ---------------------- СПРАВОЧНИКИ -------------------------------
    path('all_directories/', AllDirectories.as_view(), name='all_directories'),
    #     ----------------------------------------------------------------
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
    path('directory_breakdowns/', DirectoryBreakdownList.as_view(),
         name='directory_breakdowns'),
    path('directory_breakdowns/<int:modelMachine_pk>/',
         DirectoryBreakdown.as_view(), name='directory_breakdown'),
    #     ----------------------------------------------------------------
    path('directory_recovery_methods/', DirectoryRecoveryMethodList.as_view(),
         name='directory_recovery_methods'),
    path('directory_recovery_methods/<int:modelMachine_pk>/',
         DirectoryRecoveryMethod.as_view(), name='directory_recovery_method'),
    #     ----------------------------------------------------------------
    path('directory_service_companies/', DirectoryServiceCompanyList.as_view(),
         name='directory_service_companies'),
    path('directory_service_companies/<int:machine_pk>/',
         DirectoryServiceCompany.as_view(), name='directory_service_company'),
    #     ---------------------- СПРАВОЧНИКИ Create -------------------------
    path('add_model_machine/', AddModelMachine.as_view(), name='add_model_machine'),
    path('add_model_engine/', AddModelEngine.as_view(), name='add_model_engine'),
    path('add_model_transmission/', AddModelTransmission.as_view(),
         name='add_model_transmission'),
    path('add_model_drive_axle/', AddModelDriveAxle.as_view(),
         name='add_model_drive_axle'),
    path('add_model_steering_axle/', AddModelSteeringAxle.as_view(),
         name='add_model_steering_axle'),
    path('add_maintenance_type/', AddMaintenanceType.as_view(),
         name='add_maintenance_type'),
    path('add_breakdown/', AddBreakdown.as_view(), name='add_breakdown'),
    path('add_recovery_method/', AddRecoveryMethod.as_view(),
         name='add_recovery_method'),
    path('add_service_company/', AddServiceCompany.as_view(),
         name='add_service_company'),
    #     ---------------------- СПРАВОЧНИКИ Update -------------------------
    path('directory_model_machines/<int:modelMachine_pk>/',
         UpdateModelMachine.as_view(), name='update_model_machine'),
    #     ---------------------- СПРАВОЧНИКИ Delete -------------------------
    #     ---------------------------- VARIOUS ------------------------------
    path('under_construction/', under_construction, name='under_construction'),
    path('forbidden/', forbidden, name='forbidden'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),

]
