from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Book


class BookAPITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title='Django for APIs',
            subtitle='Build web APIs with Python and Django',
            author='William S. Vincent',
            isbn='9781735467221',
        )

    def test_book_api_listview(self):
        response = self.client.get(reverse('all_books'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(response, self.book)
