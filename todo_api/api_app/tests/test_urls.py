import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Task, User, Category
from ..serializers import TaskSerializer, UserSerializer


class TaskUrlsTestCase(APITestCase):
    def test_user_tasks_list(self):
        cat = Category.objects.create(title='TestCategory')
        user = User.objects.create(username='TestUser', tg_id=123)
        task = Task.objects.create(title='TestTask', comment=f'SomeText...', category=cat, user=user)

        url = f"{reverse('tasks-my-tasks')}?tg_id={user.tg_id}"
        response = self.client.get(url)
        expected_data = TaskSerializer([task], many=True).data
        self.assertEqual(expected_data, response.data.get('tasks'))

    def test_tasks_list(self):
        cat = Category.objects.create(title='TestCategory')
        user = User.objects.create(username='TestUser', tg_id=123)
        task1 = Task.objects.create(title='TestTask1', comment=f'SomeText...', category=cat, user=user)
        task2 = Task.objects.create(title='TestTask2', comment=f'SomeText...', category=cat, user=user)

        url = reverse('tasks-list')
        response = self.client.get(url).data
        expected_data = TaskSerializer([task1, task2], many=True).data
        self.assertEqual(expected_data, response)

    def test_task_delete(self):
        cat = Category.objects.create(title='TestCategory')
        user = User.objects.create(username='TestUser', tg_id=123)
        task = Task.objects.create(title='TestTask', comment=f'SomeText...', category=cat, user=user)

        url = reverse('tasks-detail', kwargs={'pk': task.pk})
        response = self.client.delete(url).status_code
        self.assertEqual(status.HTTP_204_NO_CONTENT, response)


class UserUrlsTestCase(APITestCase):
    def test_user_create(self):
        user = User.objects.create(username='TestUser', tg_id=123)
        expected_data = {'new_user': UserSerializer(user).data}

        url = reverse('user_create')
        post_data = {'username': 'TestUser', 'tg_id': 123}
        response = self.client.post(url, data=json.dumps(post_data), content_type='application/json').data
        self.assertEqual(expected_data, response)

    def test_user_delete(self):
        user = User.objects.create(username='TestUser', tg_id=123)
        url = reverse('user_delete', kwargs={'pk': user.pk})
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
