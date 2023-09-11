from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SlackSerializer
from .models import Slack

# Create your views here.

@api_view(['GET'])
def apiOverView(request):
    api_urls ={
        'list': '/slack-list/',
    }
    return Response(api_urls)


@api_view(['GET'])
def slackList(request):
    slacks= Slack.objects.all()

    serializer = SlackSerializer(slacks, many=True)

    return Response(serializer.data)