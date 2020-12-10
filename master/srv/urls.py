from django.urls import path

from . import views
from .views import TaskListView
app_name = 'srv'

urlpatterns = [
    path('api/v1/srv/unit/all', views.TaskListView.as_view(), name='api_task_list'),
]