from django.urls import path
from .views import Home,AddInvigilator

urlpatterns = [
    path('',Home.as_view(),name="home"),
    path('add/',AddInvigilator.as_view(),name="add")
]
