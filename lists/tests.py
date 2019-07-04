from django.test import TestCase
import unittest

# Create your tests here.
class SmokeTest(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1+1,3)

if __name__=='__main__':
    unittest.main()