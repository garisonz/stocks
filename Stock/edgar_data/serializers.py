# Needed to convert model instances to JSON so that the frontend can work with the received data.

from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'