from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from rest_framework import permissions
from .models import Task
from rest_framework.views import APIView
from django.conf.urls import url
from rest_framework.response import Response
from .serializers import TaskCreateSerializer, TaskListSerializer

class TaskListView(APIView):
    serializer_class = TaskListSerializer
    queryset = Task.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskListSerializer(tasks, many=True)
        return Response(serializer.data)

    def get_serializer(self):
        return TaskListSerializer()