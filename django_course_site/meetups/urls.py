from django.urls import URLPattern
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='all-meetups'), # ourdomain.com/meetups
    path('<slug:meetup_slug>/success', views.confirm_registration, name='confirm-registration'),
    path('<slug:meetup_slug>', views.meetup_details, name='meetup-detail'),  # ourdomain.com/meetups/<:meetup_id>
]
