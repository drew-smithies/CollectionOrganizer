from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_mongoengine import routers
from api import views 

router = routers.DefaultRouter()
router.register(r'tool', views.ToolViewSet, r"tool")


urlpatterns = [ 
    url(r'^', include(router.urls))
]
