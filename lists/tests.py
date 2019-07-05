from django.test import TestCase
from django.urls import resolve
from  lists.views import home_page
import unittest

# Create your tests here.
class SmokeTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found=resolve('/')
        self.assertEqual(found.func,home_page)

if __name__=='__main__':
    unittest.main()