from django.urls import path
from . import views

urlpatterns = [
    path('fullcalendar/', views.fullcalender.as_view(), name='fullcalender'),
]
