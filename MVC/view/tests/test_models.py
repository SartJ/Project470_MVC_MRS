from django.test import TestCase
from main.models import Movie, Review
from django.contrib.auth.models import User


# class TestModels(TestCase):
#     def setUp(self):
#         self.movie1 = Movie.objects.create(
#             name = 'Movie 1',
#             imdb = 'https://www.imdb.com/title/tt1853728/'
#         )

class TestModels(TestCase):

    def test_movie_str(self):
        name = Movie.objects.create(name="Test Name 1")
        imdb = Movie.objects.create(imdb="www.micTesting123.com")
        self.assertEqual(str(name), "Test Name 1")


    def test_review_str(self):
        # testuser = User.objects.create_user(username='testuser')
        # testuser2 = User.objects.create_user(username='testuser2')
        movie = Movie.objects.create(name="Django")
        comment = Movie.objects.create(name="Test Name 1")
        # rating = Review.objects.create(rating=7.3)
        self.assertEqual(str(comment), "Test Name 1")


