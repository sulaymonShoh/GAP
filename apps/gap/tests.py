from django.test import TestCase
from apps.gap.models import Opinion, Room
from django.contrib.auth.models import User


class OptionTestCase(TestCase):
    def SetUp(self):
        user = User.objects.create(username="testuser")
        user.set_password("testpass")
        user.save()
        self.user = user

        room = Room.objects.create(name="test")
        room.save()
        self.room = room

        opinion = Opinion.objects.create(
            room=self.room,
            author=self.user,
            title="Lorem ipsum dolor sit amet",
            body="opinion body"
        )
        opinion.save()
        self.opinion = opinion

    def test_opinion_list(self):
        response = self.client.get("landing_page")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Lorem ipsum dolor sit amet")

    # har doim 404 status code qaytdi negaligini hech bilolmadim ((
