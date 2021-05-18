from django.test import SimpleTestCase
from django.urls import reverse, resolve, reverse_lazy
from main.views import detail, home, add_movies, edit_movies, delete_movies, add_review, edit_review, delete_review


class TestUrls(SimpleTestCase):

    def test_detail_url_is_resolved(self):
        # Test Code
        url = reverse('main:detail', args=[2])
        # Assertion
        self.assertEquals(resolve(url).func, detail)

    def test_home_url_is_resolved(self):
        url = reverse('main:home')
        self.assertEquals(resolve(url).func, home)

    def test_add_movies_url_is_resolved(self):
        url = reverse('main:add_movies')
        self.assertEquals(resolve(url).func, add_movies)

    def test_edit_movies_url_is_resolved(self):
        url = reverse('main:edit_movies', args=[2])
        self.assertEquals(resolve(url).func, edit_movies)

    def test_delete_movies_url_is_resolved(self):
        url = reverse('main:delete_movie', args=[3])
        self.assertEquals(resolve(url).func, delete_movies)

    def test_add_review_url_is_resolved(self):
        url = reverse('main:add_review', args=[3])
        self.assertEquals(resolve(url).func, add_review)

    def test_edit_review_url_is_resolved(self):
        url = reverse('main:edit_review', args=[2,3])
        self.assertEquals(resolve(url).func, edit_review)

    def test_delete_review_url_is_resolved(self):
        url = reverse('main:delete_review', args=[2,2])
        self.assertEquals(resolve(url).func, delete_review)


