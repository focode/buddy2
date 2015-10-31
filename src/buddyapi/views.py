from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView )

from .models import Task
from .serializers import TaskSerializer


# Example using class based views
# -----------------------------------
class TaskMixin(object):
    """
    Mixin to inherit from.
    Here we're setting the query set and the serializer
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    print "serializer_class",serializer_class

class TaskList(TaskMixin, ListCreateAPIView):
    """
    Return a list of all the tasks, or
    create new ones
    """
    pass

class TaskDetail(TaskMixin, RetrieveUpdateDestroyAPIView):
    """
    Return a specific task, update it, or delete it.
    """
    pass

class UserViewSet(viewsets.ViewSet):
     """
    A simple ViewSet for listing or retrieving users.
    """

class DummyResponse(APIView):



     def get(self, request, pk, format='json'):
         queryset = Task.objects.all()
         serialized_data = serializers.serialize("json", queryset)
         print "serialized_data::",serialized_data
         return Response(serialized_data)






