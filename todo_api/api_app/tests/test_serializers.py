from django.test import TestCase
from ..models import Task, User, Category
from ..serializers import TaskSerializer, UserSerializer


class TaskSerializerTest(TestCase):
    def test_default(self):
        cat1 = Category.objects.create(title='TestCategory 1')
        cat2 = Category.objects.create(title='TestCategory 2')

        user1 = User.objects.create(username='TestUser 1', tg_id=123)
        user2 = User.objects.create(username='TestUser 2', tg_id=345)

        task1 = Task.objects.create(title='TestTask 1', comment=f'SomeText...', category=cat2, user=user1)
        task2 = Task.objects.create(title='TestTask 2', comment=f'SomeText...', category=cat2, user=user2)
        task3 = Task.objects.create(title='TestTask 3', comment=f'SomeText...', category=cat1, user=user1)

        ser_data = TaskSerializer([task1, task2, task3], many=True).data
        expected_data = [
            {
                'title': 'TestTask 1',
                'comment': 'SomeText...',
                'category': 2,
                'user': 1
            },
            {
                'title': 'TestTask 2',
                'comment': 'SomeText...',
                'category': 2,
                'user': 2
            },
            {
                'title': 'TestTask 3',
                'comment': 'SomeText...',
                'category': 1,
                'user': 1
            }
        ]
        self.assertEqual(expected_data, ser_data)


class UserSerializerTest(TestCase):
    def test_default(self):
        user1 = User.objects.create(username='TestUser 1', tg_id=123)
        user2 = User.objects.create(username='TestUser 2', tg_id=345)
        ser_data = UserSerializer([user1, user2], many=True).data
        expected_data = [
            {
                'username': 'TestUser 1',
                'tg_id': 123
            },
            {
                'username': 'TestUser 2',
                'tg_id': 345
            }
        ]
        self.assertEqual(expected_data, ser_data)
