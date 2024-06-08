from django.db import migrations

def forwards(apps, schema_editor):
    OldProfile = apps.get_model('oc_lettings_site', 'Profile')
    NewProfile = apps.get_model('profiles', 'Profile')
    
    for old_profile in OldProfile.objects.all():
        new_profile = NewProfile.objects.create(
            user=old_profile.user,
            favorite_city=old_profile.favorite_city
        )

def backwards(apps, schema_editor):
    NewProfile = apps.get_model('profiles', 'Profile')
    NewProfile.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
