from django.urls import path

from . import views
app_name = 'srv'

urlpatterns = [
    path('api/v1/srv/task/all', views.TaskListView.as_view(), name='api_task_list'),
    path('api/v1/srv/task/add', views.TaskCreateView.as_view(), name='api_task_add')
]