from rest_framework import generics
from rest_framework import mixins
from .models import User
from .serializers import UserSerializer, UserCreateSerializer

class UserListCreate(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     generics.GenericAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

  def get_serializer_class(self):
    """
      Use differnt serializers for different methods
    """
    if self.request.method == 'POST':
      return UserCreateSerializer
    return UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
