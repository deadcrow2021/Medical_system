from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('account/', views.account, name='account'),
    path('account/add_record', views.add_selfmonitor_record, name='add-record'),
    path('account/reception', views.ReceptionView.as_view(), name='reception'),
    path('account/reception/add/<profile_id>', views.ReceptionAddView.as_view(), name='add-reception'),
    path('data_sampling', views.data_sampling_page, name='data-sampling'),
]
