# -*- coding: utf-8 -*-
# author: xyp
from __future__ import unicode_literals
from rest_framework import serializers
from rest_test.snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

owner = serializers.ReadOnlyField(source='owner.username')


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Snippet.objects.all(),
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets', )
