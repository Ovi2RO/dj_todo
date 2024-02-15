from django.urls import path
from . import views

urlpatterns = [
    # path('add/', views.add, name='add'),
    path('', views.index, name='index'),
    path('delete/<int:task_id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
]


