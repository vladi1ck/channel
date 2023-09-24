from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import ParameterSerializer
from .models import Parameter


def lobby(request):
    return render(request, 'chat/lobby.html')


class ParameterView(viewsets.ModelViewSet):
    serializer_class = ParameterSerializer
    queryset = Parameter.objects.all()