from django.test import TestCase
from . import services


class TestServiceMethods(TestCase):

    def test_service_create_time_list(self):
        time_list = services.create_time_list("05:00:00", "21:05:00")
        self.assertEqual(time_list["21:05:00"], 193)
