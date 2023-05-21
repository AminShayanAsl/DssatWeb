from django.conf.urls import url
from . import views

app_name = 'app'

urlpatterns = [
    url('^$', views.home, name='home'),
    url('^login/$', views.login, name='login'),
    url('^signin/$', views.signin, name='signin'),
    url('^signup/$', views.signup, name='signup'),
    url('^computing/$', views.computing, name='computing'),
    url('^compute/$', views.compute, name='compute'),
    url('^logout/$', views.logout, name='logout'),
]