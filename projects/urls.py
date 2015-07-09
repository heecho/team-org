from django.conf.urls import url
 
from . import views
 
urlpatterns = [
 url(r'^$', views.index, name='index'),
 url(r'^new$', views.new, name='new'),
 url(r'^create$', views.create, name='create'),
 url(r'^(?P<proj_id>[0-9]+)/$', views.show, name='show'),
 url(r'^(?P<proj_id>[0-9]+)/add$', views.add_time, name='add'),
 url(r'^(?P<proj_id>[0-9]+)/assign$', views.assign, name='assign'),

]

