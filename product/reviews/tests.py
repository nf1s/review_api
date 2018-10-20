from django.contrib.auth.models import User
from django.test import Client, TestCase

from reviews.models import Review


class DashboardTestCase(TestCase):

    fixtures = ['reviews/fixtures/initial.json']

    def setUp(self):
        super().setUp()

        username, password = 'Thorgate', 'thorgate123'
        User.objects.create_user(username=username, email='info@throgate.eu', password=password)

        self.authenticated_client = Client()
        self.authenticated_client.login(username=username, password=password)

    def test_dashboard_requires_authentication(self):

        # Anonymous users can't see the dashboard

        client = Client()
        response = client.get('/dashboard/')
        self.assertRedirects(response, '/login/?next=/dashboard/')

        # Authenticated users can see the dashboard

        response = self.authenticated_client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)

    def test_Reviews_on_dashboard(self):

        # There are 3 reviews on the dashboard (loaded from the fixtures)

        response = self.authenticated_client.get('/dashboard/')
        Reviews = response.context['reviews']
        self.assertEqual(len(Reviews), 3)


class ReviewsTestCase(TestCase):
    fixtures = ['reviews/fixtures/initial.json']

    def setUp(self):
        super().setUp()

        self.Reviews = Review.objects.order_by('id')

    def test_Review_has_ended(self):

        # 2 of the reviews have ended
        self.assertListEqual([p.has_ended for p in self.Reviews], [True, True, False])

    def test_Review_is_over_budget(self):

        # 1 of the reviews is over budget
        self.assertListEqual([p.is_over_budget for p in self.Reviews], [True, False, False])

    def test_total_estimated_hours(self):

        self.assertListEqual([p.total_estimated_hours for p in self.Reviews], [690, 170, 40])

    def test_total_actual_hours(self):

        self.assertListEqual([p.total_actual_hours for p in self.Reviews], [739, 60, 5])
