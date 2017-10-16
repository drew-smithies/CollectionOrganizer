from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
  password_confirm = serializers.CharField()
  class Meta:
    model = User
    fields = '__all__'

  def validate(self, data):
    '''
    Check that passwords match
    '''
    if data['password'] != data['password_confirm']:
      raise serializers.ValidationError('Oops, your passwords did not match, try again.')
    return data
