"""CollectionOrganizer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""

from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# Browsable API URL
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/' + settings.API_VERSION + '/', include('api.urls', namespace='api')),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
]
