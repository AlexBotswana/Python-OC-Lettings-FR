from django.db import migrations
from lettings.models import Letting, Address

def create_address_with_letting(number, street, city, state, zip_code, country_iso_code, title):
    address = Address.objects.create(
        number=number,
        street=street,
        city=city,
        state=state,
        zip_code=zip_code,
        country_iso_code=country_iso_code
    )
    Letting.objects.create(
        title=title,
        address=address
    )

def forwards(apps, schema_editor):

    create_address_with_letting(7217, "Bedford Street", "Brunswick",
                                "GA", 31525, "USA",
                                "Joshua Tree Green Haus /w Hot Tub")
    create_address_with_letting(4, "Military Street", "Willoughby",
                                "OH", 44094, "USA",
                                "Oceanview Retreat")
    create_address_with_letting(340, "Wintergreen Avenue", "Newport News",
                                "VA", 23601, "USA",
                                "'Silo Studio' Cottage")
    create_address_with_letting(9230, "E. Joy Ridge Street", "Marquette",
                                "MI", 49855, "USA",
                                "Pirates of the Caribbean Getaway")
    create_address_with_letting(9606, "Harvard Street", "Aliquippa", "PA",
                                15001, "USA",
                                "The Mushroom Dome Retreat & LAND of Paradise Suite")
    create_address_with_letting(588, "Argyle Avenue", "East Meadow",
                                "NY", 11554, "USA", "Underground Hygge")

def backwards(apps, schema_editor):
    Letting.objects.all().delete()
    Address.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
