from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('account/', views.account, name='account'),
    path('account/add_record', views.add_selfmonitor_record, name='add-record'),
]
