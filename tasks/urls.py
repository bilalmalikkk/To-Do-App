from django.urls import path
from . import views
from .api_views import (
    TaskListCreateAPIView,
    TaskRetrieveUpdateDestroyAPIView
)



urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('<int:task_id>/', views.task_detail, name='task_detail'),
    path('<int:task_id>/update/', views.task_update, name='task_update'),
    path('<int:task_id>/delete/', views.task_delete, name='task_delete'),

    path('api/tasks/', TaskListCreateAPIView.as_view(), name='task_list_create_api'),
    path('api/tasks/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task_retrieve_update_destroy_api'),
]
