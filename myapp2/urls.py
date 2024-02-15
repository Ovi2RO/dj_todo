from django.urls import path
from .views import TaskListView, TaskDetailView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', TaskListView.as_view(), name='index2'),
    path('detail/<int:pk>/', TaskDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='delete2'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='update2'),
]


