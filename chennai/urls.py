from django.conf.urls import url
from chennai import views

urlpatterns=[
    url(r'^hellochennai$', views.chennai)
]