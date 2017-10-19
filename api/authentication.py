from datetime import datetime
import pytz
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

class ExpiringTokenAuthentication(TokenAuthentication):

  def authenticate_credentials(self, key):
    model = self.get_model()
    try:
      token = model.objects.select_related('user').get(key=key)
    except model.DoesNotExist:
      raise AuthenticationFailed(_('Invalid token.'))

    if not token.user.is_active:
      raise AuthenticationFailed(_('User inactive or deleted.'))

    utc_now = datetime.utcnow()
    utc_now = utc_now.replace(tzinfo=pytz.utc)
    if token.created < utc_now - settings.TOKEN_EXPIRE_TIME:
      raise AuthenticationFailed('Token has expired')

    return (token.user, token)
