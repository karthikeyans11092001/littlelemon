from django.test import TestCase
from .models import Menu, Booking

class MenuModelTestCase(TestCase):
    def test_menu_model(self):
        menu = Menu.objects.create(name='Item 1', description='Description 1', price=10)
        self.assertEqual(menu.name, 'Item 1')
        self.assertEqual(menu.description, 'Description 1')
        self.assertEqual(menu.price, 10)

class BookingModelTestCase(TestCase):
    def test_booking_model(self):
        booking = Booking.objects.create(customer_name='John', table_number=1, date='2023-06-10')
        self.assertEqual(booking.customer_name, 'John')
        self.assertEqual(booking.table_number, 1)
        self.assertEqual(str(booking), 'John - Table 1')


