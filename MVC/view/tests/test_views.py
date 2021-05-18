from django.test import TestCase, Client
from django.urls import reverse
from main.models import Movie, Review, User
import json



class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('main:home')

    def test_home_GET(self):
        # Test Code
        response = self.client.get(self.list_url)
        # Assertion
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/base.html')


