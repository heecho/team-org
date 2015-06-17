from django.conf.urls import url
 
from . import views
 
urlpatterns = [
 url(r'^$', views.index, name='index'),
 url(r'^new$', views.new, name='new'),
 url(r'^create$', views.create, name='create'),
 url(r'^(?P<dept_id>[0-9]+)/$', views.show, name='show'),
]
