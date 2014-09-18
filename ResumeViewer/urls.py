import os
from django.conf.urls import patterns, include, url
from tastypie.api import Api
from ResumeViewer.api import JobResource, UserResource
from ResumeViewer import views
from django.views.generic.base import TemplateView

# admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(JobResource())
v1_api.register(UserResource())

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', views.register, name='register'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^login/', views.user_login, name='login'),
                       url(r'^api/', include(v1_api.urls)),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^cv/$', views.main_view)
                       )
