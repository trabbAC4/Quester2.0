from rest_framework import serializers
from .models import Quester

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quester
        fields = ('id', 'title', 'description', 'level', 'completed')