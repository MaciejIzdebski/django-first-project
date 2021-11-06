from datetime import timezone
import datetime
from django.test import TestCase
from django.urls import reverse
from .models import *
# Create your tests here.



class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        '''
            was_published_recently() returns False for 
            question whose pub_date is in the future.
        '''

        time = timezone.now() + datetime.timedelta(days=30)

        future_question = Question(pub_date=time)

        self.assertIs(future_question.was_recently_published(), False)


    def test_was_published_recently_with_old_question(self):
        '''
            returns False for question whose pub_date was in the far past
        '''

        time = timezone.now() - datetime.timedelta(days=30)

        future_question = Question(pub_date=time)
        
        self.assertIs(future_question.was_recently_published(), False)


    def test_was_published_recently_with_recent_question(self):
        '''
            returns False for question whose pub_date was in the far past
        '''

        time = timezone.now() - datetime.timedelta(minutes=30)

        future_question = Question(pub_date=time)
        
        self.assertIs(future_question.was_recently_published(), True)




class QuestionViewTests(TestCase):

    def on_no_questions_view_should_return_no_polls_available(self):

        result = self.client.get(reverse("polls:index"))

        self.assertEquals(result.context["questions_list"], [])
        self.assertContains(result.content, "No polls are available.")