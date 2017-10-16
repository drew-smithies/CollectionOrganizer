from rest_framework import serializers
from .models import User

class UserCreateSerializer(serializers.ModelSerializer):
  password_confirm = serializers.CharField(write_only=True)

  class Meta:
    model = User
    fields = '__all__'

  def validate(self, data):
    '''
    Check that passwords match
    '''
    if data['password'] != data['password_confirm']:
      raise serializers.ValidationError('Oops, your passwords did not match, try again.')
    data.pop('password_confirm')
    return data

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'
