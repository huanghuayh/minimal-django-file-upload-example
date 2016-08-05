# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from . import views

from django.views.decorators.csrf import csrf_exempt

urlpatterns = patterns('myproject.fuck.views',
    url(r'^fuck/$', 'fuck', name='fuck'),

)
