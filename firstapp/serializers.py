from rest_framework import serializers
from .models import Firstapp


class FirstappSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firstapp
        fields = ("title", "description")