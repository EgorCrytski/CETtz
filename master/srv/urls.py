from django.urls import path
from . import views

app_name = 'srv'

urlpatterns = [
    path('api/v1/srv/task/all', views.TaskListView.as_view(), name='api_task_list'),
    path('api/v1/srv/task/add', views.TaskCreateView.as_view(), name='api_task_add'),
    path('api/v1/srv/unit/add', views.UnitRegisterView.as_view(), name='api_unit_add'),
    path('api/v1/srv/unit/list', views.UnitListView.as_view(), name='api_unit_list'),
    path('api/v1/srv/thread/list', views.ThreadListView.as_view(), name='api_thread_list'),
]