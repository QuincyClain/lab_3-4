from django.test import TestCase
from django.urls import reverse

class MoviesTestCase(TestCase):
    def test_get(self):
        url = reverse('movie-list')
        print(url)
        response = self.client.get(url)
        print(response)