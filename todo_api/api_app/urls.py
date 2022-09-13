from django.urls import path, include
from .views import TaskAPIViewSet, UserCreateDeleteAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tasks', TaskAPIViewSet, basename='tasks')


urlpatterns = [
    path('', include(router.urls), name='tasks'),

    path('user/create/', UserCreateDeleteAPIView.as_view(), name='user_create'),
    path('user/delete/<int:pk>/', UserCreateDeleteAPIView.as_view(), name='user_delete'),
]
