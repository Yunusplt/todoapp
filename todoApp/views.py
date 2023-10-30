from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.

from django.http import HttpResponse
def home(request):
    return HttpResponse(
        '<center><h1 style="background-color:powderblue;">Welcome to Todo APP</h1></center>'
    )


class TodosMVS(ModelViewSet):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer

