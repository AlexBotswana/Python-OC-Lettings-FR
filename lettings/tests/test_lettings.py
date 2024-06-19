import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from lettings.models import Letting, Address

@pytest.mark.django_db
def test_lettings_index(client):
    response = client.get(reverse('lettings:index'))
    assert response.status_code == 200
    assert b"<h1 class=\"page-header-ui-title mb-3 display-6\">Lettings</h1>" in response.content

@pytest.mark.django_db
def test_letting_detail(client):
    user = User.objects.create_user(username='testuser', first_name='Test', last_name='User')
    address = Address.objects.create(number='1', street='test street', city='test city', state='test state', zip_code='123', country_iso_code='01')
    letting = Letting.objects.create(title='Test Letting', address=address)
    response = client.get(reverse('lettings:letting', args=[letting.id]))
    assert response.status_code == 200
    assert b"Test Letting" in response.content

@pytest.mark.django_db
def test_address_detail(client):
    user = User.objects.create_user(username='testuser', first_name='Test', last_name='User')
    address = Address.objects.create(number='1', street='test street', city='test city', state='test state', zip_code='123', country_iso_code='01')
    letting = Letting.objects.create(title='Test Letting', address=address)
    response = client.get(reverse('lettings:letting', args=[letting.id]))
    assert response.status_code == 200
    assert b"test street" in response.content

@pytest.mark.django_db
def test_lettings_creation(client):
    address = Address.objects.create(number='1', street='test street', city='test city', state='test state', zip_code='123', country_iso_code='01')
    letting = Letting.objects.create(title='Test Letting', address=address)
    assert letting.title == 'Test Letting'

@pytest.mark.django_db
def test_address_creation(client):
    address = Address.objects.create(number='1', street='test street', city='test city', state='test state', zip_code='123', country_iso_code='01')
    letting = Letting.objects.create(title='Test Letting', address=address)
    assert letting.address.city == 'test city'
