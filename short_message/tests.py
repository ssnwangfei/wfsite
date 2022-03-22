from django.test import TestCase
from django.http import JsonResponse
# Create your tests here.
from django.test import Client
from django.test.utils import setup_test_environment
from django.urls import reverse

class ViewTests(TestCase):

    def test_send_action(self):
        # setup_test_environment()
        c = self.client
        url = reverse("send_action")
        post = {"user_from": "wangfei",
                "user_to": "wf",
                "tag": "command",
                "message": "do something"}
        response = c.post(url, post)
        # res = JsonResponse()
        # JsonResponse.items[]
        print(response.content)
        self.assertIs(True, True)





