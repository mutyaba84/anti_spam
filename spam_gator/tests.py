from django.test import TestCase

from .models import BlockedEmails
from .utils import email_check

# Create your tests here.

class BlockedEmailTestCase(TestCase):
	def setUp(self):
		BlockedEmails.objects.create(email="test@example.com")
		BlockedEmails.objects.create(email="test@gmail.com")

	def test_blocked_emails(self):
		"""email block test"""
		email_1 = BlockedEmails.objects.get(email="test@example.com")
		email_2 = BlockedEmails.objects.get(email="test@gmail.com")


		self.assertTrue(email_check(email_1))
		self.assertTrue(email_check(email_2))

		