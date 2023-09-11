from rest_framework import serializers
from .models import Slack


class SlackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slack
        fields = '__all__'
