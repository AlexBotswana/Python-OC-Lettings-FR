from django.db import migrations
from django.contrib.auth.models import User
from profiles.models import Profile


def create_user_with_profile(username, email, first_name, last_name, favorite_city):
    user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name)
    Profile.objects.create(user=user, favorite_city=favorite_city)

def forwards(apps, schema_editor):
    # User admin creation
    admin_user = User.objects.create_user('admin', password='admin_password')
    admin_user.is_superuser = True
    admin_user.is_staff = True
    admin_user.save()

    create_user_with_profile("HeadlinesGazer", "jssssss33@acee9.live", "Jamie", "Lal", "Buenos Aires")
    create_user_with_profile("DavWin", "5houssam.kessaiso@facpidif.ml", "Grahm", "Cassandra", "Barcelona")
    create_user_with_profile("AirWow", "flocation.vam4@glendenningflowerdesign.com", "Ada", "Paul", "Budapest")
    create_user_with_profile("4meRomance", "coemperor@famemma.net", "John", "Rodriguez", "Berlin")

def backwards(apps, schema_editor):
    User.objects.filter(username__in=["HeadlinesGazer", "DavWin", "AirWow", "4meRomance"]).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
