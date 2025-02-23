from django.test import TestCase, RequestFactory
from polls.models import Task
from polls.views import TaskViewSet
from datetime import datetime


class TaskTest(TestCase):
    BASE_URL = ""

    def setUp(self):
        self.factory = RequestFactory()

    @classmethod
    def setUpTestData(cls):
        cls.task1 = Task.objects.create(
            id="134be9ab-0bb0-403c-a484-47e2e66f289b",
            description="test note 1",
            date=datetime.now(),
            priority=2,
        )
        cls.task2 = Task.objects.create(
            id="f88d6cfe-f5f8-495a-ba56-f3b32ccf133a",
            description="test note 2",
            date=datetime.now(),
        )

    def test_get(self):
        request = self.factory.get(self.BASE_URL)

        response = TaskViewSet.as_view({"get": "list"})(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
