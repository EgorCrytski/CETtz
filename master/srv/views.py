from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from rest_framework import permissions
from .models import Task, Unit, Thread
from rest_framework.views import APIView
from django.conf.urls import url
from rest_framework.response import Response
from .serializers import TaskCreateSerializer, TaskListSerializer, UnitCreateSerializer, UnitRegisterSerializer, \
    UnitListViewSerializer, ThreadViewSerializer
from .utils import get_client_ip


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


class TaskCreateView(APIView):

    def post(self, request):
        task = TaskCreateSerializer(data=request.data)
        print(get_client_ip(request))
        if task.is_valid():
            task.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def get_serializer(self):
        return TaskCreateSerializer()


class UnitListView(APIView):

    def get(self, request):
        units = Unit.objects.all()
        serializer = UnitListViewSerializer(units, many=True)
        return Response(serializer.data)


class ThreadListView(APIView):

    def get(self, request):
        threads = Thread.objects.all()
        serializer = ThreadViewSerializer(threads, many=True)
        return Response(serializer.data)


class UnitRegisterView(APIView):

    def post(self, request):
        data = {'ip': get_client_ip(request), 'port': request.data['port']}
        unit = UnitCreateSerializer(data=data)
        if unit.is_valid():
            u = Unit.objects.create(ip=data['ip'], port=data['port'])
            for t in range(request.data['threads']):
                Thread.objects.create(unit=u)
            return Response(status=201)
        else:
            return Response(status=400)

    def get_serializer(self):
        return UnitRegisterSerializer()
