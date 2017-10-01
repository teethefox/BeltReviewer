from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$',views.register),
    url(r'^success$', views.success),
    url(r'^home$', views.home),
    url(r'^logout', views.logout),
    url(r'^add/(?P<id>\d+)', views.add),
    url(r'^book/(?P<id>\d+)', views.book),
    url(r'^user/(?P<id>\d+)', views.user),
]