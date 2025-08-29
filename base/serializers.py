from rest_framework import serializers
from .models import Task , Category , Profile , Priority


class taskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields='__all__'

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class profileSerializer (serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields='__all__'

class prioritySerializer(serializers.ModelSerializer):
    class Meta:
        model=Priority
        fields='__all__'     