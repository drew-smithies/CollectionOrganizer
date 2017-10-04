from rest_framework_mongoengine import viewsets
from api.serializers import *  
from api.models import Tool

class ToolViewSet(viewsets.ModelViewSet):
    '''
    Contains information about inputs/outputs of a single program
    that may be used in Universe workflows.
    '''
    lookup_field = 'id'
    serializer_class = ToolSerializer

    def get_queryset(self):
        return Tool.objects.all()