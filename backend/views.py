from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SlackSerializer
from .models import Slack

# Create your views here.

@api_view(['GET'])
def apiOverView(request):
    return Response("API BASE POINT", safe=False)


@api_view(['GET'])
def slackList(request):
    slack_name = request.GET.get('slack_name')
    current_day = request.GET.get('current_day')

    queryset = Slack.objects.all()

    if slack_name:
        queryset = queryset.filter(slack_name=slack_name)
    if current_day:
        queryset = queryset.filter(current_day=current_day)

    serializer = SlackSerializer(queryset, many=True)

    return Response(serializer.data)