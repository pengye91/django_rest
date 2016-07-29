# -*- coding: utf-8 -*-
# author: xyp
from __future__ import unicode_literals
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_test.snippets import views

urlpatterns = [
    url(r'^snippets/$', views.SnippetsList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)$', views.SnippetDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                                namespace='rest_framework')),
]
