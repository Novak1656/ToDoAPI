from django.urls import path
from .views import TaskAPIViewSet, UserCreateDeleteAPIView

urlpatterns = [
    path('task/my_tasks/', TaskAPIViewSet.as_view({'get': 'my_tasks'}), name='task_list'),
    path('task/create/', TaskAPIViewSet.as_view({'post': 'create'}), name='task_create'),
    path('task/update/<int:pk>/', TaskAPIViewSet.as_view({'put': 'update'}), name='task_update'),
    path('task/delete/<int:pk>/', TaskAPIViewSet.as_view({'delete': 'destroy'}), name='task_delete'),

    path('user/create/', UserCreateDeleteAPIView.as_view(), name='user_create'),
    path('user/delete/<int:pk>/', UserCreateDeleteAPIView.as_view(), name='user_delete'),
]
