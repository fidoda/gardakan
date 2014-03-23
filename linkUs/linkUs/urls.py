from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from chatUs import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'linkUs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^index.html$', views.login, name='home'),
    url(r'^createEvent.html$', views.create_event, name='create_event'),
   # url(r'^event.html$', views.event, name='event'),
    url(r'^(?P<event_id>\d+)/event.html$', views.event, name='event'),
    url(r'^eventList.html$', views.event_list, name='event_list'),
    url(r'^send_coord.html$', views.receive_coord, name='send_coord'),
    url(r'^admin/', include(admin.site.urls)),
<<<<<<< HEAD
    url("", include('django_socketio.urls'))
=======
    
>>>>>>> 06733dc0ed761110e1df99b788a794b61d31b42b
)