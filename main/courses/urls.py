from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:course_id>/remove', views.remove),
    path('<int:course_id>/delete', views.delete),
    path('create', views.create),
]