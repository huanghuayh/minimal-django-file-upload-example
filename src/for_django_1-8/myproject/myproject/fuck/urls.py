# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('myproject.fuck.views',
    url(r'^fuck/$', 'fuck', name='fuck'),

)
