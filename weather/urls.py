from django.conf.urls import url

from myweather import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]