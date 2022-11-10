from django.urls import path
from . import views


urlpatterns = [
    path('',views.Home,name="index"),
    path('save',views.saveData,name="save"),
    path('delete',views.DeleteData,name="delete"),
    path("edit",views.EditData,name="edit"),
]