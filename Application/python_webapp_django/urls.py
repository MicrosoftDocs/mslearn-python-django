"""
Definition of urls for python_webapp_django.
"""

from datetime import datetime
from django.urls import include, re_path
import django.contrib.auth
from django.contrib.auth.views import LoginView
from django.views.static import serve
from django.conf import settings

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    re_path(r'^$', app.views.home, name='home'),
    re_path(r'^contact$', app.views.contact, name='contact'),
    re_path(r'^about', app.views.about, name='about'),
    re_path(r'^login/$', LoginView.as_view(template_name='app/login.html'), name='login'),
    re_path(r'^logout$',
        django.contrib.auth.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
