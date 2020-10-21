from .views import loadselectroom, getRoomTotal
from django.test import TestCase
from django.urls import resolve

# Create your tests here.


class RoomBookingTest(TestCase):
    def test_select_room_url_resolves_to_select_room_page(self):
        found = resolve('/roomBooking/selectRoom/')
        self.assertEqual(found.func, loadselectroom)

    def test_get_room_total(self):
        self.assertEqual(getRoomTotal(2, 25000.00), 50000)
