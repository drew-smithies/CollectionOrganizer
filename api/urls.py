from django.conf.urls import url
from rest_framework.authtoken import views as auth_views


# Browsable API URL: url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
app_name = "api"
urlpatterns = [
    url(r'/auth/', auth_views.obtain_auth_token, name="auth")
]
