from rest_framework import serializers
from rest_framework.authtoken.models import Token
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
    if data['password'] and not data['password_confirm']:
      raise serializers.ValidationError('Please confirm your password.')
    if data['password'] != data['password_confirm']:
      raise serializers.ValidationError('Oops, your passwords did not match, try again.')
    data.pop('password_confirm')
    return data

  def create(self, validated_data):
    '''
      Create new user
    '''
    password = validated_data.pop('password', None)
    instance = self.Meta.model(username=validated_data['username'], email=validated_data['email'])
    if password is not None:
      instance.set_password(password)
    instance.save()

    # Create token
    Token.objects.create(user=instance)

    return instance

class UserSerializer(serializers.ModelSerializer):
  password_confirm = serializers.CharField(write_only=True)

  class Meta:
    model = User
    fields = '__all__'

  def validate(self, data):
    '''
      If password being pudated, check that passwords match
    '''
    if 'password' in data:
      if not 'password_confirm' in data:
        raise serializers.ValidationError('Please confirm your password.')
      elif data['password'] != data['password_confirm']:
        raise serializers.ValidationError('Oops, your passwords did not match, try again.')
      data.pop('password_confirm')
    return data

  def update(self, instance, validated_data):
    '''
      If password is updated, hash it
    '''
    for attr, value in validated_data.items():
      if attr == 'password':
        instance.set_password(value)
      else:
        setattr(instance, attr, value)
    instance.save()
    return instance
