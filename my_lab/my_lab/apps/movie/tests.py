from asgiref.sync import async_to_sync
from django.test import RequestFactory, TestCase
from django.urls import reverse
from .async_functionality import *
from .views import *


class MoviesTestCase(TestCase):
    def setUp(self) -> None:
        Actor.objects.create(name='Vlad', age=40, description='Good guy')
        self.movie = Movie.objects.create(
            title='test_movie',
            description='test description',
            genre='Drama',
            price=100,
            url='new1'
            )
        self.client.login(username='vlad2', password='mypass')

    def test_movie_create_form(self):
        form_data = {'title': 'Test movie', 'description': 'test description', 'genre': 'Drama',
                     'actors': ['Vlad'], 'price': 100, 'url': 'test'}
        request = RequestFactory().post('/movie/create/', form_data)
        view = MovieCreateView()
        view.setup(request)
        response = view.post(request)
        self.assertEqual(response.status_code, 200)

    def test_movie_create_form_unauthorized(self):
        self.client.logout()
        response = self.client.get('/movie/create/')
        self.assertEqual(response.status_code, 302)

    def test_movie_delete(self):
        self.client.login(username='vlad2', password='Vladgoogle1234')
        response = self.client.get(reverse('delete_movie', args=[str(self.movie.id)]))
        self.assertEqual(response.status_code, 302) #redirect to confirmation


class MemberTestCase(TestCase):
    def setUp(self) -> None:
        self.member = Member.objects.create(
            member_name='member',
            email_address='member@gmail.com',
            age=30,
            birthday='2001-05-30',
            gender='male'
        )
        self.client.login(username='vlad2', password='mypass')

    def test_member_create_form(self):
        form_data = {'member_name': 'member', 'email_address': 'member@gmail.com', 'age': 30, 'birthday': '2001-05-30', 'gender': 'male'}
        request = RequestFactory().post('/member/create/', form_data)
        view = MemberCreateView()
        view.setup(request)
        response = view.post(request)
        self.assertEqual(response.status_code, 200)

    def test_member_redirect_unauthorized(self):
        self.client.logout()
        response = self.client.get('/member/create/')
        self.assertEqual(response.status_code, 302)

    def test_member_delete(self):
        self.client.login(username='vlad2', password='Vladgoogle1234')
        response = self.client.get(reverse('delete_member', args=[str(self.member.id)]))
        self.assertEqual(response.status_code, 302) #redirect to confirmation


class ActorTestCase(TestCase):
    def setUp(self) -> None:
        self.actor = Actor.objects.create(
            name='Vlad',
            age=40,
            description='Good guy'
        )
        self.client.login(username='vlad2', password='mypass')

    def test_actor_create_form(self):
        form_data = {'name': 'actor', 'age': 10, 'description': 'some description'}
        request = RequestFactory().post('/actor/create/', form_data)
        view = ActorCreateView()
        view.setup(request)
        response = view.post(request)
        self.assertEqual(response.status_code, 200)

    def test_actor_redirect_unauthorized(self):
        self.client.logout()
        response = self.client.get('/actor/create/')
        self.assertEqual(response.status_code, 302)

    def test_member_delete(self):
        self.client.login(username='vlad2', password='Vladgoogle1234')
        response = self.client.get(reverse('delete_actor', args=[str(self.actor.id)]))
        self.assertEqual(response.status_code, 302) #redirect to confirmation


class AsyncFunctionalityTestCase(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title='my movie',
            description='movie description',
            genre='Drama',
            price=100,
            url='new_movie'
        )
        self.actor = Actor.objects.create(
            name='Vlad',
            age=40,
            description='Good guy'
        )
        self.member = Member.objects.create(
            member_name='man',
            email_address='member@gmail.com',
            age=30,
            birthday='2001-05-30',
            gender='male'
        )
    @async_to_sync
    def sync_get_movies(self):
        return get_all_movies()

    @async_to_sync
    def get_sync_movie_by_id(self, id):
        return get_movie_by_id(id)

    @async_to_sync
    def sync_get_actors(self):
        return get_all_actors()

    @async_to_sync
    def get_sync_actor_by_id(self, id):
        return get_actor_by_id(id)

    @async_to_sync
    def sync_get_members(self):
        return get_all_members()

    @async_to_sync
    def get_sync_member_by_id(self, id):
        return get_member_by_id(id)

    def test_movies_get(self):
        movies = Movie.objects.all()
        async_movies = self.sync_get_movies()
        self.assertQuerysetEqual(movies, async_movies)

    def test_actors_get(self):
        actors = Actor.objects.all()
        async_actors = self.sync_get_actors()
        self.assertQuerysetEqual(actors, async_actors)

    def test_movie_by_id(self):
        movie = Movie.objects.get(id=self.movie.id)
        async_movie = self.get_sync_movie_by_id(self.movie.id)
        self.assertEqual(movie, async_movie)

    def test_actor_by_id(self):
        actor = Actor.objects.get(id=self.actor.id)
        async_actor = self.get_sync_actor_by_id(self.actor.id)
        self.assertEqual(actor, async_actor)

    def test_members_get(self):
        members = Member.objects.all()
        async_members = self.sync_get_members()
        self.assertQuerysetEqual(members, async_members)

    def test_member_by_id(self):
        member = Member.objects.get(id=self.member.id)
        async_member = self.get_sync_member_by_id(self.member.id)
        self.assertEqual(member, async_member)


class ViewsTestCase(TestCase):
    def test_movies_view(self):
        self.client.login(username='vlad2', password='mypass')
        self.movie_1 = Movie.objects.create(
            title='my movie',
            description='movie description',
            genre='Drama',
            imageURL='dont_look_up.jpeg',
            price=100,
            url='new_movie_1'
        )
        response = self.client.get(reverse('movie_views'))
        self.assertQuerysetEqual(response.context['movie_list'], [self.movie_1])

    def test_actors_view(self):
        self.client.login(username='vlad2', password='mypass')
        self.actor = Actor.objects.create(
            name='Vlad',
            age=40,
            imageURL='dont_look_up.jpeg',
            description='Good guy'
        )
        response = self.client.get(reverse('actors_view'))
        self.assertQuerysetEqual(response.context['actor_list'], [self.actor])