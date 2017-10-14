from django.conf.urls import url
from rest_framework.authtoken import views as auth_views


app_name = "api"
urlpatterns = [
    url(r'auth/', auth_views.obtain_auth_token, name="auth")
]
