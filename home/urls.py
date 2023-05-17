from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('account/', views.account, name='account'),
    # path('account/add_record', views.add_selfmonitor_record, name='add-record'),
    path('account/reception', views.ReceptionView.as_view(), name='reception'),
    path('account/reception/add/<profile_id>', views.reception_add_page, name='add-reception'),
    path('account/reception/update/<profile_id>/<note_id>', views.update_reception_page, name='update-reception'),
    path('account/records', views.records_page, name='records'),
    path('account/records/add', views.add_selfmonitor_record, name='add-record'),
    path('account/records/update/<record_id>', views.update_reception_page, name='update-record'),
    path('data_sampling', views.data_sampling_page, name='data-sampling'),
    path('update_mo_delivery/<profile_id>', views.update_mo_delivery, name='update-mo-delivery'),
    path('statistics_report', views.statistics_report, name='statistics-report'),
    path('download_report/<report_id>', views.download_report, name='download-report'),
]
