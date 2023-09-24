from rest_framework import serializers
from .models import Parameter
from rest_framework.validators import UniqueTogetherValidator
from django.utils import dateformat
from django.conf import settings
from datetime import datetime



class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter
        fields = '__all__'