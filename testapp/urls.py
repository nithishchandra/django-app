from django.conf.urls import url

from testapp import views

urlpatterns = [

    url(r'^hello_django$', views.helloDjango),
    url(r'^hello_nithish$', views.hellonithish)


]