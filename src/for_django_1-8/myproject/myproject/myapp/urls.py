# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('myproject.myapp.views',
    url(r'^list/$', 'list', name='list'),
    #url(r'^test/$','test',name='test'),
    # url(r'^fuck/$','fuck', name='fuck'),
)



# urlpatterns = [
#     # ex: /polls/
#     url(r'^$', views.index, name='index'),
#     # ex: /polls/5/
#     url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
#     # ex: /polls/5/vote/
#     url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
# ]
