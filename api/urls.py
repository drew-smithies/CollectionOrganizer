from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import *

urlpatterns = {
    url(r'^tool/$', ToolViewSet, name="create"),
}

urlpatterns = format_suffix_patterns(urlpatterns)