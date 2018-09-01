from django.conf.urls import url
from student import views
urlpatterns=[
    url('^create$', views.create),
    url('^index$', views.index),
    url('^update/(?P<pk>[0-9]+)$', views.update),
    url('^view/(?P<pk>[0-9]+)$', views.view),
    url('^delete/(?P<pk>[0-9]+)$', views.delete)
]