from rest_framework import serializers
from .models import BOOK

class BOOKSerializer(serializers.ModelSerializer):
    class Meta:
        model = BOOK
        fields = '__all__'