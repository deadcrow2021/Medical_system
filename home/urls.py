from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('account/<user_id>', views.account, name='account'),
]
