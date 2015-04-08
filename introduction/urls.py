from django.conf.urls import url
from . import views


urlpatterns= [
    url(r'^mn/', views.index_mn, name='index_mn'),
    url(r'^$', views.index, name='index'),
]
