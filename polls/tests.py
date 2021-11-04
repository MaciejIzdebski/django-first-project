from datetime import timezone
import datetime
from django.test import TestCase
from .models import *
# Create your tests here.


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        '''
            was_published_recently() returns False for 
            questions whose pub_date is in the future.
        '''

        time = timezone.now() + datetime.timedelta(days=30)

        future_question = Question(pub_date=time)

        self.assertIs(future_question.was_recently_published(), False)


    def test_was_published_recently_with_old_question(self):
        '''
            returns True for question
        '''