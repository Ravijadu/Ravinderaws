from django.urls import path
from . import views


urlpatterns = [
    path('owner', views.owner, name='owner'),
    path('', views.ownerdetail, name='ownerdetail'),


]
