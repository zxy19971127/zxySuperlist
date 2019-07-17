from django.test import TestCase
from django.urls import resolve
from  lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
import unittest
from lists.models import Item

# Create your tests here.
class SmokeTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found=resolve('/')
        self.assertEqual(found.func,home_page)


class ListViewTest(TestCase):
    def test_uses_list_template(self):
        response=self.client.get('/lists/the_only_list_in_the_world/')
        self.assertTemplateUsed(response,'list.html')

    def test_displays_all_list_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/lists/the_only_list_in_the_world/')
        #print(response)
        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')


class NewListView(TestCase):
    def test_can_save_a_POST_request(self):
        response = self.client.post('/lists/new', data={"item_text": "A new list item"})

        self.assertEqual(Item.objects.count(), 1)
        new_iten = Item.objects.first()
        self.assertEqual(new_iten.text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post('/lists/new', data={"item_text": "A new list item"})

        self.assertRedirects(response,'/lists/the_only_list_in_the_world/')

#if __name__=='__main__':
 #   unittest.main()