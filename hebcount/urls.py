from django.urls import path
from . import views

urlpatterns=[
    path("", views.HomePageView.as_view(), name='home'),    #homepage
    path("bmicva", views.kalkul, name="bmicva"),           #kalkulacka bar/bat micva        
    ]   