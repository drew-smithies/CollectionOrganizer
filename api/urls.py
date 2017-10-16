from django.conf.urls import url
from rest_framework.authtoken import views as auth_views
from api import views


app_name = "api"
urlpatterns = [
    url(r'auth/', auth_views.obtain_auth_token, name="auth"),
    url(r'user/$', views.UserListCreate.as_view(), name="user-create-list"),
    url(r'user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name="user-detail"),
]
