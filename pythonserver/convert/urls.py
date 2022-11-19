from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('stt', views.uploadSpeachToText),
    path('summarization', views.getSummaryFromText)
]