from django.conf.urls import url
from university import views

urlpatterns=[
    url(r'^Goodmorning$', views.Goodmorning)
]