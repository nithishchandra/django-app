from django.conf.urls import url

from india import views

urlpatterns = [

    url(r'^Andhrapradesh$', views.india)
 ]