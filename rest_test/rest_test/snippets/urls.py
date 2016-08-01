# -*- coding: utf-8 -*-
# author: xyp
from __future__ import unicode_literals
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
# from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_test.snippets import views

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)
#
# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
#
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'post': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
#
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, rederer_classes=[renderers.StaticHTMLRenderer])
#
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
#
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })

# urlpatterns = [
#     url(r'^snippets/$', snippet_list, name='snippet-list'),
#     url(r'^snippets/(?P<pk>[0-9]+)$', snippet_detail, name='snippet-detail'),
#     url(r'^users/$', user_list, name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)$', user_detail, name='user-detail'),
#     url(r'^$', api_root, name='root'),
#     url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet-highlight'),
# ]

urlpatterns = [
    url(r'^', include(router.urls)),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
