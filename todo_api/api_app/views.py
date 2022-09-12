from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import TaskSerializer, UserSerializer
from .models import Task, User


class TaskAPIViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(methods=['get'], detail=False)
    def my_tasks(self, request):
        tasks = User.objects.get(tg_id=request.GET.get('tg_id')).task.all()
        return Response({'tasks': TaskSerializer(tasks, many=True).data})


class UserCreateDeleteAPIView(APIView):
    def post(self, request):
        user = UserSerializer(data=request.data)
        user.is_valid()
        user.save()
        return Response({'new_user': user.data})

    def delete(self, request, pk):
        User.objects.get(pk=pk).delete()
        return Response({'message': 'User has been deleted.'})
