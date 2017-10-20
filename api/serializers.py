from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import User

class UserSerializer(serializers.ModelSerializer):
  password_confirm = serializers.CharField(write_only=True)

  class Meta:
    model = User
    fields = '__all__'

  def validate(self, attrs):
    '''
      Validate password and password_confirm
    '''
    if 'password' in attrs:
      if not 'password_confirm' in attrs:
        raise serializers.ValidationError('Please confirm your password.')
      elif attrs['password'] != attrs['password_confirm']:
        raise serializers.ValidationError('Oops, your passwords did not match, try again.')
      attrs.pop('password_confirm')
    return attrs

  def create(self, validated_data):
    '''
      Create new user
    '''
    password = validated_data.pop('password', None)
    instance = self.Meta.model(username=validated_data['username'], email=validated_data['email'])
    if password is not None:
      # Set password and create token
      instance.set_password(password)
      Token.objects.create(user=instance)
    instance.save()

    return instance

  def update(self, instance, validated_data):
    '''
      Update User
    '''
    for attr, value in validated_data.items():
      if attr == 'password':
        # Update password, delete token and create a new one
        instance.set_password(value)
        Token.objects.get(user=instance.pk).delete()
        Token.objects.create(user=instance)
      else:
        setattr(instance, attr, value)
    instance.save()


    return instance
