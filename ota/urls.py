from django.conf.urls import url
from . import views

app_name = 'ota'

urlpatterns = [
    # bookings.lk
    url(r'^$', views.index,name='index'),

    # /music/124/
    #url(r'^(?P<album_id>[0-9]+)/$', views.details, name='detail'),

    # /music/124/
    #url(r'^(?P<album_id>[0-9]+)/favorite$', views.favorite, name='favorite'),

]
