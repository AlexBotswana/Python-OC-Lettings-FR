import pytest
from django.urls import reverse
from lettings.models import Letting, Address

def test_dummy():
    assert 1
    
@pytest.mark.django_db
def test_lettings_index(client):
    response = client.get(reverse('lettings:index'))
    assert response.status_code == 200
    assert b"<h1 class=\"page-header-ui-title mb-3 display-6\">Lettings</h1>" in response.content

@pytest.mark.django_db
def test_letting_detail(client):
    address = Address.objects.create(
        number=123,
        street='Main St',
        city='City',
        state='State',
        zip_code='12345',
        country_iso_code='USA'
    )
    letting = Letting.objects.create(title='Test Letting', address=address)
    response = client.get(reverse('lettings:letting', args=[letting.id]))
    assert response.status_code == 200
    assert b"Test Letting" in response.content
    assert b"123 Main St" in response.content
