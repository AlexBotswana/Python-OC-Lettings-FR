import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


def test_dummy():
    assert 1


@pytest.mark.django_db
def test_profiles_index(client):
    response = client.get(reverse('profiles:index'))
    assert response.status_code == 200
    assert b"<h1 class=\"page-header-ui-title mb-3 display-6\">Profiles</h1>" in response.content


@pytest.mark.django_db
def test_profile_detail(client):
    user = User.objects.create_user(username='testuser', first_name='Test', last_name='User')
    Profile.objects.create(user=user, favorite_city='Test City')
    response = client.get(reverse('profiles:profile', args=[user.username]))
    assert response.status_code == 200
    assert b"testuser" in response.content
    assert b"Test City" in response.content


@pytest.mark.django_db
def test_profile_creation(client):
    user = User.objects.create_user(username='anotheruser', first_name='Another', last_name='User')
    profile = Profile.objects.create(user=user, favorite_city='Another City')
    assert profile.user.username == 'anotheruser'
    assert profile.favorite_city == 'Another City'
