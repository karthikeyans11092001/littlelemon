from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Menu, Booking

class MenuViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_url = reverse('menu-list')

    def test_get_menu_list(self):
        response = self.client.get(self.menu_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class BookingViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.booking_url = reverse('booking-list')

    def test_get_booking_list(self):
        response = self.client.get(self.booking_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
