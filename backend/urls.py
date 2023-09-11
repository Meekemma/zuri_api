from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverView, name="api-overview"),
    path('slack-list/', views.slackList, name="slack-list"),
]