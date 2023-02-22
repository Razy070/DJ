from unittest import TestCase

from django.contrib.auth.models import User, Group
from django.db import models


# Create your models here.


class PostModelTest(TestCase):

    @classmethod
    def book(self, cls=None):
        super().setUpClass()
        self.user = User.objects.create_user(username='auth')
        self.group = Group.objects.create(title='Тестовая группа',
                                          slug='Тестовый слаг',
                                          description='Тестовое описание', )
        self.post = Post.objects.create(author=cls.user,
                                        text='Тестовое описание', )
