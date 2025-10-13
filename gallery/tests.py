from django.test import TestCase
from django.contrib.auth.models import User
from .models import Child, Artwork


class ChildModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.child = Child.objects.create(name='Alice', age=7, parent=self.user)

    def test_child_str(self):
        self.assertEqual(str(self.child), 'Alice')

    def test_child_parent(self):
        self.assertEqual(self.child.parent.username, 'testuser')

